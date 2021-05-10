from pizza2 import Pizza
from orderlog import OrderLog


class PizzaOrder:

    def __init__(self):
        self.log = OrderLog()
        self.id_count = 0

    def create_order(self):
        self.id_count += 1
        self.log.create_order(self.id_count)
        return self.id_count

    def add_pizza(self, order_id, pizza_name):
        pizza = Pizza(pizza_name)
        self.log.add_to_order(order_id, pizza)

    def serve_order(self, orderID):
        self.log.mark_served(orderID)

    def __str__(self, ord_id):
        pass

    def print_log(self):
        self.log.print_log()


if __name__ == '__main__':
    order = PizzaOrder()
    order1 = order.create_order()
    order.add_pizza(order1, "Svepperoni")
    order.add_pizza(order1, "Prinsessann")
    order.add_pizza(order1, "Sweetnspicy")
    order.add_pizza(order1, "Pepperoni")
    order.print_log()
    order2 = order.create_order()
    order.add_pizza(order2, "kukapizza")
    order3 = order.create_order()
    order.add_pizza(order3, "skinka")
    order.add_pizza(order3, "skitur")
    order.serve_order(order2)
    order.print_log()

