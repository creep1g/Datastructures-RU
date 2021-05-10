from DLL_class import _DoubleLinkedList

class Set(_DoubleLinkedList):
    
    def add(self, data):
        node = self.sentinel.next
        inn = False
        while node != self.sentinel:
            if node.element == data:
                inn = True
                break
            node = node.next

        if not inn:
            self.insert_front(data)
    



sete = Set()
sete.add(2)
sete.add(3)
sete.add(2)
sete.add(239)
sete.add(2)
print(sete)
