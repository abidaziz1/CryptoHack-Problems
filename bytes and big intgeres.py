from Crypto.Util.number import long_to_bytes

# Given integer
integer_value = 11515195063862318899931685488813747395775516287289682636499965282714637259206269

# Convert the integer to bytes
byte_message = long_to_bytes(integer_value)

# Decode the bytes to a string
message = byte_message.decode('utf-8')

print("The decoded message is:", message)
