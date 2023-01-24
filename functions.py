FILEPATH = "todos.txt"

#Read function
def get_todos(filepath=FILEPATH):                    #filename = "xx.ttxt"  --> default argument                      
    """Read the text file and return the list"""        #Way to add doc string --> if you use help() function in python console way to describe your function
    with open(filepath, "r") as file_local:             #Faster way to open and read file --> no need to close file
        todos_local = file_local.readlines()            #readlines = get everything in the file
    return todos_local

#Write procedure
def write_todos(todo_arg, filepath=FILEPATH):       #place no default parameter first then default parameters to avoid errors
    """Write the to do items list in the text file"""
    with open(filepath, "w") as file:
        file.writelines(todo_arg)                      #no return because nothing to return --> purpose is just to modify


# __name__ --> defined by python internally // allow to execute condition below only when we run this script, not when we run another script which call these functions
if __name__ == "__main__":
    print("hello from function")