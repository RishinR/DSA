# leetcode 51
def main():
    def issafe(row, col):
        # check column
        for i in range(n):
            if i != row and matrix[i][col] == "Q":
                return False

        # check left diagonal
        i, j = row - 1, col - 1
        while i >= 0 and j >= 0:
            if matrix[i][j] == "Q":
                return False
            i -= 1
            j -= 1

        # Check right diagonal
        i, j = row - 1, col + 1
        while i >= 0 and j < n:
            if matrix[i][j] == "Q":
                return False
            i -= 1
            j += 1

        return True

    def solve(row):
        if row == n:
            result.append(["".join(r) for r in matrix])
            return
        for col in range(n):
            if issafe(row, col):
                matrix[row][col] = "Q"
                solve(row + 1)
                matrix[row][col] = "."

    n = 4
    matrix = [["." for _ in range(n)] for _ in range(n)]
    result = []
    solve(0)
    print(result)


if __name__ == "__main__":
    main()
