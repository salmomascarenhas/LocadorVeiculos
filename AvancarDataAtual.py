import datetime


def avancaUmDia(dataAtual = datetime.datetime.now()):
    dataAtual = dataAtual + datetime.timedelta(1)
    return dataAtual