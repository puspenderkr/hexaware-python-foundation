class User:
    def __init__(self, userID, userName, email, password, contactNumber, address):
        self.__userID = userID
        self.__userName = userName
        self.__email = email
        self.__password = password
        self.__contactNumber = contactNumber
        self.__address = address

    def __str__(self):
        return f"User(ID: {self.__userID}, Name: {self.__userName}, Email: {self.__email}, " \
               f"Contact: {self.__contactNumber}, Address: {self.__address})"






