from flask import Flask, request


app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World!'


@app.route("/info", methods=["GET", "POST"])
def student_info():
    stu_id = int(request.args["id"])
    return f"Hello Old boy {stu_id}"

if __name__ == '__main__':
    app.run()
