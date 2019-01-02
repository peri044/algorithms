class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        letters=[]
        
        index=0
        counts=[]
        max=0
        if len(s)==1:
            return 1
        elif len(s)==0:
            return 0
        else:
            for i in range(len(s)):
                hashmap={}
                hashmap[s[i]] = 1
                count=1
                if len(s)-i-1 >= max:
                    for j in range(i+1, len(s)):
                        if s[j] not in hashmap.keys():
                            hashmap[s[j]]=1
                            count+=1
                            if count > max: max=count
                            counts.append(count)
                        else:
                            if count > max: max=count
                            counts.append(count)
                            break
                else:
                    return max
            return max
        
                
        