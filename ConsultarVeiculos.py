from Veiculo import Veiculo
import os
from time import sleep
import datetime



def mostrarConsulta(listVeiculos = [], dataAtual = datetime.datetime.now()):
    if( len(listVeiculos) == 0 ): #Se lista vazia.            
        for sec in ['3','2','1']:
            os.system("cls")
            print("+-----------------------------------------+")
            print("+        Nenhum veículo cadastrado.       +")
            print("+        Retornando em: "+ sec + " segundos...     +")
            print("+-----------------------------------------+\n")
            sleep(1)
            
        from MenuPrincipal import MenuPrincipal
        menuPrincipal = MenuPrincipal(listVeiculos, dataAtual)
        menuPrincipal.mostrarMenu()

    else: #Se a lista conter pelo menos um elemento do tipo Veiculo.
        dia = dataAtual.day     
        mes = dataAtual.month
        ano = dataAtual.year
        dataAtual = datetime.datetime(ano,mes,dia) #Zera horas,minutos,segundos
        listVeiculos = mudaParaAlugado(listVeiculos,dataAtual)
        os.system("cls")
        for veiculo in listVeiculos:
            if int(veiculo.getCodigo()) > 100:
                print("\n    Código nº: " + str(veiculo.getCodigo()))
                        
            elif int(veiculo.getCodigo()) > 9 and int(veiculo.getCodigo()) < 100:
                print("\n    Código nº: 0" + str(veiculo.getCodigo()))
                        
            else:
                print("\n    Código nº: 00" + str(veiculo.getCodigo()))

            print("    Modelo: " + str(veiculo.getModelo()))
            print("    Status: " + str(veiculo.getStatus()))
            if( int(len(listVeiculos)) > 1 ):
                print("\n    -------------------")
            print("")

        veiculo = 0
        print("\n[1] Consultar mais detalhes.")
        print("[2] Retornar ao menu principal.")
        opcao = int(input("\nEscolha uma das opções acima (ex:2):\n->"))

        if opcao == 1: #Consulta com mais detalhes.
            os.system("cls")
            for veiculo in listVeiculos:
                if int(veiculo.getCodigo()) > 100:
                    print("\n    Código nº: " + str(veiculo.getCodigo()))
                        
                elif int(veiculo.getCodigo()) > 9 and int(veiculo.getCodigo()) < 100:
                    print("\n    Código nº: 0" + str(veiculo.getCodigo()))
                        
                else:
                    print("\n    Código nº: 00" + str(veiculo.getCodigo()))
                        
                print("    Modelo: " + str(veiculo.getModelo()))
                print("    Marca: " + str(veiculo.getMarca()))
                print("    Ano: " + str(veiculo.getAno()))
                print("    Status: " + str(veiculo.getStatus()))
                print("    Valor: R$" + str(veiculo.getValorDiaria()))
                if( int(len(listVeiculos)) > 1 ):
                    print("\n    -------------------")
                print("")
                
            input("\nPressione ENTER para voltar ao menu principal . . .")
            from MenuPrincipal import MenuPrincipal
            menuPrincipal = MenuPrincipal(listVeiculos, dataAtual)
            menuPrincipal.mostrarMenu()

        elif opcao == 2: #Volta ao menu principal.
            from MenuPrincipal import MenuPrincipal
            menuPrincipal = MenuPrincipal(listVeiculos, dataAtual)
            menuPrincipal.mostrarMenu()

        else: #Qualquer valor diferente de 1 ou 2.
            input("Opção inválida.\n\nPressione ENTER para voltar ao menu principal . . .")
            from MenuPrincipal import MenuPrincipal
            menuPrincipal = MenuPrincipal(listVeiculos, dataAtual)
            menuPrincipal.mostrarMenu()

def mudaParaAlugado(listVeiculos, dataAtual):
    total = int(len(listVeiculos))
    for index in range(total):
        print(listVeiculos[index].getStatus())
        if (listVeiculos[index].getStatus() == "Reservado") and (listVeiculos[index].getDataLocacao() == dataAtual):
            listVeiculos[index].setStatus("Alugado")

    return listVeiculos