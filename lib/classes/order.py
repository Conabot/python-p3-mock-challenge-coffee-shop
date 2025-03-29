
class Order:
    all = []

    def __init__(self, customer, coffee, price):
        from classes.customer import Customer
        from classes.coffee import Coffee

        if not isinstance(customer, Customer):
            raise Exception("Customer must be of type Customer")
        self._customer = customer

        if not isinstance(coffee, Coffee):
            raise Exception("Coffee must be of type Coffee")
        self._coffee = coffee
        

        self.price = price

        customer.orders(self)
        coffee.orders(self)

        Order.all.append(self)

    @property
    def customer(self):
        return self._customer
    @customer.setter
    def customer(self, value):
        from classes.customer import Customer
        if not isinstance(value, Customer):
                raise Exception("Customer must be of type Customer")
        self._customer = value

    @property
    def coffee(self):
        return self._coffee
    @coffee.setter
    def coffee(self, value):
        if not isinstance(value, Coffee):
            from classes.coffee import Coffee
            raise Exception("Coffee must be of type Coffee")
        self._coffee = value
        

    @property
    def price(self):
        return self._price
        
    @price.setter
    def price(self, value):
        if not isinstance(value, (int, float)):
            raise Exception("Price must be a number")
        if not 1 <= value <= 10:
            raise Exception("Price must be non-negative")
        self._price = value


        # self.customer = customer
        # self.coffee = coffee
        # self.price = price
