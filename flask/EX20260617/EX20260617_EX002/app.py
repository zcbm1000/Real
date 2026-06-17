from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    # return "This Page is Main Home"
    str = 'abcd'
    return render_template('index.html', return_data = str)

@app.route('/usres')
def users():
    user_list = ['gildong', 'chanho', 'saeri']
    return render_template('users_html', users = user_list)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
