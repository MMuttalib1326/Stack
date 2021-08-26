# Implementation of Stack using List.

class stack:
    def __init__(self):
        self.list=[]
    
    def __str__(self):
        values=self.list.reverse()
        values=[str(x) for x in self.list]
        return '\n'.join(values)    
# Is empty    
    
    def isempty(self):
        if self.list==[]:
            return True
        else:
            return False

# push

    def push(self,value):
        self.list.append(value)
        return "The element has been succesfully inserted" 

# pop

    def pop(self):
        if self.isempty():
            return "There is not any element in the stack"
        else:
            return self.list.pop()

# peek

    def peek(self):
        if self.isempty():
            return "There is no any element in the stack"
        else:
            self.list[len(self.list)-1] 

# delete

    def delete(self):
        self.list=None                                            
customstack=stack()
print(customstack.isempty())
customstack.push(1)  
customstack.push(2)
customstack.push(3)
customstack.push(4)
#print(customstack)
print(customstack.pop())
print(customstack.peek())
print(customstack.delete())          