from MysqlUtils import DBConn
class TeacherSelect(object):
    def __init__(self):
        pass
        # self.conn = DBConn("127.0.0.1","root","root","teachers_for_test","")
    def selectByName(self,name):
        db = DBConn("127.0.0.1", "root", "root", "airlines", "")

        sql  = "select id,name,title,info from teachers_for_test where name = %s limit 1"
        values = (name)
        print("sql:",sql)
        return db.searchByCondition(sql,values)
