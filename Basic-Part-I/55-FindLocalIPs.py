# https://www.w3resource.com/python-exercises/python-basic-exercises.php
"""
Write a Python program to find local IP addresses using Python's stdlib.
"""

# Import the 'socket' module to work with network-related functions.
import socket

# The following code retrieves the local IP address of the current machine:
# 1. Use 'socket.gethostname()' to get the local hostname.
# 2. Use 'socket.gethostbyname_ex()' to get a list of IP addresses associated with the hostname.
# 3. Filter the list to exclude any IP addresses starting with "127." (loopback addresses).
# 4. Extract the first IP address (if available) from the filtered list.
# 5. Print the obtained IP address to the console.

# Step 1: Get the local hostname.
local_hostname = socket.gethostname()
print(f"Get the local hostname: {local_hostname}")

# Step 2: Get a list of IP addresses associated with the hostname.
ip_addresses = socket.gethostbyname_ex(local_hostname)[2]
print(f"Get a list of IP addresses associated with the hostname: {ip_addresses}")

# Step 3: Filter out loopback addresses (IPs starting with "127.").
filtered_ips = [ip for ip in ip_addresses if not ip.startswith("127.")]

# Step 4: Extract the first IP address (if available) from the filtered list.
first_ip = filtered_ips[:1]
print(f"Extract the first IP address (if available) from the filtered list:{first_ip}")

# Step 5: Print the obtained IP address to the console.
print(f"IP's computer: {first_ip[0]}")

"""
Explanation:

What is socket module in Python?

On top of the operating system, the socket module defines how servers and clients communicate at hardware level. 
In addition to supporting connection-oriented protocols, the socket API also supports connectionless protocols. 
It is available on all modern Unix systems, Windows, MacOS, and probably additional platforms.

socket.gethostbyname_ex(hostname) - Translate a host name to IPv4 address format, extended interface. 
Return a triple (hostname, aliaslist, ipaddrlist) where hostname is the host’s primary host name.

socket.gethostname() - Return a string containing the hostname of the machine where the Python interpreter is currently executing.

socket.socket(family=AF_INET, type=SOCK_STREAM, proto=0, fileno=None) 
- Create a new socket using the given address family, socket type and protocol number.

The above Python code first imports the socket module.

The code uses a list comprehension to extract the IP address of the current machine from the output of the socket.gethostbyname_ex() function.

The innermost list comprehension filters out any IP addresses that start with 127. 
(which are reserved for loopback testing) and selects the first IP address in the resulting list. 
This is done using the if statement and the [:1] slice notation.

The outer list comprehension combines the list of IP addresses obtained 
from the previous step with a list that contains the IP address of Google's DNS server (8.8.8.8). 
This is done using nested lists and a list comprehension that creates a UDP socket and queries the server for its IP address.

Finally, the print() function is used to print the IP address of the current machine.
"""