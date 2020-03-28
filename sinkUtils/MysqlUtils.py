import pymysql

#数据库连接信息工具类
class DBConn(object):
    def __init__(self,ipAddress,userName,passWd,db,sql):
        self.ipAddress=ipAddress
        self.userName = userName
        self.passWd = passWd
        self.dbName = db
        self.sql = sql
    #获取数据库连接
    def getConn(self):
        return pymysql.connect(self.ipAddress,self.dbName,self.passWd,self.dbName)
    #查询
    def searchByCondition(self):
        #获取连接
        connection = self.getConn()
        #获取游标
        cursor = connection.cursor()
        cursor.execute(query=self.sql)
        result = cursor.fetchall()
        connection.close()
        return result
    def insert(self):
        connect = self.getConn()
        try:
            connect.cursor().execute(query=self.sql)
            connect.commit()
        except:
            connect.rollback()
        connect.close()







