def triplet(a, b, c):
    n1 = a**2 + b**2
    n2 = c**2
    if n1 == n2:
        return True
    else:
        return False
if __name__=="__main__":
    print("Enter the edges: ")
    string = input()
    edges = list(map(int, string.split(" ")))
    a = min(edges)
    c = max(edges)
    for i in edges:
        if i != a and i != c:
            b = i
    if triplet(a, b, c):
        print("The numbers {}, {}, {} are a pythagorean triplet".format(a, b, c))
    else:
        print("The numbers {}, {}, {} are not a pythagorean triplet".format(a, b, c))