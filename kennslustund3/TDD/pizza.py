# Class that represents a pizza.


class Pizza:

    def __init__(self):
        self.data = dict()
        self.pizzanum = 0
        pass

    def create_pizza(self, topping_list):
        '''Takes a list of toppings as an argument, adds pizza with ID to data
        dict'''
        self.pizzanum += 1
        topping_list.append(False)
        self.data[str(self.pizzanum)] = topping_list
        return self.pizzanum

    def serve(self, id):
        '''Takes id of pizza as argument, marks pizza as served in data
        dict.'''
        try:
            pizza_info = self.data[str(id)]
            pizza_info[-1] = True
            return True
        except KeyError:
            return False

    def info_all(self):
        '''Returns a string with information about all pizzas.'''
        ret_str = ""
        for key, value in self.data.items():
            ret_str += "ID: {}, Toppings: ".format(key)
            for toppings in value:
                if type(toppings) is bool:
                    break
                ret_str += "{}, ".format(toppings)
            ret_str += "Served: {}\n".format(value[-1])

        return ret_str

    def remove_served(self):
        '''Remove every served pizza from data dictionary '''
        to_be_deleted = []
        for key, value in self.data.items():
            if value[-1] is True:
                to_be_deleted.append(key)
        
        for key in to_be_deleted:
            del self.data[key]


if __name__ == '__main__':
    pizza = Pizza()
    assert pizza.create_pizza(["A", "B", "C"]) == 1
    assert pizza.serve(1) is True
    assert pizza.serve(3) is False
    assert pizza.create_pizza(['D', 'E', 'F']) == 2
    print(pizza.info_all())
    assert pizza.info_all() == "ID: 1, Toppings: A, B, C, Served: True\nID: 2, Toppings: D, E, F, Served: False\n"
    assert pizza.create_pizza(['G', 'H', 'J']) == 3
    pizza.serve(3)
    pizza.remove_served()
    assert pizza.info_all() == "ID: 2, Toppings: D, E, F, Served: False\n"
