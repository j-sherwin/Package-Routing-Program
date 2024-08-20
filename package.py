red = '\033[31m'
yellow = '\033[93m'
green = '\033[92m'
default = '\033[0m'

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
        if self.status == "At Hub":
            return f"{red}{self.id} | {self.address}, {self.city}, {self.state} {self.zipcode} | {self.deadline} | {self.weight} | {self.status}{default}"
        elif self.status == "En Route":
            return f"{yellow}{self.id} | {self.address}, {self.city}, {self.state} {self.zipcode} | {self.deadline} | {self.weight} | {self.status}{default}"
        else:
            return f"{green}{self.id} | {self.address}, {self.city}, {self.state} {self.zipcode} | {self.deadline} | {self.weight} | {self.status}{default}"






