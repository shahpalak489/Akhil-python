
class Solution(object):
    def numJewelsInStones(self, J, S):
        """
        :type J: str
        :type S: str
        :rtype: int
        """
        n=0
        for x in range(len(S)):
            if S[x] in J:
                n=n+1
        return n