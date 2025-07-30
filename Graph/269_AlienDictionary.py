# Topological Sort!

from collections import defaultdict, Counter, deque

class Solution:
    def alienOrder(self, words: List[str]) -> str:

        # Step 1: create data structures + the in_degree of each unique letter to 0.
        adj_list = defaultdict(set)
        in_degree = Counter({c: 0 for word in words for c in word})

        # Step 2: populate adj_list and in_degree
        # For each pair of adjacent words
        for first_word, second_word in zip(words, words[1:]): # Compare the 1st-2nd, 2nd-3rd,....
                                                            # 2 words as a pair in the words(parameter)
            for c, d in zip(first_word, second_word): # Compare every word in these two words
                if c != d:
                    if d not in adj_list[c]:
                        adj_list[c].add(d)
                        in_degree[d] += 1
                    break
            else:  # If jump to else, means that the c, d in first and second word are same
                if len(second_word) < len(first_word): # so if len(second_word) < len(first_word)
                # it means that second word is a prefix of first word
                    return ""

        # Step 3: Repeatedly pick off nodes with an indegree of 0.
        output = []
        queue = deque([c for c in in_degree if in_degree[c] == 0])
        while queue:
            c = queue.popleft()
            output.append(c)
            for d in adj_list[c]:
                in_degree[d] -= 1
                if in_degree[d] == 0:
                    queue.append(d)

         # If not all letters are in output, that means there was a cycle and so
        # no valid ordering. Return "" as per the problem description.
        if len(output) < len(in_degree):
            return ""
        # Otherwise, convert the ordering we found into a string and return it.
        return "".join(output)
