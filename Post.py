"""
====
Post
====

La classe Post s'encarrega de reprensentar un element que es tracta d'un post d'una xarxa social
"""


from datetime import date
import datetime
import xarxaSocial
import Hashtag



class Post(object):
    """
    Classe que representa un post en una xarxa social.

    Attributes:
        contingut (str): El contingut del post.
        id (int): Identificador del post.
        hashtags (list): Llista de hashtags associats al post.
        __date (str): Data i hora en què es va crear el post (format HH:MM:SS).
        nick (str): Nom d'usuari associat al post.

    Methods:
        __init__: Inicialitza un nou objecte Post.
        getid: Obté l'identificador del post.
        setid: Estableix un identificador nou pel post.
        getC: Obté el contingut del post.
        __eq__: Compara si dos objectes Post són iguals pel contingut.
        registra_usuari: Registra el nom d'usuari associat al post.
        registra_hashtag: Registra un hashtag associat al post.
        afegeix_hashtag: Afegeix un hashtag nou al post.
        __str__: Retorna una representació en forma de cadena del post.
    """

    def __init__(self, contingut):
        """
        Inicialitza un nou objecte Post amb el contingut donat.

        Args:
            contingut (str): El contingut del post.
        """
        self.contingut = contingut
        self.id = 0
        self.hashtags = []
        now = date.today()
        self.__date = datetime.datetime.now().strftime('%H:%M:%S')

    def getid(self):
        """
        Obté l'identificador del post.

        Returns:
            int: L'identificador del post.
        """
        return self.id

    def setid(self, iNou=1):
        """
        Estableix un identificador nou pel post.

        Args:
            iNou (int, optional): El valor a afegir a l'identificador actual. Per defecte és 1.
        """
        self.id += iNou

    def getC(self):
        """
        Obté el contingut del post.

        Returns:
            str: El contingut del post.
        """
        return self.contingut

    def __eq__(self, other):
        """
        Compara si dos objectes Post són iguals pel contingut.

        Args:
            other (Post): L'altre objecte Post a comparar.

        Returns:
            bool: True si els continguts són iguals, False altrament.
        """
        return self.contingut == other.contingut
        
    def registra_usuari(self, nick):
        """
        Registra el nom d'usuari associat al post.

        Args:
            nick (str): El nom d'usuari a registrar.
        """
        self.nick = nick

    def registra_hashtag(self, id):
        """
        Registra un hashtag associat al post.

        Args:
            id (str): L'identificador de l'hashtag a registrar.
        """
        self.hashtag = id

    def afegeix_hashtag(self, id):
        """
        Afegeix un hashtag nou al post.

        Si l'hashtag ja existeix a la llista de hashtags, no es fa res.

        Args:
            id (str): L'identificador de l'hashtag a afegir.
        """
        if id not in self.hashtags:
            self.hashtags.append(id)

    def __str__(self):
        """
        Retorna una representació en forma de cadena del post.

        Returns:
            str: Una cadena que conté la informació del post.
        """
        return f"Post id: {self.id}, info: {self.contingut} Date: {self.__date}\nNick: {self.nick} Available hashtags: #{' #'.join(hashtag for hashtag in self.hashtags)}\n"