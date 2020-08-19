import eel
from ler_excel import Read_excel

@eel.expose
def emitir(file):
    print(file)

    
    #gerar = Read_excel(file)
    #gerar.read_dcomp()

eel.init('web')
eel.start('index.html', size=(700, 600), port=0)
