#%%

class Student: 
    
    def __init__(self, name, gpa): 
        self.name = name
        self.gpa = gpa 


#We create a call-response between methods becase we want different
#instances to respond differently.         
    
    def apply(self, university): 
        if university.accepts(self): 
            return True
        else:
            return False
        


class University: 
    
    def __init__(self, min_gpa, course_list): 
        self.min_gpa = min_gpa
        self.course_list = course_list
        
    def accepts(self, student): 
        if student.gpa >= self.min_gpa: 
            return True
        else: 
            return False 
        
class Course: 
 
#Writting this and the self.students initialized to an empyt list, 
#is the same. 
    
    students = []
    
    def __init__(self, name, max_students): 
        self.name = name
        self.max_students = max_students   
#        self.students = []
        
    def enroll(self, student): 
        if self.max_students > len(self.students): 
            self.students.append(student)
        else: 
            print("bad luck fella")
            
            
courses_delaware = [Course("tax evasion 101", 100)]
delaware_uni = University(1.3, courses_delaware)
pepe = Student("Pepe", 1.3)

print(pepe.apply(delaware_uni))

programming = Course("programming", 1)
persuasion = Course("persuasion skills", 27)

courses_ie = [
        programming, 
        persuasion
        
        ]

ie_uni = University(3.6, courses_ie)

print