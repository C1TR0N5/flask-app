from flask import Flask, request, jsonify, redirect, render_template_string
app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        # Check if username begins with a capital letter
        if username[0].isupper():
            # Check if the password contains at least one letter and one digit
            if any(c.isalpha() for c in password) and any(c.isdigit() for c in password):
                return redirect('/login_success')

    return render_template_string('''
        <html>
        <head><title>Login</title></head>
        <body>
            <h1>Login</h1>
            <form method="POST" action="/">
                <label for="username">Username:</label>
                <input type="text" id="username" name="username" required><br><br>
                <label for="password">Password:</label>
                <input type="password" id="password" name="password" required><br><br>
                <input type="submit" value="Login">
            </form>
        </body>
        </html>
    ''')

@app.route('/login_success')
def login_success():
    return 'Login Successful'

if __name__ == '__main__':
    app.run(host="0.0.0.0", debug=True, port=8081)
