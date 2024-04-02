def flashcard():
    qu_an={"which sea is near central america":"caribbean sea",
           "how many meters can a tsunami reach":"30",
           "Who event the first airplane":"the written brother",
           "how many can a zombie be rare ":"00000000.1",
           "how many block can enderman carry":"1 block"}
    score = 0
    for q,a in qu_an.items():
        user = input(q)
        if user.lower()== a.lower():
         print("Correct answer👍👍👍")
         score+=1
         print(score)
        else:
           print("Wrong answer bro😶😶😶the answer is",a)
    print(f"Quiz completed your final score is {score}/{len(qu_an)}.")
flashcard()


