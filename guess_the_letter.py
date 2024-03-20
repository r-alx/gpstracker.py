import random
def jumble_word(word):
    jumble_word = list(word)
    random.shuffle(jumble_word)
    return ''.join(jumble_word)
def main():
    words = ['qwerty_keyboard','home_schooling','caterpillar','soul_of_darkness','👋👍hehe_why','herobrine']
    word = random.choice(words)
    jumbled= jumble_word(word)

    print("welcome to the hardest jummble word😶😶😶")
    print("Unscrmble the letter to make a word")
    print("Your word is:",jumbled)

    guess = input("Enter your guess:" ).lower()
    if guess == word:
        print("Congratulation you beat the most hardest jumbled word🙃🙃🙃")
    else:
        print("LLLLOOOSSSEERRRR!!!!!🤪🤪🤪")
main()