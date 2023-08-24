def get_age():
	age = int(input("How old are you: "))
	return age

def get_name():
	name = input("What is your name: ")
	return name

user_age  = get_age()
user_name = get_name()

print(f"Your name is {user_name} and you are {user_age} years old.")
