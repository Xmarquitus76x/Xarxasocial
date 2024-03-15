import datetime
import xarxaSocial
import Hashtag
from datetime import date
class Post(object):
    def __init__(self, contingut):
        self.contingut=contingut
        self.id=0
        self.hashtags = [] 
        now = date.today()
        self.__date=datetime.datetime.now().strftime('%H:%M:%S')

    def getid(self):
        return self.id

    def setid(self, iNou=1):
        self.id+=iNou

    def getC(self):
        return self.contingut

    def __eq__(self, other):
        return self.contingut==other.contingut
        
    def registra_usuari(self,nick):
        self.nick = nick
        
    def registra_hashtag(self,id):
        self.hashtag = id

    def afegeix_hashtag(self,id):
        for I in self.hashtags:
            if I==id:
                print('Ja existeix aquest Hashtag')
            else:
                self.hashtags.append(Hashtag(id))

    def __str__(self):
        hasht=" ".join(hashtag for hashtag in self.hashtags)
        return f"Post id: {self.id}, info: {self.contingut} Date: {self.__date}\n Nick user: {self.nick} Available hashtags: {hasht} "
    
    
i=Post("hola")
i.afegeix_hashtag("h")
print(i)   
    
        
    
