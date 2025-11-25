import random 
import time 
initial_list =[119, 104, 96, 41]

t=4294967295

random_int  =int(t*random.random())
random_int=int(t*0.5705449357227173)
arr=[random_int&255,random_int>>8&255,random_int>>16&255,random_int>>24&255]

result_list=initial_list+arr
print(result_list)
#[119, 104, 96, 41, 159, 59, 15, 146]

t+=1
timestamp=time.time()*1000
init_digit=int(timestamp/t)

