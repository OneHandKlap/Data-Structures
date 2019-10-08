class HashTable():
    def __init__(self,size):
        self.size=size
        self.slots=[None]*self.size
        self.data=[None]*self.size

    def get_data(self):
        return self.data
    def __getitem__(self,key):
        return self.get(key)

    def __setitem__(self,key,data):
        self.put(key,data)

    def hashFunction(self,key):
        return key%self.size

    def reHash(self,oldhash):
        return (oldhash+1)%size

    def put(self, key, data):
        hashvalue = self.hashFunction(key)

        if self.slots[hashvalue]== None:
            self.slots[hashvalue]=key
            self.data[hashvalue]=data
        else:
            if self.slots[hashvalue]==key:
                self.data[hashvalue]=data
            else:
                nextSlot = self.reHash(hashvalue)
                while self.slots[nextSlot] != None and self.slots[nextSlot]!=key:
                    nextSlot= self.rehash(nextSlot)
                if self.slots[nextSlot]== None:
                    self.slots[nextslot]=key
                    self.data[nextslot]=data

                else:
                    self.data[nextSlot]=data

        def get(self,key):
            firstSlot = self.hashFunction(key)

            data = None
            stop = False
            found = False
            position = firstSlot

            while self.slots[position] != None and not found and not stop:
                if self.slots[position]==key:
                    found = True
                    data = self.data[position]
                else:
                    position = self.rehash(position)
                    if position == firstSlot:
                        stop = True

            return data

test=HashTable(11)
test[54]="cat"
test[26]="dog"
test[93]="lion"

print(test.data)

