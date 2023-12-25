string=input("Enter a string:")
reverse_string=""
for i in string:
    reverse_string=i+reverse_string
if string==reverse_string:
    print("The string is palindrome")
else:
    print("The string is not a palindrome")