#!
from random import choice
#import string
#SOWPODS_FILENAME= "sowpods.txt"

def words():
	#print("loading words ...")
	f=open("sowpods.txt","r")
	file = f.readlines()
	return choice(file)
print(words())
	


