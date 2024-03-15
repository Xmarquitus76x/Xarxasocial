class Usuari(object):
    def __init__(self, nick, email, password):
        self.nick=nick
        self.__email=email
        self.__pwd=password
        self.Usuariposts=[]


        

    def __eq__(self, other):
        return self.nick==other.nick and self.__email==other.__email and self.__pwd==other.__pwd

    def getN(self):
        return self.nick
    def getE(self):
        return self.__email
    def getP(self):
        return self.__pwd

    def setN(self, Nnou):
        self.nick=Nnou
    def setE(self, Enou):
        self.__email=Enou
    def setP(self, Pnou):
        self.__pwd=Pnou

    def registra_post(self, post):
        if post not in self.Usuariposts:
            self.Usuariposts.append(post)
        



    def cesar(self, misstage, shift=2):
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
        if len(self.Usuariposts)>0:
            return f"Usuari: {self.nick} Mail: {self.__email}, Encripted Password: {self.cesar(self.__pwd)}\nPublished posts:"
        else:
            return f"Usuari: {self.nick} Mail: {self.__email}, Encripted Password: {self.cesar(self.__pwd)}\nPublished posts: not available"

if __name__=='__main__':
    p1=Usuari("john24","john24@gmail.com","abracadabra")
    p2=Usuari("johh24","john244@gmail.com","patadecabra")
    print(p1)
    print(p2)
    p3=Usuari("john24","john2444@gmail.com","supercalifra")
    print(p3.nick)
    print(p1==p3)



        
