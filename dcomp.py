from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time as time


class AcessarPerdcom():
    def __init__(self, browser):
        self.browser = browser

    def Login(self):
        self.browser.get('https://cav.receita.fazenda.gov.br/autenticacao/login')
        time.sleep(1)
        self.browser.find_element_by_xpath("//img[@alt='Acesso Gov BR']").click()
        time.sleep(2)
        self.browser.find_element_by_link_text("Certificado digital").click()

        #self.browser.find_element_by_id("caixa1-login-certificado").click()
        self.browser.maximize_window()
   
    def find_tag(self, tag):
        return self.browser.find_elements_by_tag_name(tag)

    def alterar_perfil(self, cnpj):
        time.sleep(1)
        self.browser.find_element_by_xpath("//a[@id='btnPerfil']/span").click()
        time.sleep(1)
        self.browser.find_element_by_id("txtNIPapel2").send_keys(cnpj)
        time.sleep(1)
        self.browser.find_element_by_xpath("(//input[@value='Alterar'])[2]").click()
        #self.browser.find_element_by_xpath("//div[6]/div/a/span").click()

    def new_dcomp(self):
        try:
            self.browser.find_element(By.CLASS_NAME("icon-NovoDocumento")).click()
        except:
            try:
                self.browser.find_element_by_xpath("//div[@id='sidebar-wrapper']/ul/li[2]/a/div/div/i").click()
                self.browser.find_element_by_xpath(
                    "//div[@id='page-content-wrapper']/perdcomp-template-documento/div/perdcomp-identificacao-documento/form/div/div[2]/div/div/label/span/i").click()

            except:
                print("erro")


    def novo_perdcomp(self):

        time.sleep(4)
        
        element = self.find_tag("a")
        for tag in element:
            if tag.text == "Restituição e Compensação":
                tag.click()
                break
        time.sleep(5)
        self.browser.get("https://cav.receita.fazenda.gov.br/ecac/Aplicacao.aspx?id=10006&origem=menu")
        time.sleep(1)
        try:
            self.browser.find_element_by_xpath("//div[@id='sidebar-wrapper']/ul/li[2]/a/div/div/i").click()
            self.browser.find_element_by_xpath("//div[@id='sidebar-wrapper']/ul/li[2]/a/div/div[2]").click()
            self.browser.find_element_by_xpath(
                "//div[@id='page-content-wrapper']/perdcomp-template-documento/div/perdcomp-identificacao-documento/form/div/div[2]/div/div/label/span").click()

        except:

            self.browser.get("https://www3.cav.receita.fazenda.gov.br/perdcomp-web/#/documento/identificacao-novo")
            time.sleep(1)


    def preencher_perdcomp(self, tipo, retif, numRetif, tipoCredito, apelido, qualificacao, detalhamento, dcompAnterior):
        time.sleep(3)
        element = self.find_tag("span")
        for tag in element:
            print(tag.text)
            if tag.text.strip(" ") == "Declaração de Compensação":  #tipo
                tag.click()
                break
        time.sleep(2)
        self.browser.find_element_by_xpath(
            "//div[@id='page-content-wrapper']/perdcomp-template-documento/div/perdcomp-identificacao-documento/form/div[2]/div/div/div/div/div[2]/div/label/div").click()
        self.browser.find_element_by_id("tipoCredito").click()

        if retif == "Sim":
            print(numRetif)
        self.browser.find_element_by_id("tipoCredito").click()

        time.sleep(1)
        self.browser.find_element_by_id("tipoCredito").send_keys(tipoCredito)
        self.browser.find_element_by_id("qualificacaoContribuinte").click()
        #time.sleep(2)
        self.browser.find_element_by_id("qualificacaoContribuinte").send_keys(qualificacao)
        self.browser.find_element_by_id("apelidoDocumento").click()
        self.browser.find_element_by_id("apelidoDocumento").clear()
        self.browser.find_element_by_id("apelidoDocumento").send_keys(apelido)
        self.browser.find_element_by_id("tipoIdentificacaoCredito").click()
        #time.sleep(2)
        self.browser.find_element_by_id("tipoIdentificacaoCredito").send_keys(detalhamento)

        self.browser.find_element_by_xpath("//html").click()
        #time.sleep(1)
        self.browser.find_element_by_name("btnProsseguir").click()
        time.sleep(1)
        self.browser.find_element_by_xpath(
            "//div[@id='page-content-wrapper']/perdcomp-template-documento/div/perdcomp-identificacao-documento/form/div[2]/perdcomp-modal/div/div/div/div[2]/div/div/label/div").click()
        time.sleep(1)
        self.browser.find_element_by_id("botaoOkTermoAceito").click()


    def credAnterior(self, tipoCredito, qualificacao, apelido, detalhamento, dcompAnterior, credito_inicial, selic):
       
        time.sleep(2)
        element = self.find_tag("span")
        for tag in element:
            print(tag.text)
            if tag.text.strip(" ") == "Declaração de Compensação":  #tipo
                tag.click()
                break
        time.sleep(2)
        self.browser.find_element_by_xpath(
            "//div[@id='page-content-wrapper']/perdcomp-template-documento/div/perdcomp-identificacao-documento/form/div[2]/div/div/div/div/div[2]/div/label/div").click()

        time.sleep(1)
        self.browser.find_element_by_id("tipoCredito").send_keys(tipoCredito)
        self.browser.find_element_by_id("qualificacaoContribuinte").click()
        #time.sleep(2)
        self.browser.find_element_by_id("qualificacaoContribuinte").send_keys(qualificacao)
        self.browser.find_element_by_id("apelidoDocumento").click()
        self.browser.find_element_by_id("apelidoDocumento").clear()
        self.browser.find_element_by_id("apelidoDocumento").send_keys(apelido)
        self.browser.find_element_by_id("tipoIdentificacaoCredito").click()
        #time.sleep(2)
        self.browser.find_element_by_id("tipoIdentificacaoCredito").send_keys(detalhamento)
        self.browser.find_element_by_xpath("//html").click()
        time.sleep(2)
        self.browser.find_element_by_xpath("(//input[@type='text'])[2]").click()
        #self.browser.find_element_by_xpath("(//input[@type='text'])[2]").clear()
        self.browser.find_element_by_xpath("(//input[@type='text'])[2]").send_keys(dcompAnterior)
        time.sleep(1)

        self.browser.find_element_by_xpath("//html").click()
        #time.sleep(1)
        self.browser.find_element_by_name("btnProsseguir").click()
        time.sleep(1)
        self.browser.find_element_by_xpath(
            "//div[@id='page-content-wrapper']/perdcomp-template-documento/div/perdcomp-identificacao-documento/form/div[2]/perdcomp-modal/div/div/div/div[2]/div/div/label/div").click()
        time.sleep(1)
        self.browser.find_element_by_id("botaoOkTermoAceito").click()

        try:
            self.browser.find_element_by_link_text(u"Demonstrativo do Crédito").click()
        except:
            time.sleep(2)
            self.browser.find_element_by_name("btnProsseguir").click()
            #time.sleep(2)
            #self.browser.find_element_by_name("btnProsseguir").click()


        self.browser.find_element_by_id("creditoOriginalDataEntrega").click()
        self.browser.find_element_by_id("creditoOriginalDataEntrega").clear()
        self.browser.find_element_by_id("creditoOriginalDataEntrega").send_keys(credito_inicial)
        self.browser.find_element_by_id("selicAcumulada").clear()
        self.browser.find_element_by_id("selicAcumulada").send_keys(selic)
        self.browser.find_element_by_name("btnSalvar").click()
        time.sleep(1)
        self.browser.find_element_by_name("btnProsseguir").click()
        time.sleep(2)

    def credits_identify(self,detentor, cnpjDetentor,dataEventoEspecial, tipoEventoEspecial, percentualCredito,
                         anoCompetencia, mesCompetencia, recolhimentoCei, matriculaCei):


        time.sleep(1)
        element = WebDriverWait(self.browser, 10).until(
            EC.presence_of_element_located((By.ID, "detentor"))
        )
        element.send_keys(detentor)

        if detentor == "Crédito apurado por empresa sucedida":
            #colocar o codigo para os dados do detentor aqui
            cnpjDetentor
            dataEventoEspecial
            tipoEventoEspecial
            percentualCredito
            recolhimentoCei
            matriculaCei

        try:
            element = WebDriverWait(self.browser, 10).until(
                EC.presence_of_element_located((By.ID, "ordemCnpjDetentorCredito"))
            )
            self.browser.find_element_by_id("ordemCnpjDetentorCredito").click()
            self.browser.find_element_by_id("ordemCnpjDetentorCredito").clear()
            #print(cnpjDetentor[8:])
            element.send_keys(cnpjDetentor[8:])
        except:
            print('erro a informar o cnpj')

        self.browser.find_element_by_id("anoCompetencia").click()
        self.browser.find_element_by_id("anoCompetencia").send_keys(anoCompetencia)
        self.browser.find_element_by_id("mesCompetencia").click()
        self.browser.find_element_by_id("mesCompetencia").send_keys(mesCompetencia)
        self.browser.find_element_by_id("mesCompetencia").click()
        self.browser.find_element_by_xpath(
            "//div[@id='page-content-wrapper']/perdcomp-template-documento/div/perdcomp-informar-credito/perdcomp-tabs/perdcomp-tab/div/perdcomp-cpim-identificar-credito/div/div/div/div/div/div[3]/div[3]/div/div/label/div").click()

    def click_gps(self):

        self.browser.find_element_by_link_text("Detalhamento GPS").click()
        # self.browser.find_element_by_xpath("//div[@id='page-content-wrapper']/perdcomp-template-documento/div/perdcomp-informar-credito/perdcomp-tabs/perdcomp-tab[2]/div/perdcomp-gps/perdcomp-informar-gps/div/div").click()


    def gps_details(self, codGps, valorInss, valorOutrasEntidades, valorMultaJuros, dataArrecadacao, valorTotal):

       
        element = WebDriverWait(self.browser, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, "btnGPSGfip")))


        element.click()
        time.sleep(2)
        self.browser.find_element_by_id("codigoPagamento").click()
        self.browser.find_element_by_id("codigoPagamento").send_keys(codGps)
        self.browser.find_element_by_id("valorINSS").send_keys(valorInss)
        self.browser.find_element_by_id("valorOutrasEntidades").clear()
        self.browser.find_element_by_id("valorOutrasEntidades").send_keys(valorOutrasEntidades)
        self.browser.find_element_by_id("valorATMJurosMulta").clear()
        self.browser.find_element_by_id("valorATMJurosMulta").send_keys(valorMultaJuros)
        self.browser.find_element_by_xpath("//input[@id='dataArrecadacao']").clear()
        self.browser.find_element_by_xpath("//input[@id='dataArrecadacao']").send_keys(dataArrecadacao)
        self.browser.find_element_by_name("btnSalvar").click()

        time.sleep(2)
        self.browser.find_element_by_name("btnSalvar").click()
        time.sleep(1)


    def demonstrativo_credito(self, credito_inicial, selic):
        try:
            self.browser.find_element_by_link_text(u"Demonstrativo do Crédito").click()
        except:
            time.sleep(2)
            self.browser.find_element_by_name("btnProsseguir").click()
            time.sleep(2)
            self.browser.find_element_by_name("btnProsseguir").click()


        self.browser.find_element_by_id("valorOriginalCreditoInicial").click()
        self.browser.find_element_by_id("valorOriginalCreditoInicial").clear()
        self.browser.find_element_by_id("valorOriginalCreditoInicial").send_keys(credito_inicial)
        #self.browser.find_element_by_id("selicAcumulada").clear()
       # self.browser.find_element_by_id("selicAcumulada").send_keys(selic)
        self.browser.find_element_by_name("btnSalvar").click()
        time.sleep(1)
        self.browser.find_element_by_name("btnProsseguir").click()
        time.sleep(2)


    def debito_apurado(self,tipo_debito, categoria, mes, ano):

        element = WebDriverWait(self.browser, 10).until(
            EC.presence_of_element_located((By.NAME, "btnCarregarDctf")))

        element.click()

        self.browser.find_element_by_id("tipoDebito").click()
        self.browser.find_element_by_id("tipoDebito").send_keys(tipo_debito)
        self.browser.find_element_by_id("tipoDebito").click()
        self.browser.find_element_by_id("categoria").click()
        self.browser.find_element_by_id("categoria").send_keys(categoria)
        self.browser.find_element_by_id("anoPeriodoApuracao").click()
        self.browser.find_element_by_id("anoPeriodoApuracao").send_keys(ano)

        self.browser.find_element_by_id("mesPeriodoApuracao").click()
        self.browser.find_element_by_id("mesPeriodoApuracao").send_keys(mes)
        self.browser.find_element_by_id("mesPeriodoApuracao").click()
        self.browser.find_element_by_name("btnPesquisar").click()


    def close_alert_and_get_its_text(self):
        try:
            alert = self.browser.switch_to_alert()
            alert_text = alert.text
            if self.accept_next_alert:
                alert.accept()
            else:
                alert.dismiss()
            return alert_text
        finally:
            self.accept_next_alert = True

if __name__ == '__main__':
    
    options = webdriver.ChromeOptions()
    options.add_experimental_option('prefs', {
    #"download.default_directory": "C:\\Users\\Nicolas\\Downloads", #Change default directory for downloads
    "download.prompt_for_download": False, #To auto download the file
    "download.directory_upgrade": True,
    "plugins.always_open_pdf_externally": True #It will not show PDF directly in chrome
    })


    PATH = "C:\Program Files (x86)\chromedriver.exe"
    driver = webdriver.Chrome(PATH,options=options)

    Acessar = AcessarPerdcom(driver)
    Acessar.Login()
    Acessar.novo_perdcomp()
    Acessar.preencher_perdcomp()
    Acessar.credits_identify()
