import csv



class ColadaDeAcero:
    """
    Clase que genera ColadasDeAcero con sus composición química
    en valores porcentuales (%).
    """

    # Acá se define la composición objetivo. 

    composicion_objetivo = {'carbono': 0.65, 'silicio': 0.29, 'manganeso': 0.8, 'cromo': 0.43
        }
    

    def __init__(
        self,
        carbono,
        silicio,
        manganeso,
        fosforo,
        azufre,
        cromo,
        molibdeno,
        niquel,
        niobio,
        cobre,
        titanio,
        aluminio,
        vanadio,
        masa_total,
    ):
        self.carbono = carbono
        self.silicio = silicio
        self.manganeso = manganeso
        self.fosforo = fosforo
        self.azufre = azufre 
        self.cromo = cromo 
        self.molibdeno  = molibdeno
        self.niobio = niobio
        self.niquel = niquel
        self.cobre = cobre 
        self.titanio = titanio 
        self.aluminio = aluminio 
        self.vanadio = vanadio  
        self.masa_total = masa_total #en kg


        

    def __str__(self):
        """
        Devuelve la representación de la ColadaDeAcero como cadena
        de tetxo.
        """
        return f"Colada de {self.masa_total} kg de acero de composición: C: {self.carbono:.4f}%, Si: {self.silicio:.4f}%, Mn: {self.manganeso:.4f}%, Cr: {self.cromo:.4f}%"

    def agregar_adicion(self, adicion, masa):

        self.carbono = (self.carbono * self.masa_total + adicion.carbono * masa) / (self.masa_total + masa)        
        self.silicio = (self.silicio * self.masa_total + adicion.silicio * masa) / (self.masa_total + masa)
        self.manganeso = (self.manganeso * self.masa_total + adicion.manganeso * masa) / (self.masa_total +  masa)
        self.azufre = (self.azufre * self.masa_total + adicion.azufre * masa) / (self.masa_total + masa)
        self.fosforo = (self.fosforo * self.masa_total + adicion.fosforo * masa) / (self.masa_total + masa)
        self.aluminio = (self.aluminio * self.masa_total + adicion.aluminio * masa) / (self.masa_total + masa)
        self.molibdeno = (self.molibdeno * self.masa_total + adicion.molibdeno * masa) / (self.masa_total + masa)
        self.cromo = (self.cromo * self.masa_total + adicion.cromo * masa) / (self.masa_total + masa)

    def get(self, elemento):
        return self.__getattribute__(elemento)
        



cuchara = ColadaDeAcero(
    0.76424,
    0.06267,
    0.46864,
    0.01872,
    0.00799,
    0.11846,
    0.02023,
    0.087,
    0.00988,
    0.05545,
    0.00654,
    0.0099,
    0.0066,
    88000
)

class Adicion:

    def __init__(self, carbono, silicio, manganeso, azufre, fosforo, hierro, aluminio, molibdeno, cromo, masa):
        self.carbono = carbono
        self.silicio = silicio
        self.manganeso = manganeso        
        self.azufre = azufre
        self.fosforo = fosforo
        self.hieroo = hierro
        self.aluminio = aluminio
        self.molibdeno = molibdeno
        self.cromo = cromo
        self.masa = masa # en kg
    
    def get(self, elemento):
        return self.__getattribute__(elemento)

       
FeMn_bajo_C = Adicion(0.85,
0.5,
81.5,
0.1,
0.25,
0,
0,
0,
0,
1
)



print(FeMn_bajo_C.fosforo)

silico_cromo = Adicion(1.82,
25.33,
0,
0.015,
0.014,
0,
0,
0,
38.23,
1,
)


print(f"Carbono pre adición: {cuchara.carbono}")
print(f"Manganeso pre adición: {cuchara.manganeso}")
print(f"Silicio pre adición: {cuchara.silicio}")

# cuchara.agregar_adicion(silico_cromo, 2000)

print(f"Carbono pos adición: {cuchara.carbono}")
print(f"Manganeso pos adición: {cuchara.manganeso}")
print(f"Silicio pos adición: {cuchara.silicio}")

def calcular_masa_de_adicion(cuchara, adicion, elemento):

    delta_porcentaje_objetivo = cuchara.composicion_objetivo[elemento] - cuchara.get(elemento)
    masa_adicion = 100 * delta_porcentaje_objetivo * cuchara.masa_total / (adicion.get(elemento) * 95)

    return masa_adicion

masa_adicion = calcular_masa_de_adicion(cuchara, silico_cromo, 'cromo')     

print(f"Masa de adicón: {masa_adicion}")


def calcular_masa_de_adicion_corregida(cuchara, adicion, elemento):
    delta_porcentaje_objetivo = cuchara.composicion_objetivo[elemento] - cuchara.get(elemento)
    masa_corregida = 100 * delta_porcentaje_objetivo * cuchara.masa_total / (
        adicion.get(elemento) * 95 * (1 - delta_porcentaje_objetivo/adicion.get(elemento))
    )
    
    return masa_corregida

masa_compensada = calcular_masa_de_adicion_corregida(cuchara, silico_cromo, 'cromo')
print(f"Masa compensada: {masa_compensada:.2f} kg")

cuchara.agregar_adicion(silico_cromo, masa_adicion)

# print(f"Delta con masa compensada: {cuchara.cromo - cuchara.composicion_objetivo['cromo']}")

print(f"Delta con masa adicion:  {cuchara.cromo - cuchara.composicion_objetivo['cromo']}")



