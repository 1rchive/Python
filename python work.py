/* this does not work at all since this is my first "code".
print("welcome to the experimental test that I have made.")
answer = input('Would you like to proceed? (Yes/No)')
score = 0
total_questions = 3

if answer.lower() == "Yes":
    answer = input("First question, do you like python")
if answer == 'yes':
    score = 1
    print("nice")
else:
    print("Then why are you here?")

answer = input("Second Question, would you prefer walking in the park or driving ")
if answer.input() != 'Walking':
    print("What are you nuts?!")
else:
    score = 1
    print("Same.")

answer = input("Third and final question, would you prefer going to school and study or do something else")
if answer == 'do something else':
    score = 1
    print("I agree.")
else:
    print("NERRRRRRRRRRRRRRRRRRRRRRRRRRRRRRD")

print('Thank you for Playing this small quiz game, you attempted', score, "questions correctly!")
mark = (score / total_questions) * 100
print('Marks obtained:', mark)
print('BYE!')
