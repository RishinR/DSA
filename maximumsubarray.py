""" kickstart question """
if __name__=="__main__":
    string = input()
    a = list(map(int, string.split(" ")))
    n = len(a)
    pd = a[1] - a[0] #previous difference
    current = 2 # current length of substring
    ans = 2 # min length of substring anyways
    for j in range(2, n):
        if pd == a[j] - a[j-1]:
            current += 1 # if the next pair have the same pd
            # then count can be incremented by 1
        else:
            pd = a[j] - a[j-1]
            current = 2# if the next pair have a different pd 
            # then we will change the pd to the new difference
            # set currrent max length = 2 
        ans = max(current, ans)
    print(ans)