import streamlit as st
import functions

# Load todos from file
todos = functions.get_todos()

# Function to handle adding todos
def add_todo():
    new_todo = st.session_state["new_todo_input"]
    if new_todo.strip():
        todos.append(new_todo + "\n")
        functions.write_todos(todos)

# App title and description
st.title("My To-Do App")
st.subheader("Stay organized and productive!")
st.write("Add, check off, and manage your to-do tasks below.")

# Display todos with checkboxes
for index, todo in enumerate(todos):
    checkbox = st.checkbox(todo, key=f"todo_{index}")
    if checkbox:
        todos.pop(index)
        functions.write_todos(todos)
        st.experimental_rerun()  # Refresh the page to reflect changes

# Input to add new todo
st.text_input(label="Add a new to-do", 
              placeholder="Enter your task here...",
              on_change=add_todo,
              key="new_todo_input")
