blist = [1, 2, 3, 4]
b = blist[0]
multi = 1
for i in range(1, len(blist)):
    b = blist[i]
    multi = b * multi
print(multi)
