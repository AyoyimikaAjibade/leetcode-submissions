class Solution:
    def calPoints(self, operations: List[str]) -> int:
        operated_nums = []
        for i in range(len(operations)):
            if operations[i] == "+":
                operated_num = operated_nums[-1] + operated_nums[-2]
            elif operations[i] == "D":
                operated_num = operated_nums[-1] * 2
            elif operations[i] == "C":
                operated_nums.pop()
                continue
            else:
                operated_num = int(operations[i])
            operated_nums.append(operated_num)
        return sum(operated_nums)