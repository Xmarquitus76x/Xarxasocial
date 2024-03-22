"""
=======
Hashtag
=======

La classe Hashtag representa un element en format hashtag propi d'una xarxa social
"""

class Hashtag(object):
    """
    Classe que representa un hashtag en una xarxa social.

    Attributes:
        id (str): Identificador del hashtag.

    Methods:
        __init__: Inicialitza un nou objecte Hashtag.
        __eq__: Compara si dos objectes Hashtag són iguals.
        getI: Obté l'identificador del hashtag.
        setI: Estableix un nou identificador per al hashtag.
        __str__: Retorna una representació en forma de cadena del hashtag.
    """

    def __init__(self, id):
        """
        Inicialitza un nou objecte Hashtag amb l'identificador donat.

        Args:
            id (str): Identificador del hashtag.
        """
        self.id = id

    def __eq__(self, other):
        """
        Compara si dos objectes Hashtag són iguals.

        Args:
            other (Hashtag): L'altre objecte Hashtag a comparar.

        Returns:
            bool: True si els hashtags són iguals, False altrament.
        """
        return self.id == other.id

    def getI(self):
        """
        Obté l'identificador del hashtag.

        Returns:
            str: L'identificador del hashtag.
        """
        return self.id
    
    def setI(self, iNou):
        """
        Estableix un nou identificador per al hashtag.

        Args:
            iNou (str): El nou identificador per al hashtag.
        """
        self.id = iNou
    
    def __str__(self):
        """
        Retorna una representació en forma de cadena del hashtag.

        Returns:
            str: Una cadena que conté la representació del hashtag.
        """
        return f"#{self.getI()}"
