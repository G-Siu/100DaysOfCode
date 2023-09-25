# PascalCase
class User:
    # Initialise attributes
    def __init__(self, user_id, username):
        print("New user being created...")
        self.id = user_id
        self.username = username
        self.followers = 0  # Can default value so 0 doesn't have to be created everytime down below
        self.following = 0

    def follow(self, user):
        user.followers += 1
        self.following += 1


user_1 = User("001", "Gary") # Initialises __init__ everytime User() is called
user_2 = User("002", "Jack")

user_1.follow(user_2)
print(user_1.followers)
print(user_1.following)
print(user_2.followers)
print(user_2.following)

# user_1id = "001"
# user_1.username = "Gary"

# print(user_1.id)

# user_2 = User()
# user_2.id = "002"
# user_2.username = "Jack"

# print(user_2.username)
