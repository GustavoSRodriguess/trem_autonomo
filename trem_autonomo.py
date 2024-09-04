class TremAutonomo:
    def __init__(self):
        self.posicao = 0
        self.movimentos_consecutivos = 0
        self.direcao_anterior = None
        self.distancia_percorrida = 0

    def processar_comandos(self, comandos):
        if not all(comando in ['ESQUERDA', 'DIREITA'] for comando in comandos):
            return "Erro: Comando inválido. Use 'ESQUERDA' ou 'DIREITA'."

        for comando in comandos:
            if self.distancia_percorrida >= 50:
                break

            if comando == self.direcao_anterior:
                self.movimentos_consecutivos += 1
            else:
                self.direcao_anterior = comando
                self.movimentos_consecutivos = 1

            if self.movimentos_consecutivos > 20:
                return "Erro: Mais de 20 movimentos consecutivos na mesma direção."

            if comando == 'DIREITA':
                self.posicao += 1
            elif comando == 'ESQUERDA':
                self.posicao -= 1

            self.distancia_percorrida += 1

        return f"Posição Final: {self.posicao}"
