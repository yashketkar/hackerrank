# Enter your code here. Read input from STDIN. Print output to STDOUT
n = int(raw_input())
for i in range(n):
    stringA = raw_input()
    stringB = []
    stringC = []
    for j in range(0,len(list(stringA)),2):
        stringB.append(list(stringA)[j])
    for j in range(1,len(list(stringA)),2):
        stringC.append(list(stringA)[j])
    print "".join(stringB) + " " + "".join(stringC)
