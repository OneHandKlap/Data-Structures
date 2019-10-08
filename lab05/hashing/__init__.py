class hashtable():
    def __init__(self,size=11):
        self.size=size
        self.slots=[None]*size
        self.data=[None]*size

    def put(self,key,data):
        load_factor = self.get_load()
        if load_factor>.75:
            self.resize_map()
        hashvalue = self.hashfunction(key,self.size)
        if self.slots[hashvalue]==None:
            self.slots[hashvalue]=key
            self.data[hashvalue]=data
        else:
            if self.slots[hashvalue]==key:
                self.data[hashvalue]=data
            else:
                nextslot = self.rehash(hashvalue,self.size)
                while self.slots[nextslot]!=None and self.slots[nextslot]!=key:
                    nextslot=self.rehash(nextslot,self.size)
                if self.slots[nextslot]==None:
                    self.slots[nextslot]=key
                    self.data[nextslot]=data
                else:
                    self.data[nextslot]=data

    def get(self,key):
        startslot = self.hashfunction(key,len(self.slots))

        data = None
        stop = False
        found = False
        position = startslot
        while self.slots[position] != None and  \
                            not found and not stop:
            if self.slots[position] == key:
                found = True
                data = self.data[position]
            else:
                position=self.rehash(position,len(self.slots))
                if position == startslot:
                    stop = True
        return data

    def __getitem__(self,key):
        return self.get(key)

    def __setitem__(self,key,data):
         self.put(key,data)

    def hashfunction(self,key,size):
        return key%size

    def rehash(self,oldhash,size):
        return (oldhash+1)%size
    def get_data(self):
        return self.data
    def get_load(self):
        used_slots=0
        for x in self.data:
            if x != None:
                used_slots+=1
        return float(used_slots/self.size)

    def resize_map(self):
        temp_slots=self.slots
        temp_data=self.data
        self.size=2*self.size
        self.slots=[None]*self.size
        self.data=[None]*self.size
        
        for x in range(len(temp_slots)):
            if temp_slots[x]!=None:
                self.put(temp_slots[x],temp_data[x])
        