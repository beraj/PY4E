#Letter counter
def lettercounter(fnword,fnletter):
    count = 0
    for letter in fnword:
        if letter == fnletter:
            count = count + 1
        
    return count

word = input('Enter a word:')
letter = input('Enter a letter:')

output = lettercounter(word,letter)

print(output)