from fabrica_fila import FabricaFila
from estatistica import Estatistica
from estatistica_resumida import EstatisticaResumida

teste_fabrica = FabricaFila.pega_fila('prioridade')
teste_fabrica.atualiza_fila()
teste_fabrica.atualiza_fila()
teste_fabrica.atualiza_fila()
teste_fabrica.atualiza_fila()
print(teste_fabrica.chama_cliente(10))
print(teste_fabrica.chama_cliente(10))
print(teste_fabrica.chama_cliente(10))
print(teste_fabrica.estatistica(EstatisticaResumida('20/03/2021', 120)))
print(teste_fabrica.estatistica(Estatistica('20/03/2021', 120)))
