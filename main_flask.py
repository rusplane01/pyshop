from flask import Flask 

print(__name__)

app = Flask(__name__)

@app.route('/')
def index():
    return "мой сайт"


app.run(debug=True)



# from flask import Flask 

# app = Flask(__name__)

# @app.route('/')
# def index():
#     return "Hello, world!"

@app.route('/feed/book')
def history():
    return "comics"

@app.route('/test')
def test():
    return "Test"

app.add_url_rule('/', "index", index)
# app.run(debug=True)