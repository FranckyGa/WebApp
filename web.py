import streamlit as st
import functions as func

#Get existing list
todos = func.get_todos()

#Add new items in the list
def add_todo():
    todo = st.session_state["new_todo"]  + "\n"        #kind of a dictionnary --> extract input from user
    todos.append(todo)
    func.write_todos(todos)


#to run it --> use terminal : streamlit run web.py              // replace web.py by the name of your file
#Order is important --> determine the order on the webpage
#NB : a refresh webpage re-run all the code

st.title("My Todo App")
st.subheader("This is my todo app.")
st.write("This app is designed to improve my productivity")

#Import existing todo list
for index, todo in enumerate(todos):
    checkboxs = st.checkbox(todo, key=todo)       #key = todo --> dynamic input and create a dictionary of each todo and get TRUE if user tick the box
    
    #Remove todo if box is ticked
    if checkboxs:
        todos.pop(index)
        func.write_todos(todos)
        del st.session_state[todo]
        st.experimental_rerun()

st.text_input(label="Enter a todo: ", placeholder="Add a new todo...", 
                on_change = add_todo, key = "new_todo")          #placeholder = hint for the user










