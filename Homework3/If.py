# if statement


#check the type of the parameters

def func(a,b,c):
	if type(a)==type(b) or type(b)==type(c) or type(a)==type(c):
		return("True")
	else: return("fail")
func(6,5,'5')

# check the parameters equality


def com(a,b,c):
	if int(a)==int(b) or int(b)==int(c) or int(a)==int(c):
		return("True")
	else: return("fail")

condition1=com(6,5,'5')
print("condition 1 ", condition1)
condition2=com(6,5,4)
print("condition 2 ", condition2)
condition3=com('6',5,'4')
print("condition 3 ", condition3)
