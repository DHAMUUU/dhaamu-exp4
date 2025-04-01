#initializing variable
num = 1234
reverse = int(str(num)[::-1])
#printing results
if num == reverse:
  print('Palindrome')
else:
  print("Not Palindrome")
