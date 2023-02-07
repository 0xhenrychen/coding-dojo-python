# import the function that will return an instance of a connection
from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
import re
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

# model the class after the user table from our database
class User:
    def __init__(self , data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        
    # class method to get all users from the database
    @classmethod
    def get_all(cls):
        query = "SELECT * FROM users;"
        results = connectToMySQL('users_schema').query_db(query)
        users = []
        for user in results:
            users.append( cls(user) )
        return users
    
    # class method to save our user to the database
    @classmethod
    def save(cls, data):
        query = ''' INSERT
                    INTO users ( first_name , last_name , email , created_at, updated_at )
                    VALUES ( %(first_name)s , %(last_name)s , %(email)s , NOW() , NOW() );'''
        return connectToMySQL('users_schema').query_db(query, data)
    
    # class method to delete our user from the database
    @classmethod
    def delete(cls, data):
        query = ''' DELETE FROM users
                    WHERE ID = %(id)s'''
        return connectToMySQL('users_schema').query_db(query, data)
    
    # class method to select our user from the database
    @classmethod
    def get_by_id(cls, data):
        query = ''' SELECT * FROM users
                    WHERE ID = %(id)s'''
        results = connectToMySQL('users_schema').query_db(query, data)
        return cls(results[0])
    
    # class method to update our user to the database
    @classmethod
    def edit(cls, data):
        query = ''' UPDATE users
                    SET first_name = %(first_name)s, last_name = %(last_name)s, email = %(email)s, created_at = NOW(), updated_at = NOW()
                    WHERE ID = %(id)s'''
        return connectToMySQL('users_schema').query_db(query, data)
    
    @staticmethod
    def validate_user(user):
        is_valid = True
        if len(user['first_name']) == 0:
            flash("Please enter a first name.")
            is_valid = False
        if len(user['last_name']) == 0:
            flash("Please enter a last name.")
            is_valid = False
        # if len(user['email']) == 0:
        #     flash("Please enter an email address.")
        #     is_valid = False
        if not EMAIL_REGEX.match(user['email']):
            flash("Please enter a valid email address.")
            is_valid = False
            
        query = '''SELECT * FROM users
                    WHERE email = %(email)s'''
        
        results = connectToMySQL('users_schema').query_db(query, user)
        # print(">>>query results[0] is:",results)
        
        if results != ():
            flash("That email address already exits. Please enter a new one.")
            is_valid = False
        return is_valid