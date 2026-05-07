class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        counter1 = Counter(s)
        counter2 = Counter(t)
        for i in counter1:
            if counter1[i] != counter2[i]:
                return False
        for i in counter2:
            if counter2[i] != counter1[i]:
                return False
        return True

        