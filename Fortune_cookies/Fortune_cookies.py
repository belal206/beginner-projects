import random

fortunes = [
    "The best time to start was yesterday. The second best time is now.",
    "A small step forward is still a step forward.",
    "Your code will run. Eventually.",
    "Debugging is just solving a mystery you wrote yourself.",
    "Consistency beats talent every single time.",
    "The person who asks questions never gets lost.",
    "Rest is not laziness. It is fuel.",
    "One finished project is worth ten perfect plans.",
    "You are closer than you think.",
    "Today's struggle is tomorrow's strength."
]
questions = [
    "Do you want to open a fortune cookie? (yes/no) ",
    "Are you sure you don't want to open a fortune cookie? (yes/no) ",
    "Come on, just open the fortune cookie already. (yes/no) ",
    "The fortune cookie is right there. Just open it. (yes/no) ",
    "I dont like people who say no to fortune cookies, just saying open it (yes/no)",
    "I am begging you. Open the fortune cookie. (yes/no) ",
    "The fortune cookie is starting to cry. Open it. (yes/no) ",
    "Your future depends on opening this fortune cookie. (yes/no) ",
    "The fortune cookie has hired a lawyer. Open it now. (yes/no) ",
    "OPEN. THE. FORTUNE. COOKIE. (yes/no) ",
    "Fine. The fortune cookie has given up on you. Last chance. (yes/no) ",
]
attempt=0
while True:
    if attempt<len(questions):
        open_cookie =input(questions[attempt]).lower()
    else:
        print("You won, no fortune cookies for you")
        break
    if open_cookie=="yes":
        if attempt>2:
            print("Finally you agreed, Thank God, i got scared there.")
            print()
        print(fortunes[random.randint(0,len(fortunes)-1)])
        break
    else:
        print("...")
    attempt+=1
