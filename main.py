"""  calculation_to_seconds = 30*40*10,
print(f"20 days are {20 * calculation_to_seconds} seconds"),
days = 7,

#function code in python
def days_in_week(days_number_count, custom_message):
  print(f"{days_number_count} starting from monday to sunday that's {days_number_count * days}"),

days_in_week(30,"hello favour")
days_in_week(50,"tech bro")

#we use scope function to get data from other function without writing them in my scope_check, function
def scope_check(custom_message):
  my_var = "variable inside function"
  print(custom_message)
  print(my_var)
scope_check("am a good developer")

input("give me your age \n"), num_one = 20

def name_of_boys():
    if num_one > 50:
     return f"call all the boys number here is called what again"
    else:
        return "you enter wrong number, try again"

user_input = "",
while user_input != "exit":
    user_input = input("hey user enter number of days i will convert it to hours ")
    name_of_boys() """
"""  [1,3,5].count()
"2, 3".split() """

def days_in_week(num_of_days, conversion_unit):
    if conversion_unit == "hours":
        return  f"{num_of_days} days are {num_of_days * 24} hours"
    elif conversion_unit == "minutes":
        return f"{num_of_days} days are {num_of_days * 24 * 60} minutes"
    else:
        return "unsupported unit",

user_input = "",
def check_days_now():
    if user_input == "hours":
        return input("number of hours in ")
    elif user_input == "minutes":
        return  input("number of minutes")
    else:
        return "no one match"

check_days_now()