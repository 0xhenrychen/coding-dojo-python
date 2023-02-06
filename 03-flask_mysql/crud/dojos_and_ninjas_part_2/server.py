from flask_app import app
from flask_app.controllers import dojos_and_ninjas_part_2

if __name__ == "__main__":
    app.run(debug=True, host='localhost', port=5004)