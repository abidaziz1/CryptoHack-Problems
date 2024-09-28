from pwn import *  # For handling network communication
import json
import base64
import codecs
from Crypto.Util.number import bytes_to_long, long_to_bytes

# Connect to the challenge server
r = remote('socket.cryptohack.org', 13377)

# Function to receive JSON data from the server with a timeout
def json_recv():
    try:
        # Set a timeout of 15 seconds to avoid waiting indefinitely
        line = r.recvline(timeout=15)
        if line.strip() == b"":  # Check if the line is empty
            print("Warning: Received empty response.")
            return None
        return json.loads(line.decode())
    except EOFError:
        print("Connection closed by the server.")
        return None
    except json.JSONDecodeError as e:
        print(f"Error decoding JSON: {e}")
        print(f"Raw response: {line}")
        return None
    except Exception as e:
        print(f"Error receiving data: {e}")
        return None

# Function to send JSON data to the server
def json_send(hsh):
    request = json.dumps(hsh).encode()
    r.sendline(request)

# Function to handle different encoding types and decode them
def decode_message(encoded, encoding_type):
    if encoding_type == "base64":
        return base64.b64decode(encoded).decode()
    elif encoding_type == "hex":
        return bytes.fromhex(encoded).decode()
    elif encoding_type == "rot13":
        return codecs.decode(encoded, 'rot_13')
    elif encoding_type == "bigint":
        return long_to_bytes(int(encoded, 16)).decode()
    elif encoding_type == "utf-8":
        return ''.join(chr(b) for b in encoded)
    else:
        raise ValueError(f"Unknown encoding type: {encoding_type}")

# Main loop to solve all 100 levels
for level in range(100):
    # Receive the challenge from the server
    received = json_recv()
    
    if received is None:
        print(f"Failed to receive data for level {level + 1}. Exiting...")
        break

    # Print the received challenge details for debugging
    print(f"Level: {level + 1}")
    print(f"Received type: {received['type']}")
    print(f"Received encoded value: {received['encoded']}")
    
    # Decode the message based on the encoding type
    try:
        decoded_message = decode_message(received["encoded"], received["type"])
    except Exception as e:
        print(f"Error decoding: {e}")
        break
    
    # Print the decoded message (for debugging)
    print(f"Decoded message: {decoded_message}")
    
    # Send the decoded message back to the server
    to_send = {
        "decoded": decoded_message
    }
    
    print(f"Sending: {to_send}")
    json_send(to_send)

    # Get and print the server's response
    response = json_recv()

    if response is None:
        print(f"Failed to receive response for level {level + 1}. Exiting...")
        break

    print(f"Response: {response}")

    # If we reach the last level, the flag will be returned
    if "flag" in response:
        print(f"Flag: {response['flag']}")
        break
