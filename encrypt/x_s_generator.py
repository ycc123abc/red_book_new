import random 
import time 
initial_list =[119, 104, 96, 41]

t=4294967295
qarams='/api/sns/web/v1/homefeed{"cursor_score": "","num": 39,"refresh_type": 1,"note_index": 33,"unread_begin_note_id": "","unread_end_note_id": "","unread_note_count": 0,"category": "homefeed_recommend","search_key": "","need_num": 14,"image_formats": ["jpg","webp","avif"],"need_filter_image": false}'
md5_str='b5c8461d9b11f34d56d087d95db75a6b'
cookie='abRequestId=9f029439-8c95-5463-a15b-48bd5bf64748; a1=19ab462768dbnostuyyqujnz1j5fyrt8egmfrrr1n50000440764; webId=401ec8f68cc5bc61d5d759d23190de90; gid=yj0D4KJ0q2dKyj0D4KJWKkFFYfDIlM97vvA76yIVIuyV2i28ivF9YF888448WK488SKiKy8f; xsecappid=xhs-pc-web; webBuild=4.86.0; websectiga=f3d8eaee8a8c63016320d94a1bd00562d516a5417bc43a032a80cbf70f07d5c0; unread={%22ub%22:%2269087af10000000003037d22%22%2C%22ue%22:%2269120603000000000303647d%22%2C%22uc%22:41}; loadts=1764142964607'
a1='19ab462768dbnostuyyqujnz1j5fyrt8egmfrrr1n50000440764'
random_int  =int(t*random.random())
random_int=int(t*0.3645888406208544)
arr=[random_int&255,random_int>>8&255,random_int>>16&255,random_int>>24&255]

result_list=initial_list+arr
print(result_list)
# [119, 104, 96, 41, 159, 59, 15, 146]

t+=1
timestamp=1764139892236
integer_part=int(timestamp / t)
fractional_part = (timestamp / t) - integer_part

init_num = int(fractional_part * t)
right_move=0
c=0

num_list_second=[]
result=0
print(init_num)
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
print(num_list_second)
for i in range(4):
    init_num=integer_part
    first_num=init_num&255
    second_num=init_num+result
    third_num=second_num&255
    fourth_num=third_num+1
print(fourth_num)

result_list.append(fourth_num^41)
for index,value in enumerate(num_list_second):
    if index==0:
        continue
    result_list.append(value^41)
result_list+=[179,40,41,41]
print(result_list)
###################
init_part=int((0.18809002079069614)*(t+1))
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
print(convert_to_uint32_array(uint8_list, False))
t=[
  119,104,96,
  41,220,
  136,
  242,
  84,
  174,
  16,
  216,
  235,
  179,
  40,
  41,
  41,
  0,
  0,
  0,
  0,
  0,
  0,
  0,
  0,
  1,
  0,
  0,
  0,
  186,
  0,
  0,
  0,
  27,
  0,
  0,
  0,
  172,
  193,
  161,
  109,
  244,
  43,
  75,
  235,
  52,
  49,
  57,
  57,
  97,
  52,
  50,
  55,
  54,
  101,
  51,
  100,
  122,
  109,
  56,
  104,
  107,
  113,
  118,
  121,
  116,
  117,
  108,
  113,
  109,
  120,
  116,
  104,
  97,
  109,
  106,
  114,
  102,
  103,
  103,
  101,
  121,
  113,
  102,
  49,
  100,
  55,
  51,
  48,
  48,
  48,
  48,
  51,
  49,
  48,
  55,
  55,
  54,
  10,
  120,
  104,
  115,
  45,
  112,
  99,
  45,
  119,
  101,
  98,
  1,
  175,
  248,
  172,
  102,
  103,
  201,
  183,
  129,
  98,
  95,
  7,
  68,
  251,
  132,
  21,
]
print(convert_to_uint32_array(t, True))

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


result_list=uint32_array_to_uint8_array([
  3824717586, 2279402056, 976766202, 1217645403, 812956054, 2118438510,
  1868406736, 1622411888, 3030276304, 3612621250, 763288327, 1639915843,
  3835578375, 1142288051, 3765211505, 2132232372, 2862751668, 2501687603,
  2725868098, 3114663414, 2517332015, 3788305621, 3361130946, 4009640323,
  570483359, 4032519973, 3452718685, 1660408586, 3501996765, 1249338241,
  4018719874, 1131506642
])
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

result_list=[217, 58, 64, 18, 211, 179, 207, 20, 101, 138, 197, 76, 138, 224, 164, 127, 169, 159, 126, 247, 158, 156, 204, 117, 107, 75, 92, 100, 168, 142, 18, 207, 98, 58, 68, 106, 15, 5, 70, 216, 189, 170, 146, 44, 168, 98, 54, 125, 82, 195, 140, 51, 91, 84, 92, 203, 142, 10, 10, 67, 83, 132, 226, 94, 28, 177, 25, 118, 95, 228, 164, 228, 203, 198, 72, 12, 57, 251, 57, 160, 110, 129, 197, 172, 166, 164, 254, 0, 254, 199, 218, 69, 110, 39, 39, 181, 98, 159, 45, 168, 34, 105, 225, 240, 21, 164, 168, 25, 137, 189, 17, 50, 112, 217, 96, 102, 16, 165, 35, 240, 218, 150, 242, 143, 104, 103, 108, 168]
print("mns0201_"+Base64(result_list, 'MfgqrsbcyzPQRStuvC7mn501HIJBo2DE'))