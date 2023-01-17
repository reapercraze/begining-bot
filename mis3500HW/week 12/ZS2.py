class Customer:
    def __init__(self, name, address, creditcard):
        self.name = name
        self.address = address
        self.__creditcard = creditcard
    
    def get_creditcard(self):
        return self.__creditcard
        
    def set_creditcard(self, creditcard):
        self.__creditcard = creditcard
        
    def print_info(self):
        print("customer's name:", self.name)
        print("customer's address:", self.address)
        print("customer's creditcard(last 4):", str(self.__creditcard)[-4:])

cust1 = Customer("Tyler Gale", "1234 address", 123412345678)
print(cust1.print_info())
cust1.set_creditcard(1234123412345678)
print(cust1.get_creditcard())