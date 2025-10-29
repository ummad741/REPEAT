# Binary (Base-2):
# Uses only two digits, 0 and 1. Each position in a binary number represents a power of 2 (e.g., 1011₂ = 12³ + 02² + 12¹ + 12⁰ = 8 + 0 + 2 + 1 = 11₁₀).
# Octal (Base-8):
# Uses eight digits, 0 through 7. Each position represents a power of 8.
# Decimal (Base-10):
# The familiar number system, using digits 0 through 9, where each position represents a power of 10.
# Hexadecimal (Base-16):
# Uses 16 digits: 0-9 and A-F (where A=10, B=11, C=12, D=13, E=14, and F=15). Each position represents a power of 16.

number = 17
for i in range(number):
    binary = str(bin(i+1))[2:]
    hexadecimal = str(hex(i+1))[2:].upper()
    octal = str(oct(i+1))[2:]
    print(i+1, octal, hexadecimal, binary)


dividend = 177
divisor = 10
divmod(dividend, divisor)
# output (17,7)

# Return the value of 4 to the power of 3, modulus 5 (same as (4 * 4 * 4) % 5):
num1 = 4
num2 = 3
modulus = 5
pow (num1,num2,modulus)
# qoldiq 63 5ga boladi va 4 qoldiq chiqaradi

