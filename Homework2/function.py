def albumName(name):
	return name

def singerName(name):
	return name

def releasedDate(date):
	return date

def album():
	name="Dancing World"
	return name
    
def singer():
	name="Swapna Sahu"
	return name

def released():
	date="1/1/1000"
	return date

def albumDetails1():
        Album=album()
        Singer=singer()
        Released=released()
        print("Album -- " ,Album,",Singer -- " ,Singer,",Released -- " ,Released)

def albumDetails():
	Album="Dancing World"
	Singer="Swapna"
	Released="1/1/1000/"
	print("Album --",Album,", Singer -- ",Singer, ", Released --",Released)

albumDetails()
albumDetails1()
