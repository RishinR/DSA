def sum(a, n):
    if n == 0 :
        return 0
    return a[n] + sum(a, n-1)
def reverseTraversal(a, n):
    if n < 0:
        return 
    print(a[n])
    reverseTraversal(a, n-1)

def traversal(a, i):
    if i > len(a)-1:
        return
    print(a[i])
    traversal(a, i+1)

minimum = 0
def findmin(a, j):
    # global needs to be used as python creates a local variable named minimum 
    global minimum 
    if j > len(a) - 1:
        return 
    if a[j] < a[minimum]:
        minimum = j
    findmin(a, j+1)

a = [1, 5, 3, 0, 4, -1, 10]
print("The sum of all elements in the array is: ")
print(sum(a, len(a)-1))
print("The reverse traversal of the array is: ")
reverseTraversal(a, len(a)-1)
print("The traversal of the list is: ")
traversal(a, 0)
print("The minimum element is: ")
findmin(a, 0)
print(a[minimum])