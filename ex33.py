
numbers = []

#Uses while loop
def loop(limit,incrementer):
    i = 0
    while i < limit:
        print "At the top i is %d" % i
        numbers.append(i)

        i = i + incrementer
        print "Numbers now: ", numbers
        print "At the bottom i is %d" % i

#Uses for loop
def forLoopy(limit,incrementer):
    for i in range(0,limit,incrementer):
        numbers.append(i)
        print "Numbers now: ", numbers
        print "At the bottom i is %d" % i

loop(9,2)
forLoopy(9,2)

print "The numbers: "

for num in numbers:
    print num
