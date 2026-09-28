class Solution:
    def calPoints(self, operations: List[str]) -> int:
        score = []

        for index, op in enumerate(operations):
            if op == "C":
                score.pop()
            elif op == "+":
                result = score[-1] + score[-2]
                score.append(result)
            elif op == "D":
                result = score[-1] * 2
                score.append(result)
            else:
                score.append(int(op))

        return sum(score)