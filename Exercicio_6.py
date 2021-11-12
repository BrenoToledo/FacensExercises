"""

Implemente uma classe especial de ordenação, chamada OrdenaEspecial

>>> # Criar OrdenaEspecial
>>> from Exercicio_6 import OrdenaEspecial
>>> a_lista = [9,8,7,6,5,4,3,2,1]
>>> dados = OrdenaEspecial(a_lista,'shell')

    Essa classe deverá ter dois atributos:

>>> # Verifica se possui os dois atributos
>>> print('lista' in list(dir(dados)))
>>> 'lista' in dir(dados)
>>> true


        • lista: contém uma lista de números. Esse atributo deverá ser obrigatório na
        instanciação do objeto.

        • metodo: contém o nome de um método de ordenação. Esse atributo deverá ser
        opcional na instanciação do objeto e conter o seguinte valor default: “combina”.

    A classe OrdenaEspecial deverá conter também três métodos:

        • método chamado ordena-quickSort que faz a ordenação usando o algoritmo quick sort.

        • método chamado ordena-shellSort para fazer a ordenação usando o algoritmo shell sort.

        • método chamado ordena-insertionSort para fazer a ordenação usando o algoritmo insertion sort.

Condições :

    ◦ se o atributo metodo receber o valor “quick”, deverá ordenar a lista usando o método ordena-quickSort.

>>> # Metodo quick - teste de ordenacao:
>>> testes_metodos = OrdenaEspecial(a_lista,'quick')
>>> testes_metodos
>>> [1,2,3,4,5,6,7,8,9]

    ◦ se o atributo metodo receber o valor “shell”, deverá ordenar a lista usando o método ordena-shellSort.

>>> # Metodo shell - teste de ordenacao:
>>> testes_metodos = OrdenaEspecial(a_lista,'shell')
>>> testes_metodos
>>> [1,2,3,4,5,6,7,8,9]

    ◦ se o atributo metodo receber o valor “insertion”, deverá ordenar a lista usando o método ordena-insertionSort.

>>> # Metodo insertion - teste de ordenacao:
>>> testes_metodos = OrdenaEspecial(a_lista,'insertion')
>>> testes_metodos
>>> [1,2,3,4,5,6,7,8,9]

    ◦ Se o atributo metodo estiver com o valor default combina, deverá ordenar a metade da lista usando o método
    ordena-quickSort, a segunda metade usando o método ordena-shellSort. Por fim, deve combinar as duas metades
    ordenadas anteriormente e ordená-las com o método ordena-insertionSort.

        ▪ Esse método deverá retornar a lista ordenada.

    Crie um vetor de 40 números aleatórios e faça os seguintes testes:

        • Crie um objeto chamado ordena1, que instancie a classe OrdenaEspecial passando como parâmetro a lista de números
        e o parâmetro metodo = “shell”.

        • Crie um objeto chamado ordena2, que instancie a classe OrdenaEspecial
        passando como parâmetro a lista de números e o parâmetro metodo = “insertion”.

        • Crie um objeto chamado ordena3, que instancie a classe OrdenaEspecial
        passando como parâmetro a lista de números e o parâmetro metodo = “quick”.

        • Crie um objeto chamado ordena4, que instancie a classe OrdenaEspecial
        passando como parâmetro apenas a lista de números. Neste teste, o parâmetro
        metodo não deve ser informado.

        Para cada um dos quatro objetos criados, use o método ordena para fazer a
        ordenação.

        Ex.
        Shell Sort

DOCTESTES:

    #exemplo:

    # >>> # Testando o motor
    # >>> import pandas_datareader as pdr
    # >>> import datetime
    # >>> aapl = pdr.get_data_yahoo('AAPL', start=datetime.datetime(2006, 10, 1), end=datetime.datetime(2012, 1, 1))
    # >>> print(aapl)
    # >>> Candle = Candle(a_date,a_high,a_low,a_open,a_close,a_volume,a_adj_Close)
    # >>> candle.abertura
    # 0
    # >>> # Testando a aceleracao
    # >>> motor.acelera()
    # >>> motor.velocidade
    # 1

"""


class OrdenaEspecial:

    def __init__(self, lista, metodo='combina'):
        self.lista = lista
        self.metodo = metodo

    def print_args(self):
        print(self.lista)
