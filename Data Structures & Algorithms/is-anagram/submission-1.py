class Solution:
    def _loopThruDict(self, d, word):
        for char in word:
            if d.get(char) == None:
                # add key/val pair
                d[char] = 1
            else:
                # update value
                prev = d[char]
                d[char] = prev + 1
        return d

    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        dict1 = {}
        dict2 = {}

        dict1 = self._loopThruDict(dict1, s)
        dict2 = self._loopThruDict(dict2, t)

        if dict1 == dict2:
            return True
        else:
            return False