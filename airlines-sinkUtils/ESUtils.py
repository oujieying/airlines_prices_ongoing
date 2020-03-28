from elasticsearch import Elasticsearch


class ESConn(object):
    def __init__(self,url,index,mapping,data,condition):
        self.url = url
        self.index = index
        self.mapping = mapping
        self.data = data
        self.searchCondition  =  condition
        self.es =Elasticsearch(self.url)
    #创建索引
    def createIndex(self):
        if(self.es.indices.exists(self.index) == False):
            result = self.es.indices.create(self.index)
            self.es.indices.analyze(self.index, body=self.mapping)
        return result
    #插入数据
    def insertData(self):
        for k, row in enumerate(self.datas):
            print("K", k, "row", row)
            self.es.index(self.index, body=row, doc_type='user', id=(k + 1))
    #查询数据
    def selectByCondition(self):
        return self.es.search(index=self.index,body=self.searchCondition)





