"""
114. Filter Positive Numbers

Write a Python program to filter positive number from a list.
"""
# Ma solution
print("Solution 1:")
nums = [34, 1, 0, -23, 12, -88]
print("Original numbers in the list: ", nums)
print(f"Positive numbers in the said list: {list(filter(lambda x: x>0, nums))}")

print()
print("Solution 2: ")
# W3resource
# Print a message along with the original list of numbers.
print("Original numbers in the list: ", nums)

# Print a message indicating that positive numbers in the list will be listed.
print("Positive numbers in the said list: ", end="")

# Iterate through each number in the "nums" list.
for pos_nums in nums:
    # Check if the number is greater than 0 (positive).
    if pos_nums > 0:
        # Print positive numbers on the same line with a space separator.
        print(pos_nums, end=" ")