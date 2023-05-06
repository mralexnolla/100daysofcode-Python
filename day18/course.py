class Users:
    def __init__(self, user_id, username):
        self.id = user_id
        self.username = username
        self.follower = 0
        self.following = 0

    def follow(self, user):
        user.follower += 1
        self.following += 1


user1 = Users("001", "alexnolla")
user2 = Users("002", "Esenolla")
user3 = Users("003", "Omame")

user1.follow(user2)
user3.follow(user2)

print("User3 follower", user3.following)



