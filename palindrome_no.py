num=int(input("Enter the number:"))
def is_palindrome(num):
    return str(num) == str(num)[::-1]
if is_palindrome(num)==False:
    print(f"The Number {num} is not a Palindrome")
else:
     print(f"The Number {num} is a Palindrome")

