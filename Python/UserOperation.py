from User import *

class Users:
    def __init__(self):
        self.Users_list = []

    def add(self, new_User):
        isFind = False

        for Us in self.Users_list:
            if(Us._chat_id == new_User._chat_id):
                isFind = True
                Us = new_User
                break
        
        if(isFind != True):
            self.Users_list.append(new_User)

    def print(self):
        for User in self.Users_list:
            print(User.toString())

        print("- - - - - - - - - - - - - -")

    def get_user_by_chat_id(self, chat_id):
        for user in self.Users_list:
            if user.chat_id == chat_id:
                return user

        return None