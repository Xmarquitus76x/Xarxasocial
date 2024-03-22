from Usuari import *
from Post import *
from Hashtag import *
from xarxaSocial import *



class Interpret:
    def __init__(self):
        self.prompt = ""
        self.dcom = {}

    def set_prompt(self, p):
        self.prompt = p

    def afegeix_ordre(self, nomc, ordre):
        if nomc in self.dcom:
            print("Ja existeix una ordre amb aquest nom.")
        else:
            self.dcom[nomc] = ordre
        return self.dcom
    
    def run(self):
        while True:
            entrada = input(self.prompt + " ")
            paraules = entrada.split()
            #ordre = paraules[0]
            if entrada != "surt":
                for element in paraules:
                    self.dcom[element]= paraules[1:]
                #if ordre in self.dcom:
                #   funcio = self.dcom[ordre]
                #   funcio(paraules[1:])
                print(self.dcom)
            elif entrada == "\n" or entrada == "\t":
                print("Ordre desconeguda.")
            else:
                break
if __name__=="__main__":
    def c1(l): print ("executo l’ordre 1: {0}".format(self.dcom[0]))
    def c2(l): print ("executo l’ordre 2: {0}".format(self.dcom[0]))
    i = Interpret()
    i.set_prompt("∗∗")
    i.afegeix_ordre("llista", c1)
    i.afegeix_ordre("bloqueja", c2)
    i.run()
    
