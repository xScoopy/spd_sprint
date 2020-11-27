from flask import Flask, render_template
app = Flask(__name__)


@app.route('/')
def home():
    """defining homepage route"""
    return render_template('home.html')

@app.route('/my_profile')
def profile():
    """defining profile page route"""
    return render_template('my_profile.html')

if __name__ == '__main__':
    app.run()