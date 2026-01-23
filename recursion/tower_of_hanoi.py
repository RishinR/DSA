def solve(n, source, destination, helper):
    if n == 1:
        print(f"Disk {n} moved from {source} -> {destination}")
        return
    solve(n-1, source, helper, destination)
    print(f"Disk {n} moved from {source} -> {destination}")
    solve(n-1, helper, destination, source)

def main():
    n = 2
    solve(n, "A", "C", "H")

if __name__ == "__main__":
    main()