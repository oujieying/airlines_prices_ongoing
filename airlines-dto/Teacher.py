class TeacherInfo(object):
    def __init__(self):
        self.name = ''
        self.title = ''
        self.info=''
    def __str__(self):
        return self.name+", "+self.title+", "+self.info