# from fila_normal import FilaNormal
# from fila_prioridade import FilaPrioridade
#
# fila_teste = FilaNormal()
# fila_teste.atualiza_fila()
# fila_teste.atualiza_fila()
# fila_teste.atualiza_fila()
# fila_teste.atualiza_fila()
#
# print(fila_teste.chama_cliente(5))
# print(fila_teste.chama_cliente(10))
#
# fila_teste2 = FilaPrioridade()
# fila_teste2.atualiza_fila()
# fila_teste2.atualiza_fila()
# fila_teste2.atualiza_fila()
# fila_teste2.atualiza_fila()
#
# print(fila_teste2.chama_cliente(10))
# print(fila_teste2.chama_cliente(1))
# print(fila_teste2.estatistica('10/01/1993', 198, 'detail'))

from fabrica_fila import FabricaFila

teste_fabrica = FabricaFila.pega_fila('normal')
teste_fabrica.atualiza_fila()
teste_fabrica.atualiza_fila()
teste_fabrica.atualiza_fila()
print(teste_fabrica.chama_cliente(10))
