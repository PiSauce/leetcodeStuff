class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        # Trivial Solutions need trivial answers
        if(len(s) == 0):
            return 0
        elif(len(s) == 1):
            return 1

        # Check if string has no repeating characters
        if(len(s) == len(set(s))):
            return len(s) # No repeats, so whole string is ok
        
        start = 0
        end = 0
        largest = 0

        for _ in range(len(s)):
            end += 1
            # If there's a duplicate character, keep increasing starting value until there isn't
            while(len(s[start:end]) != len(set(s[start:end]))):
                start += 1
                if end < start:
                    end += 1

            # debug to see string
            print(s[start:end])

            # If current substring is the largest, update largest
            if end-start > largest:
                largest = end-start
                
        return largest