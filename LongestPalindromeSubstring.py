class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        start = 0
        end = 0
        
        # If the string has no characters, return an empty string
        if len(s) > 0:
            longest = s[0]
        else:
            return ""

        # While there is enough of the string left to pass longest
        while(len(s)-start > len(longest)):
            # Decrease length of substring until a palindrome is found or the string is smaller than the longest
            end = len(s)
            while end-start+1 > len(longest) and not self.checkPalindrome(s[start:end]):
                end -= 1
            
            if end-start > len(longest):
                longest = s[start:end]
            start += 1
        return longest

    def checkPalindrome(self, s):
        start = 0
        end = len(s)-1
        while start < end:
            if s[start] == s[end]:
                start += 1
                end -= 1
            else:
                return False
        return True