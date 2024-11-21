


from collections import deque, namedtuple

# Representação do Estado
Estado = namedtuple('Estado', ['loc1', 'loc2', 'lock', 'x'])

# Localizações para as duas threads
LOC1 = ['L0', 'L1', 'L2', 'L3']  # Localizações da Thread 1
LOC2 = ['L0_p', 'L1_p', 'L2_p', 'L3_p']  # Localizações da Thread 2 (substituindo ' por _p)

# Estado inicial
estado_inicial = Estado('L0', 'L0_p', 0, 0)  # (loc Thread1, loc Thread2, lock, x)

# Fila para BFS e conjunto de estados visitados
fila = deque([estado_inicial])
visitados = set([estado_inicial])

# Lista de transições para gerar o gráfico
transicoes_grafo = []

# Função para definir as transições
def transicoes(estado):
    loc1, loc2, lock, x = estado
    novas_transicoes = []
    
    # Transições para Thread 1
    if loc1 == 'L0' and lock == 0:
        novas_transicoes.append(Estado('L1', loc2, 1, x))  # Thread 1 avança para L1 e lock é ativado
    elif loc1 == 'L1' and lock == 1:
        novas_transicoes.append(Estado('L2', loc2, lock, 1))  # Thread 1 avança para L2 e x é alterado para 1
    elif loc1 == 'L2' and lock == 1:
        novas_transicoes.append(Estado('L3', loc2, 0, x))  # Thread 1 avança para L3 e libera lock
    
    # Transições para Thread 2
    if loc2 == 'L0_p' and lock == 0:
        novas_transicoes.append(Estado(loc1, 'L1_p', 1, x))  # Thread 2 avança para L1' e lock é ativado
    elif loc2 == 'L1_p' and lock == 1:
        novas_transicoes.append(Estado(loc1, 'L2_p', lock, 2))  # Thread 2 avança para L2' e x é alterado para 2
    elif loc2 == 'L2_p' and lock == 1:
        novas_transicoes.append(Estado(loc1, 'L3_p', 0, x))  # Thread 2 avança para L3' e libera lock

    return novas_transicoes

# BFS para explorar todos os estados acessíveis
while fila:
    estado_atual = fila.popleft()

    for novo_estado in transicoes(estado_atual):
        if novo_estado not in visitados:
            visitados.add(novo_estado)
            fila.append(novo_estado)
            # Adicione a transição ao grafo
            transicoes_grafo.append((estado_atual, novo_estado))

# Gerar o arquivo DOT para o CFG!!!!!!!!!!!
with open("cfg.dot", "w") as dot_file:
    dot_file.write("digraph ControlFlowGraph {\n")
    for origem, destino in transicoes_grafo:
        dot_file.write(f'    "{origem}" -> "{destino}";\n')
    dot_file.write("}\n")

print("\nArquivo DOT gerado: cfg.dot")
print("Estados acessíveis:")
for estado in visitados:
    print(estado)
