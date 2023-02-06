from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models import dojo

class Ninja:
    def __init__(self, data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.age = data['age']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
    
    @classmethod
    def get_all_ninjas(cls):
        query = "SELECT * FROM ninjas;"

        results = connectToMySQL('dojos_and_ninjas_schema').query_db(query)
        
        ninjas = []

        for ninja in results:
            ninjas.append(cls(ninja))
        return ninjas
    
    @classmethod
    def save_ninja(cls, data):
        query = ''' INSERT
                    INTO ninjas (first_name, last_name, age, dojo_id)
                    VALUES (%(first_name)s, %(last_name)s, %(age)s, %(dojo_id)s);
                '''
        return connectToMySQL('dojos_and_ninjas_schema').query_db(query, data)
    
    @classmethod
    def get_ninjas_by_dojo(cls, data):
        query = ''' SELECT * FROM ninjas
                    LEFT JOIN dojos
                    ON ninjas.dojo_id = dojos.id
                    WHERE dojo_id = %(id)s;
                '''
                
        results = connectToMySQL('dojos_and_ninjas_schema').query_db(query, data)    
        return results