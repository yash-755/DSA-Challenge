class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        i = len(digits) - 1
        
        while i >= 0:
            if digits[i] < 9:
                digits[i] += 1
                return digits
            digits[i] = 0  # 9 + 1 = 10 -> place 0 and carry
            i -= 1
        
        # If all digits were 9: example [9,9,9]
        return [1] + digits