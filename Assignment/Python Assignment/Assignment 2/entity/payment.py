class Payment:
    def __init__(self, payment_id, student, amount, payment_date):
        self.payment_id = payment_id
        self.student = student
        self.amount = amount
        self.payment_date = payment_date

    def get_student(self):
        # Retrieves the student associated with the payment
        return self.student

    def get_payment_amount(self):
        # Retrieves the payment amount
        return self.amount

    def get_payment_date(self):
        # Retrieves the payment date
        return self.payment_date