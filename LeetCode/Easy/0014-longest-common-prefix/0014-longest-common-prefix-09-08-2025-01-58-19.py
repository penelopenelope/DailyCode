class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        min_len = min(len(s) for s in strs)
        if min_len == 0: return ""
        i = 1
        while i <= min_len:
            # print(i)
            prefix = set([string[0:i] for string in strs])
            if len(prefix) == 1:
                i+=1
                continue
            else: 
                # print(strs[0][0:i-1])
                # break
                return strs[0][0:i-1]
            i+=1
        return strs[0][0:i-1]