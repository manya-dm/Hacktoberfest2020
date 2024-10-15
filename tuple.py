# Python3 code to demonstrate working of
# Convert String to tuple list
# using loop + replace() + split()

# initializing string 
test_str = "(1, 3, 4), (5, 6, 4), (1, 3, 6)"

# printing original string 
print("The original string is : " + test_str)

# Convert String to tuple list
# using loop + replace() + split()
res = []
temp = []
for token in test_str.split(", "):
	num = int(token.replace("(", "").replace(")", ""))
	temp.append(num)
	if ")" in token:
	res.append(tuple(temp))
	temp = []

# printing result
print("List after conversion from string : " + str(res))
