from .fund_score_processor import FundScoreProcessor
from .fund_indicator_processor import FundIndicatorProcessor
from .derived_index_val import IndexValProcess

class DerivedDataProcessor(object):
    def __init__(self):
        self.fund_indicator_processor = FundIndicatorProcessor()
        self.fund_score_processor = FundScoreProcessor()
        self.index_val_processor = IndexValProcess()

    def process_all(self, start_date, end_date):
        self.fund_indicator_processor.process(start_date, end_date)
        self.fund_score_processor.process(start_date, end_date)
        self.index_val_processor.process(start_date, end_date)

if __name__ == '__main__':
    ddp = DerivedDataProcessor()
    start_date = '20200421'
    end_date = '20200422'
    ddp.process_all(start_date, end_date)