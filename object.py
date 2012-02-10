# -*- coding: utf-8 -*-

class Object():  
    def __init__(self,id):

        self.data = {'id':id,
                     'name':'ooo Иван Петрович Сидоров',
                     "contacts":{
                         "Age":29,
                         "E-Mail":"ivan@sidorov.ru",
                         "Twitter":"@sidorov",
                         "Cell Phone":"+7-916-555-55-55",
                         "Work Phone":"+7-495-555-55-55",
                         "Home Phone":"+7-496-555-55-55",
                     },
                     "rels":{
                         "Жена":{
                             "id":2,
                             "name":"Мария Сергеевна Сидорова"
                         },
                         "Сын":{
                             "id":3,
                             "name":"Андрей Иванович Сидоров"
                         },

                     }}
        # print ("fname=%s" % self.data['fname']);                     
    
    def get(self,k):
        return self.data[k]

    def getall(self):
        return self.data
