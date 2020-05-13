import random
l = "l"
q = "q"
def listDices():
	print("""Welcome to the dice simulator!

		Dice number: description
		1: Normal Dice (D6)
		2: Tetrahedron (D4)
		3: Octahedron (D8)
		4: Pentagonal trapezohedron (D10)
		5: Dodecahedron (D12)
		6: Icosahedron (D20)

		l: display dices
		q: quits this program

		Which dice would you like to roll?
		""") #lists options to choose from

def rollDice(min, max): #define dice roll
	return random.randint(min,max)

listDices()

while 1==1:
	answer = input("Dice number: ")

	if answer == 1:
		print("Rolling a normal dice...")
		print(rollDice(1,6))
	elif answer == 2:
		print("Rolling a tetrahedron...")
		print(rollDice(1,4))
	elif answer == 3:
		print("Rolling a octahedron...")
		print(rollDice(1,8))
	elif answer == 4:
		print("Rolling a pentagonal trapezohedron...")
		print(rollDice(1,10))
	elif answer == 5:
		print("Rolling a dodecahedron")
		print(rollDice(1,12))
	elif answer == 6:
		print("Rolling a icosahedron")
		print(rollDice(1,20))
	elif answer == q:
		print("Goodbye!")
		break
	elif answer == l:
		listDices()
	else:
		print("Please input a correct dice number!");
