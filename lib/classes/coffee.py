class Coffee:
    def __init__(self, name):
        self._orders = []
        self._name = name

    @property
    def name(self):
        return self._name
   
    @name.setter
    def name(self, value):
        if hasattr(self,'_name'):
            raise Exception("Can not change after the coffee is created")
        if not isinstance(value, str):
            raise Exception("Name must be a string")
        self._name = value
        
    def orders(self, new_order=None):
        from classes.order import Order
        if new_order is not None:
            if not isinstance(new_order, Order):
                raise Exception("Order must be of type Order")
            self._orders.append(new_order)
        return self._orders
        
    
    def customers(self, new_customer=None):
        from classes.customer import Customer
        if new_customer is not None:
            if not isinstance(new_customer, Customer):
                raise Exception("New customer must be of type Customer")
        return list(set(order.customer for order in self._orders))
       
    
    def num_orders(self):
        return len(self._orders)
        
    
    def average_price(self):
        if not self._orders:
            return 0
        total_price = sum(order.price for order in self._orders)
        return total_price / len(self._orders)
        