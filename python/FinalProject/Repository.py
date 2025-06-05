import os
from Files import *
class Repository:
    def __init__(self,path):
        self.path = os.path.join(path,".wit")
    def init(self):
        create_wit(self.path[:len(self.path)-5])
    def add(self,file1):
        if os.path.exists(os.path.join(self.path,"allFiles",file1)):
            add(self.path,file1)
        else:
            raise Exception("there isn't such a file")
    def commit(self,message):
        commit(self.path,message)
    def log(self):
        path_version = os.path.join(self.path, "versions")
        li = os.listdir(path_version)
        for i in range(len(li)):
            f = open(os.path.join(path_version,li[i],"info.txt"),'r')
            print(f.read())
            f.close()

    def status(self):
        if len(os.listdir(os.path.join(self.path,"add"))) > 0:
            print("there are uncommitted changes")
        else:
            print("there aren't any uncommitted changes")
    def checkout(self,commit_id):
        return_to_commit(self.path,os.path.join(self.path,"versions",commit_id))


