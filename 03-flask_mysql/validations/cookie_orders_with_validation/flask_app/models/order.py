from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
import re
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

class Order:
    def __init__(self, data):
        self.id = data['id']
        self.customer_name = data['customer_name']
        self.cookie_type = data['cookie_type']
        self.number_of_boxes = data['number_of_boxes']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        
    @classmethod
    def get_all(cls):
        query = ''' SELECT * FROM orders;
                '''
        results = connectToMySQL('cookie_orders').query_db(query)
        orders = []
        for order in results:
            orders.append(cls(order))
        return orders
    
    @classmethod
    def save(cls, data):
        query = ''' INSERT INTO orders (customer_name, cookie_type, number_of_boxes)
                    VALUES (%(customer_name)s, %(cookie_type)s, %(number_of_boxes)s);
                '''
        return connectToMySQL('cookie_orders').query_db(query, data)
    
    @classmethod
    def get_order_by_id(cls, data):
        query = ''' SELECT * FROM orders
                    WHERE ID = %(id)s
                '''
        results = connectToMySQL('cookie_orders').query_db(query, data)
        return cls(results[0])
    
    @classmethod
    def update_order(cls, data):
        query = ''' UPDATE orders
                    SET customer_name = %(customer_name)s, cookie_type = %(cookie_type)s, number_of_boxes = %(number_of_boxes)s, created_at = NOW(), updated_at = NOW()
                    WHERE ID = %(order_id)s
                '''
        results = connectToMySQL('cookie_orders').query_db(query, data)
        return results
    
    @classmethod
    def remove_order(cls, id):
        query = ''' DELETE FROM orders
                    WHERE ID = %(id)s
                '''
        results = connectToMySQL('cookie_orders').query_db(query, id)
        return results
    
    @staticmethod
    def validate_order(order):
        is_valid = True
        if len(order["customer_name"]) < 2:
            flash("Name must be at least 2 letters.")
            is_valid = False
        if len(order["cookie_type"]) < 2:
            flash("Cookie type must be at least 2 letters.")
            is_valid = False
        if len(order["number_of_boxes"]) == 0:
            order["number_of_boxes"] = 0
        if int(order["number_of_boxes"]) <= 0:
            flash("Number of boxes must be at least 1.")
            is_valid = False
        return is_valid