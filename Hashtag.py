class Hashtag(object):
    def __init__(self, id):
        self.id=id

    def __eq__(self, other):
        return self.id==other.id

    def getI(self):
        return self.id
    
    def setI(self, iNou):
        self.id=iNou
    
    def __str__(self):
        return f"#{self.getI()}"


if __name__=='__main__':
    h1=Hashtag("adventure")
    h2=Hashtag("winter")
    print(h1)
    print(h1==h2)