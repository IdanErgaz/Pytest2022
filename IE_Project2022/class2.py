class worker:
    def __init__(self, first, last, role, age):
        self.first=first
        self.last=last
        self.role=role
        self.age=age

    def printDetails(self):
        print('The worker details are: firatName:{}, LastName={}, Role:{} and Age:{}'.format(self.first, self.last, self.role, self.age))

newWorker=worker('Idan', 'Ergaz', 'Manager', 42)

newWorker.printDetails()