from flask import Flask, request
from SelectTeacher import TeacherSelect
teacherInfo = Flask(__name__)

@teacherInfo.route('/showTearchersByNames',methods=["GET", "POST"])
def showTearchersByName():
    name = request.args["name"]
    res = TeacherSelect().selectByName(name)
    return res.__str__()
if __name__ == '__main__':
    teacherInfo.run()