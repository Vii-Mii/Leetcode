class Solution:
    def compress(self, chars: list[str]) -> int:
        read = 0
        write = 0

        while read < len(chars):
            count = 0 
            char = chars[read] 

            while read < len(chars) and chars[read] == char:
                read += 1
                count += 1
            
            chars[write] = char
            write += 1

            if count > 1:
                for i in str(count):
                    chars[write] = i
                    write += 1
        return write

# Time Complexity: O(n)
# Space Complexity: O(1)
# Approach: read & write pointers
# Tags: two-pointer
