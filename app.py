from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def register_form():
    return render_template('register.html')

@app.route('/register', methods=['POST'])
def register():
    name = request.form['name']
    email = request.form['email']
    with open('registrations.txt', 'a') as f:
        f.write(f'{name}, {email}\n')
    return render_template('success.html', name=name)

if __name__ == '__main__':
    app.run(debug=True)
