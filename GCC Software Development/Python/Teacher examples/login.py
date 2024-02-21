# variable username = yourname
# variable password = glasgow

# for i in range 0 to 4
#    input strUser
#    input strPassword
#    if strUser == username and strPassword == password
#        print "Welcome"
#        break
#    else
#        print "Invalid details"
#    

username = "Paul"
password = "glasgow"
number_of_attempts = 2

for i in range(number_of_attempts) :
    strUsername = input("Please enter your username : ")
    strPassword = input("Please enter your password : ")
    
    if strUsername == username and strPassword == password :
        print("Welcome")
        break
    else :
        print("Wrong details entered")

