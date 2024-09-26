'''
Another common encoding scheme is Base64, which allows us to represent binary data as an ASCII string using an alphabet of 64 characters. One character of a Base64 string encodes 6 binary digits (bits), and so 4 characters of Base64 encode three 8-bit bytes. 

Base64 is most commonly used online, so binary data such as images can be easily included into HTML or CSS files.

Take the below hex string, decode it into bytes and then encode it into Base64.

72bca9b68fc16ac7beeb8f849dca1d8a783e8acf9679bf9269f7bf

 In Python, after importing the base64 module with import base64, you can use the base64.b64encode() function. Remember to decode the hex first as the challenge description states.
'''
import base64

# The hex string to be converted
hex_string = "72bca9b68fc16ac7beeb8f849dca1d8a783e8acf9679bf9269f7bf"

# Step 1: Convert the hex string to bytes
byte_data = bytes.fromhex(hex_string)

# Step 2: Encode the byte data into Base64
base64_encoded = base64.b64encode(byte_data)

# Convert the Base64 bytes back to a string for display
base64_string = base64_encoded.decode("utf-8")

# Print the Base64 encoded string
print(base64_string)
