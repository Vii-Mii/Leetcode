class Solution:
    def isHappy(self, n: int) -> bool:
        
        def get_next(n):
            total_num = 0
            while n > 0:
                n, digit = divmod(n,10)
                total_num += digit**2
            return total_num

        slow = n
        fast = get_next(n)

        while fast != 1 and slow != fast:
            slow = get_next(slow)
            fast = get_next(get_next(fast))
        
        return fast == 1

# Time Complexity: O(n)
# Space Complexity: O(1)
# Approach: Using fast & slow pointers
# Tags: two-pointer

# --------------------------------------------------------------------------------
# Next Solution Version
# --------------------------------------------------------------------------------

class Solution:
    def isHappy(self, n: int) -> bool:
        values = set()

        while n != 1:
            if n in values:
                return False
            values.add(n)
            val = sum([int(i)**2 for i in str(n)])
            n = val
        
        return True

# Time Complexity: O(n)
# Space Complexity: O(n)
# Approach: Using Set
