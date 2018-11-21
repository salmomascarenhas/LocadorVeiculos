def atualizarCodigoVeiculos(listVeiculos = []):
    total = int(len(listVeiculos))
    for index in range(total):
        codigo = index + 1
        listVeiculos[index].setCodigo(codigo)
    return listVeiculos
