from openpyxl import load_workbook
from dcomp import AcessarPerdcom
from selenium import webdriver
import time as time
from tkinter import messagebox

class Read_excel(AcessarPerdcom):


    def __init__(self, arquivo):
        self.arquivo = load_workbook(arquivo)
        self.apelido =''
        self.PATH = "C:\Program Files (x86)\chromedriver.exe"
        self.driver = webdriver.Chrome(self.PATH)

        self.acessar = AcessarPerdcom(self.driver)


    def read_dcomp(self):

        self.acessar.Login()
        cont = 1

        sheet = self.arquivo['Preechimento PER DCOMP WEB']


        for celula in sheet["C"]:

            print(celula.value)
            if celula.value == "" or celula.value == None:
                break
            cont = cont +1

            if cont >= 6:
                #TELA INCICIAL DO PER/DCOMP WEB
                cnpjPerfil = celula.offset(0,-1).value
                tipo =  celula.value
                retif =  celula.offset(0,1).value
                numRetif = celula.offset(0,2).value
                tipoCredito = celula.offset(0,3).value
                self.apelido = celula.offset(0,4).value
                qualificacao = celula.offset(0,5).value
                detalhamento = celula.offset(0,6).value
                dcompAnterior = celula.offset(0,7).value

                #ETAPA 1
                detentor = celula.offset(0,8).value
                cnpjDetentor = celula.offset(0,9).value
                dataEventoEspecial = celula.offset(0,10).value
                tipoEventoEspecial = celula.offset(0,11).value
                percentualCredito = celula.offset(0,12).value
                anoCompetencia = celula.offset(0,13).value
                mesCompetencia = celula.offset(0,14).value
                recolhimentoCei = celula.offset(0,15).value
                matriculaCei = celula.offset(0,16).value

                #ESTAPA 2
                valorCreditoInicial = self.ajustar_valor(celula.offset(0,17).value)
                selicAcumulada = self.ajustar_valor(celula.offset(0,18).value)
                creditoAtualizado = celula.offset(0,19).value

                #ETAPA 3
                cpf = celula.offset(0,20).value
                crc = celula.offset(0,21).value
                telefone = celula.offset(0,22).value
                email = celula.offset(0,23).value
                ufCrc = celula.offset(0,24).value

                try:
                    if cnpjPerfil != None:
                        self.acessar.alterar_perfil(cnpjPerfil)
                except:
                    messagebox.showinfo(title=None, message="Erro ao alterar o perfil")

                    #self.root.destroy()

                if cont == 6:
                    self.acessar.novo_perdcomp()
                time.sleep(1)

                if detalhamento == 'O crédito já foi detalhado em PER/DCOMP anterior':
                    self.acessar.credAnterior(tipoCredito,qualificacao,self.apelido,detalhamento,dcompAnterior,
                                                valorCreditoInicial,selicAcumulada)
                else:
                    try:
                        self.acessar.preencher_perdcomp(tipo, retif, numRetif, tipoCredito, self.apelido, qualificacao,
                                                detalhamento, dcompAnterior)
                    except:
                        self.acessar.preencher_perdcomp(tipo, retif, numRetif, tipoCredito, self.apelido, qualificacao,
                                                detalhamento, dcompAnterior)
                    #messagebox.showinfo(title="ERRO", message="Erro ao preecher DCCOMP: " + self.apelido)
                    #self.root.destroy()

                    time.sleep(1)

                    self.acessar.credits_identify(detentor, cnpjDetentor,dataEventoEspecial, tipoEventoEspecial,
                                                percentualCredito,anoCompetencia, mesCompetencia,
                                                recolhimentoCei, matriculaCei)

                    #EMITIR AS GUIAS DE GPS
                    self.acessar.click_gps()
                    self.read_gps()
                    
                    time.sleep(3)

                    #DEMONSTRATIVO DO CRÉDITO
                    try:
                        time.sleep(1)
                        self.acessar.demonstrativo_credito(valorCreditoInicial, selicAcumulada)
                    except:
                        time.sleep(1)
                        self.acessar.demonstrativo_credito(valorCreditoInicial, selicAcumulada)
                        #messagebox.showinfo(title="ERRO", message="Erro ao preecher o crédito DCCOMP: " + self.apelido)    

                #DEMONSTRATIVO DO DÉBITO
                #self.read_debit()
                self.acessar.new_dcomp()


    def ajustar_valor(self, valor):

        valor_ajustado = ""
        try:
          valor = round(float(valor),2)
        except:
            pass

        valor = str(valor)
        if valor != "None":

            if valor[-2:][:1] == ".":
                valor_ajustado = valor.replace(".", "") + "0"
            elif valor[-3:][:1] == ".":
                valor_ajustado = valor.replace(".", "")
            else:
                valor_ajustado = valor.replace(".", "") + "00"

        return valor_ajustado

    def read_gps(self):
        linha = 0
        sheet_gps = self.arquivo['GPS']



        for line in sheet_gps['A']:
            linha = linha + 1

            if linha >2 :
                codGps = str(line.offset(0,1).value)
                valorInss = self.ajustar_valor(str(line.offset(0,2).value))
                valorOutrasEntidades = self.ajustar_valor(str(line.offset(0,3).value))
                valorMultaJuros = self.ajustar_valor(str(line.offset(0,4).value))
                dataArrecadacao = str(line.offset(0,5).value)
                valorTotal = self.ajustar_valor(str(line.offset(0,6).value))

                if line.value == self.apelido:

                    self.acessar.gps_details(codGps, valorInss, valorOutrasEntidades, valorMultaJuros, dataArrecadacao,
                                     valorTotal)

    def read_debit(self):
        linha = 0
        sheet_gps = self.arquivo['Etapa 2']

        for line in sheet_gps['A']:
            linha = linha + 1

            if linha > 3:
                tipo_debito= str(line.offset(0, 1).value)
                categoria = self.ajustar_valor(str(line.offset(0, 2).value))
                mes = self.ajustar_valor(str(line.offset(0, 3).value))
                ano = self.ajustar_valor(str(line.offset(0, 4).value))
                dataVencimento = str(line.offset(0, 5).value)
                codigoReceita = self.ajustar_valor(str(line.offset(0, 6).value))
                codigoReceita = self.ajustar_valor(str(line.offset(0, 6).value))

                if line.value == self.apelido:
                    self.acessar.debito_apurado(tipo_debito, categoria, mes, ano)


if __name__ == "__main__":
    #PATH = "C:\Program Files (x86)\chromedriver.exe"
    #driver = webdriver.Chrome(PATH, options=options)

    #difal = AcessarSite(driver)

    # emissor = Ler_excel("C:\\Users\\Nicolas\\PycharmProjects\\darj\\Memória de Cálculo DIFAL - 03.2020.xlsx")
    # emissor.read_difal()

    emitir = Read_excel("C:\\Users\\Nicolas\\PycharmProjects\\dcom_web\\PerDcompWeb.xlsx")
    emitir.read_dcomp()