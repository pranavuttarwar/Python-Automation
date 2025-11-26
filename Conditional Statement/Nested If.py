primalary=450
maine=450

if primalary >= 450:   ##outer if
    print("You have cleared the primalary ")
    print("Next will be your main exam")
    if maine>=500:  ##Nested/Inner If
        print("You have cleared the main EXAM")
    else:
        print("You have failed in the main EXAM")

else:
    print("You are failed in the primlary exam")