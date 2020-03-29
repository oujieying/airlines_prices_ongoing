from flask import Flask, request
from SelectTeacher import TeacherSelect
teacherInfoController = Flask(__name__)

@teacherInfoController.route('/showTearchersByNames',methods=["GET", "POST"])
def showTearchersByName():
    name = request.args["name"]
    res = TeacherSelect().selectByName(name)
    return res.__str__()
if __name__ == '__main__':
    teacherInfoController.run()