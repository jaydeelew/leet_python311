# 433. Minimum Genetic Mutation
# A gene string can be represented by an 8-character long string, with choices from 'A', 'C', 'G', and 'T'.
# Suppose we need to investigate a mutation from a gene string startGene to a gene string endGene
# where one mutation is defined as one single character changed in the gene string.
# For example, "AACCGGTT" --> "AACCGGTA" is one mutation.
# There is also a gene bank bank that records all the valid gene mutations.
# A gene must be in bank to make it a valid gene string.
# Given the two gene strings startGene and endGene and the gene bank bank,
# return the minimum number of mutations needed to mutate from startGene to endGene.
# If there is no such a mutation, return -1.

# Note that the starting point is assumed to be valid, so it might not be included in the bank.
from collections import deque


class Solution:
    def minMutation(self, startGene: str, endGene: str, bank: list[str]) -> int:
        queue = deque([(startGene, 0)])  # (gene, steps)
        seen = {startGene}
        bases = ("A", "C", "G", "T")

        while queue:
            gene, steps = queue.popleft()
            if gene == endGene:
                return steps
            for i in range(len(gene)):
                # for every char in gene, substitute the three other bases to form a gene mutation
                for base in bases:
                    if gene[i] != base:
                        # "[:i] - up to but not including i [i + 1:]"
                        # + "replace i with base"
                        #  + "next char after i until end of str"
                        mutation = gene[:i] + base + gene[i + 1 :]  # noqa
                        if mutation in bank and mutation not in seen:
                            queue.append((mutation, steps + 1))
                            seen.add(mutation)
        return -1


# startGene = "AACCGGTT"
# endGene = "AACCGGTA"
# bank = ["AACCGGTA"]
# # Output: 1

startGene = "AACCGGTT"
endGene = "AAACGGTA"
bank = ["AACCGGTA", "AACCGCTA", "AAACGGTA"]
# Output: 2

sol = Solution()
print(sol.minMutation(startGene, endGene, bank))
