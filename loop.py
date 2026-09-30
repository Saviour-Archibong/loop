#for loop


for i in range(5):
    print("hello world")

name = ["saviour","david", "john","mark","joy"]
for i in name:
    print(i)

total = 0

for number in range(1,7):
    total =+ number
    print(f'that is the   {total}')

number = 1
while number <= 5:
    print(number)
    number += 1




    import random
total_score = 0
print("welcome to python ")
for throw in range (1, 6):
    p_score = random.randint(0, 10)
    print(f"throw  {throw}")
    total_score = total_score + p_score
print("\n game is over")
print(f"the total score is {total_score}")


player_name = input("enter your name")
total_score = 0
print(f"\n welcome to python {player_name}")
print("you can score 18 or more point to win? let find out \n  ")
for throw in range (1, 6):
    input(f"press enter to throw the dice  {throw}")
    p_score = random.randint(0, 10)
    print(f"you score {p_score} point \n ")
    total_score = total_score + p_score 
print("\n game is over")
print(f"the total score is {total_score}")
if total_score >= 18:
   print(f"amazing job {player_name}")
elif total_score >= 10:
   print(f"not bad {player_name}")
else:
   print(f"you lose {player_name}") 



