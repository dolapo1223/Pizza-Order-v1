# 🚨 Don't change the code below 👇
print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M, or L:  ")
add_pepperoni = input("Do you want pepperoni? Y or N : ")
extra_cheese = input("Do you want extra cheese? Y or N:  ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇 
#Constant
SMALL_PIZZA = 15
MEDIUM_PIZZA = 20
LARGE_PIZZA = 25


#Total bill here
bill = 0

if size == "S":
  bill += SMALL_PIZZA
elif size == "M":
  bill += MEDIUM_PIZZA
else:
  size == LARGE_PIZZA

if add_pepperoni == "Y":
  if size == "Y":
    bill+=2
  else:
    bill+=3
if extra_cheese == "Y":
  bill+= 1

print(f"You final total is {bill}")





