"""
    Listas e Tuplas
        São tipos de coleções que podem armazenar vários itens, mas tem algumas diferenças.

        Listas:  - São MUTÁVEIS, o que siginifica que podemos alterar seus elementos após a sua definição.
                 - Podendo adicionar, remover ou modificar os elementos.
                 - São definidas usando colchetes [ ].
                 EX:
                    frutas = ['banana', 'abacaxi', 'kiwi']
                    frutas.append('maça') # Adiciona um item na lista
                    frutas.remove('abacaxi') # Remove um item da lista
                    frutas[0] = 'Caja' # Modifica um determinado item na lista


        Tuplas: - São IMUTÁVEIS,  o que significa que uma vez definida, seus elementos não podem ser alterados.
                - NÃO podendo, adicionar, remover ou modificar os elementos
                - São definidas usando parênteses ( ) .
                EX:
                    tupla = (1, 2, 3, 4, 2, 2, 5)
                    tupla.index(4) # é usado para encontrar o indice da primeira ocorrencia de um elemento na tupla.
                    tupla.count(2) # é usado para contar quantas vezes um elemento específico aparece na tupla.

"""

lista_frutas = ['banana', 'abacaxi', 'kiwi']
lista_frutas.append('Maça')  # Adiciona um item na lista
lista_frutas.remove('abacaxi')  # Remove um item da lista
lista_frutas[0] = 'Caja'  # Modifica um determinado item na lista
print(lista_frutas)


tupla = (1, 2, 3, 4, 2, 2, 5)
tupla.index(4)  # é usado para encontrar o indice da primeira ocorrencia de um elemento na tupla.
tupla.count(2)  # é usado para contar quantas vezes um elemento específico aparece na tupla.
