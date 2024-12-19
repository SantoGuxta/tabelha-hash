class Nodo:
    def __init__(self, sigla, nomeEstado):
        self.sigla = sigla
        self.nomeEstado = nomeEstado
        self.proximo = None

class TabelaHash:
    def __init__(self):
        self.tabela = [None] * 10

    def funcao_hash(self, sigla):
        if sigla == "DF":
            return 7
        return (ord(sigla[0]) + ord(sigla[1])) % 10

    def inserir(self, sigla, nomeEstado):
        indice = self.funcao_hash(sigla)
        nodo = Nodo(sigla, nomeEstado)
        nodo.proximo = self.tabela[indice]
        self.tabela[indice] = nodo

    def imprimir_tabela(self):
        for i in range(10):
            print(f"Posição {i}: ", end="")
            atual = self.tabela[i]
            while atual:
                print(f"{atual.sigla} ", end="")
                atual = atual.proximo
            print()

def main():
    estados = [
        ("AC", "Acre"), ("AL", "Alagoas"), ("AP", "Amapá"), ("AM", "Amazonas"),
        ("BA", "Bahia"), ("CE", "Ceará"), ("DF", "Distrito Federal"), ("ES", "Espírito Santo"),
        ("GO", "Goiás"), ("MA", "Maranhão"), ("MT", "Mato Grosso"), ("MS", "Mato Grosso do Sul"),
        ("MG", "Minas Gerais"), ("PA", "Pará"), ("PB", "Paraíba"), ("PR", "Paraná"),
        ("PE", "Pernambuco"), ("PI", "Piauí"), ("RJ", "Rio de Janeiro"), ("RN", "Rio Grande do Norte"),
        ("RS", "Rio Grande do Sul"), ("RO", "Rondônia"), ("RR", "Roraima"), ("SC", "Santa Catarina"),
        ("SP", "São Paulo"), ("SE", "Sergipe"), ("TO", "Tocantins")
    ]

    tabela = TabelaHash()

    # Saída de console antes de inserir qualquer informação
    print("Tabela Hash antes de inserir qualquer informação:")
    tabela.imprimir_tabela()

    # Os 26 estados e o Distrito Federal na tabela hash
    for sigla, nome in estados:
        tabela.inserir(sigla, nome)

    # Saída de console após inserir os 26 estados e o Distrito Federal
    print("\nTabela Hash após inserir os 26 estados e o Distrito Federal:")
    tabela.imprimir_tabela()

    # Estado fictício
    tabela.inserir("LA", "Luiz Alves")

    # Saída de console após inserir o estado fictício
    print("\nTabela Hash após inserir os 26 estados, o Distrito Federal e o estado fictício:")
    tabela.imprimir_tabela()

if __name__ == "__main__":
    main()
