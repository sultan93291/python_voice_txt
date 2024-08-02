# this is a normal task file who will take a contribution . if the the contribution is greater or equal one it will thanks you else it will say insufficient contribution 

# declaring a variable who will store the user inputed contribution 
contribution  = int(input('enter your contribution : '))

# importing pyttsx3 for voice command 
import pyttsx3
engine = pyttsx3.init()


# checking user input contribution and giving outuput though the if else logic
if contribution >= 1 :
  engine.say(" thanks for your contributions ");
else : 
  engine.say("insufficient contribution")


engine.runAndWait()



def main():
  arg_for_usr = 0
  while arg_for_usr <=55 :
      arg_for_usr +=1;
      print(arg_for_usr)

main()

