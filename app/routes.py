from app import app
from flask import jsonify

@app.route('/')
@app.route('/index')
def index():
    # return "Hello, World!"
    return jsonify({"message": "Hello World!"})


# if __name__ == '__main__':
#   app.run()