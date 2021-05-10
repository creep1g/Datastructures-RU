

class Key:
    
    def __init__(self, key, val):
        self.key = key
        self.val = val

    def __lt__(self, other):
        if self.key < other.key:
            return True

    def __str__(self):
        return '{'+str(self.key)+':'+str(self.val)+'}'

class Map:

    def __init__(self):
        self.map = []

    def insert(self, key, value):
        
        exists = self.__check_if_exists(self.map, 0, len(self.map)-1, key)

        if not exists:
            element = Key(key, value)
            self.map.insert(0, element)
            self.map.sort()

    def sort(self):
        self.map.sort()
        if self.map[-1] is None:
            self.map.pop(len(self.map)-1)

    def __check_if_exists(self, lis, low, high, key):
        if high >= low:
            mid = high + low // 2
            
            if lis[mid].key == key:
                return lis[mid]
            
            elif lis[mid].key > key:
                return self.__check_if_exists(lis, low, mid - 1, key)

            else:
                return self.__check_if_exists(lis, mid + 1, high, key)
        else:
            return None

    def find(self, key):
        data = self.__check_if_exists(self.map, 0, len(self.map)-1, key)
        return data

    def update(self, key, value):
        data = self.__check_if_exists(self.map, 0, len(self.map)-1, key)
        if data is not None:
            data.val = value

    def remove(self, key):
        for i in range(len(self.map)):
            if self.map[i].key == key:
                self.map.pop(i)
                break
    
    def __setitem__(self, key, value):
        exists = self.__check_if_exists(self.map, 0, len(self.map)-1, key)
        if exists is not None:
            self.update(key, value)
        else:
            self.insert(key, value)

    def __str__(self):
        ret_str = ''
        for i in self.map:
            ret_str += str(i) + ' '
        return ret_str

if __name__ == '__main__':
    dataMap = Map()
    dataMap.insert(1, 'eiddn')
    dataMap.insert(5, 'e')
    dataMap.insert(9, 'ei')
    dataMap.insert(4, 'eid')
    dataMap.insert(1, 'eidddd')
    dataMap.insert(5, 'eidddd')
    dataMap.insert(2, 'eidd')
    dataMap.insert(3, 'eiddd')
    dataMap.insert(8, 'eidddd')
    print(dataMap.find(9))
    print(dataMap.find(10))
    dataMap.update(1, 'piss')
    print(dataMap.find(1))
    dataMap.remove(4)
    dataMap[4] = 'Bubo'
    print(dataMap)
