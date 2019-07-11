from flask import Flask

# This is the first command that happens when we run this file
if __name__ == "__main__":
    app = Flask(__name__)
    app.run(debug=True)
    


@app.route('/')
def hello():
    return "Hello World!"


