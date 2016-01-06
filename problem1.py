__author__ = 'runwei_zhang'
import math
import random

def experiment1():
    num = 10
    range = 3
    sumprob = 0.0
    for i in xrange(0,num+1):
        for j in xrange(0,num+1-i):
            for k in xrange(0,num+1-i-j):
                l = num-i-j-k
                if abs(i-j)*abs(i-j)+abs(k-l)* abs(k-l) >= range*range:
                    sumprob += math.factorial(num)/math.factorial(i)/math.factorial(j)/math.factorial(k)/math.factorial(l)
    sumprob /= math.pow(4,num)
    print sumprob

def experiment2():
    num = 60
    range = 10
    sumprob = 0.0
    for i in xrange(0,num+1):
        for j in xrange(0,num+1-i):
            for k in xrange(0,num+1-i-j):
                l = num-i-j-k
                if abs(i-j)*abs(i-j)+abs(k-l)* abs(k-l) >= range*range:
                    sumprob += math.factorial(num)/math.factorial(i)/math.factorial(j)/math.factorial(k)/math.factorial(l)
    sumprob /= math.pow(4,num)
    print sumprob

def experiment3():
    length = 10
    sumprob = 0.0
    for num in xrange(0,int(math.pow(4,length))):
        mylist = []
        for i in xrange(0,10):
            mylist.append(num % 4)
            num /= 4
        if check3(mylist):
            sumprob += 1.0
    sumprob /= math.pow(4,length)
    print sumprob

def check3(mylist):
    x,y = 0,0
    for num in mylist:
        if num==0:
            x +=1
        elif num==1:
            x -=1
        elif num==2:
            y +=1
        else:
            y -=1
        if x*x+y*y >= 25:
            return True
    return False

def experiment4():
    sumval = 0.0
    round = 100000000
    for i in xrange(0,round):
        sumval += trial4()
    print sumval /round
    return 0

def trial4():
    x,y,count = 0,0,0
    while count<60:
        rn = random.randint(0,3)
        if rn == 0:
            x -= 1
        elif rn ==1:
            x += 1
        elif rn ==2:
            y -= 1
        else:
            y += 1
        count += 1
        if x * x + y * y >= 100:
            return 1
    return 0

def experiment5():
    length = 10
    sumprob = 0.0
    for num in xrange(0,int(math.pow(4,length))):
        mylist = []
        for i in xrange(0,10):
            mylist.append(num % 4)
            num /= 4
        if check5(mylist):
            sumprob += 1.0
    sumprob /= math.pow(4,length)
    print sumprob

def check5(mylist):
    x,y = 0,0
    flag = False
    for num in mylist:
        if num==0:
            x +=1
        elif num==1:
            x -=1
        elif num==2:
            y +=1
        else:
            y -=1
        if x > 1:
            flag = True
    return flag and x<-1

def experiment6():
    sumval = 0.0
    round = 100000000
    for i in xrange(0,round):
        sumval += trial6()
    print sumval /round
    return 0

def trial6():
    x,y,count = 0,0,0
    flag = False
    while count<30:
        rn = random.randint(0,3)
        if rn == 0:
            x -= 1
        elif rn ==1:
            x += 1
        elif rn ==2:
            y -= 1
        else:
            y += 1
        count += 1
        if x>1:
            flag = True
    return flag and x<-1

def experiment7():
    sumval = 0.0
    round = 100000
    for i in xrange(0,round):
        sumval += trial7()
    print sumval /round
    return 0

def trial7():
    x,y,count = 0,0,0
    while True:
        rn = random.randint(0,3)
        if rn == 0:
            x -= 1
        elif rn ==1:
            x += 1
        elif rn ==2:
            y -= 1
        else:
            y += 1
        count += 1
        if x*x +y*y >= 100:
            break
    return count

def experiment8():
    sumval = 0.0
    round = 1000000
    for i in xrange(0,round):
        sumval += trial8()
    print sumval /round
    return 0

def trial8():
    x,y,count = 0,0,0
    while True:
        rn = random.randint(0,3)
        if rn == 0:
            x -= 1
        elif rn ==1:
            x += 1
        elif rn ==2:
            y -= 1
        else:
            y += 1
        count += 1
        if x*x +y*y >= 3600:
            break
    return count


if __name__ == "__main__":
    # experiment1()
    # experiment2()
    # experiment3()
    # experiment4()
    # experiment5()
    # experiment6()
    # experiment7()
    experiment8()