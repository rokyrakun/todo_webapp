import streamlit as st  #streamlit library to create web apps
                        #integrates very well with apps
                        #easy deployment
import functions

todos = functions.get_todos()

def add_todo():
    new_todo = st.session_state["add"] + "\n" #gives us the value of the session_state object
    todos.append(new_todo)
    functions.write_todos(todos)


st.title("My To-Do list App")
st.subheader("This is my todo app")
st.write("This app is to increase your productivity")

for index, todo in enumerate(todos):
    checkbox = st.checkbox(todo, key=todo)  #so, the key is now all the todo items in the todos list
                                            #as you scroll down the list, whichever one you're on is True
    if checkbox: #implies checkbox = true
        todos.pop(index)
        functions.write_todos(todos)
        del st.session_state[todo]
        st.rerun()  #must add this refresh page command when processing checkboxes
                    #not much explanation beyond that


st.text_input(label=" ", placeholder="Add new To-Do Item ...",
              on_change=add_todo, key="add")


