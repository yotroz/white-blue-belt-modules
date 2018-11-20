
 #%%       
class University: 
    students_university = []
    
    def __init__(self, name, courses, students): 
        
        self.name = name
        self.courses = courses
        self.students = students
        
        
        
class Student: 
    
    def __init__(self, name, gpa, courses): 
        self.name = name
        self.gpa = gpa
        self.courses = courses
        
    def apply_university(self, gpa): 
        if self.gpa > 3.8: 
            students_university.append(self)
            
    def apply_courses(self): 
        if students_course < maximum_students: 
            students_course.append(self)           
            

class Course: 
    
    
    students_course = []
    
    def __init__(self, name, code, maximum_students): 
        self.name = name
        self.code = code
        self.maxiumum_students = maximum_students        
    
    
    
         



