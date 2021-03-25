def loop(a,b):
	for i in range(a):
		if(i!=a-1):
			for  j in range(b):
				if(j%2 == 0):
					if(j!= b-1):
						print("__",end="")
					else:
						print("__")
				else :
					if(j!= b-1):
						print("|",end="")
					else:
						print("|")
		else:
			for  j in range(b):
				if(j%2 == 0):
					if(j!= b-1):
						print("  ",end="")
					else:
						print("  ")
				else :
					if(j!= b-1):
						print("|",end="")
					else:
						print("|")
						
print("rows - 4 , columns -7")
loop(4,7)
print("rows - 3 , columns -5")
loop(3,5)
