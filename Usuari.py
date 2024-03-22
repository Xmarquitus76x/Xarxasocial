"""
======
Usuari
======

La classe Usuari s'encarrega de reprensentar un element que es tracta d'un usuari qualsevol d'una xarxa social
"""





import Post
import Hashtag
class Usuari(object):
    """
    Classe que representa un usuari en una xarxa social.

    Attributes:
        nick (str): El nom de l'usuari.
        __email (str): El correu electrònic de l'usuari.
        __pwd (str): La contrasenya de l'usuari, encriptada.
        Usuariposts (list): Llista dels posts publicats per l'usuari.

    Methods:
        __init__: Inicialitza un nou objecte Usuari.
        __eq__: Compara si dos objectes Usuari són iguals.
        getN: Obté el nom de l'usuari.
        getE: Obté el correu electrònic de l'usuari.
        getP: Obté la contrasenya encriptada de l'usuari.
        setN: Estableix un nou nom per a l'usuari.
        setE: Estableix un nou correu electrònic per a l'usuari.
        setP: Estableix una nova contrasenya encriptada per a l'usuari.
        registra_post: Registra un post publicat per l'usuari.
        cesar: Encripta un missatge utilitzant el xifrat de Cèsar.
        __str__: Retorna una representació en forma de cadena de l'usuari.
    """

    def __init__(self, nick, email, password):
        """
        Inicialitza un nou objecte Usuari amb el nom, correu electrònic i contrasenya donats.

        Args:
            nick (str): El nom de l'usuari.
            email (str): El correu electrònic de l'usuari.
            password (str): La contrasenya de l'usuari.
        """
        self.nick = nick
        self.__email = email
        self.__pwd = password
        self.Usuariposts = []

    def __eq__(self, other):
        """
        Compara si dos objectes Usuari són iguals.

        Args:
            other (Usuari): L'altre objecte Usuari a comparar.

        Returns:
            bool: True si els usuaris són iguals, False altrament.
        """
        return self.nick == other.nick and self.__email == other.__email and self.__pwd == other.__pwd

    def getN(self):
        """
        Obté el nom de l'usuari.

        Returns:
            str: El nom de l'usuari.
        """
        return self.nick

    def getE(self):
        """
        Obté el correu electrònic de l'usuari.

        Returns:
            str: El correu electrònic de l'usuari.
        """
        return self.__email

    def getP(self):
        """
        Obté la contrasenya encriptada de l'usuari.

        Returns:
            str: La contrasenya encriptada de l'usuari.
        """
        return self.__pwd

    def setN(self, Nnou):
        """
        Estableix un nou nom per a l'usuari.

        Args:
            Nnou (str): El nou nom per a l'usuari.
        """
        self.nick = Nnou

    def setE(self, Enou):
        """
        Estableix un nou correu electrònic per a l'usuari.

        Args:
            Enou (str): El nou correu electrònic per a l'usuari.
        """
        self.__email = Enou

    def setP(self, Pnou):
        """
        Estableix una nova contrasenya encriptada per a l'usuari.

        Args:
            Pnou (str): La nova contrasenya encriptada per a l'usuari.
        """
        self.__pwd = Pnou

    def registra_post(self, post):
        """
        Registra un post publicat per l'usuari.

        Si el post ja existeix a la llista de posts de l'usuari, actualitza els hashtags existents.

        Args:
            post (Post): El post a registrar.
        """
        if len(self.Usuariposts) > 0:
            for contingut in self.Usuariposts:
                if contingut.getC() == post.getC():
                    for hashtag in post.hashtags:    
                        contingut.afegeix_hashtag(hashtag)
                else:
                    self.Usuariposts.append(post)
        else:
            self.Usuariposts.append(post)

    def cesar(self, misstage, shift=2):
        """
        Encripta un missatge utilitzant el xifrat de Cèsar amb un desplaçament determinat.

        Args:
            misstage (str): El missatge a encriptar.
            shift (int, optional): El desplaçament per al xifrat de Cèsar. Per defecte és 2.

        Returns:
            str: El missatge encriptat.
        """
        encriptat = ""
        for lletra in misstage:
            if lletra.isalpha():
                if lletra.islower():
                    encriptat += chr((ord(lletra) - ord('a') + shift) % 26 + ord('a'))
                else:
                    encriptat += chr((ord(lletra) - ord('A') + shift) % 26 + ord('A'))
            else:
                encriptat += lletra
        return encriptat

    def __str__(self):
        """
        Retorna una representació en forma de cadena de l'usuari.

        Returns:
            str: Una cadena que conté la informació de l'usuari.
        """
        if len(self.Usuariposts) > 0:
            return f"Usuari: {self.nick} Correu electrònic: {self.__email}, Contrasenya encriptada: {self.cesar(self.__pwd)}\nPosts publicats:"
        else:
            return f"Usuari: {self.nick} Correu electrònic: {self.__email}, Contrasenya encriptada: {self.cesar(self.__pwd)}\nPosts publicats: no disponible"
