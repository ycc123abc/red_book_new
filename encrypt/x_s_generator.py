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


