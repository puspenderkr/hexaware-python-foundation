class TrackingNumberNotFoundException(Exception):
    def __init__(self, message):
        super().__init__(message)


class InvalidEmployeeIdException(Exception):
    pass

