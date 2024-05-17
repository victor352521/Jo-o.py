class Animal():
    quantidade_patas = 4
    tem_rabo = False
    tem_pelo = True
    especie = ''
    sexo = 'macho'

class Cachorro(Animal):
    tem_rabo = True
    especie = 'Canis Lupus Familiaris'
    raca = 'Vira Lata'
    nome = 'Sérgio Perez'
    porte = 'Gigantesco'

    def latir():
        return 'AUAUAUUAUAUUAUAUUUAUAUAUAUAUU COMI SEU SAPATO'
    
    def comer():
        return 'Hummmmm chesburguer'
    
    def dormir():
        return 'ZZZZZZZZZZZZZZZZZZZZZZZ'
    

print(Cachorro.latir())
print(Cachorro.comer())
print(Cachorro.dormir())