import logging
import fileinput
import os
import time
from typing import Any

class LoggerCollect:
    
    def __init__(self, filename) -> None:
        self.logpath = filename
        self.time_kick = 5
        self.record_count = 0
        self.init_flag = True
        self.pre_time = int(time.time() * 1000)
        self.offset = 0
        
    def process(self, line) -> Any:
        print(line, self.offset)
        
    def output(self, data) -> None:
        output_eng = ""
        dict(
            clickhouse=ClickHouseEng,
            elasticsearch=ElasticSeachEng,
            kafka=KafkaEng,
        )[output_eng](data)
        pass
        
    def handler(self, line) -> None:
        self.now_time = int(time.time() * 1000)
        if self.now_time == self.pre_time:
            self.offset += 1
        else:
            self.offset = 0
        self.output(self.process(line))
        self.pre_time = int(time.time() * 1000)
    
    def _first_read(self) -> None:
        self.record_count = 0
        for line in fileinput.input(self.logpath):
            self.handler(line)
            self.record_count += 1
        
    def start(self) -> None:
        while True:
            logging.info(f"current read: {self.record_count} lines")
            if not os.path.exists(self.logpath):
                time.sleep(self.time_kick)
                continue
            try:
                if self.init_flag:
                    self._first_read()
                    self.init_flag = False
                    continue
                
                total_count = int(os.popen(f'wc -l {self.logpath}').read().split()[0])
                if total_count < self.record_count:
                    self._first_read()
                    continue
                
                for line in fileinput.input(self.logpath):
                    line_no = fileinput.filelineno()
                    if line_no > self.record_count:
                        self.handler(line)
                        self.record_count += 1
                        
                time.sleep(self.time_kick)
                        
            except Exception as e:
                logging.error(f'faild messages: {e}')
                
                
                

