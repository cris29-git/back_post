from flask import Flask, request, render_template
import MySQLdb
import pymysql

app = Flask(__name__)

@app.route('/index.html', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        # Get the username and password sent in the form
        user_id = request.form['user']
        password = request.form['password']

        # Function to validate the user in the database
        def validate_user(user):
            # Connection to the database
            conn = MySQLdb.connect(r'C:\Users\Usuario\Desktop\back_post\Facturacionybonificacion.db')
            cursor = conn.cursor()

            # Query to find the user in the database
            cursor.execute("SELECT role FROM users WHERE username=?", (user,))
            result = cursor.fetchone()

            # Close the connection to the database
            conn.close()

            if result is not None:
                return result[0]  # Return the role of the user if it is found in the database
            else:
                return None  # Return None if the user does not exist

        # Function to validate the password in the database
        def validate_password(user, password):
            # Connection to the database
            conn = MySQLdb.connect(r'C:\Users\Usuario\Desktop\back_post\Facturacionybonificacion.db')
            cursor = conn.cursor()

            # Query to find the password in the database
            cursor.execute("SELECT role FROM users WHERE username=? AND password=?", (user, password))
            result = cursor.fetchone()

            # Close the connection to the database
            conn.close()

            if result is not None:
                return result[0]  # Return the role of the user if the password matches
            else:
                return None  # Return None if the password does not match

        # Validate username and password in the database
        user_role = validate_user(user_id)
        role_password = validate_password(user_id, password)

        # Check the assigned role
        if user_id == "ID_user" and password == "ID_password":
            if user_role == "Administrator":
                # Code for handling administrator role
                return "Administrator role"
            elif user_role == "Supervisor":
                # Code for handling supervisor role
                return "Supervisor role"
            elif user_role == "Coordinator":
                # Code for handling coordinator role
                return "Coordinator role"
            elif user_role == "Operator":
                # Code for handling operator role
                return "Operator role"
            else:
                return "Unassigned role for user " + user_id
        else:
            return "Invalid username or password."

    return render_template('index.html')

if __name__ == "__main__":
    app.run()
