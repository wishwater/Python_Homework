from flask import Flask , render_template

app = Flask(__name__)

@app.route('/login')
def login():
    return(render_template('login.html'))

@app.route('/logout',methods = ["GET","POST"])
def logout():
    return(render_template('logout.html'))


if __name__ == "__main__":
    app.run()
