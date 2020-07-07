import random 

global words

words=["dog","cat","horse","neurobiological","india","england","malayalam","racecar","allegiance","divergence","melbourne","aukland","procastination","hallucination","aggrandize"]   

def draw_man(guesses):
    if(guesses==4):
      print(" ----")
      print("|    |")
      print("|")
      print("|")
    
    elif(guesses==3):
      print(" ----")
      print("|    |")
      print("|    O")
      print("|    |")
    
    elif(guesses==2):
      print(" ----")
      print("|    |")
      print("|    O")
      print("|   /|\ ")
    
    elif(guesses==1):
      print(" ----")
      print("|    |")
      print("|    O")
      print("|   /|\ ")
      print("|   / ")

    elif(guesses==0):
      print(" ----")
      print("|    |")
      print("|    O")
      print("|   /|\ ")
      print("|   / \ ")
    
      
def hangman():
    rand=len(words)
    i=random.randint(0,rand-1)
    word=list(words[i])
    actual_word="".join(word)
    guesses=5
    guess_word=[" * "]
    used_word=[]
    guess_word*=len(word)
    while guesses>0:
       draw_man(guesses)
       print("\n\n")
       print(" ".join(guess_word))
       print("\n\n")
       ch=input("Enter the character: ")
       if(ch not in used_word):
        used_word+=ch
       print("\nUsed letters: ")
       used_word.sort()
       print(used_word)
       if(ch in word):
             i=0
             for i in range(len(word)):
                if(ch==word[i]):
                   pos=i;
                   guess_word[pos]=ch
       elif(ch not in word):
            guesses-=1
       if " * " not in guess_word:
         print(" ".join(guess_word))
         print("\n\n",name," you won! Congratulations :) ")        
         break    
    if(guesses<=0):
         draw_man(guesses)
         print("You lost!You were hanged :(")
         print("\nIt was {}".format(actual_word))
ans='y'
print("Welcome to Hangman")
name=input("Enter your name: ")
while(ans=='y' or ans=='y'):
    print("Menu")
    print("\n")
    print("1.Play the game")
    ch1=input("Enter 1 to play the game: ")
    if(ch1=='1'):
         hangman()
    ch=input("Do you want to try again(y/n): ")
    if(ch=='n' or ch=='N'):
        break 
