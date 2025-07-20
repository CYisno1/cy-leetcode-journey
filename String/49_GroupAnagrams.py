class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # Use a defaultdict to group anagrams together
        # Keys will be tuples representing character frequencies, values will be lists of strings
        ans = collections.defaultdict(list)

        for s in strs:
            # Create a list of size 26 (for each letter a-z) to count character frequency
            count = [0] * 26
            for c in s:
                # Map character to an index: 'a' → 0, 'b' → 1, ..., 'z' → 25
                count[ord(c) - ord("a")] += 1

            # Convert the list to a tuple to use it as a dictionary key
            # Reason: For Python, lists can't be used as dictionary keys because they're mutable and not hashable
            # Tuples are immutable and hashable, so they are allowed as keys
            key = tuple(count)

            # Add the string to the list corresponding to the same character frequency key
            # All anagrams will have the same frequency count, so they’ll go into the same group
            ans[key].append(s)

        # Return the grouped anagram lists
        return list(ans.values())
