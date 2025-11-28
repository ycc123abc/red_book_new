import random 
import time 

initial_list =[119, 104, 96, 41]

t=4294967295
qarams='/api/sns/web/v1/homefeed{"cursor_score": "","num": 39,"refresh_type": 1,"note_index": 33,"unread_begin_note_id": "","unread_end_note_id": "","unread_note_count": 0,"category": "homefeed_recommend","search_key": "","need_num": 14,"image_formats": ["jpg","webp","avif"],"need_filter_image": false}'
md5_str='b5c8461d9b11f34d56d087d95db75a6b'

a1='19ab462768dbnostuyyqujnz1j5fyrt8egmfrrr1n50000440764'
random_int  =int(t*random.random())
random_int=int(t*0.3645888406208544)

arr=[random_int&255,random_int>>8&255,random_int>>16&255,random_int>>24&255]

result_list=initial_list+arr
print(result_list)
# [119, 104, 96, 41, 159, 59, 15, 146]

t+=1
timestamp=1764139892236
# timestamp=int(time.time()*1000)
integer_part=int(timestamp / t)
fractional_part = (timestamp / t) - integer_part
init_num = int(fractional_part * t)

right_move=0
c=0

num_list_second=[]
result=0
print("init_num",init_num)
for i in range(4):
    a=init_num>>right_move
    b=a&255
    num_list_second.append(b)
    if i==0:
        c=0
        d=b
    else:
        c+=b
        d=c&255
    right_move+=8
    result=d
    print(a, b, c, d,result)
print(integer_part,result)
for i in range(4):
    init_num=integer_part
    first_num=init_num&255
    second_num=init_num+result
    third_num=second_num&255
    fourth_num=third_num+1
    print(init_num,first_num,second_num,third_num,fourth_num)

result_list.append(fourth_num^41)
for index,value in enumerate(num_list_second):
    if index==0:
        continue
    result_list.append(value^41)
result_list+=[179,40,41,41]
print(result_list)
###################
init_part=int((0.18809002079069614)*(t+1))
print(init_part)
right_move=0
for i in range(8):
    result_num=init_part&255
    init_part=init_part>>8
    result_list.append(result_num)
print(result_list)
#####################
init_part=1
for i in range(4):
    result_num=init_part&255
    init_part=init_part>>8
    result_list.append(result_num)
print(result_list)
#####################
init_part=int(random.randint(150,200))
for i in range(4):
    result_num=init_part&255
    init_part=init_part>>8
    result_list.append(result_num)
print(result_list)
#####################
init_part=len(qarams)
for i in range(4):
    result_num=init_part&255
    init_part=init_part>>8
    result_list.append(result_num)
print(result_list,len(result_list))
#####################
for i in range(0, len(md5_str), 2):
    pair = md5_str[i:i+2]
    result_list.append(int(pair, 16)^result_list[4])
    if i==14:
        break
print(result_list,len(result_list))
#####################
# 转换为字节数组 (类似于 Uint8Array)
a1_byte_array = a1.encode('utf-8')
a1_byte_array_list = list(a1_byte_array)
#“xhs-pc-web” 生成数组   120, 104, 115, 45, 112, 99, 45, 119, 101, 98]  10 为固定值
result_list=result_list+[52]+a1_byte_array_list+[10, 120, 104, 115, 45, 112, 99, 45, 119, 101, 98]
print(result_list,len(result_list))
#####################
#248, 172, 102, 103, 201, 182, 129, 98, 95, 7, 68, 251,132, 21]  暂时固定
result_list+=[1, result_list[4]^115, 248, 172, 102, 103, 201, 182, 129, 98, 95, 7, 68, 251,132, 21]
print(result_list,len(result_list))
#######################
str_val = 'e6483ca2a1eed5e3'
uint8_list = [ord(char) for char in str_val]
print("uint8_list",uint8_list)
def convert_to_uint32_array(n, r):
    """
    将字节数组转换为32位无符号整数数组
    
    Args:
        n: 输入的字节数组（列表）
        r: 布尔值，决定是否添加长度信息
        
    Returns:
        32位无符号整数列表
    """
    e = len(n)
    a = e >> 2  # 等价于 e // 4
    
    # 如果长度不是4的倍数，增加一个单位
    if (3 & e) != 0:  # 等价于 e % 4 != 0
        a += 1
    
    # 根据参数r决定是否添加长度信息
    if r:
        t = [0] * (a + 1)
        t[a] = e  # 在末尾存储原始长度
    else:
        t = [0] * a
    
    # 将输入数组n的每个字节按小端序打包到数组中
    for o in range(e):
        t[o >> 2] |= n[o] << ((3 & o) << 3)  # 等价于 t[o // 4] |= n[o] << ((o % 4) * 8)
    
    return t
key=convert_to_uint32_array(uint8_list, False)
result_list = [119, 104, 96, 41, 186, 177, 85, 93, 236, 87, 199, 151, 179, 40, 41, 41, 232, 170, 38, 48, 0, 0, 0, 0, 1, 0, 0, 0, 200, 0, 0, 0, 39, 1, 0, 0, 15, 114, 252, 167, 33, 171, 73, 247, 52, 49, 57, 97, 98, 52, 54, 50, 55, 54, 56, 100, 98, 110, 111, 115, 116, 117, 121, 121, 113, 117, 106, 110, 122, 49, 106, 53, 102, 121, 114, 116, 56, 101, 103, 109, 102, 114, 114, 114, 49, 110, 53, 48, 48, 48, 48, 52, 52, 48, 55, 54, 52, 10, 120, 104, 115, 45, 112, 99, 45, 119, 101, 98, 1, 201, 248, 172, 102, 103, 201, 182, 129, 98, 95, 7, 68, 251, 132, 21]
data=convert_to_uint32_array(result_list, True)
class OptimizedDecryptor:
    """使用类来避免重复计算常量"""
    
    def __init__(self):
        self.const = 1013904243
        self.n_mapping = {4: 3, 5: 0, 6: 1}
    
    def single_decrypt(self, m, x, a, idx, n, key, sign=1):
        """优化的单个解密操作"""
        n_val = self.n_mapping.get(n, n)
        k = (n_val ^ idx) % 4
        
        number_7 = ((a >> 5) ^ (x << 2)) + ((x >> 3) ^ (a << 4))
        number_12 = (m ^ x) + (a ^ key[k])
        
        result = number_7 ^ number_12
        
        if sign != 1:
            print(f"Debug: n={n}, idx={idx}, k={k}, result={result}")
            
        return result
    
    def get_iv(self, e):
        return e / self.const, e + self.const
    
    def decrypt(self, r, key):
        """使用优化算法的解密"""
        length = len(r)
        last_idx = length - 1
        a = r[last_idx]
        e = 0
        
        iterations = 6 + 52 // length
        
        for _ in range(iterations):
            n, e = self.get_iv(e)
            n_int = int(n)
            
            for idx in range(last_idx):
                x = r[idx + 1]
                r[idx] = (r[idx] + self.single_decrypt(e, x, a, idx, n_int, key)) & 0xFFFFFFFF
                a = r[idx]
            
            x = r[0]
            r[last_idx] = (r[last_idx] + self.single_decrypt(e, x, a, last_idx, n_int, key)) & 0xFFFFFFFF
            a = r[last_idx]
        
        return r

decryptor = OptimizedDecryptor()
result2 = decryptor.decrypt(data.copy(), key)
print(result2)
######################
def uint32_array_to_uint8_array(uint32_arr):
    """
    将一个32位无符号整数列表转换为8位无符号整数列表
    
    Args:
        uint32_arr: 包含32位无符号整数的列表
        
    Returns:
        包含8位无符号整数的列表
    """
    byte_length = len(uint32_arr) * 4
    uint8_arr = [0] * byte_length
    
    for i in range(len(uint32_arr)):
        value = uint32_arr[i]
        offset = i * 4
        
        # 小端序转换
        uint8_arr[offset]     = (value >> 0)  & 0xFF
        uint8_arr[offset + 1] = (value >> 8)  & 0xFF
        uint8_arr[offset + 2] = (value >> 16) & 0xFF
        uint8_arr[offset + 3] = (value >> 24) & 0xFF
    
    return uint8_arr
result_list=uint32_array_to_uint8_array(result2)
#######################
def Base64(t, tt):
    """
    将输入的字节列表进行自定义 Base64 编码
    
    Args:
        t: 128位的字节列表
        tt: 自定义的Base64字符集
    
    Returns:
        str: 编码后的字符串
    """
    tt = tt + "FTKdeNOwxWXYZap89+/A4UVLhijkl63G"
    r = []
    
    for e in range(0, len(t), 3):
        o = t[e]
        l = t[e + 1] if e + 1 < len(t) else 0
        n = t[e + 2] if e + 2 < len(t) else 0
        
        u = o << 16 | l << 8 | n
        F = [
            (u >> 18) & 63,
            (u >> 12) & 63,
            (u >> 6) & 63,
            u & 63
        ]
        
        _ = 0 if len(t) - e >= 3 else 3 - (len(t) - e)
        
        for f in range(4 - _):
            r.append(tt[F[f]])
            
        for h in range(_):
            r.append("=")
    
    return "".join(r)
print("mns0201_"+Base64(result_list, 'MfgqrsbcyzPQRStuvC7mn501HIJBo2DE'))