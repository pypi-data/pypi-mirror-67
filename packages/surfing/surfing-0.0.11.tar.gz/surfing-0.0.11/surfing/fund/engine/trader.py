from ...data.struct import AssetWeight, AssetPrice, AssetPosition, AssetValue
from ...data.struct import AssetTrade, FundTrade, FundPosition
from ...data.struct import AssetTradeParam, FundTradeParam
from . import Helper
import numpy as np
class AssetTrader(Helper):

    def __init__(self, asset_param: AssetTradeParam=None):
        self.asset_param = asset_param or AssetTradeParam()

    def calc_asset_trade(self, dt, 
                               cur_position: AssetPosition, 
                               cur_price: AssetPrice, 
                               target_allocation: AssetWeight):
        cur_mv = AssetValue(prices=cur_price, positions=cur_position)
        tot_mv = cur_mv.sum()

        trades = []
        launch_trade = False
        for index_id, target_weight in target_allocation.__dict__.items():
            if index_id != 'cash':
                target_amt = tot_mv * target_weight
                p = cur_price.__dict__[index_id]
                cur_amt = cur_mv.__dict__[index_id]
                if abs(target_amt - cur_amt) > tot_mv * self.asset_param.MinCountAmtDiff:
                    amount = abs(target_amt - cur_amt)
                    is_buy = target_amt > cur_amt
                    trades.append(AssetTrade(
                        index_id=index_id, 
                        mark_price=p, 
                        amount=amount, 
                        is_buy=is_buy,
                        submit_date=dt
                    ))
                launch_trade = launch_trade or abs(target_amt - cur_amt) > tot_mv * self.asset_param.MinActionAmtDiff

        
        if not launch_trade:
            return cur_position, None
        else:
            trades.sort(key=lambda x: x.is_buy)       
            new_position = cur_position.copy()
            for trd in trades:
                new_position.update(trd)
            return new_position, trades

    def finalize_trade(self, dt, trades: list, t1_price: AssetPrice, bt_position: AssetPosition):
        pendings = []
        traded_list = []
        if trades is None or len(trades) == 0:
            return pendings, traded_list
        # TODO: if some trades needs more time
        for trd in trades:
            # TODO: commision calculate
            #trd.commission = ?
            # update position
            trd.trade_price = t1_price.__dict__[trd.index_id]
            trd.volume = trd.volume if trd.volume else (trd.amount / trd.trade_price)
            trd.trade_date = dt
            if not trd.is_buy:
                if not(bt_position.__dict__[trd.index_id] - trd.volume > -1e-8):
                    print(f'trade volume exceeds, adjusted to pos (index_id){trd.index_id} (vol){trd.volume} (is_buy){trd.is_buy} (pos){bt_position.__dict__[trd.index_id]}')
                    trd.volume = bt_position.__dict__[trd.index_id]
                    trd.amount = trd.volume * trd.trade_price
            bt_position.update(trd)
            traded_list.append(trd)
        return pendings, traded_list

class FundTrader(AssetTrader):

    def __init__(self, asset_param: AssetTradeParam=None, fund_param: FundTradeParam=None):
        AssetTrader.__init__(self, asset_param=asset_param)
        self.fund_param = fund_param or FundTradeParam()

    def calc_fund_trade(self, dt,
                              cur_asset_position: AssetPosition, 
                              cur_asset_price: AssetPrice,
                              target_allocation: AssetWeight, 
                              cur_fund_position: FundPosition, 
                              cur_fund_nav: dict, # fund_id -> nav
                              cur_fund_score: dict): # index_id -> fund_id -> score
        target_asset_position, trade_list = self.calc_asset_trade(dt,
            cur_asset_position, cur_asset_price, target_allocation)
        # 大类资产是否需要调仓的标志
        asset_needs_adjust = trade_list != None and len(trade_list) > 0
        # 如果资产需要调整，那么统一看最优的基金配置是多少（这里如果资产不需要调整，那么基金也不会调）
        if asset_needs_adjust:
            # init
            new_fund_position = cur_fund_position.copy()
            fund_trades = []

            target_asset_mv = AssetValue(prices=cur_asset_price, positions=target_asset_position)
            target_asset_wgts = target_asset_mv.get_weight()
            fund_tot_mv, cur_fund_wgts = cur_fund_position.calc_mv_n_w(fund_navs=cur_fund_nav)
            
            for index_id in target_asset_wgts.__dict__.keys():
                asset_wgt = target_asset_wgts.__dict__[index_id]
                _scores = sorted(cur_fund_score.get(index_id, {}).items(), key=lambda item: item[1], reverse=True)
                fund_weights = {}
                fund_tot_weight = 0
                fund_selected_num = 0
                for i in range(0, len(_scores)):
                    fund_id, score_as_weight = _scores[i]
                    # 最多不超过 MaxFundNumUnderAsset 个基金
                    if not np.isnan(cur_fund_nav[fund_id]):
                        fund_weights[fund_id] = score_as_weight
                        fund_tot_weight += score_as_weight
                        fund_selected_num += 1
                        if fund_selected_num == self.fund_param.MaxFundNumUnderAsset:
                            break
                #assert fund_selected_num > 0, f'index {index_id} must have at least scored fund'
                # normalize
                fund_weights = {fund_id: fund_weights[fund_id] / fund_tot_weight for fund_id in fund_weights.keys()}
                # 计算每只基金的具体仓位变动情况
                for fund_id in set(list(fund_weights.keys()) + cur_fund_position.get_funds(index_id)):
                    target_fund_amt = fund_weights.get(fund_id, 0) * asset_wgt * fund_tot_mv
                    cur_fund_volume = cur_fund_position.get_volume(fund_id) or 0
                    p = cur_fund_nav[fund_id]
                    cur_fund_amt = cur_fund_volume * p

                    if abs(target_fund_amt - cur_fund_amt) > fund_tot_mv * self.fund_param.MinCountAmtDiff or (target_fund_amt == 0 and cur_fund_amt > 0):
                        # TODO: commision and 如果是清某一只基金的逻辑，清空可以执行
                        _trade = FundTrade(
                            fund_id=fund_id,
                            index_id=index_id, 
                            mark_price=p, 
                            amount=abs(target_fund_amt - cur_fund_amt),
                            is_buy=target_fund_amt > cur_fund_amt,
                            submit_date=dt
                        )
                        fund_trades.append(_trade)
                        # print(f'(fund){fund_id} (p){p} (amt0){cur_fund_amt} (amt1){target_fund_amt} (idx){index_id} (tar){asset_mv}')

            fund_trades.sort(key=lambda x: x.is_buy)
            for _trade in fund_trades:
                new_fund_position.update(_trade)
            trade_list += fund_trades
            return new_fund_position, trade_list
        else:
            return cur_fund_position, None


    def finalize_trade(self, dt, trades: list, 
                            t1_price: AssetPrice, 
                            bt_position: AssetPosition,
                            cur_fund_position: FundPosition, 
                            cur_fund_nav: dict):

        if trades is None or len(trades) == 0:
            return [], []
        asset_trades = []
        fund_trades = []
        for trd in trades:
            if isinstance(trd, FundTrade):
                fund_trades.append(trd)
            else:
                asset_trades.append(trd)
        
        pendings, traded_list = AssetTrader.finalize_trade(self, dt, asset_trades, t1_price, bt_position)
        # TODO: if some trades needs more time
        for trd in fund_trades:
            # TODO: commision calculate
            trd.trade_price = cur_fund_nav[trd.fund_id]
            trd.volume = trd.volume if trd.volume else (trd.amount / trd.trade_price)
            trd.trade_date = dt            
            if not trd.is_buy:
                cur_vol = cur_fund_position.get_volume(trd.fund_id)
                if not((cur_vol or 0) - trd.volume > -1e-8):
                    print(f'trade volume exceeds, adjusted to pos (fund_id){trd.fund_id} (vol){trd.volume} (is_buy){trd.is_buy} (pos){cur_vol}')
                    assert cur_vol is not None, 'sell fund with no current position!'
                    trd.volume = cur_vol
                    trd.amount = trd.volume * trd.trade_price
            trade_status = cur_fund_position.update(trd)
            
            assert trade_status, f"trade failed {trd}"
            if trade_status:
                traded_list.append(trd)
        #print('trade: ', trades)
        #print()

        return pendings, traded_list
