from bucket import Bucket, NotFoundException, ItemExistsException


class HashMap:

    def __init__(self):
        '''Initialize hashmap as an array'''
        self.capacity = 8
        self.arr = [None] * self.capacity
        self.size = 0

    def insert(self, key, data):
        '''Drops key:data into a bucket corresponding to its generated index'''
        
        if self.contains(key):
            raise ItemExistsException()

        self._check_if_at_capacity()
        index = self.__hash(key)
        if self.arr[index] is None:
            self.arr[index] = Bucket()
        self.arr[index].insert(key, data)

    def __hash(self, key):
        '''Generates index by hashing key value'''
        index = hash(key) % self.capacity
        return index

    def _check_if_at_capacity(self):
        '''Checks if datastructure is 120% above the defined capacity of its
        array, if at capacity > rebuild. '''
        counter = 0
        if self.__len__() > round(1.2 * self.capacity):
            self._rebuild()

    def _rebuild(self):
        '''Rebuilds the array doubling its capacity.'''
        self.capacity *= 2
        temp = self.arr
        self.arr = [None] * self.capacity
        
        for bucket in temp:
            if bucket is not None:
                for item in bucket:
                    self.insert(item.key, item.value)

    def update(self, key, data):
        '''Update data value of key:value pair where key is equal'''
        index = self.__hash(key)
        if self.contains(key):
            self.arr[index][key] = data
        else:
            raise NotFoundException

    def find(self, key):
        '''Returns data from key:data pair where key is equal'''
        index = self.__hash(key)
        if self.contains(key):
            self.arr[index][key]
        else:
            raise NotFoundException

    def contains(self, key):
        '''Checks if key is found in the data structure'''
        index = self.__hash(key)
        if self.arr[index] is not None:
            return self.arr[index].contains(key)
        else:
            return False

    def remove(self, key):
        '''Removes key:value pair with equal key'''
        index = self.__hash(key)
        if self.contains(key):
            self.arr[index].remove(key)
        else:
            raise NotFoundException()

    def __setitem__(self, key, data):
        '''If key already exists, update its data, else insert a new instance'''
        if self.contains(key):
            self.update(key, data)
        else:
            self.insert(key, data)

    def __getitem__(self, key):
        '''Returns data of key:value pair with equal key'''
        self.find(key)

    def __len__(self):
        '''Returns size of datastructure'''
        counter = 0
        for i in self.arr:
            if i is not None:
                counter += len(i)
        return counter

    def __str__(self):
        return str(self.arr)


if __name__ == '__main__':
    hass = HashMap()
    hass.insert(1, ["pap"])
    hass.insert('2', ["3"])
    hass.insert(3, ["12"])
    hass.insert('4', ["8"])
    hass.insert(5, ["8"])
    hass.insert(6, ["8"])
    hass.insert(7, ["8"])
    hass.insert(8, ["8"])
    hass.insert(10, ["8"])
    hass.insert(11, ["8"])
    hass.insert(12, ["8"])
    hass.insert(13, ["8"])
    hass.insert(14, ["8"])
    print(hass.contains(4))
    print(hass.contains(8))
    print(hass.contains("asoeu"))
    hass.remove(8)
    print(hass.contains(8))
    print(hass)
    hass[8] = 'aeou'
    hass[8] = '388338'
    print(len(hass))
