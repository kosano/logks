
class OutPutEng(object):

    def __init__(self, *args, **kwargs) -> None:
        self.batch_cnt = int(kwargs.get('batch_cnt', '100'))
        self.datas = list()
    
    def add(self, data):
        if len(self.datas) < self.batch_cnt:
            self.datas.append(data)
        else:
            self.write(data)
    
    def write(self, data):
        pass
    
    
class ClickhouseEng(OutPutEng):
    def __init__(self, *args, **kwargs):
        super(ClickhouseEng, self).__init__(*args, **kwargs)
        self.host = kwargs.get('host')
        self.port = kwargs.get('port')
        self.database = kwargs.get('database')
        self.user = kwargs.get('user')
        self.password = kwargs.get('password')
        self.db = self._connect()
        
    def _connect(self):
        pass
    
    def write(self, data):
        pass
        
    
    

class ElasticsearchEng(OutPutEng):
    def __init__(self, *args, **kwargs):
        super(ElasticsearchEng, self).__init__(*args, **kwargs)
        self.host = kwargs.get('host')
        self.port = kwargs.get('port')
        self.index = kwargs.get('database')
        self.user = kwargs.get('user')
        self.password = kwargs.get('password')
        
    
    def write(self, data):
        pass
        

    
class ABC(object):
    def __init__(self):
        self.datas = list()
        
    def write(self, data):
        self.datas.append(data)
        print(self.datas)
        
    
    
if __name__ == '__main__':
    abc = ABC()
    abc.write("a")
    abc.write("b")
    abc.write("c")
        