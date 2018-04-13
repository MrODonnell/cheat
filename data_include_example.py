rightAnswers = []
choices1 = []
choices2 = []
questions = []
count = 0
class gameMove:
    def __init__(self, rightAnswer, choice1, choice2, question):
        self.rightAnswer = rightAnswer
        self.choice1 = choice1
        self.choice2 = choice2
        self.question = question
        
for line in open('data/rightAnswers'):
    rightAnswers.append(line.strip())
for line in open('data/choices'):
    if len(line.strip()) > 0:
        x = []
        print(line)
        x = line.split('xxx')
        print(x[0].strip())
        print(x[1].strip())
        choices1.append(x[0].strip())
        choices2.append(x[1].strip())
for line in open('data/questions'):
    questions.append(line.strip())
    
while count < len(rightAnswers):
    move = gameMove(rightAnswers[count], choices1[count], choices2[count], questions[count])
    print(move.rightAnswer)
    print(move.choice1)
    print(move.choice2)
    print(move.question)
    del move
    count += 1
