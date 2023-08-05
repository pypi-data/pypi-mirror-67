from .processor import IfaProcessor
from .message_parser import WechatMessageParser
from .message_sender.image_message_sender import ImageMessageSender
from .message_sender.text_message_sender import TextMessageSender
import time
import json
import urllib.parse
import sys
import datetime
from .config import Configurator
from .struct import WxMsgItem

class WechatMessageProcessor(IfaProcessor):

    def __init__(self):
        self.message_parser = WechatMessageParser()
        self.image_message_sender = ImageMessageSender()
        self.text_message_sender = TextMessageSender()

        self.start_ts = int(datetime.datetime.now().timestamp() * 1000)

    def process(self, msg: WxMsgItem):
        if msg.msgtime < self.start_ts:
            return

        if len(msg.to_ids) != 1 or msg.to_ids[0] != '006':
            return

        if not (msg.from_id.startswith('wo') or msg.from_id.startswith('wm')):
            return

        result = self.message_parser.parse(msg.from_id, msg.to_ids, msg.text_content)
        # we can handle scenario 1 only
        if result['type'] == 'fund':
            target_url = 'http://fund.puyuan.tech/FundInfo?id='
            content = target_url + urllib.parse.quote_plus(result['fund'])
            self.text_message_sender.send(msg.to_ids, content)
            self.image_message_sender.send(msg.to_ids, content)
        else:
            content = json.dumps(result)
            self.text_message_sender.send(msg.to_ids, content)

if __name__ == "__main__":
    if len(sys.argv) > 1:
        config_path = sys.argv[1]
        print(f'config path is set: {config_path}')
        Configurator(config_path).config_path = config_path
    wmp = WechatMessageProcessor()
    wmp.run()