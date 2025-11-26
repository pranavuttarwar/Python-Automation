shoppingamt=600

if shoppingamt>=500:   #outer if
    print("You dont have to pay the delivery charge")

    if shoppingamt>=1000: #Inner/Nested If
        print("You will received 10% discount on payment")
    else:
        print("You are not eligible for 10% discount minimum 1000rs required.")

else:
    print("You will be charges 50rs for the delivery")