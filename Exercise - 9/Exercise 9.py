## NIELIT Calicut python Training session
## ADVAIT GURUNATH CHAVAN
## Excercise No 9
"""Task -> Write a program that asks for your age in human years. 
Hint: Store the age in a variable and calculate your age in bird years. 
1 human year equals 9 bird years. 
 
If I am 1 year old in human years, my age in bird years is 9.If 
I am 2, then my age in dog years would be 18 and so on. 
 
The formula then is this: 
Age in bird years = Age in human years * 9 """


print("Hi There!!!")
print("Welcome to Age in Bird Years program")
name = input("Enter your name : ")
age_human = int(input(f"Hi {name}, enter your age here : "))
age_birds = age_human * 9
print(f"So {name} your age in human years is {age_human} and your age in bird years is {age_birds}")
