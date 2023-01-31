from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key = 'keep it safe, keep it safe'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/process', methods=['POST'])
def result():
    print(f'Got info for /process')
    print(request.form)
    
    session['name'] = request.form['name']
    session['dojo'] = request.form['dojo']
    session['language'] = request.form['language']
    session['program'] = request.form['program']
    session['stack'] = request.form['stack']
    session['comment'] = request.form['comment']
    
    # stacks = []
    # for userinfo in request.form:
    #     print(request.form[userinfo])
    #     if userinfo == 'stack':
    #         stacks.append(request.form[userinfo])
    # print(stacks)
    
    return redirect('/result')

@app.route('/result')
def show_user():
    print('Got info for /result')
    return render_template('result.html', entire_form = request.form, form_name = session['name'], form_dojo = session['dojo'], form_language = session['language'], form_program = session['program'], form_stack = session['stack'], form_comment = session['comment'])

if __name__ == '__main__':
    app.run(debug=True, host='localhost', port=5001)