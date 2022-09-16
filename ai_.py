class AI_john:
    def __init__(self):
        self.response = {}
        self.learning = 0
        self.reply = ""

        while(1):
            data = str(input())
            self.__brain__(data)

    def __brain__(self, data):
        if "*****" in data:
            self.learning = 1
        else:
            if self.learning == 0:
                self.__processing__(data)
            elif self.learning == 1 and '-' in data:
                self.__M_learning__(data)
            else:
                self.__processing__(data)

    def __M_learning__(self, data):
        data = data.split("-")
        key = data[0]
        value = data[1]
        self.__input__(key, value)

    def __processing__(self, key):
        if self.response.get(key):
            self.reply = self.response[key]
            self.__output__(self.reply)
        else:
            self.__output__("")


    def __output__(self, reply):
        if (reply == ""):
            print("\t")
            print("I do not uunderstand. You can teach me. Use *****")
        else:
            print("\t")
            print(reply)
    def __input__(self, key, value):
        self.response[key] = value
        self.__output__("it is understood")

person = AI_john()
