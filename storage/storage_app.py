from flask import Flask
import storage


app = Flask(__name__)

@app.route('/')
def hello():
    return {"hello": "world"}


@app.route('/getcases/<int:size>')
def eval(size):
    cases = storage.get_cases(size)
    return {'cases': cases}



if __name__ == '__main__':
    app.run(port=5000)


