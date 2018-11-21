from Veiculo import Veiculo
from ConsultarVeiculos import mostrarConsulta
from AdicionarVeiculos import mostrarAdicionarVeiculos
from ReservarVeiculos import mostrarReserva
from ExcluirVeiculos import mostrarExcluir
from LiberarVeiculos import mostrarLiberar
from atualizarCodigoVeiculos import atualizarCodigoVeiculos
from AvancarDataAtual import avancaUmDia
import datetime
from time import sleep
import os


class MenuPrincipal:
    def __init__(self, listVeiculos, dataAtual = datetime.datetime.now()):
        self.listVeiculos = listVeiculos
        self.dataAtual = dataAtual

    def mostrarMenu(self, opcao = 0):
        os.system("cls")# Limpa a tela do terminal.
        dia = self.dataAtual.day     
        mes = self.dataAtual.month
        ano = self.dataAtual.year
        self.dataAtual = datetime.datetime(ano,mes,dia)
        nCadastros = 0
        nAlugados = 0
        nAtrasados = 0
        if self.listVeiculos != [] and self.listVeiculos != None:
            nCadastros = len(self.listVeiculos)
            nAlugados = self.verificaLocacao()
            nAtrasados = self.verificaAtraso()
        print("+++++++++++++++++++++++++++++++++++++++++++")
        print("+                 DATA ATUAL              +")
        print("+                  " + self.dataAtual.strftime("%d/%m/%y") + "               +")
        print("+-----------------------------------------+")
        print("|  Quantidade de veículos cadastrados: " + str(nCadastros) + "  |")
        print("|    Quantidade de veículos alugados: " + str(nAlugados) +     "   |")
        print("|         Quantidade de atrasos: " + str(nAtrasados) + "        |")
        print("+-----------------------------------------+")
        print("|            +++++ MENU +++++             |")
        print("|  [1]      Consultar veículos.           |")
        print("|  [2]      Adicionar veículos.           |")
        print("|  [3]   Alugar/Reservar veículos.        |")
        print("|  [4]  Devolver/Liberar veículos.        |")
        print("|  [5]       Excluir veículos.            |")
        print("|  [6]      Avançar data atual.           |")
        print("|  [7]            Sair.                   |")
        print("+-----------------------------------------+\n")

        if opcao == 0:
                opcao = int(input("Escolha uma das opções acima (ex: 1):\n->"))

          
        if opcao == 1: #Consultar.
            self.listVeiculos = atualizarCodigoVeiculos(self.listVeiculos)
            mostrarConsulta(self.listVeiculos, self.dataAtual)

        elif opcao == 2: #Adicionar.
            self.listVeiculos = mostrarAdicionarVeiculos(self.listVeiculos, self.dataAtual)
            self.listVeiculos = atualizarCodigoVeiculos(self.listVeiculos)
            menuPrincipal = MenuPrincipal(self.listVeiculos, self.dataAtual)
            menuPrincipal.mostrarMenu()
                 
        elif opcao == 3: #Alugar/Reservar.
            self.listVeiculos = mostrarReserva(self.listVeiculos, self.dataAtual)
            menuPrincipal = MenuPrincipal(self.listVeiculos, self.dataAtual)
            menuPrincipal.mostrarMenu()

        elif opcao == 4: #Devolver/Liberar.
            self.listVeiculos = mostrarLiberar(self.listVeiculos,self.dataAtual)
            menuPrincipal = MenuPrincipal(self.listVeiculos, self.dataAtual)
            menuPrincipal.mostrarMenu()

        elif opcao == 5: #Excluir.
            self.listVeiculos = mostrarExcluir(self.listVeiculos)
            self.listVeiculos = atualizarCodigoVeiculos(self.listVeiculos)
            menuPrincipal = MenuPrincipal(self.listVeiculos, self.dataAtual)
            menuPrincipal.mostrarMenu()

        elif opcao == 6: #Avançar dataAtual.
            self.dataAtual = avancaUmDia(self.dataAtual)
            menuPrincipal = MenuPrincipal(self.listVeiculos, self.dataAtual)
            menuPrincipal.mostrarMenu()

        elif opcao == 7: #Sair.
            confirmacao = str(input("Você realmente gostaria de sair ? (s/n)\n"))
            confirmacao = confirmacao.lower()

            if confirmacao == 's':
                confirmacao = True

            else:
                confirmacao = False

            if(confirmacao):
                SystemExit()   
            else:
                menuPrincipal = MenuPrincipal(self.listVeiculos, self.dataAtual)
                menuPrincipal.mostrarMenu()
        else:            
            opcao = int(input("Opção incorrreta, selecione uma das opções acima (ex: 1):\n"))
            menuPrincipal = MenuPrincipal(self.listVeiculos, self.dataAtual)
            menuPrincipal.mostrarMenu(opcao)


    def verificaLocacao(self):
        locados = 0
        for veiculo in self.listVeiculos:
            status = veiculo.getStatus()
            if status == "Alugado":
                locados = locados + 1
        return locados

    def verificaAtraso(self):
        atrasados = 0        
        for veiculo in self.listVeiculos:
            status = veiculo.getStatus()
            if status == "Alugado":
                dataFinal = veiculo.getDataLocacao() + datetime.timedelta(veiculo.getDiasLocacao())
                
                if dataFinal < self.dataAtual:
                    atrasados = atrasados + 1
            else: continue
        return atrasados
            
