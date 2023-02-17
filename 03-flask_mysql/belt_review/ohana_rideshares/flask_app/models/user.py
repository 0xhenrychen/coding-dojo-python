from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
from flask_app.models import ride

import re
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

database = "ohana_rideshares"

class User:
    def __init__(self, data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.password = data['password']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.creator = None
    
    @classmethod
    def get_user_by_email(cls, data):
        query = ''' SELECT * FROM users
                    WHERE email = %(email)s
                '''
        results = connectToMySQL(database).query_db(query, data)
        return results[0]
    
    @classmethod
    def get_user_by_id(cls, data):
        query = ''' SELECT * FROM users
                    WHERE ID = %(user_id)s;
                '''
        results = connectToMySQL(database).query_db(query, data)
        return results[0]
    
    @classmethod
    def save(cls, data):
        query = ''' INSERT INTO users (first_name, last_name, email, password)
                    VALUES (%(first_name)s, %(last_name)s, %(email)s, %(password)s);
                '''
        results = connectToMySQL(database).query_db(query, data)
        return results
    
    # @classmethod
    # def get_passenger_by_id(cls, data):
    #     query = ''' SELECT * FROM users
    #                 JOIN rides on users.id = rides.passenger_id
    #                 WHERE passenger_id = %(passenger_id)s;
    #             '''
    #     results = connectToMySQL(database).query_db(query, data)
    #     return results[0]
    
    # @classmethod
    # def get_driver_by_id(cls, data):
    #     query = ''' SELECT * FROM users
    #                 JOIN rides on users.id = rides.driver_id
    #                 WHERE driver_id = %(user_id)s;
    #             '''
    #     results = connectToMySQL(database).query_db(query, data)
    #     return results[0]
    
    @staticmethod
    def validate_user_register_form(user):
        is_valid = True
        
        if len(user["first_name"]) < 2:
            flash("First name must be at least 2 letters.", "register")
            is_valid = False
        if len(user["last_name"]) < 2:
            flash("Last name must be at least 2 letters.", "register")
            is_valid = False
        if not EMAIL_REGEX.match(user['email']):
            flash("Please enter a valid email address.", "register")
            is_valid = False
        
        query = ''' SELECT * FROM users
                    WHERE email = %(email)s
                '''
        results = connectToMySQL(database).query_db(query, user)
        
        if results != ():
            flash("That email already exits. Please enter a new one.", "register")
            is_valid = False
        if len(user["password1"]) < 1:
            flash("Please create a password.", "register")
            is_valid = False
        if user["password1"] != user["password2"]:
            flash("Passwords are not equal to each other.", "register")
            is_valid = False
        elif len(user["password1"]) and len(user["password2"]) < 8:
            flash("Password must be at least 8 characters.", "register")
            is_valid = False
            
        # for letter in user["password1"]:
        #     if letter.isupper():
        #         password_has_uppercase = True
        #     if letter.isnumeric():
        #         password_has_number = True
        # if password_has_uppercase == False:
        #     flash("Password must contain at least 1 uppercase letter.", "register")
        #     is_valid = False
        # if password_has_number == False:
        #     flash("Password must contain at least 1 number.", "register")
        #     is_valid = False
        return is_valid
    
    @staticmethod
    def validate_user_login_form(user):
        is_valid = True
        check_if_email_exists = False

        if not EMAIL_REGEX.match(user['email']):
            flash("Please enter a valid email address.", "login")
            check_if_email_exists = True
            is_valid = False
            
        query = ''' SELECT * FROM users
                    WHERE email = %(email)s
                '''
        results_email_check = connectToMySQL(database).query_db(query, user)
        
        if results_email_check == () and check_if_email_exists == False:
            flash("That email doesn't exist. Please register for a new account.", "login")
            check_if_email_exists = True
            is_valid = False
        if len(user["password3"]) < 1:
            flash("Please enter a password.", "login")
            is_valid = False
        return is_valid