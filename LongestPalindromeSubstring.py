class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        start = 0
        end = 0
        longest = ""

        # While there is enough of the string left to pass longest
        while(len(s)-start > len(longest)):
            # Decrease length of string until a palindrome is found
            for end in range(len(s), start, -1):
                # If it's the longest, then replace longest
                if(len(s[start:end]) > len(longest) and self.checkPalindrome(s[start:end])):
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