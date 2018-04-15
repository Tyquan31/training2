from flask import Flask

# // init app
app = Flask(__name__)

# // routes
@app.route("/")
def hello():
    return "Hello World"

# // run app
if __name__ == '__main__':
    app.run(debug=True)