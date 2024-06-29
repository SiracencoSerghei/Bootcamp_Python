# class User:
#     pass
#
# user_1 = User()
# user_1.id = "001"
# user_1.username = "Sergio"

# print(user_1)
# print(user_1.username)


#  Constructor

# class User:
#     def __init__(self, user_id,username,):
#         print("New user is being created....")
#         self.id = user_id
#         self.username = username
#         self.followers = 0
# # user_1 = User()  # TypeError: User.__init__() missing 2 required positional arguments: 'user_id' and 'username'
# user_1 = User("1", "Sergio")

# print(user_1.id, user_1.username)
# user_1.id = "001"
# user_1.username = "Pietro"
# print(user_1.id)
# print(user_1.username)
# print(user_1.followers)

#  Methods


class User:
    def __init__(self, user_id, username):
        print("New user is being created....")
        self.id = user_id
        self.username = username
        self.followers = 0

    def follow(self):
        self.followers += 1

    def unfollow(self):
        self.followers -= 1


user_1 = User("1", "Sergio")

user_1.follow()
user_1.follow()
print(user_1.followers)

user_1.unfollow()
print(user_1.followers)
