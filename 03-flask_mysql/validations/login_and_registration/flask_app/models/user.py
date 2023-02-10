from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
import re
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

my_database = "users"

class User:
    def __init__(self, data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.password1 = data['password1']
        self.password2 = data['password2']
        self.password3 = data['password3']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        
    @classmethod
    def save_user(cls, data):
        query = ''' INSERT INTO users (first_name, last_name, email, password)
                    VALUES (%(first_name)s, %(last_name)s, %(email)s, %(password1)s);
                '''
        return connectToMySQL(my_database).query_db(query, data)
    
    @classmethod
    def get_user_by_email(cls, data):
        query = ''' SELECT * FROM users
                    WHERE email = %(email)s
                '''
        results = connectToMySQL(my_database).query_db(query, data)
        return results[0]
    
    # @classmethod
    # def get_all(cls):
    #     query = ''' SELECT * FROM orders;
    #             '''
    #     results = connectToMySQL('cookie_orders').query_db(query)
    #     orders = []
    #     for order in results:
    #         orders.append(cls(order))
    #     return orders
    
    # @classmethod
    # def update_order(cls, data):
    #     query = ''' UPDATE orders
    #                 SET customer_name = %(customer_name)s, cookie_type = %(cookie_type)s, number_of_boxes = %(number_of_boxes)s, created_at = NOW(), updated_at = NOW()
    #                 WHERE ID = %(order_id)s
    #             '''
    #     results = connectToMySQL('cookie_orders').query_db(query, data)
    #     return results
    
    # @classmethod
    # def remove_order(cls, id):
    #     query = ''' DELETE FROM orders
    #                 WHERE ID = %(id)s
    #             '''
    #     results = connectToMySQL('cookie_orders').query_db(query, id)
    #     return results
    
    @staticmethod
    def validate_user_register(user):
        is_valid = True
        password_has_uppercase = False
        password_has_number = False
        
        if len(user["first_name"]) < 2:
            flash("First name must be at least 2 letters.", "register")
            is_valid = False
        if len(user["last_name"]) < 2:
            flash("Last name must be at least 2 letters.", "register")
            is_valid = False
        if len(user["password1"]) and len(user["password2"]) < 8:
            flash("Password must be at least 8 characters.", "register")
            is_valid = False
            
        for letter in user["password1"]:
            if letter.isupper():
                password_has_uppercase = True
            if letter.isnumeric():
                password_has_number = True
        if password_has_uppercase == False:
            flash("Password must contain at least 1 uppercase letter.", "register")
            is_valid = False
        if password_has_number == False:
            flash("Password must contain at least 1 number.", "register")
            is_valid = False
        if user["password1"] != user["password2"]:
            flash("Passwords are not equal to each other.", "register")
            is_valid = False
        if not EMAIL_REGEX.match(user['email']):
            flash("Please enter a valid email address.", "register")
            is_valid = False
        
        query = ''' SELECT * FROM users
                    WHERE email = %(email)s
                '''
        results = connectToMySQL(my_database).query_db(query, user)
        
        if results != ():
            flash("That email already exits. Please enter a new one.", "register")
            is_valid = False
        return is_valid
    
    @staticmethod
    def validate_user_login(user):
        is_valid = True
        check_password_twice = False
        check_if_email_exists = False

        if not EMAIL_REGEX.match(user['email']):
            flash("Please enter a valid email address.", "login")
            is_valid = False
        
        query = ''' SELECT * FROM users
                    WHERE email = %(email)s
                '''
        results_email_check = connectToMySQL(my_database).query_db(query, user)
        
        if results_email_check == ():
            flash("That email doesn't exist. Please register for a new account.", "login")
            check_if_email_exists = True
            is_valid = False
            
        if len(user["password3"]) < 1 and check_if_email_exists == False:
            flash("Please enter a password.", "login")
            check_password_twice = True
            is_valid = False

        query = ''' SELECT * FROM users
                    WHERE password = %(password3)s AND email = %(email)s;
                '''
        results_password_check = connectToMySQL(my_database).query_db(query, user)
        
        if results_password_check == () and check_password_twice == False and check_if_email_exists == False:
            flash("Password is incorrect. Please try again.", "login")
            is_valid = False
        return is_valid