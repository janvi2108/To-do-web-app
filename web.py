import streamlit as st
import functions

todos = functions.get_todos()

def add_todos():
    todo = st.session_state["new_todo"] + "\n"
    todos.append(todo)
    functions.write_todos(todos)

st.title("My To-Do App")
st.subheader("This is my to-do app")
st.write("This app helps you increase your productivity.")

# Display existing todos with checkboxes
for index, todo in enumerate(todos):
    checkbox = st.checkbox(todo, key=todo)
    if checkbox:
        todos.pop(index)
        functions.write_todos(todos)
        break  # Exit the loop to avoid modifying list while iterating

# Input box to add new todo
st.text_input(label="", placeholder="Add new todo",
              on_change=add_todos, key="new_todo")

