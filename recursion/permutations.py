# leetcode 46
def main():
    def solve(index, subarr, visited):
        if index == len(nums):
            result.append(subarr.copy())
            return

        for num in nums:
            if num not in visited:
                visited.add(num)
                subarr.append(num)
                solve(index + 1, subarr, visited)
                visited.remove(num)
                subarr.pop()

    nums = [1, 2, 3]
    result = []
    solve(0, [], set())
    print(result)


if __name__ == "__main__":
    main()
