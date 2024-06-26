'''
Given two strings s and t, return true if t is an anagram of s, and false otherwise.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

 

Example 1:

Input: s = "anagram", t = "nagaram"
Output: true
Example 2:

Input: s = "rat", t = "car"
Output: false
 

Constraints:

1 <= s.length, t.length <= 5 * 104
s and t consist of lowercase English letters.
'''

'''
dono string ko dictionary mein store karo aur phir check karo ki dictionary equal ho.
'''

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        count_s, count_t = {}, {}

        if len(s) != len(t):
            return False

        for i in range(len(s)):
            count_s[s[i]] = 1+count_s.get(s[i],0)

            count_t[t[i]] = 1+count_t.get(t[i],0)

        print(count_s,count_t)
        
        if count_s == count_t:
            return True
