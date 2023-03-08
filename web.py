import streamlit as st
import functions

todos = functions.get_todos()


def add_todo():
    todo_local = st.session_state["new_todo"] + "\n"
    todos.append(todo_local)
    functions.write_todos(todos)


st.title("My To-Do App")
st.subheader("It's a minimalize To-Do application")
st.write("This app could possibly increase your productivity.")

for todo in todos:
    st.checkbox(todo)

st.text_input(label="",
              placeholder="Add new To-Do...",
              on_change=add_todo, key="new_todo")

st.session_state