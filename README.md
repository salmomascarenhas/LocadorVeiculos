## Autor
Aluno: Salmo da Cruz Mascarenhas - 431447
Curso: Engenharia da computação

>**NOTA:**
> Language version: **Python 3** 
> S.O: **Windows 10**


## Descrição

O seguinte programa tem como objetivo pôr em prática os assuntos abordados na disciplina de **Técnicas de programação** com a linguagem Python. 

## Do programa

--Gerenciador de locação de veículos --
Este programa está dividido nos seguintes **principais módulos**:
- main.py (início do programa)
- MenuPrincipal.py (Mostra todas as opções do menu)
- ConsultarVeiculos.py (Consulta todos os veículos, se existentes)
- AdicionarVeiculos.py (Cadastra um novo veículo)
- ReservarVeiculos.py (Aluga/Reserva um veículo)
- LiberarVeiculos.py (Libera/devolve um veículo, se alugado ou reservado)
- ExcluirVeiculos.py (Exclui um veículo cadastrado, se possível)
- AvancarDataAtual.py (Avança um dia na data atual do sistema)




## Clonando repositório

**1º** **No Windows**  Faça o download do git no link:  [https://git-scm.com/download/win](https://git-scm.com/download/win)

**2º** Após download, execute o instalador e dê **next, next...**  e por último **finish**.

**3º** Na sua **Área de trabalho** dê clique com o botão direito do mouse e vá em GIT bash here, irá abrir o GitBash. 

**4º** No GitBash digite (copy and paste):
>$ git clone https://github.com/salmomascarenhas/LocadorVeiculos.git
>
**5º** Faça o login com a sua conta do github na tela, caso peça (login e senha).

**6º** Verifique a nova pasta clonada com o nome de **LocadorVeiculos** e 		dê dois cliques na mesma.

**7º** Procure pelo arquivo chamado **main.py** e dê um clique duplo no mesmo.

Pronto, o programa deve iniciar.
>**NOTA:**
>Para que o programa abra, é necessário ter o **Python 3** instalado no Windows. Pode ser baixado no seguinte link:
https://www.python.org/ftp/python/3.7.1/python-3.7.1.exe

## Funcionamento
>**NOTA:**
>Para uma execução sem  **excessões e erros**, deve ser estritamente seguido os formatos de **exemplos (ex: )** no decorrer do programa (estarão nas perguntas).

**Consultar veículos**:
>No menu principal aperte **1** e depois **ENTER**. Como não há veículos cadastrados, não será possível consultá-los. O programa retornará ao **menu principal** em 3 segundos. Tente novamente após o cadastro.

**Adicionar veículos**:
>No menu principal aperte **2** e depois **ENTER**. Preencha de acordo com o modelo dado em cada pergunta (**ex: Fiat**) e assim por diante até completar o cadastro.

**Alugar/Reservar veículos**:
>No menu principal aperte **3** e depois **ENTER**. Preencha de acordo com o modelo dado em cada pergunta (**ex: Joao, ex:001, ex: 21/11/2018**) e assim por diante até completar @ aluguel/reserva.

**Devolver/Liberar veículos**:
>No menu principal aperte **4** e depois **ENTER**. Forneça o código de um dos veículos cadastrados que estão na tela (**ex: 001**) e assim será retornado um resultado (dependendo do status do veículos).

**Excluir veículos**:
>No menu principal aperte **5** e depois **ENTER**. Forneça o código de um dos veículos consultados anteriormente (**ex: 001**) para excluir do sistema (se disponível).

**Avançar  data atual**:
>No menu principal aperte **6** e depois **ENTER**. Avança em um dia a data atual (no topo) e ocorrem alterações no sistema (com reservas e atrasos), caso necessário.

**Sair**:
>No menu principal aperte **7** e depois **ENTER**. Finaliza o programa.
