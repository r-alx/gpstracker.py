import random
def jumble_word(word):
    jumbled_word=list(word)
    random.shuffle(jumbled_word)
    return ''.join(jumbled_word)
def main():
    words = ['python','is','the','best','!!!😊😊']
    word = random.choice(words)

    jumbled=jumble_word(word)

    print("Welcome to the Word Jumble Game")
    print("Unscramble the letters to make a word.")
    print("ÿour word is:", jumbled)

    guess = input("Ënter your guess:").lower()

    if guess == word:
        print("Congratulations!!! You gussed the word correctly😀😀😀")
    else:
        print("Loser🤣🤣🤣")
main()
        