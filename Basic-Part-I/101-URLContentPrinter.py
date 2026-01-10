# https://www.w3resource.com/python-exercises/python-basic-exercises.php
"""
101. URL Content Printer

Write a Python program to access and print a URL's content to the console.
Click me to see the sample solution 
"""
# W3resource 
# Solution 1:

print("Solution 1")
from http.client import HTTPConnection

# Create an HTTPConnection object for the "example.com" host.
conn = HTTPConnection("example.com")

# Send a Get request to the root path ("/") of the host.
conn.request("Get", "/")

# Get the response from the server.
result = conn.getresponse()

# Retrieve the entire contents of the response.
contents = result.read()

# Print the contents of the response.
print(contents)

# W3resource 
# Solution 2
print()
print("Solution 2")

# Import the requests library to make HTTP requests.
import requests

# Send an HTTP GET request to the 'https://google.com/' URL and store the response.
data = requests.get('https://google.com')

# Access the text content of the response, which contains the webpage's HTML.
webpage_text = data.text

# Print the HTML content of the webpage.
print(webpage_text)
