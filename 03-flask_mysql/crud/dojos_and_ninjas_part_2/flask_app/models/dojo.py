from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models import ninja

class Dojo:
    def __init__(self, data):
        self.id = data['id']
        self.name = data['name']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        
        self.ninjas = []

    @classmethod
    def get_all_dojos(cls):
        query = "SELECT * FROM dojos;"

        results = connectToMySQL('dojos_and_ninjas_part_2_schema').query_db(query)
        
        dojos = []

        for dojo in results:
            dojos.append(cls(dojo))
        return dojos
    
    @classmethod
    def save_dojo(cls, data):
        query = ''' INSERT
                    INTO dojos (name)
                    VALUES (%(name)s);
                '''
        return connectToMySQL('dojos_and_ninjas_part_2_schema').query_db(query, data)
    
    # !!! Currently not able to get dojo by a particular ninja.
    @classmethod
    def get_dojo_by_ninja(cls, data):
        print("ID is: ", data)
        query = ''' SELECT * FROM dojos
                    LEFT JOIN ninjas
                    ON ninjas.dojo_id = dojos.id
                    WHERE ninjas.id = %(id)s;
                '''
        results = connectToMySQL('dojos_and_ninjas_part_2_schema').query_db(query, data)
        return cls(results[0])