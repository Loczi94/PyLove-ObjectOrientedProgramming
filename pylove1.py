# encoding: utf-8
import json
import math

class Czlowiek:
    def __init__(self,imie,wzrost,waga):
        self.imie = imie
        self.wzrost = wzrost
        self.waga = waga
        self.bmi = round(self.waga/(self.wzrost**2),2)

    def speak(self):
        print("Mówię prawdę.")

    def count_bmi(self):
        if(self.wzrost>10): #jeśli wzrost jest podany w centymetrach
            self.wzrost=self.wzrost/100
        self.bmi = round(self.waga/(self.wzrost**2),2)
        return self.bmi

    def diff_to_norm(self):
        bmi_niedowaga = 18.5
        bmi_nadwaga = 25.0
        waga_min = bmi_niedowaga * (self.wzrost**2)
        waga_max = bmi_nadwaga * (self.wzrost**2)
        if (self.waga<waga_min):
            self.diff = waga_min - self.waga
            #print("Do normy brakuje "+str(self.diff)+" kg.")
        elif (self.waga>waga_max):
            self.diff = self.waga - waga_max
            #print("Norma przekroczona o "+str(self.diff)+" kg.")
        else:
            self.diff = 0
            #print("Waga w normie.")
        return self.diff

    def save_data(self):
        with open('{}.json'.format(self.imie), 'w') as outfile:
            json.dump({
                'imie': self.imie,
                'waga': self.waga,
                'wzrost': self.wzrost
            },outfile)

    def to_burn(self):
        waga_max = 25.0 * (self.wzrost ** 2)
        if (self.waga>waga_max):
            self.diff = round(self.waga - waga_max,2)
            kcal = self.diff * 6000
            run = math.ceil(kcal / 500)
            bike = math.ceil(kcal / 600)
            hobby = math.ceil(kcal / 250)
            chess = math.ceil(kcal / 150)
            print('Aby schudnąć '+str(self.diff)+' kg powinieneś:\nbiegać przez '+str(run)+' h\nlub\njezdzic na rowerze przez '+str(bike)+' h\nlub\nuprawiać hobby przez '+str(hobby)+' h\nlub\ngrać w szachy przez '+str(chess)+' h.')
        else:
            print('Nie musisz schudnąć ;)')

    def to_eat(self):
        waga_min = 18.5 * (self.wzrost ** 2)
        if self.waga<waga_min:
            self.diff = round(waga_min - self.waga,2)
            kcal = self.diff * 6000
            chocolate = math.ceil(kcal / 4500)
            potatoes = math.ceil(kcal / 800)
            print('Aby przytyć '+str(self.diff)+' kg powinieneś zjeść '+str(chocolate)+' kg czekolady lub '+str(potatoes)+' kg ziemniaków.')
        else:
            print("Nie musisz przytyć ;)")

    def what_to_do(self):
        if self.count_bmi()<18.5:
            print('Powinieneś przytyć '+str(self.diff_to_norm())+' kg.')
        elif self.count_bmi()>25.0:
            print('Powinieneś schudnąć ' + str(self.diff_to_norm()) + ' kg.')
        else:
            print("Twoja waga jest w normie.")

class Polityk(Czlowiek):
    bribe=False
    def speak(self):
        if self.bribe:
            super().speak()
        else:
            print("Kłamię, bo mogę.")

    def recive_bribe(self):
        self.bribe=True


if __name__ == '__main__':
    polityk = Polityk("Roman",1.9,100)
    dziewczyna = Czlowiek("Paulina",1.66,44)
    dziewczyna.what_to_do()