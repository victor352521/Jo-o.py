class Celular():
    bateria = 'infinita'
    tela = '4x3'
    tem_camera = True
    tem_botao = True
    tem_antena = True
    cor = 'Cinza'
    modelo = 'Tijolao'

    def Ligacao():
        print('ligando...')

    def Mensagem():
        print('Enviando mensagem...')

    def Bateria():
        print('Infinita')

    def jogo_Cobrinha():
        print('Jogo bom demaize :)')


print(Celular.bateria)
print(Celular.jogo_Cobrinha())