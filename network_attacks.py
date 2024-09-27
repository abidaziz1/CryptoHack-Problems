#!/usr/bin/env python3

from pwn import *  # pip install pwntools
import json

# Step 1: Define the host and port
HOST = "socket.cryptohack.org"
PORT = 11112

# Step 2: Connect to the server
r = remote(HOST, PORT)

# Step 5: Function to receive JSON data from the server
def json_recv():
    line = r.readline()  # Read a line from the server
    return json.loads(line.decode())  # Decode the bytes into a string and parse JSON

# Step 6: Function to send JSON data to the server
def json_send(hsh):
    request = json.dumps(hsh).encode()  # Encode the dictionary into JSON and then into bytes
    r.sendline(request)  # Send the encoded JSON

# Step 3: Print initial server responses
print(r.readline())  # Could be an introduction or server information
print(r.readline())
print(r.readline())
print(r.readline())

# Step 4: Create the request to buy the "flag"
request = {
    "buy": "flag"  # Modify the value to "flag" as required
}

# Step 7: Send the JSON request
json_send(request)

# Step 8: Receive the server's response
response = json_recv()

# Step 9: Print the server's response
print(response)
