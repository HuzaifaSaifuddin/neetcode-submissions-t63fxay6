class Solution:
    def calPoints(self, operations: List[str]) -> int:
        record = []
        for op in operations:
            if op == "+":
                last2_sum = sum(record[-2:])
                record.append(last2_sum)
            elif op == "D":
                double_score = record[-1] * 2
                record.append(double_score)
            elif op == "C":
                if record:
                    record.pop()
            else:
                record.append(int(op))

        return sum(record)
