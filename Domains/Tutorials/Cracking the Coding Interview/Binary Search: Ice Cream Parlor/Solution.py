t = int(raw_input().strip())
for a0 in xrange(t):
    m = int(raw_input().strip())
    n = int(raw_input().strip())
    a = map(int, raw_input().strip().split(' '))
    found = False
    for i in range(len(a)):
        for j in range(len(a)):
            if m==a[i]+a[j] and i!=j:
                found = True
                print str(i+1) + " " +str(j+1)
                break
        if found:
            break
