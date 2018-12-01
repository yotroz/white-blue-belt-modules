#%%
#Create a function that reads through a file 
#and prints all the lines in uppercase.
#
# 
#
#be sure to control exceptions that may occur here, 
#such as the file not existing



def print_file_uppercase(filename): 
    
    try: 
    
        file = open(filename)
        for line in file: 
            print(line.upper().strip())
    except Exception: 
        print("file doesnt exist")
        
    
print_file_uppercase("data.txt")
print_file_uppercase("other_file.txt")


    