
red = '\033[31m'

class Package:
    def __init__(self, id, address, city, state, zipcode, deadline, weight, status):
        self.id = id
        self.address = address
        self.city = city
        self.state = state
        self.zipcode = zipcode
        self.deadline = deadline
        self.weight = weight
        self.status = status

    def __str__(self):
        return f"{self.id} | {self.address}, {self.city}, {self.zipcode} {self.state}, {self.deadline}, {self.weight}, {self.status}"




