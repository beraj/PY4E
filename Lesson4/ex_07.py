#Grade calculator
def computegrade(score):
    if score > 1.0:
        return 'Bad score'
    elif score >= 0.9 and score <= 1.0:
        return 'A'
    elif score >= 0.8 and score <= 0.9:
        return 'B'
    elif score >= 0.7 and score <= 0.8:
        return 'C'
    elif score >= 0.6 and score <= 0.7:
        return 'D'
    else:
        return 'F'
        
strScore = input('Enter score: ')

try:
    fltScore = float(strScore)
except:
    print('Bad score')
    quit()

output = computegrade(fltScore)
print(output)