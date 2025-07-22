class listadd:
    sum = 0
    def list_add(self, values):
        for i in values:
            self.sum += i
ll = listadd()
ll.list_add([1,2])
ll.list_add([3])
ll.list_add([4,5,6])
print(ll.sum)
    
    
    
