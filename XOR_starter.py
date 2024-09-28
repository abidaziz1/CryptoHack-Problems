def xor_string(label, key):
    # XOR each character with the integer key
    new_string = ''.join(chr(ord(char) ^ key) for char in label)
    return new_string

# Input string (label)
label = "your_input_string_here"

# XOR key is 13
key = 13

# Get the new XORed string
new_string = xor_string(label, key)

# Format and print the result as crypto{new_string}
flag = f"crypto{{{new_string}}}"
print(flag)
