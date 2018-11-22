#Create a Student class that has the following attributes:
#
#name
#last name
#age
#master (either MCSBT or MDBI)
# Make sure you parametrize all those fields in the constructor.


#%%

class Student: 
    def __init__(self, name, last_name, age, master): 
        self.name = name
        self.last_name = last_name
        self.age = age
        self.master = master

tancredi = Student("Tancredi", "Rossetti", "9", "MCSBT")
    

print(tancredi.name + " " + tancredi.last_name + " " + " is " + tancredi.age + " and in the " + tancredi.master)