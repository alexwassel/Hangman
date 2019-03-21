phrase = input("Enter a word or phrase: ")
data = "_".join(phrase) + "_"
print(data)

run = 0
while "_" in data and run < 10:
    print("The word to guess: ", data[1::2])
    letter = input("Guess a letter: ").lower()
    if len(letter) != 1:
        letter = input("Guess a letter ").lower()
    data = data.replace(letter + "_", letter + letter)
    run += 1
    #go back to line 5

if "_" in data:
    print("You lose; it was", phrase)

else:
    print("You won! ")
