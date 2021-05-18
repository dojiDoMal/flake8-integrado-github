from typing import Union

from fila_normal import FilaNormal
from fila_prioridade import FilaPrioridade
from constantes import TIPO_FILA_NORMAL, TIPO_FILA_PRIORIDADE


class FabricaFila:
    @staticmethod
    def pega_fila(tipo_fila) -> Union[FilaNormal, FilaPrioridade]:
        if tipo_fila == TIPO_FILA_NORMAL:
            return FilaNormal()
        elif tipo_fila == TIPO_FILA_PRIORIDADE:
            return FilaPrioridade()
        else:
            raise NotImplementedError('Tipo da fila não existe')
