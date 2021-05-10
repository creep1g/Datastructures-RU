
class OrderLog:

    def __init__(self):
        self.order_list = []

    def print_log(self):
        print_str = "" 
        for order in self.order_list:
            print_str += "ID: {}, Pizzaz: ".format(order[0])
            for i in order:
                if order.index(i) > 1 and order.index(i) < len(order):
                    print_str += "{}, ".format(str(i))
            
            print_str += "Served: {}".format(order[1])
            print(print_str)
            print_str = ""

    def create_order(self, order_id):
        new_order = [order_id, False]
        self.order_list.append(new_order)

    def add_to_order(self, order_id, pizza):
        for order in self.order_list:
            if order[0] == order_id:
                order.append(pizza)

    def mark_served(self, order_id):
        for order in self.order_list:
            if order[0] == order_id:
                order[1] = True

    def delete_served(self):
        pass

