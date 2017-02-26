def is_matched(value):
    words = list(value)
    mystack = []
    flag=True
    for word in words:
        if word == '{' or word == '(' or word == '[':
            mystack.append(word)
        elif word == '}' and mystack and mystack[-1] == '{':
            del mystack[-1]
        elif word == ')' and mystack and mystack[-1] == '(':
            del mystack[-1]
        elif word == ']' and mystack and mystack[-1] == '[':
            del mystack[-1]
        else:
            flag=False
            break
    if mystack:
        flag=False
    return flag

t = int(raw_input().strip())
for a0 in xrange(t):
    expression = raw_input().strip()
    if is_matched(expression) == True:
        print "YES"
    else:
        print "NO"
