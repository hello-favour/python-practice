class User:
    def __init__(self, user_email,name,password,current_job_title):
        self.email = user_email
        self.name = name
        self.password = password
        self.current_job_title = current_job_title

    def change_password(self,new_password):
        self.password = new_password

    def change_job_title(self,current_job_title):
        self.current_job_title = current_job_title

    def get_user_info(self):
        print(f"user {self.name} currently working as a {self.current_job_title}. you can contact them at {self.email} and his password is {self.password}")

app_user_info = User("favour@gmail.com","favour", "123", "developer")
app_user_info.get_user_info()

app_user_info.change_job_title("software engineer")
app_user_info.get_user_info()

app_user_info.change_password("flutter")
app_user_info.get_user_info()
