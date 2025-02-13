class User:

    #constructor
    def __init__(self,name,userId):
        #creates new attribute
        self.name=name
        self.userId=userId

    def change_name(self,new_name):
        self.name=new_name

