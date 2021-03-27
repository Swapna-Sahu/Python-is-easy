SongInfo={"Key1":"Album","Key2":"Rating","Key3":"Singer","Key4":"Writer","Key5":"Musician","Key6":"Released","Key7":"Genre","Key8":"Duration","Key9":"Recorded","Key10":"Producer"}
for song in SongInfo:
	print(song ,":", SongInfo[song])

def guessKeyValue(guessKey,guessValue):
	length = len(SongInfo)
	for song in SongInfo:
		length -= 1
		if(song==guessKey):
			if(SongInfo[song]==guessValue):
				print("True - ",song,",",SongInfo[song])
				break
			else:
				print("False - Incorrect value of ",song)
				break
		else:
			if(length==0):
				print("False, No such key found!")
			else:
				continue

while(True):
	guessKey = input("which key do you want to guess?\n")
	guessValue = input("what is the value of the key?\n")
	guessKeyValue(guessKey,guessValue)
