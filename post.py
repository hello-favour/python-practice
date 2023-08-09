from class_function import User

app_user_info = User("favour@gmail.com","favour", "123", "developer")
app_user_info.get_user_info()

app_user_info.change_job_title("software engineer")
app_user_info.get_user_info()

app_user_info.change_password("flutter")
app_user_info.get_user_info()
