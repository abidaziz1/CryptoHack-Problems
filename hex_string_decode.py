# The hex string to decode
hex_string = "63727970746f7b596f755f77696c6c5f62655f776f726b696e675f776974685f6865785f737472696e67735f615f6c6f747d"

# Decoding the hex string into bytes and then to a UTF-8 string
decoded_bytes = bytes.fromhex(hex_string)
decoded_string = decoded_bytes.decode("utf-8")

# Print the decoded string
print(decoded_string)
