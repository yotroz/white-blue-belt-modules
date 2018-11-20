#Add a print_student method in the Student class that 
#prints a line like follows for the object
#
#
#Pepe García is a 55 year old student of the MCSDBI masters programme
#
# 
#Create a list of all 28 Students representing all students in this class.  
#Then iterate over all of them and call 
#print_student on each one to print its description.
#%%


class Student:
    
    def __init__(self, name, last_name, age, master):
        self.name = name
        self.last_name = last_name
        self.age = age
        self.master = master
        
        
class Master:
    
    master_students = []
    
    def __init__(self, name):
        self.name = name
                
    def add_master_students_list(self, master_students_list):
        self.master_students += master_students_list
        
    def print_student(self):
        for student in self.master_students:      
            print(student.name + " is a "+ student.age + " years old student of the " + student.master + " masters program")      
         
mcsbt = Master("MCSBT")

master_students_list = [
    Student("Alejandro", "Meneses", "27", "MCSBT"),
    Student("Agata", "Kaczmarek", "31","MDBI"),
    Student("Anastasia", "Lasunina", "25", "MDBI"),
    Student("Anikken", "Barstad Gjeruldsen", "27", "MDBI"),
    Student("Arthur", "Maroquene-Froissart","23", "MCSBT"), 
    Student("Candela", "Noya", "24", "MDBI"),
    Student("Daniil", "Osipov", "21", "MDBI"),
    Student("David", "Barrero Gonzalez", "31", "MCSBT"),
    Student("Edem", "Francois", "28", "MCSBT"),
    Student("Felix ", "Fastrich", "23", "MDBI"),
    Student("Eduardo", "Paraja", "23", "MDBI"),
    Student("Florian", "Diegruber", "25", "MCSBT"),
    Student("Hannah", "Oldorf", "23", "MCBT"),
    Student("Isabella", "Rosenthal", "27", "MDBI"),
    Student("Javier", "Fernandez", "24", "MCSBT"),
    Student("Lukas", "Hauser", "28","MDBI"),
    Student("Leila", "Tazi", "27", "MCSBT"),
    Student("Laura", "Kageneck", "23", "MCSBT"),
    Student("Monica", "Alvarenga","28", "MDBI"),
    Student("Natalie", "Cedeno", "26", "MDBI"),
    Student("Octavio", "Ramírez", "28", "MDBI"),
    Student("Tancredi", "Bernard", "21", "MCSBT"),
    Student("Yasmine", "Lyagoubi", "23", "MDBI"),
    Student("Zineb", "Mezzour","22","MCSBT")
]


mcsbt.add_master_students_list(master_students_list)

mcsbt.print_student()

