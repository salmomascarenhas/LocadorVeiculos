import datetime
import os
from time import sleep

def mostrarLiberar(listVeiculos, dataAtual = datetime.datetime.now()):
    os.system("cls")
    dia = dataAtual.day        
    mes = dataAtual.month
    ano = dataAtual.year
    dataAtual = datetime.datetime(ano,mes,dia) #Zera horas,minutos,segundos
    strDataAtual = dataAtual.strftime("%d/%m/%y")
    if len(listVeiculos) == 0:
        for sec in ['3','2','1']:
            os.system("cls")
            print("+-----------------------------------------+")
            print("+        Nenhum veículo cadastrado.       +")
            print("+        Retornando em: "+ sec + " segundos...     +")
            print("+-----------------------------------------+\n")
            sleep(1)
        return listVeiculos
        
    print("+++++++++++++++++++++++++++++++++++++++++++")
    print("+                 DATA ATUAL              +")
    print("+                  " + strDataAtual + "               +")
    print("+-----------------------------------------+")

    print("+  LISTA DE VEÍCULOS ALUGADOS/RESERVADOS  +")
    listarVeiculos(listVeiculos)

    codigo = int(input("Qual o código do veículo que você gostaria de devolver/liberar ? (ex:001)\n->"))
    index = codigo - 1
    status = listVeiculos[index].getStatus()
    if status == "Disponível":
        print("Veículo disponível, não há como liberar/devolver.")
        input("\nPressione ENTER para voltar ao menu principal . . .")
        from MenuPrincipal import MenuPrincipal
        menuPrincipal = MenuPrincipal(listVeiculos, dataAtual)
        menuPrincipal.mostrarMenu()
        
    elif status == "Reservado":
        print(listVeiculos[index].getLocador() + " o veículo foi liberado com sucesso!")
        listVeiculos[index].setLocador("Locador não definido")
        listVeiculos[index].setDataLocacao(0)
        listVeiculos[index].setDiasLocacao(0)
        listVeiculos[index].setStatus("Disponível")
        input("\nPressione ENTER para voltar ao menu principal . . .")
        from MenuPrincipal import MenuPrincipal
        menuPrincipal = MenuPrincipal(listVeiculos, dataAtual)
        menuPrincipal.mostrarMenu()
    else:
        valorTotal = calculaValor(listVeiculos[index],dataAtual)
        print("\n" + listVeiculos[index].getLocador() + " o veículo foi devolvido com sucesso!")
        print("Valor a pagar (com diária majotaria, se for o caso): R$" + str(valorTotal))
        listVeiculos[index].setLocador("Locador não definido")
        listVeiculos[index].setDataLocacao(0)
        listVeiculos[index].setDiasLocacao(0)
        listVeiculos[index].setStatus("Disponível")
        input("\nPressione ENTER para voltar ao menu principal . . .")
        from MenuPrincipal import MenuPrincipal
        menuPrincipal = MenuPrincipal(listVeiculos, dataAtual)
        menuPrincipal.mostrarMenu()



def listarVeiculos(listVeiculos):
    total = int(len(listVeiculos))
    for index in range(total):
        status = listVeiculos[index].getStatus()
        if status == "Alugado" or status == "Reservado":
            if int(listVeiculos[index].getCodigo()) > 100:
                print("\n    CÓDIGO nº: " + str(listVeiculos[index].getCodigo()))
                        
            elif int(listVeiculos[index].getCodigo()) > 9 and int(listVeiculos[index].getCodigo()) < 100:
                print("\n    CÓDIGO nº: 0" + str(listVeiculos[index].getCodigo()))
                        
            else:
                print("\n    CÓDIGO nº: 00" + str(listVeiculos[index].getCodigo()))
                
            print("    Locador: " + listVeiculos[index].getLocador())
            print("    Modelo: " + str(listVeiculos[index].getModelo()))
            print("    Diária: R$" + str(listVeiculos[index].getValorDiaria()))
            print("    Status: " + str(listVeiculos[index].getStatus()))
            if total > 1:
                print("\n    -------------------")

            print("")


def calculaValor(veiculo,dataAtual):
    dataInicialVeiculo = veiculo.getDataLocacao()
    dataFinalVeiculo = dataInicialVeiculo + datetime.timedelta(int(veiculo.getDiasLocacao())) - datetime.timedelta(1)
        
    if dataFinalVeiculo < dataAtual:
        diferenca = int(dataAtual.day - dataFinalVeiculo.day)
        diasTotal = int(veiculo.getDiasLocacao()) + diferenca
        valor = diasTotal * int(veiculo.getValorDiaria())
        return valor
    else:
        valor = int(veiculo.getValorDiaria()) * int(veiculo.getDiasLocacao())
        return valor
