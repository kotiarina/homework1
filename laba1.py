my_name = "Ekaterina"
print(my_name)
my_age = "18"
print("My name is", my_name, ". I'm", my_age,"years old.")
my_name_5x = my_name*5
print(my_name_5x)
user_name = input("What's your name?")
user_age = input("How old are you?")
try:
    user_age_int = int(user_age)
except ValueError:
    print("Enter value")
if user_age_int < 30:
    print("Hello,", user_name, ".", "OMG you're", user_age, "years old. It's time to die for you.^_^")
else:
    print("Hello,", user_name, ".", "OMG you're", user_age, "years old. Sweet baby.^_^")
user_name_stroka = str(user_name)
print(user_name_stroka[1:-1:1])
print(user_name_stroka[::-1])
print(user_name_stroka[-3::1])
print(user_name_stroka[:5:1])
length_of_user_name =len(user_name_stroka)
multiplication_age = 1
summ_age = 0
user_age = int(user_age)
while (user_age != 0):
    summ_age = summ_age + (user_age % 10)
    multiplication_age = multiplication_age * (user_age % 10)
    user_age = user_age // 10
print("length=", length_of_user_name,"summ=",summ_age,"multiplication=", multiplication_age)
answer = input("Print the rezult of 2+2")
if (answer != 4):
    print("Error!")
else:
    print("Correct")
    