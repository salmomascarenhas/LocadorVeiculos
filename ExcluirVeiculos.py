import os


def mostrarExcluir(listVeiculos = []):
    os.system("cls")
    codigo = int(input("Qual o código do veículo a ser removido ? (ex:1)\n->"))
    index = codigo - 1
    try:
        status = listVeiculos[index].getStatus()
    except:
        print("Código inexistente.")
        input("\nPressione ENTER para voltar ao menu principal . . .")
    else:
        if status == "Disponível":
            listVeiculos.pop(index)
            print("Veículo removido com sucesso!")
            input("\nPressione ENTER para voltar ao menu principal . . .")
        else:
            print("Veículo não está disponível para remoção pelo seguinte motivo: " + str(listVeiculos[index].getStatus()))
            input("\nPressione ENTER para voltar ao menu principal . . .")
    return listVeiculos
         
