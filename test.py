n = int(input('层数：'))
A = [i for i in range(n)]
B = []
C = []
if n%2 == 0:
    towers = (A,B,C)
    tower_name = ('A','B','C')
else:
    towers = (A,C,B)
    tower_name = ('A','C','B')
top = 0
while True:
    top_next = (top+1)%3
    x = towers[top].pop(0)
    towers[top_next].insert(0,x)
    print(f'{tower_name[top]}>>{tower_name[top_next]}')
    if len(C) == n:
        break
    else:
        order_1 = top
        order_2 = (top-1)%3
        try:
            tag_1 = towers[order_1][0]
        except:
            tag_1 = n
        try:
            tag_2 = towers[order_2][0]
        except:
            tag_2 = n
        if tag_1 < tag_2:
            x = towers[order_1].pop(0)
            towers[order_2].insert(0,x)
            print(f'{tower_name[order_1]}>>{tower_name[order_2]}')
        else:
            x = towers[order_2].pop(0)
            towers[order_1].insert(0,x)
            print(f'{tower_name[order_2]}>>{tower_name[order_1]}')
        top = top_next
