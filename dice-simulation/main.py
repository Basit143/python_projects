import random

num_dice = int(input("Enter the number of dice to roll: "))
num_sides = int(input("Enter the number of sides per die: "))

rolls = []
for i in range(num_dice):
    roll = random.randint(1, num_sides)
    rolls.append(roll)

print(f"You rolled: {', '.join(str(roll) for roll in rolls)}")

total = sum(rolls)
print(f"The sum of the rolls is: {total}")
