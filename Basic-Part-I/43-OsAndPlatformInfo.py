# https://www.w3resource.com/python-exercises/python-basic-exercises.php
"""
Write a Python program to get OS name, platform and release information.
"""
import os
print("with os library")
print(os.name)

print()

import platform
print("with platform library")
print(platform.uname())
print(f"OS Name:", platform.system())
print(f"OS release: {platform.release()}")
print(f"OS Version: {platform.version()}")
print(f"OS Architecture: {platform.architecture()}")

print()
print("with sys library")
import sys
print(f"OS platform: {sys.platform}")

print()
print("with sysconfig library")
import sysconfig
print(sysconfig.get_platform())