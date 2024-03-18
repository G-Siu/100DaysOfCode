# prompt user for username
# promt user for password
# validUserName is Admin
# validPassword is Password
# if username == validUserName and password == validPassword
#    print Welcome back
# else
#    print Wrong username or password

username = input("Please enter your username : ")
password = input("Please enter your password : ")
validUserName = "Admin"
validPassword = "Password"
if username == validUserName and password == validPassword :
    print("Welcome back")
else :
    print("Wrong username or password")