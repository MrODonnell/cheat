newScore = 130
scores = []
f = open('data\leader.txt', 'r+')
for score in f:
    scores.append(int(score))

scores.append(newScore)
sortedScores = scores.sort(reverse=True)
print(scores)
f.close()
s = ''

if len(scores) > 3:
    scores = scores[0:3]
    
for score in scores:
    s += str(score) + "\n"

s = s.strip()
print(s)
writeFile = open('data\leader.txt', 'w')
writeFile.write(s)
writeFile.close()

