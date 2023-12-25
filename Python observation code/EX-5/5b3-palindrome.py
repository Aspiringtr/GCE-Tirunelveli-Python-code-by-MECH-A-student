string=input("Enter a string:")
rev_string="".join(reversed(string))
if string==rev_string:
    print("The string is palindrome")
else:
    print("The string is not a palindrome")
