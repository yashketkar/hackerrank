[d,m,y] = list(map(int,raw_input().split()))
[d2,m2,y2] = list(map(int,raw_input().split()))
if (d<=d2 and m<=m2 and y==y2) or y<y2:
    print 0
elif m<=m2 and y<=y2:
    print 15*(d-d2)
elif y<=y2:
    print 500*(m-m2)
else:
    print 10000
