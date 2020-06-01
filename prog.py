import os
name_of_file = "data.txt"


def Sequence(filename):
    t = 0
    n = 0
    k = 0
    res1 = "" #res1 = 0
    res2 = ""  # res2 = 0
    try:
        f=open(filename, "r")
        words = [s5 for s1 in f for s2 in s1.split(' ') for s3 in s2.split('\n') for s4 in s3.split(',') for s5 in s4.split('\t') if s5!='']
        k = len(words)
        # for _ in words:
        #     k+=1
        if k == 0:
            print(0)
        else:
            for s in words[::-1]:
                try:
                    t=int(s)*(n)
                    if (n == 0):
                        if k==1:
                            res1 += "0" #
                            res2 += str(s) + "*x^" + str(n)  # res2 += s*(x**(n))
                        else:
                            res2 += str(s) + "*x^" + str(n) + " + "  # res2 += s*(x**(n))
                    elif n<(k-1):
                        if (n>0):
                            res1 += str(t)+"*x^"+str(n-1)+" + "  #res1 += t*(x**(n-1))
                            res2 += str(s) + "*x^" + str(n) + " + "  # res2 += s*(x**(n))
                    elif (n == (k-1)):
                        res1 += str(t) + "*x^" + str(n - 1) #res1 += t*(x**(n-1))
                        res2 += str(s) + "*x^" + str(n)  # res2 += s*(x**(n))
                except:
                    print('word ',s,' ignored',sep='')
                n += 1
        f.close()
        return res1, res2
    except FileNotError:
        print("Can't open file")
        return None


a, b = Sequence(name_of_file)
print("function derivative = ", a)
print("function = ", b)