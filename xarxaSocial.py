"""
===========
xarxaSocial
===========

Aquest mòdul és la representació d'una xarxa Social simple amb els seus mètodes i classes pertinents
"""




from Usuari import *
from Post import*
from Hashtag import*

class App(object):
    """
    Classe que representa una aplicació de xarxa social.

    Attributes:
        s (int): Comptador de posts.
        __usuaris (dict): Diccionari que emmagatzema els usuaris registrats.
        hashtags (dict): Diccionari que emmagatzema els hashtags disponibles.

    Methods:
        __init__: Inicialitza un nou objecte App.
        afegeix_usuari: Afegeix un nou usuari a l'aplicació.
        afegeix_hashtag: Afegeix un nou hashtag a l'aplicació.
        publicar_post: Publica un nou post d'un usuari amb un hashtag associat.
        users: Mostra tots els usuaris registrats amb els seus posts publicats.
        posts: Mostra tots els posts publicats pels usuaris.
        llistarPostsUser: Retorna una llista del contingut dels posts d'un usuari donat.
        registra_usuari: Registra un nou usuari a l'aplicació.
        registra_hashtag: Registra un nou hashtag a l'aplicació.
    """

    def __init__(self, s=0):
        """
        Inicialitza un nou objecte App amb un comptador de posts, usuaris i hashtags buits.

        Args:
            s (int, optional): Comptador de posts. Per defecte és 0.
        """
        self.s = s
        self.__usuaris = {}
        self.hashtags = {}

    def afegeix_usuari(self, nick, email, password):
        """
        Afegeix un nou usuari a l'aplicació.

        Si ja existeix un usuari amb el mateix nom, mostra un missatge d'error.

        Args:
            nick (str): El nom de l'usuari.
            email (str): El correu electrònic de l'usuari.
            password (str): La contrasenya de l'usuari.
        """
        if nick in self.__usuaris.keys():
            print('Ja existeix aquest Usuari')
        else:
            self.__usuaris[nick] = Usuari(nick, email, password)
                
    def afegeix_hashtag(self, id):
        """
        Afegeix un nou hashtag a l'aplicació.

        Args:
            id (str): L'identificador del hashtag.
        """
        if Hashtag(id) not in self.hashtags.values():
            self.hashtags[id] = Hashtag(id)

    def publicar_post(self, nick, hashtag, contingut):
        """
        Publica un nou post d'un usuari amb un hashtag associat.

        Si l'usuari no existeix, mostra un missatge d'error.

        Args:
            nick (str): El nom de l'usuari que publica el post.
            hashtag (str): El hashtag associat al post.
            contingut (str): El contingut del post.
        """
        if nick in self.__usuaris:
            post = Post(contingut)
            post.registra_usuari(nick)
            post.afegeix_hashtag(hashtag)
            self.__usuaris[nick].registra_post(post)
        else:
            print("L'usuari no existeix!")

    def users(self):
        """
        Mostra tots els usuaris registrats amb els seus posts publicats.
        """
        for nick in self.__usuaris.values():
            print(nick)
            for post in nick.Usuariposts:
                self.s += 1
                post.setid(self.s)
                print(post)
                
    def posts(self):
        """
        Mostra tots els posts publicats pels usuaris.
        """
        for nick in self.__usuaris:
            if nick in self.__usuaris:
                for post in reversed(self.__usuaris[nick].Usuariposts):
                    print(post)
            else:
                print("L'usuari no existeix!")
            
    def llistarPostsUser(self, nick):
        """
        Retorna una llista del contingut dels posts d'un usuari donat.

        Args:
            nick (str): El nom de l'usuari.

        Returns:
            list: Una llista que conté el contingut dels posts de l'usuari.
        """
        if nick in self.__usuaris.keys():
            return [post.getC() for post in self.__usuaris[nick].Usuariposts]

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
    i.posts()
    print(i.llistarPostsUser("pere"))