'''
Using while loop , if else , for, break

Divisible by 3 - Fizz
Divisible by 5 - Buzz
Divisible by 3 and 5 - Fizz Buzz
Prime number - Prime

'''

count=1
while(count<=100):
	if(count%3==0 and count%5==0):
		print(count ,"-","Fizz Buzz")
	elif(count==1 or count==2 or count==3 or count==5):
		print(count ,"-","Prime")
	elif(count%5==0 and count!=5):
		print(count, "-","Buzz")
	elif(count%3==0 and count!=3):
		print(count ,"-","Fizz")
	elif(count%2 != 0):
		for i in range(3, 100):
		   if (count % i) != 0:
			   print(count ,"-","Prime")
		   break
	else:
		print(count)
	count=count+1
