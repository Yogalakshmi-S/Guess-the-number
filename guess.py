guess_number=4
guess_count=0
guess_limit=3
while guess_count<guess_limit:
    guess=int(input("enter the number"))
    guess_count+=1
    if guess==guess_number:
        print("you won")
        break
else:
    print("you lose!!")
