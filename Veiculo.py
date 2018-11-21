class Veiculo:
    
    def __init__(self, marca = None, modelo = None, ano = None, valorDiaria = None, status = "Disponível", codigo = None, locador = None, dataLocacao = None, diasLocacao = None):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano
        self.valorDiaria = valorDiaria
        self.status = status
        self.codigo = codigo
        self.locador = locador
        self.dataLocacao = dataLocacao
        self.diasLocacao = diasLocacao

    #getters
    def getMarca(self):
        return self.marca
    
    def getModelo(self):
        return self.modelo

    def getAno(self):
        return self.ano

    def getValorDiaria(self):
        return self.valorDiaria

    def getStatus(self):
        return self.status

    def getCodigo(self):
        return self.codigo

    def getLocador(self):
        return self.locador
    
    def getDataLocacao(self):
        return self.dataLocacao

    def getDiasLocacao(self):
        return self.diasLocacao
    
    #setters
    def setMarca(self, marca):
        self.marca = marca
    
    def setModelo(self, modelo):
        self.modelo = modelo
    
    def setAno(self, ano):
        self.ano = ano
    
    def setValorDiaria(self, valorDiaria):
        self.valorDiaria = valorDiaria

    def setStatus(self, status):
        self.status = status

    def setCodigo(self, codigo):
        self.codigo = codigo

    def setLocador(self, locador):
        self.locador = locador

    def setDataLocacao(self, dataLocacao):
        self.dataLocacao = dataLocacao

    def setDiasLocacao(self, diasLocacao):
        self.diasLocacao = diasLocacao


