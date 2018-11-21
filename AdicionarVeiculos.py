from Veiculo import Veiculo
import datetime
import os


    
def mostrarAdicionarVeiculos(listVeiculos = [], dataAtual = datetime.datetime.now()):
    os.system("cls")
    dia = dataAtual.day        
    mes = dataAtual.month
    ano = dataAtual.year
    dataAtual = datetime.datetime(ano,mes,dia) #Zera horas,minutos,segundos
    strDataAtual = dataAtual.strftime("%d/%m/%y")
    print("+++++++++++++++++++++++++++++++++++++++++++")
    print("+                 DATA ATUAL              +")
    print("+                  " + strDataAtual + "               +")
    print("+-----------------------------------------+")

    print("+          ADICIONAR NOVO VEÍCULO         +")
    veiculo = Veiculo()
    veiculo.setMarca(input("\nQual a marca do veículo ? (ex: Fiat)\n->"))
    veiculo.setModelo(input("Qual o modelo do veículo ? (ex: UNO)\n->"))
    veiculo.setAno(int(input("Qual o ano do veículo ? (ex: 2018)\n->")))
    veiculo.setValorDiaria(float(input("Qual o valor da diária do veículo ? (ex: 100.5)\nR$")))
    input("\nVeículo adicionado com sucesso!\n\nPressione ENTER para voltar ao menu principal . . .")
    listVeiculos.append(veiculo)
        
    return listVeiculos
