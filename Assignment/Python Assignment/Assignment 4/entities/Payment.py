class Payment:
    def __init__(self, paymentID, courierID, amount, paymentDate):
        self.__paymentID = paymentID
        self.__courierID = courierID
        self.__amount = amount
        self.__paymentDate = paymentDate


    def __str__(self):
        return f"Payment(ID: {self.__paymentID}, CourierID: {self.__courierID}, " \
               f"Amount: {self.__amount}, Date: {self.__paymentDate})"
