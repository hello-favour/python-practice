from class_function import User
from another_post import  Anotherpost

app_user_info = User("favour@gmail.com","favour", "123", "developer")
app_user_info.get_user_info()

app_user_info.change_job_title("software engineer")
app_user_info.get_user_info()

app_user_info.change_password("flutter")
app_user_info.get_user_info()

app_another_user_info = Anotherpost("on a secret mission today", "favor")
app_another_user_info.get_another_post_info()