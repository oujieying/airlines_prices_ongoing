from flask import Flask
from SelectTeacher import TeacherSelect
app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World!'
@app.route('/showTearchersByName')
def showTearchersByName(name):
    return TeacherSelect.selectByName(name)


if __name__ == '__main__':
    app.run()
