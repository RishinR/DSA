class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        def sum_all(l):
            start = l[0]
            for i in range(1, len(l)):
                carry = 0
                len1 = len(start)
                len2 = len(l[i])

                j, k = 0, 0
                out = ""
                while j < len1 and k < len2:
                    curr_sum = int(start[j]) + int(l[i][k]) + carry
                    if curr_sum > 9:
                        s = str(curr_sum)
                        carry = int(s[0])
                        out += s[1]
                    else:
                        s = str(curr_sum)
                        carry = 0
                        out += s[0]
                    j += 1
                    k += 1

                while j < len1:
                    curr_sum = int(start[j]) + carry
                    if curr_sum > 9:
                        s = str(curr_sum)
                        carry = int(s[0])
                        out += s[1]
                    else:
                        s = str(curr_sum)
                        carry = 0
                        out += s[0]
                    j += 1

                while k < len2:
                    curr_sum = int(l[i][k]) + carry
                    if curr_sum > 9:
                        s = str(curr_sum)
                        carry = int(s[0])
                        out += s[1]
                    else:
                        s = str(curr_sum)
                        carry = 0
                        out += s[0]
                    k += 1

                if carry == 1:
                    out += "1"

                # print(out)
                start = out
            # print(start)
            return start

        def multiply_two(num1, num2):
            output = []
            count = 0
            for i in range(len(num2) - 1, -1, -1):
                carry = 0
                curr_out = ""
                for j in range(len(num1) - 1, -1, -1):
                    pdt = int(num2[i]) * int(num1[j]) + carry
                    if pdt > 9:
                        pdt = str(pdt)
                        carry = int(pdt[0])
                        curr_out += pdt[1]
                    else:
                        pdt = str(pdt)
                        carry = 0
                        curr_out += pdt
                    # print(pdt, carry)
                if carry > 0:
                    curr_out += str(carry)
                output.append("0" * count + curr_out)
                count += 1

            # print(output)
            result = sum_all(output)
            # print(result[::-1])
            return result[::-1]

        if num1 == "0" or num2 == "0":
            return "0"

        result = multiply_two(num1, num2)
        return result
