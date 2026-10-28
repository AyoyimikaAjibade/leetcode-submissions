class Solution:
    def calPoints(self, operations: List[str]) -> int:
        operated_nums = []
        for i in range(len(operations)-1):
            first_prev = i - 1
            if operations[i] == "+":
                sec_prev = i - 2
                operations[i] = int(operations[first_prev]) + int(operations[sec_prev])
            elif operations[i] == "D":
                operations[i] = int(operations[first_prev]) * 2
            elif operations[i] == "C":
                val = operations.pop(first_prev)
                val1 = operated_nums.pop()
                print('VAL', val, val1)

            operated_nums.append(int(operations[i]))
            print('operated_nums', operated_nums)
        return sum(operated_nums)