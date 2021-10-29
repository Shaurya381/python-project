print("Hello its a 5 step answer guessing game, by Shaurya Grewal\n")
import random

l = [70, 20, 80, 32, 54, 28, 12, 50, 30, 90, 40, 10, 38, 60, 62, 78, 76, 74, 72]
add = random.choice(l)

input("Step 1:\nThink of a number in your mind between 1 to 20\nType yes to continue : \n")

input("Step 2:\nMultiply your number with 2\nType yes to continue : \n") 

input(f"Step 3:\nNow add the answer with {add}\nType yes to continue : \n")

input("Step 4:\nNow make it half\nType yes to continue : \n")

input("Step 5:\nNow subtract your original number that you chose earlier \nType yes to get shocked now : \n")

input(f"Is your answer {int(add/2)} !\n")