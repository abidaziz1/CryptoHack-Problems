def binary_to_flag(encoded_text):
    # Step 1: Map 'B' -> '0' and 'D' -> '1'
    binary_string = encoded_text.replace('B', '0').replace('D', '1')
    
    # Step 2: Split the binary string into groups of 5 bits
    binary_groups = binary_string.split()
    
    flag_characters = []
    
    for group in binary_groups:
        # Step 3: Convert each 5-bit binary group to decimal
        decimal_value = int(group, 2)
        # Step 4: Convert decimal to ASCII character
        flag_characters.append(chr(decimal_value + 96))  # Adding 96 to align to lower case alphabets
    
    # Step 5: Join the characters to form the flag
    flag = ''.join(flag_characters)
    return flag

# Example input
input_text = "BDDDD DDDBD BDDDB DDDBD DDDBD BDDDD BDBBD DBBBD BDDBD DBBDB DBDDD BDDDB DDBDB BDDBB DBBDD"
flag = binary_to_flag(input_text)
print(f"RCSC{{{flag}}}")
