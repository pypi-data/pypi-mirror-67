import pandas as pd
import numpy as np
import datetime
import copy
from pprint import pprint 
import platform
import matplotlib as mpl
import pylab as pl
import matplotlib.pyplot as plt
import matplotlib.cm as cm
import matplotlib.colors as colors
import matplotlib.dates as mdates
from matplotlib.patches import Rectangle
from .asset_helper import SAAHelper, TAAHelper
from .painter.asset_painter import AssetPainter
from .painter.fund_painter import FundPainter
from .painter.hybrid_painter import HybridPainter
from ...data.manager.manager_fund import FundDataManager
from ...data.struct import AssetWeight, AssetPosition, AssetPrice, AssetValue
from ...data.struct import FundPosition, FundPosItem, FundTrade
from ...data.manager.score import FundScoreManager

CURRENT_PLATFORM = platform.system()
if CURRENT_PLATFORM == 'Darwin':
    mpl.rcParams['font.family'] = ['Heiti TC']
else:
    mpl.rcParams['font.family'] = ['STKaiti']

class ReportHelper:
    
    '''
    save backtest history
    '''
    TRADING_DAYS_PER_YEAR = 242

    def __init__(self):
        pass

    def init(self): 
        pass

    def plot_init(self, dm, taa_helper):
        self.index_price = dm.get_index_price()
        self.fund_info = dm.get_fund_info()
        self.fund_nav = dm.dts.fund_nav
        self.fund_indicator = dm.dts.fund_indicator
        self.taa_params = taa_helper.params if isinstance(taa_helper, TAAHelper) else None
        self.index_pct = dm.dts.index_pct

    def setup(self, saa:AssetWeight):
        self.saa_weight = saa.__dict__
        self.asset_cash_history = {}
        self.asset_position_history = {}
        self.asset_market_price_history = {}
        self.pending_trade_history = {}
        self.asset_weights_history = {}
        self.tactic_history = {}
        self.fund_position_history = {}
        self.trade_history = {}
        self.rebalance_date = []
        self.fund_cash_history = {}
        self.fund_marktet_price_history = {}
        self.fund_weights_history = {}
        self.fund_score = {}
        self.fund_score_raw = {}
        self.target_allocation = {}

    def update(self,dt:datetime, asset_cur_position:AssetPosition, asset_cur_price:AssetPrice, pend_trades:list, fund_cur_position:FundPosition, fund_nav:dict, traded_list:list, fund_score:dict, fund_score_raw:dict, target_allocation):   
        # 检查回测时使用
        self.asset_cash_history[dt] = asset_cur_position.cash##
        self.asset_position_history[dt] = asset_cur_position.__dict__##
        self.pending_trade_history[dt] = pend_trades##
        if fund_cur_position is not None:
            dic = {f : f_info.__dict__  for f, f_info in fund_cur_position.funds.items()}
            for f, f_info in dic.items():
                f_info['price'] =  fund_nav[f]
            self.fund_position_history[dt] = dic##        
            self.fund_cash_history[dt] = fund_cur_position.cash
            mv, fund_w = fund_cur_position.calc_mv_n_w(fund_navs=fund_nav)
            self.fund_marktet_price_history[dt] = mv
            self.fund_weights_history[dt] = { fund_id : w_i for fund_id, w_i in fund_w.items() if w_i > 0}
            self.fund_score[dt] = fund_score
            self.fund_score_raw[dt] = fund_score_raw

        self.asset_market_price_history[dt] = AssetValue(prices=asset_cur_price, positions=asset_cur_position).sum() 
        asset_w = AssetValue(prices=asset_cur_price, positions=asset_cur_position).get_weight().__dict__
        self.asset_weights_history[dt] = { index_id : w_i for index_id, w_i in asset_w.items() if w_i > 0}
        if traded_list is not None:
            if len(traded_list) > 0:
                self.trade_history[dt] = traded_list
        self.target_allocation[dt] = target_allocation

    def _calc_stat(self, df):
        year = df.shape[0]/self.TRADING_DAYS_PER_YEAR
        total_return = df['mv'][-1] / df['mv'][0]
        try:
            five_year_return = (df['mv'][-1] / df['mv'][-(5 * self.TRADING_DAYS_PER_YEAR)] - 1)
        except:
            five_year_return = five_year_return = (df['mv'][-1] / df['mv'][0] - 1)
        annualized_return = np.exp(np.log(total_return)/year) - 1
        annualized_volatiltity = (df['mv'].shift(1) / df['mv']).std() * np.sqrt((df.shape[0] - 1) / year)
        sharpe = annualized_return / annualized_volatiltity
        mdd = 1 - (df.loc[:, 'mv'] / df.loc[:, 'mv'].rolling(10000, min_periods=1).max()).min()
        mdd_part1 = (df.loc[:, 'mv'] / df.loc[:, 'mv'].rolling(10000, min_periods=1).max())
        mdd_date1 = df.loc[:mdd_part1.idxmin(),'mv'].idxmax()
        mdd_date2 = mdd_part1.idxmin()
        w = copy.deepcopy(self.saa_weight)
        w['mdd'] = mdd
        w['annual_ret'] = annualized_return
        w['sharpe'] = sharpe
        w['5_year_ret'] = five_year_return
        w['annual_vol'] = annualized_volatiltity
        w['mdd_d1'] = mdd_date1
        w['mdd_d2'] = mdd_date2
        w['market_value'] = df
        return w

    def get_asset_stat(self):
        self.asset_mv = pd.DataFrame([ {'date':k, 'mv':v} for k,v in self.asset_market_price_history.items()]).set_index('date')
        w = self._calc_stat(self.asset_mv.copy())
        return w
    
    def get_fund_stat(self):
        self.fund_mv = pd.DataFrame([ {'date':k, 'mv':v} for k,v in self.fund_marktet_price_history.items()]).set_index('date')
        w = self._calc_stat(self.fund_mv.copy())
        return w

    def get_fund_trade(self):
        fsdf = self.fund_score.copy()
        fund_info_df = self.fund_info.copy().set_index('fund_id')
        fund_trade = []
        for d in self.trade_history:
            f_t = [ i.__dict__  for i in self.trade_history[d] if isinstance(i, FundTrade)]
            fund_trade.extend(f_t)
        if len(fund_trade) < 1:
            return pd.DataFrame()
        ft_res = []
        for ft in fund_trade:
            ft['desc_name'] = fund_info_df.loc[ft['fund_id'], 'desc_name']
            index_id = fund_info_df.loc[ft['fund_id'], 'index_id']
            try:
                s = fsdf[ft['submit_date']][index_id][ft['fund_id']]
            except:
                s = np.nan
            ft['submit_d_score'] = s
            fund_id = ft['fund_id']
            submit_d = ft['submit_date']
            traded_d = ft['trade_date']
            ft['before_w']  = self.fund_weights_history[submit_d].get(fund_id,0)
            ft['after_w'] = self.fund_weights_history[traded_d].get(fund_id,0)
            ft_res.append(ft)
        fund_trade_df = pd.DataFrame(ft_res)
        return fund_trade_df

    def get_asset_trade(self):
        asset_trade = []
        for d in self.trade_history:
            a_t = [ i.__dict__  for i in self.trade_history[d] if not isinstance(i, FundTrade)]
            asset_trade.extend(a_t) 
        res = []
        for dic in asset_trade: 
            index_id = dic['index_id']
            submit_d = dic['submit_date']
            traded_d = dic['trade_date']
            dic['before_w'] = self.asset_weights_history[submit_d].get(index_id, 0)
            dic['after_w'] = self.asset_weights_history[traded_d].get(index_id, 0)
            res.append(dic)
        return pd.DataFrame(res)

    def backtest_asset_plot(self):
        bt_type = 'asset'
        print(f'{bt_type} report')
        w = self.get_asset_stat()
        del w['market_value']
        pprint(w)
        AssetPainter.plot_asset_weights(self.asset_weights_history)
        HybridPainter.plot_market_value(self.asset_mv, bt_type, self.index_price, self.saa_weight)
        AssetPainter.plot_asset_mdd_period(self.asset_mv, self.saa_weight, self.index_price)

    def backtest_fund_plot(self):
        bt_type = 'fund'
        print(f'{bt_type} report')
        w = self.get_fund_stat()
        del w['market_value']
        pprint(w)
        
        FundPainter.plot_fund_weights(self.fund_weights_history, self.fund_cash_history, self.fund_marktet_price_history)
        HybridPainter.plot_market_value(self.fund_mv, bt_type, self.index_price, self.saa_weight)
        FundPainter.plot_fund_mdd_periods(self.fund_mv, self.fund_weights_history, self.fund_nav, self.fund_info)
        HybridPainter.plot_asset_fund_mv_diff(self.asset_mv, self.fund_mv)

    def plot_whole(self):
        bt_type = 'asset'
        print(f'{bt_type} report')
        w = self.get_asset_stat()
        del w['market_value']
        pprint(w)
        AssetPainter.plot_asset_weights(self.asset_weights_history)
        HybridPainter.plot_market_value(self.asset_mv, bt_type, self.index_price, self.saa_weight)
        AssetPainter.plot_asset_mdd_period(self.asset_mv, self.saa_weight, self.index_price)
        
        bt_type = 'fund'
        print(f'{bt_type} report')
        w = self.get_fund_stat()
        del w['market_value']
        pprint(w)
        FundPainter.plot_fund_weights(self.fund_weights_history, self.fund_cash_history, self.fund_marktet_price_history)
        HybridPainter.plot_market_value(self.fund_mv, bt_type, self.index_price, self.saa_weight)
        FundPainter.plot_fund_mdd_periods(self.fund_mv, self.fund_weights_history, self.fund_nav, self.fund_info)
        HybridPainter.plot_asset_fund_mv_diff(self.asset_mv, self.fund_mv)
    
    def _plot_fund_score(self, asset, is_tuning):
        FundPainter.plot_fund_score(self.fund_mv, 
                                    self.fund_weights_history, 
                                    self.trade_history,
                                    self.index_price, 
                                    self.asset_weights_history,
                                    self.fund_info,
                                    self.fund_nav,
                                    self.fund_score,
                                    self.fund_score_raw,
                                    self.fund_indicator,
                                    asset,
                                    is_tuning,
                                    )
   
    def _index_pct_plot(self, index_id:str, saa_mv:pd.DataFrame, taa_mv:pd.DataFrame):
        AssetPainter.plot_taa_analysis(saa_mv, taa_mv, index_id, self.index_pct, self.taa_params, self.index_price)
        
    def _plot_taa_saa(self, saa_mv, taa_mv, index_id):
        AssetPainter.plot_asset_taa_saa(saa_mv, taa_mv, index_id, self.index_pct)
       