n = 4
x = [0] * n
def nqueens(k, n):
    global x  # Added global declaration to access the 'x' list

    if k == n:
        print(x)
        return

    for i in range(n):
        if place(k, i):
            x[k] = i+1
            nqueens(k+1, n)

def place(k, i):
    for j in range(k):
        if x[j] == i+1 or abs(x[j] - i-1) == abs(j-k):
            return False
    return True

nqueens(0, n)
