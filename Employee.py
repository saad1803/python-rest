class Employee :
    emp = 0
    __name = ''
    __salary = 0
    
    def __init__(self,name,salary) :
        self.name = name
        self.salary = salary
        Employee.emp += 1

    def printEmployee (self) :
        print self.name + ' ' + str(self.salary)
    
