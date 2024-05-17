class Animal:
    def emitir_som(self):
        return'Qualquer som'

class Cachorro(Animal):
    def emitir_som(self):
        return 'Auauauauauau'
    
cachorro = Cachorro()
print(cachorro.emitir_som())

class Gato(Animal):
    def emitir_som(self):
        return 'miaumiau'
