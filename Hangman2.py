def clueword():
	word={}

#display words currently found
def display_word(word):
  for letters in word.key():
   for i in range(hand[letters]):
     print ("letters")
     print(" ")
   print ("found!!") 
display_word(word)

#display message and stop game
def findword(word,sowpod):
  found=raw_input("Enter word....")
  if found==".":
    print("")
  else:
   if correct(found,sowpod):
       print("wrong letter please try again")
   else:
    	print("thumbs up...continue")

findword(word,sowpod)