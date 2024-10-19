class Person:    
    def __init__(self, name, age):    
        self.name = name    
        self.age = age    
        
    def __str__(self):    
        return f"{self.name} ({self.age})"  
      
person = Person('Vikas', 22)  
print(person)  