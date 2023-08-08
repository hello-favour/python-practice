from datetime import datetime

user_input = input("enter your goal with a deadline separated \n ")
input_list = user_input.split(":")

goal = input_list[0]
deadline = input_list[1]
print(input_list)

deadline_date = datetime.strptime(deadline, "%d.%m.%Y")
today_date = datetime.today()
time_till = deadline_date - today_date

print(f"there user time remaining for your: {goal} is {time_till}")
