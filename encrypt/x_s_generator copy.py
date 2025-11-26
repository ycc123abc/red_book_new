import random
import time

class XSGenerator:
    def __init__(self, initial_list=None):
        """
        初始化XSGGenerator类
        
        Args:
            initial_list (list): 初始值列表，默认为[119, 104, 96, 41]
        """
        self.initial_list = initial_list or [119, 104, 96, 41]
        self.t = 4294967295
        self.timestamp=time.time()*1000
        self.random_seed=random.random()
        self.timestamp=1764066115679
        self.random_seed=0.5705449357227173


    
    def generate_random_array(self):
        """
        生成随机数组部分
        
        Args:
            seed (float): 随机数种子，如果不提供则使用随机数
            
        Returns:
            list: 包含初始值和随机值的组合列表
        """
        random_int = int(self.t * self.random_seed)
        
        arr = [
            random_int & 255,
            (random_int >> 8) & 255,
            (random_int >> 16) & 255,
            (random_int >> 24) & 255
        ]
        
        return self.initial_list + arr
    
    def calculate_timestamp_parts(self):
        """
        计算时间戳相关数值
        
        Args:
            timestamp (int): 时间戳
            
        Returns:
            tuple: (integer_part, fractional_part, init_num)
        """
        integer_part = int(self.timestamp / (self.t + 1))
        fractional_part = (self.timestamp / (self.t + 1)) - integer_part
        init_num = int(fractional_part * (self.t + 1))
        
        return integer_part, fractional_part, init_num
    
    def process_num_list_second(self, init_num):
        """
        处理num_list_second数组和结果计算
        
        Args:
            init_num (int): 初始数值
            
        Returns:
            tuple: (num_list_second, result)
        """
        right_move = 0
        c = 0
        result = 0
        num_list_second = []
        
        for i in range(4):
            a = init_num >> right_move
            b = a & 255
            num_list_second.append(b)
            
            if i == 0:
                c = 0
                d = b
            else:
                c += b
                d = c & 255
                
            right_move += 8
            result = d
            
        return num_list_second, result
    
    def calculate_fourth_num(self, integer_part, result):
        """
        计算fourth_num值
        
        Args:
            integer_part (int): 整数部分
            result (int): 前面计算出的结果值
            
        Returns:
            int: fourth_num值
        """
        init_num = integer_part
        first_num = init_num & 255
        second_num = init_num + result
        third_num = second_num & 255
        fourth_num = third_num + 1
        
        return fourth_num
    
    def generate_x_s(self):
        """
        生成完整的x-s值列表
        
        Args:
            timestamp (int): 时间戳，如果不提供则使用当前时间
            random_seed (float): 随机数种子，可选
            
        Returns:
            list: 完整的x-s值列表
        """
        
        # 生成基础列表
        result_list = self.generate_random_array()
        
        # 计算时间戳相关值
        integer_part, fractional_part, init_num = self.calculate_timestamp_parts()
        
        # 处理num_list_second
        num_list_second, result = self.process_num_list_second(init_num)
        
        # 计算fourth_num
        fourth_num = self.calculate_fourth_num(integer_part, result)
        
        # 添加异或处理后的值
        result_list.append(fourth_num ^ 41)
        for index, value in enumerate(num_list_second):
            if index == 0:
                continue
            result_list.append(value ^ 41)
        
        # 添加固定结尾
        result_list += [179, 40, 41, 41]


        
        return result_list

# 使用示例
if __name__ == "__main__":
    generator = XSGenerator()
    
    # 使用默认参数生成
    x_s_result = generator.generate_x_s()
    print("默认生成结果:", x_s_result)
    
    # 使用指定的时间戳和随机种子生成（复现原始代码结果）
    x_s_result_fixed = generator.generate_x_s()
    print("固定参数生成结果:", x_s_result_fixed)