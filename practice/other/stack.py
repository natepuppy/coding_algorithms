# 394. Decode String
# Given an encoded string, return its decoded string.

# Example:
# Input: s = "ab3[a]2[bc]"
# Output: "aaabcbc"

def decode(s):
    if not s:
        return ""

    stack = []
    curr_string = [] # using array is a good option here becuase strimgs are immutable in python
    curr_digit = 0

    for char in s:
        if char.isdigit():
            curr_digit *= 10
            curr_digit += int(char)
        elif char.isalpha():
            curr_string.append(char)
        elif char == "[":
            stack.append((curr_string, curr_digit))
            curr_string = []
            curr_digit = 0
        else:
            string, digit = stack.pop()
            curr_string = string + (curr_string * digit)
    
    return "".join(curr_string) # Or a seperate result?

s = "ab3[a]2[bc]"
print(decode(s))
