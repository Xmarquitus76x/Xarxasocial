from Usuari import *
from Post import*
from Hashtag import*

class App(object):
    def __init__(self, s=0):
        self.s=s
        self.__usuaris={}
        self.hashtags={}

    def afegeix_usuari(self, nick, email, password):
        if nick in self.__usuaris.keys():
            print('Ja existeix aquest Usuari')
        else:
            self.__usuaris[nick]= Usuari(nick, email, password)
                
    def afegeix_hashtag(self,id):
        for I in self.hashtags.keys():
            if I==id:
                print('Ja existeix aquest Hashtag')
            else:
                self.hashtags[id]= Hashtag(id)
    
    def publicar_post(self, nick, hashtag, contingut):
        if nick in self.__usuaris:
            post=Post(contingut)
            post.registra_usuari(nick)
            post.registra_hashtag(hashtag)
            self.__usuaris[nick].registra_post(post)


        else:
            print("L'usuari no existeix!")

    def users(self):
        for nick in self.__usuaris.values():
            print(nick)
            for post in nick.Usuariposts:
                self.s+=1
                post.setid(self.s)
                print(post)
                print(post.hashtag)

    def posts(self):
        
        for nick in self.__usuaris:
            if nick in self.__usuaris:
                for post in reversed(self.__usuaris[nick].Usuariposts):
                    print(post)
            else:
                print("L'usuari no existeix!")
            
            
    def llistarPostsUser(self,nick):
        if nick in self.__usuaris.keys():
            return [post.getC() for post in self.__usuaris[nick].posts]


 
                
        
if __name__=="__main__":
    i=App()
    i.afegeix_usuari("pere","pere@gmail.com","gilisticoexpia")
    i.afegeix_hashtag("adventure")
    i.publicar_post("pere","adventure","into the wild")
    i.afegeix_usuari("maria","maria@gmail.com","gilisticoexpia")
    i.afegeix_hashtag("winter")
    i.afegeix_hashtag("blue")
    i.publicar_post("pere","winter","into the wild")
    i.publicar_post("pere","winter","into the wild")
    i.publicar_post("pere","february","fall again, fall better")
    i.users()
    #i.posts()
    #print(i.llistarPostsUser("pere"))
    

    #Resultats d’execuci´o
    #Usuari: pere Email: pere@gmail.com Encripted password: gilisticoexpia
   # Published posts:
    #Post id: 1 info: into the wild Date: Tue Feb 6 15:53:45 2018
    #Nick user: pere Available hashtags: #adventure #winter
    #Post id: 2 info: fall again, fall better Date: Tue Feb 6 15:53:45 2018
    #Nick user: pere Available hashtags: #february
    #Usuari: maria Email: maria@gmail.com Encripted password: gilisticoexpia
    #Published posts: not available
    #Post id: 2 info: fall again, fall better Date: Tue Feb 6 15:53:45 2018
    #Nick user: pere Available hashtags: #february
    #Post id: 1 info: into the wild Date: Tue Feb 6 15:53:45 2018
    #Nick user: pere Available hashtags: #adventure #winter
   # [’into the wild’, ’fall again, fall better’]3