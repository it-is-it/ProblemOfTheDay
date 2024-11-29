# 190. Reverse Bits
# Reverse bits of a given 32 bits unsigned integer.

# Example 1:
# Input: n = 00000010100101000001111010011100
# Output:    964176192 (00111001011110000010100101000000)
# Explanation: The input binary string 00000010100101000001111010011100 represents the unsigned integer 43261596, so return 964176192 which its binary representation is 00111001011110000010100101000000.

# Example 2:
# Input: n = 11111111111111111111111111111101
# Output:   3221225471 (10111111111111111111111111111111)
# Explanation: The input binary string 11111111111111111111111111111101 represents the unsigned integer 4294967293, so return 3221225471 which its binary representation is 10111111111111111111111111111111.


class Solution:
    def reverseBits(self, n: int) -> int:
        # Step 1: Convert to binary and pad to 32 bits
        binary_representation = bin(n)[2:].zfill(32)

        # Step 2: Reverse the string
        reversed_binary = binary_representation[::-1]

        # Step 3: Convert back to an integer
        return int(reversed_binary, 2)


solution = Solution()

# Convert the binary strings to integers using base 2
input1 = int("00000010100101000001111010011100", 2)
input2 = int("11111111111111111111111111111101", 2)

# Call the reverseBits method
print(solution.reverseBits(input1))  # Expected output: 964176192
print(solution.reverseBits(input2))  # Expected output: 3221225471
