class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stacks = []
        for ops in operations:
            if ops == "+":
                stacks.append(int(stacks[-1]) + int(stacks[-2]))
            elif ops == "D":
                stacks.append(int(stacks[-1]) * 2)
            elif ops == "C":
                stacks.pop()
            else:
                stacks.append(int(ops))
        print('stacks', stacks)
        return sum(stacks)