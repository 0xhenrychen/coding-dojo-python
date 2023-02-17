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
        self.passenger = None
        self.driver = None
    
    @classmethod
    def get_all_with_no_driver(cls):
        query = ''' SELECT * FROM rides
                    JOIN users ON users.id = rides.passenger_id
                    WHERE rides.driver_id IS NULL;
                '''
        results = connectToMySQL(database).query_db(query)
        output = []
        for row in results:
            this_ride = cls(row)
            
            user_data = {
                "id": row["users.id"],
                "first_name": row["first_name"],
                "last_name": row["last_name"],
                "email": row["email"],
                "password": row["password"],
                "created_at": row["users.created_at"],
                "updated_at": row["users.updated_at"]
            }
            user_passenger = user.User(user_data)
            this_ride.passenger = user_passenger
            output.append(this_ride)
        return output
    
    @classmethod
    def get_all_with_driver(cls):
        query = ''' SELECT * FROM rides R
                    JOIN users UP ON UP.id = R.passenger_id
                    JOIN users UD ON UD.id = R.driver_id;
            '''
        results = connectToMySQL(database).query_db(query)
        output = []
        for row in results:
            this_ride = cls(row)
            
            passenger_data = {
                "id": row["UP.id"],
                "first_name": row["first_name"],
                "last_name": row["last_name"],
                "email": row["email"],
                "password": row["password"],
                "created_at": row["UP.created_at"],
                "updated_at": row["UP.updated_at"]
            }
            
            user_passenger = user.User(passenger_data)
            this_ride.passenger = user_passenger
            
            driver_data = {
                "id": row["UD.id"],
                "first_name": row["UD.first_name"],
                "last_name": row["UD.last_name"],
                "email": row["email"],
                "password": row["password"],
                "created_at": row["UD.created_at"],
                "updated_at": row["UD.updated_at"]
            }
            
            user_driver = user.User(driver_data)
            this_ride.driver = user_driver
            
            output.append(this_ride)
        return output
    
    @classmethod
    def get_ride_and_driver_by_id(cls, data):
        query = ''' SELECT * FROM rides R
                    JOIN users UP ON UP.id = R.passenger_id
                    JOIN users UD ON UD.id = R.driver_id
                    WHERE R.id = %(ride_id)s;
                '''
        results = connectToMySQL(database).query_db(query, data)
        this_ride = cls(results[0])
        for row in results:
            passenger_data = {
                "id": row["UP.id"],
                "first_name": row["first_name"],
                "last_name": row["last_name"],
                "email": row["email"],
                "password": row["password"],
                "created_at": row["UP.created_at"],
                "updated_at": row["UP.updated_at"]
            }
            
            user_passenger = user.User(passenger_data)
            this_ride.passenger = user_passenger
            
            driver_data = {
                "id": row["UD.id"],
                "first_name": row["UD.first_name"],
                "last_name": row["UD.last_name"],
                "email": row["email"],
                "password": row["password"],
                "created_at": row["UD.created_at"],
                "updated_at": row["UD.updated_at"]
            }
            
            user_driver = user.User(driver_data)
            this_ride.driver = user_driver
            
        return this_ride
    
    @classmethod
    def save(cls, data):
        query = '''
                    INSERT INTO rides (destination, pick_up_location, rideshare_date, details, passenger_id)
                    VALUES (%(destination)s, %(pick_up_location)s, %(rideshare_date)s, %(details)s, %(user_id)s);
                '''
        connectToMySQL(database).query_db(query, data)
    
    @classmethod
    def assign_driver_to_ride(cls, data):
        query = ''' UPDATE rides
                    SET driver_id = %(driver_id)s
                    WHERE id = %(ride_id)s;
                '''
        connectToMySQL(database).query_db(query, data)
        
    @classmethod
    def remove_driver_from_ride(cls, data):
        query = ''' UPDATE rides
                    SET driver_id = %(driver_id)s
                    WHERE id = %(ride_id)s;
                '''
        connectToMySQL(database).query_db(query, data)
        
    @classmethod
    def edit(cls, data):
        query = ''' UPDATE rides
                    SET destination = %(destination)s, pick_up_location = %(pick_up_location)s, rideshare_date = %(ridesare_date)s, details = %(details)s
                    WHERE ID = %(ride_id)s;
                '''
        results = connectToMySQL(database).query_db(query, data)
        return results
        
    @classmethod
    def delete(cls, data):
        query = ''' DELETE FROM rides
            WHERE ID = %(id)s;
        '''
        connectToMySQL(database).query_db(query, data)
    
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