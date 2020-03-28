from MysqlUtils import DBConn
import json
from Teacher import  TeacherInfo
import uuid
from ESUtils import ESConn
from elasticsearch import Elasticsearch
mapping = {
                    'dynamic': '',  # 自动创建索引
                    'properties': {
                            'name': {
                                'type': 'text',
                                'analyzer': 'ik_max_word',
                                'search_analyzer': 'ik_max_word'
                            },
                            'title': {
                                'type': 'string'
                            },
                            'info': {
                                'type': 'string'
                            }
                        }
                    }
class DealWithData(object):
    def resolveJson(self,path):
        data = json.load(open(path,'rb'))
        print(data)
    def parseTeacherJson(self,path):
        file = open(path, 'r', encoding='utf-8')
        teachers = []
        teachersjsonList=[]
        for line in file.readlines():
            teacherinfo = json.loads(line[0:len(line)-2])
            newTeacher=TeacherInfo()
            newTeacher.__dict__=teacherinfo
            teachersjsonList.append(teacherinfo)
            teachers.append(newTeacher)
        print(len(teachers))
        return teachers,teachersjsonList
    def parseTeacherJson(self,path):
        file = open(path, 'r', encoding='utf-8')
        teachersjsonList=[]
        for line in file.readlines():
            teacherinfo = json.loads(line[0:len(line)-2])
            teachersjsonList.append(teacherinfo)
        return teachersjsonList
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
    def insertIntoEs(self,path):
        try:
            es = ESConn("127.0.0.1",
                    "teacher_for_test",
                    mapping
                    ,
                    "",
                    Elasticsearch("127.0.0.1"))
            print("mapping:",es.mapping,"index:",es.index)
            es.createIndex()
            jsonList = self.parseTeacherJson(path)
            es.insertData(jsonList)
        except :
            print("insert data into es error!")

if __name__ == '__main__':
    data = DealWithData()
    # data.parsejson()
    # data.resolveJson("D:\\soft\\airlines_prices_ongoing\\ITcast\itcast_pipeline.json")
    # data.parseTeacherJson("D:\\soft\\airlines_prices_ongoing\\ITcast\itcast_pipeline.json")
    print(uuid.uuid4())
    # '16fd2706-8baf-433b-82eb-8c7fada847da'
    # data.insert2Mysql("D:\\soft\\airlines_prices_ongoing\\ITcast\itcast_pipeline.json")
    # res = data.insertIntoEs()
    data.insert("D:\\soft\\airlines_prices_ongoing\\ITcast\itcast_pipeline.json")
    print()