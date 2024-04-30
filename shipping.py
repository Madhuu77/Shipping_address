class Customer:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.shipping_addresses = []
        
    def display(self):
        if self.name is None:
            print("name not found!!")
        else:
            print("Name:",self.name)
        if self.email is None:
            print("email not found!!")
        else:
            print("e-mail:",self.email)
            

    def add_shipping_address(self, address):
        self.shipping_addresses.append(address)

    def delete_shipping_address(self, address):
        if address in self.shipping_addresses:
            self.shipping_addresses.remove(address)
        else:
            print("Address not found.")

    def update_shipping_address(self, old_address, new_address):
        if old_address in self.shipping_addresses:
            index = self.shipping_addresses.index(old_address)
            self.shipping_addresses[index] = new_address
        else:
            print("Address not found.")

customer1 = Customer("Madhu", "v8000m@gmail.com")
customer1.display()
customer1.add_shipping_address("Kannurahalli, Hosakote, Karnataka")
customer1.add_shipping_address("Gptc,Channasandra , Whitefield")

print("Shipping Addresses:")
for address in customer1.shipping_addresses:
    print("-->",address,end="\n")

customer1.delete_shipping_address("Gptc,Channasandra , Whitefield")

print("\nShipping Addresses after Deletion:")
for address in customer1.shipping_addresses:
    print("-->",address,end="\n")

customer1.update_shipping_address("Kannurahalli, Hosakote, Karnataka", "Kannur,Yelahanka,Bengaluru")

print("\nShipping Addresses after Update:")
for address in customer1.shipping_addresses:
    print("-->",address)
 