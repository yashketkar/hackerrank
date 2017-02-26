def number_needed(a, b):
    x = list(a)
    y = list(b)
    add = 0
    for s in list('abcdefghijklmnopqrstuvwxyz'):
        l = x.count(s) if x.count(s)<y.count(s) else y.count(s)
        add = add +l
    return len(x+y)-2*add

a = raw_input().strip()
b = raw_input().strip()

print number_needed(a, b)
