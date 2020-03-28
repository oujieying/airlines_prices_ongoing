from MysqlUtils import DBConn
import json
from Teacher import  TeacherInfo
import uuid
class DealWithData(object):
    def resolveJson(self,path):
        data = json.load(open(path,'rb'))
        print(data)
    def parseTeacherJson(self,path):
        file = open(path, 'r', encoding='utf-8')
        teachers = []
        for line in file.readlines():
            # print("line",line)
            strline = line[0:len(line)-2]
            teacherinfo = json.loads(line[0:len(line)-2])
            newTeacher=TeacherInfo()
            newTeacher.__dict__=teacherinfo
            teachers.append(newTeacher)
        print(len(teachers))
        return teachers
    def insert2Mysql(self,path):
        teachers = self.parseTeacherJson(path)
        query = 'insert into teachers_for_test(name, title, info) values(%s, %s, %s)'
        conn  = DBConn("localhost","root","root","airlines","")
        print("dbname",conn.dbName,"user",conn.userName,"passwd",conn.passWd,"ip",conn.ipAddress)
        db = conn.getConn()
        for el in teachers:
            values = (el.name, el.title,el.info)
            print("values: ",values)
            db.cursor().execute(query,values)
            db.commit()
        db.close()
    def parsejson(self):
        data1 = {
            'name': 'jack',
            'age': 20,
            'like': ('sing', 'dance', 'swim'),
            'score': {'chinese': 80, 'math': 60, 'english': 99}
        }
        # data2 = json.dumps(data1);
        # data3 = json.loads(data2);
        json.dump(data1, open('jack.json', "w"));
        data3 = json.load(open('jack.json'));
        print(data3);

if __name__ == '__main__':
    data = DealWithData()
    # data.parsejson()
    # data.resolveJson("D:\\soft\\airlines_prices_ongoing\\ITcast\itcast_pipeline.json")
    # data.parseTeacherJson("D:\\soft\\airlines_prices_ongoing\\ITcast\itcast_pipeline.json")
    print(uuid.uuid4())
    # '16fd2706-8baf-433b-82eb-8c7fada847da'
    data.insert2Mysql("D:\\soft\\airlines_prices_ongoing\\ITcast\itcast_pipeline.json")