i=1
l=[]
with open("./test.txt", "r") as f:
    cuo=0
    for line in f:
            if (i-cuo) % 13 == 0:
                l.append(line)
            elif (i-cuo) % 13 ==1 and "+" in line:
                cuo+=1
            elif (i-cuo) % 13 == 2 and "=" in line:
                cuo+=1
            elif (i-cuo) % 13 == 3 and "&" in line:
                cuo+=1
            i+=1

with open("./test2222.txt", "w") as f:
    for i in l:
        f.write(i)
