import os
name_of_file = data.txt


def Sequence(filename):
    t = 0
    n = 0
    k = 0
    try:
        f=open(filename, "r")
         for s in [s5 for s1 in f for s2 in s1.split(' ') for s3 in s2.split('\n') for s4 in s3.split(',') for s5 in s4.split('\t') if s5!='']: 
           try:
             k+=1
        for s in [s5 for s1 in f for s2 in s1.split(' ') for s3 in s2.split('\n') for s4 in s3.split(',') for s5 in s4.split('\t') if s5!='']: 
            try:
                n+=1
                t=int(s)*(n-1)
                if n<k
                 if (n>0)
                 print(t,"*x^",n-1,"+") 
            except:
                print('word ',s,' ignored',sep='')
       
            return res
        elif (n==s):
            print(t,"*x^",s)
        elif (n==0):
            return 0
        f.close()
    except FileNotError:
        print("Can't open file")
        return None


a = Sequence(name_of_file)