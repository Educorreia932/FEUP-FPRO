num = int(input("Insira um número: "))
reverse = 0
n = num

while(n > 0):
	reminder = n % 10
	reverse = (reverse * 10) + reminder
	n = n // 10

if num == reverse:
	result = str(num) + " is a palindrome."
	print(result)
	
else:
	result = str(num) + " is not a palindrome."
	print(result)
