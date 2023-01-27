from flask import Flask, render_template
app = Flask(__name__)                     
    
@app.route('/play')                           
def playground_1():
    return render_template('index.html')

@app.route('/play/<int:num_of_boxes>')                           
def playground_2(num_of_boxes):
    return render_template('index.html', num_of_boxes=num_of_boxes)

@app.route('/play/<int:num_of_boxes>/<string:color>')
def playground_3(num_of_boxes, color):
    return render_template('index.html', num_of_boxes=num_of_boxes, color=color)
    
if __name__=="__main__":
    app.run(debug=True, host='localhost', port=5055)