def flashcard_quiz():
    q_and_a ={"What is the capital of France?": "Paris",
              "what is the largest ocean?":"Pacific",
              "Ïn which language was python written?":"Ënglish"
              }
    score = 0

    for q,a in q_and_a.items():
       user_answer = input(q)
       if user_answer.lower() == a.lower():
        print("Correct!")
        score += 1
        print(score)
       else:
          print("Wrong! The correct answer is ", a)
    print(f"Quiz complete! your final score is {score}/{len(q_and_a)}.")


flashcard_quiz()