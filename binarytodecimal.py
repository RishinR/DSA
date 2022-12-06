def binarytodecimal(n):    
    num = 0
    i = 0
    while(n>0):
        rem = n%10
        num += rem*(2**i)
        i += 1
        n = int(n/10)
    # print(num)
    return num
if __name__=="__main__":
    n = int(input())
    print(binarytodecimal(n))