class User:
    def __init__(self, chat_id, classNumber, Name):
        self._chat_id = chat_id                         # Chat id

        if(classNumber >= 1 and 11 <= classNumber):
            self._classNumber = classNumber             # Class Number

        self._name = Name                               # Name
        
    def __init__(self, chat_id, Name):
        self._chat_id = chat_id               
        self._classNumber = 1
        self._name = Name

    def toString(self):
        res = str()

        res += "\tUser: "   + str(self._name)       + "\n"
        res += "Chat id: "  + str(self._chat_id)    + "\n"
        res += "Class: "    + str(self.classNumber) + "\n"

        return res

    # property
    @property
    def classNumber(self):
        return self._classNumber

    # setters  
    @classNumber.setter
    def classNumber(self, ClassNumber):

        if(ClassNumber < 1 and 11 > ClassNumber):
            self._classNumber = 1
        else:
            self._classNumber = ClassNumber
        