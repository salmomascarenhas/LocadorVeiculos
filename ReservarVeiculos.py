import datetime
import os
from time import sleep

def mostrarReserva(listVeiculos = [], dataAtual = datetime.datetime.now()):
    os.system("cls")
    dia = dataAtual.day        
    mes = dataAtual.month
    ano = dataAtual.year
    dataAtual = datetime.datetime(ano,mes,dia) #Zera horas,minutos,segundos
    mudaParaAlugado(listVeiculos, dataAtual)
        
    strDataAtual = dataAtual.strftime("%d/%m/%y")
    if listVeiculos == []:
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

    locador = input("Nome do locatório ? (ex: Joao)\n->")
    codigo = int(input("Qual o código do veículo a ser locado ? (ex:55)\n->"))
    index = codigo - 1
    #codifica a data recebido para datetime.
    dataLocacao = input("Qual a data de locação ? (ex:dd/mm/aaaa)\n->")
    dataLocacao = dataLocacao.split("/")
    dia = int(dataLocacao[0])
    mes = int(dataLocacao[1])
    ano = int(dataLocacao[2])
    
    dataLocacao = datetime.datetime(ano,mes,dia)
    #fim codificação

    if dataLocacao < dataAtual:
        print("\nData anterior a data atual, por favor escolha outra data.")
        input("\nPressione ENTER para continuar . . .")
        from ReservarVeiculos import ReservarVeiculos
        reservarVeiculos = ReservarVeiculos()
        reservarVeiculos.mostrarReserva(listVeiculos, dataAtual)

    trintaDias = datetime.timedelta(30)
    while dataLocacao - dataAtual > trintaDias:            
        dataLocacao = input("Data de reserva ultrapassou 30 dias, digite novamente a data de locação: (ex:dd/mm/aaaa)\n->")
        dia = int(dataLocacao[0:2])
        mes = int(dataLocacao[3:5])
        ano = int(dataLocacao[6:10])
        dataLocacao = datetime.datetime(ano,mes,dia)
        
    diasLocacao = int(input("Qual o prazo de locação ? (ex:5)\n->"))
    strDataLocacao = dataLocacao.strftime("%d/%m/%y") #Codifica datetime para string no formato dd/mm/aaaa      

    if listVeiculos[index].getStatus() != "Disponível": #Entre nesse if se o carro !disponível.
        if listVeiculos[index].getStatus() == "Alugado" and comparaIntervaloData(listVeiculos[index], dataLocacao, diasLocacao):
            listVeiculos[index].setLocador(locador)
            listVeiculos[index].setStatus("Reservado")
            listVeiculos[index].setDataLocacao(dataLocacao)
            listVeiculos[index].setDiasLocacao(diasLocacao)
            print("\nVeículo RESERVADO com sucesso para a data: " + strDataLocacao + " por " + str(diasLocacao) + " dia(s).")
            input("\nPressione ENTER para voltar ao menu principal . . .")
            return listVeiculos
        if listVeiculos[index].getStatus() == "Reservado" and comparaIntervaloData(listVeiculos[index], dataLocacao, diasLocacao) :
            listVeiculos[index].setLocador(locador)
            listVeiculos[index].setStatus("Alugado")
            listVeiculos[index].setDataLocacao(dataLocacao)
            listVeiculos[index].setDiasLocacao(diasLocacao)
            print("\nVeículo ALUGADO com sucesso hoje: " + strDataLocacao + " por " + str(diasLocacao) + " dia(s).")
            input("\nPressione ENTER para voltar ao menu principal . . .")
                
            return listVeiculos
        else:
            print("\nSobreposição de datas, por favor escolha outra data ou veículo.")
            input("\nPressione ENTER para continuar . . .")
            from ReservarVeiculos import ReservarVeiculos
            reservarVeiculos = ReservarVeiculos()
            listVeiculos = reservarVeiculos.mostrarReserva(listVeiculos, dataAtual)
            return listVeiculos
    else: #Veículo está disponível.
        if strDataLocacao == strDataAtual: #Verifica se o veículo será alugado no dia atual.
            listVeiculos[index].setLocador(locador)
            listVeiculos[index].setStatus("Alugado")
            listVeiculos[index].setDataLocacao(dataLocacao)
            listVeiculos[index].setDiasLocacao(diasLocacao)
            print("\nVeículo ALUGADO com sucesso hoje: " + strDataLocacao + " por " + str(diasLocacao) + " dia(s).")
            input("\nPressione ENTER para voltar ao menu principal . . .")
            return listVeiculos

        else:
            listVeiculos[index].setLocador(locador)
            listVeiculos[index].setStatus("Reservado")
            listVeiculos[index].setDataLocacao(dataLocacao)
            listVeiculos[index].setDiasLocacao(diasLocacao)
            print("\nVeículo RESERVADO com sucesso para a data: " + strDataLocacao + " por " + str(diasLocacao) + " dia(s).")
            input("\nPressione ENTER para voltar ao menu principal . . .")
            return listVeiculos
    
def comparaIntervaloData(veiculo, dataInicialLocacao, diasLocacao):
    dataInicialVeiculo = veiculo.getDataLocacao()
    dataFinalVeiculo = dataInicialVeiculo + datetime.timedelta(veiculo.getDiasLocacao()) - datetime.timedelta(1)
    dataFinalLocacao = dataInicialLocacao + datetime.timedelta(diasLocacao) - datetime.timedelta(1)
        
    if dataInicialLocacao > dataFinalVeiculo or dataFinalLocacao < dataInicialVeiculo :
        return True
    else:
        return False
#Muda para 'alugado' todas os veiculos que estavam 'reservados' para tal dia e esse dia chega.
def mudaParaAlugado(listVeiculos, dataAtual):
    for index in range(len(listVeiculos)):
        if (listVeiculos[index].getStatus == "Reservado") and (listVeiculos[index].getDataLocacao() == dataAtual):
            listVeiculos[index].setStatus("Alugado")

    return listVeiculos
