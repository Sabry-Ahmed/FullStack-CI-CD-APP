import streamlit as st
import requests

API_URL = "http://127.0.0.1:5000/api/data"
INSERT_API_URL = "http://backend:5000/api/insert"
DELETE_API_URL = "http://backend:5000/api/delete"



def fetch_data():
    response = requests.get(API_URL)
    if response.status_code == 200:
        data = response.json()['data']
        return data
    else:
        st.error(f"Failed to fetch data. Status code: {response.status_code}")
        return []

def insert_user(name):
    payload = {'name': name}
    response = requests.post(INSERT_API_URL, json=payload)
    if response.status_code == 200:
        st.success(f"User {name} inserted successfully!")
    else:
        st.error(f"Failed to insert user. Status code: {response.status_code}")

def delete_user(name):
    payload = {'name': name}
    response = requests.post(DELETE_API_URL, json=payload)
    if response.status_code == 200:
        st.success(f"User {name} deleted successfully!")
    else:
        st.error(f"Failed to delete user. Status code: {response.status_code}")

def main():
    st.title("SIMPLE FRONT")

    data = fetch_data()

    if data:
        st.write("Data from the database:")
        st.write(data)
    else:
        st.warning("No data available.")

    # Insert user form
    st.subheader("Insert User:")
    new_name = st.text_input("Name:", key="insert_name")  # Unique key for insert_name
    if st.button("Insert"):
        insert_user(new_name)

    # Delete user form
    st.subheader("Delete User:")
    delete_name = st.text_input("Name:", key="delete_name")  # Unique key for delete_name
    if st.button("Delete"):
        delete_user(delete_name)

if __name__ == '__main__':
    main()
