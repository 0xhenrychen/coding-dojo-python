from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
from flask_app.models import user

database = "ohana_rideshares"

class Ride:
    def __init__(self, data):
        self.id = data["id"]
        self.destination = data["destination"]
        self.pick_up_location = data["pick_up_location"]
        self.rideshare_date = data["rideshare_date"]
        self.details = data["details"]
        self.created_at = data["created_at"]
        self.updated_at = data["updated_at"]
        self.passenger_id = data["passenger_id"]
        self.driver_id = data["driver_id"]
        self.creator = None
        
    @classmethod
    def get_all(cls):
        query = '''
                    SELECT * FROM recipes;
                '''
        results = connectToMySQL(database).query_db(query)
        recipes = []
        for recipe in results:
            recipes.append(cls(recipe))
        return recipes
    
    @classmethod
    def save(cls, data):
        query = '''
                    INSERT INTO rides (destination, pick_up_location, rideshare_date, details, passenger_id)
                    VALUES (%(destination)s, %(pick_up_location)s, %(rideshare_date)s, %(details)s, %(user_id)s);
                '''
        connectToMySQL(database).query_db(query, data)

    # @classmethod
    # def edit(cls, data):
    #     query = ''' UPDATE recipes
    #                 SET name = %(name)s, description = %(description)s, instructions = %(instructions)s, date = %(date)s, under_30_mins = %(under_30_mins)s
    #                 WHERE ID = %(id)s;
    #             '''
    #     results = connectToMySQL(database).query_db(query, data)
    #     return results
    
    # @classmethod
    # def delete(cls, data):
    #     query = ''' DELETE FROM recipes
    #         WHERE ID = %(id)s;
    #     '''
    #     connectToMySQL(database).query_db(query, data)
        
    # @classmethod
    # def get_recipe_by_id(cls, data):
    #     query = ''' SELECT * FROM recipes
    #                 WHERE ID = %(id)s;
    #             '''
    #     results = connectToMySQL(database).query_db(query, data)
    #     return results[0]
    
    @classmethod
    def connect_passengers_to_rides_join(cls):
        query = '''
                    SELECT * FROM rides
                    JOIN users ON users.id = rides.passenger_id
                '''
        results = connectToMySQL(database).query_db(query)
        return results
    
    # @classmethod
    # def connect_user_to_recipe_join(cls, data):
    #     query = '''
    #                 SELECT * FROM users
    #                 JOIN recipes ON users.id = recipes.users_id
    #                 WHERE recipes.id = %(id)s;
    #             '''
    #     results = connectToMySQL(database).query_db(query, data)
    #     return results[0]
    
    # @classmethod
    # def get_all_recipes_by_user_join(cls, data):
    #     query = '''
    #                 SELECT * FROM recipes
    #                 JOIN users ON users.id = recipes.users_id
    #                 WHERE recipes.users_id = %(id)s;
    #             '''
    #     results = connectToMySQL(database).query_db(query, data)
    #     output = []
    #     for row in results:
    #         this_recipe = cls(row)
            
    #         user_data = {
    #             "id": row["users.id"],
    #             "first_name": row["first_name"],
    #             "last_name": row["last_name"],
    #             "email": row["email"],
    #             "created_at": row["users.created_at"],
    #             "updated_at": row["users.updated_at"]
    #         }
            
    #         this_recipe.creator = user.User(user_data)
    #         output.append(this_recipe)
    #     return output
    
    # Validate create recipe form.
    @staticmethod
    def validate_create_ride_form(ride):
        is_valid = True
        
        if len(ride["destination"]) < 1:
            flash("Destination field can't be empty.", "ride")
            is_valid = False
        elif len(ride["destination"]) < 3:
            flash("Destination field must be at least 3 characters.", "ride")
            is_valid = False
            
        if len(ride["pick_up_location"]) < 1:
            flash("Pick-up location field can't be empty.", "ride")
            is_valid = False
        elif len(ride["pick_up_location"]) < 3:
            flash("Pick-up location field must be at least 3 characters.", "ride")
            is_valid = False
            
        if len(ride["rideshare_date"]) < 1:
            flash("Rideshare date field can't be empty.", "ride")
            is_valid = False
            
        if len(ride["details"]) < 1:
            flash("Details field can't be empty.", "ride")
            is_valid = False
        elif len(ride["details"]) < 10:
            flash("Details field must be at least 10 characters.", "ride")
            is_valid = False
        return is_valid