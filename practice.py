# # # Practice Q1

def start():
  print("Welcome to python island")
start_1=input('What is your user name ?',  )
print("Welcome home", start_1)

# # #Practice Q2
Age= input("How old are you?" )
print(Age)

# # #Practice Q3
Favourite_colour= input("What is your Favourite colour?" )

Favourite_animal= input("What is your Favourite animal?" )
Pirate_name = (Favourite_colour+Favourite_animal)
print("Welcome aboard,", Pirate_name)

# #Practice Q4
Treasure_coins= (int(input('How wany gold coins were found?')))
print(Treasure_coins)

# #Practice Q5
Number_of_pirates= int(input("How many Pirates are in the crew ?" ))
print(int(Treasure_coins/Number_of_pirates))
 
#  #Practice Q6
if (Treasure_coins/Number_of_pirates)>= 15:
  print("Yes all pirates have atleast 15 coins")

else:
 print('no all pirates do not have atleast 15 coins"')

#Practice Q7
guess=input("What is the secret number?")
if(int(guess))== 7:
 print(" You guessed right!")

else:
 print(" No sorry, Try again")

 #Practice Q8
Enter_a_word= input(str("Enter a word"))
for number in range(5): # used to create a loop
 print(Enter_a_word)

# #Practice Q9
Treasure_Inventory= ["Sword","Compass","Map","Key","Latern"]
print(Treasure_Inventory)

# #Practice Q10
print(len(Treasure_Inventory))


#Practice Q11
age=(int(input("What is your age ?")))
if age >= 18:
    print("Access Granted!")


else:
    print("Access Denied")

#Practice Q12
Gold_coins= int(input("How many gold coins"))
Silver_coins= int(input("How many silver coins"))
print (Gold_coins+Silver_coins)
print(Gold_coins-Silver_coins)
print(Gold_coins*Silver_coins)
print(Gold_coins/Silver_coins)

#Practice QFinal challenge
def start():
    print("Hello! Welcome to python Island")
Name= input("What is your name")
Age= input("What is your age")
pirate_name=(Name+ Age)
print("Your pirate name is", pirate_name)
Treasure= (int(input('How wany treasure were found?')))
print(Treasure)

Number_of_pirates= int(input("How many Pirates are in the crew that found the treasyre?" ))
print(int(Treasure/Number_of_pirates))

if (Treasure/Number_of_pirates)>= 15:
   print("Hurray! all pirates have atleast 15 coins")

else:
  print('Oops1 all pirates do not have atleast 15 coins"')
