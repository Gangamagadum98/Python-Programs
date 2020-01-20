class Socialmedia:
    noOfUsers = 100

    def __init__(self,users):
        self.noOfUsers = users

    @classmethod
    def factory(cls,users):
        return cls(users)

    @staticmethod
    def messenger(user):
        return "Messaging"+ user

#Create obj using class
facBook = Socialmedia(1000)
print(facBook.noOfUsers)

#Create obj using factory method
instagram = Socialmedia.factory(2000)
print(instagram.noOfUsers)

#Call static Method
messenger = Socialmedia.messenger("  Harshit")
print(messenger)

