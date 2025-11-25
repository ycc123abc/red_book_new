import random
import time


class XrayTraceIdGenerator:
    MAX_SEQ = 8388607
    SEQ = random.randint(0, 2**23 - 1)
    
    @staticmethod
    def random(bits):
        return random.randint(0, 2**bits - 1)
    
    @classmethod
    def seq(cls):
        if cls.SEQ > cls.MAX_SEQ:
            cls.SEQ = 0
        cls.SEQ += 1
        return cls.SEQ


    def get_xray_trace_id(self):
        # 生成时间戳部分
        timestamp = int(time.time() * 1000)  # Date.now()返回毫秒
        # 左移23位并和序列号进行或运算
        timestamp_part = (timestamp << 23) | 5878470
        print(timestamp)
        # 生成随机部分（两个32位随机数组成64位）
        random_high = self.random(32)
        random_low = self.random(32)
        # 合并为64位值（在Python中可以直接用一个整数表示）
        random_part = (random_high << 32) | random_low
        
        # 转换为十六进制字符串并补齐到16位
        timestamp_hex = format(timestamp_part, 'x').zfill(16)
        random_hex = format(random_part, 'x').zfill(16)
        
        # 拼接结果
        trace_id = timestamp_hex + random_hex
        return trace_id
