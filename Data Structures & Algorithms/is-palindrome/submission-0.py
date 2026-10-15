class Solution:
    def isPalindrome(self, s: str) -> bool:
        word1=""
        s = s.lower()
        for char in s:
           if char.isalnum():
                word1+=char;

        reverse = word1[::-1]

        if word1 == reverse :
            return True     

        else :
            return False        