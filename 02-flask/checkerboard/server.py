from flask import Flask, render_template
app = Flask(__name__)                     
    
@app.route('/')                           
def root():
    return render_template('index.html')

@app.route('/<int:num_rows>')
def gen_rows(num_rows):
    num_rows_half = int(num_rows/2)
    return render_template('index.html', num_rows_half=num_rows_half, num_rows=num_rows)

@app.route('/<int:num_rows>/<int:num_cols>')
def gen_rows_cols(num_rows, num_cols):
    num_rows_half = int(num_rows/2)
    num_cols_half = int(num_cols/2)
    return render_template('index.html', num_rows_half=num_rows_half, num_rows=num_rows, num_cols_half=num_cols_half, num_cols=num_cols)

@app.route('/<int:num_rows>/<int:num_cols>/<string:color_1>/<string:color_2>')
def gen_rows_cols_colors(num_rows, num_cols, color_1, color_2):
    num_rows_half = int(num_rows/2)
    num_cols_half = int(num_cols/2)
    return render_template('index.html', num_rows_half=num_rows_half, num_rows=num_rows, num_cols_half=num_cols_half, num_cols=num_cols, color_1=color_1, color_2=color_2)

if __name__=="__main__": 
    app.run(debug=True, host='localhost', port=5005)







