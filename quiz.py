#--------------
def new_game():
    guesses=[]
    correct_guess=0
    question_num=1
    for key in questions:
        print("-------------")
        print(key)
        for i in options[question_num-1]:
            print(i)
        guess=input("Enter (A,B,C,D):")
        guess=guess.upper()
        guesses.append(guess)

        correct_guess+=check_answer(questions.get(key),guess)
        question_num+=1
    display_score(correct_guess,guesses)
#---------------
def check_answer(answer,guess):
    if answer==guess:
        print("correct")
        return 1
    else:
        print("false")
        return 0

#---------------
def display_score(correct_guesses,guesses):
   print("-----------")
   print("RESULTS")
   print("Answers: ",end="")
   for i in questions:
       print(questions.get(i),end=",")
   print()
   print("Guesses: ",end="")
   for i in guesses:
       print(i,end=",")
   score = int((correct_guesses/len(questions))*100)
   print()
   print("your answer is "+str(score)+"%")

#---------------
def play_again():
    response=input("Play again? (yes or no)")
    response=response.upper()
    if response=="YES":
        return True
    else:
        return False


questions={
    "Who created python?: ": "A",
    "Is Earth round?: ":"A"

}
options =[["A. Guido van Rossum","B. Elon musk","C. Bill gates","D. Mark"],
          ["A. True","B. False","C. Maybe"," D. WTH is earth"]]

new_game()
while play_again():
    new_game()
print("Bye Bye")