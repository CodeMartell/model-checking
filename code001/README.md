# Model Checking: Control Flow Graph (CFG)

Este projeto implementa a geração de um **Gráfico de Fluxo de Controle (Control Flow Graph - CFG)** para modelar o comportamento de um sistema concorrente composto por duas threads interagindo com um recurso compartilhado. O código utiliza busca em largura (BFS) para explorar todos os estados possíveis do sistema, representados por combinações de localizações das threads, o estado do lock e o valor de uma variável compartilhada.

## Funcionalidades

- **Simulação de threads concorrentes:**
  - Duas threads (`Thread 1` e `Thread 2`) que interagem em um ambiente controlado por um recurso bloqueável (lock).
  - Cada thread tem suas próprias localizações (`L0`, `L1`, etc.) e transições de estado.

- **Exploração de estados:**
  - Utiliza busca em largura (BFS) para gerar todos os estados alcançáveis.
  - Estados são definidos pelas localizações das threads, o estado do lock (bloqueado/desbloqueado) e o valor de uma variável compartilhada `x`.

- **Geração de CFG:**
  - Gera um arquivo no formato `.dot` que representa o CFG do sistema.
  - O arquivo `.dot` pode ser renderizado para criar uma visualização gráfica do fluxo de controle.

## Como executar

1. Clone o repositório e acesse o diretório do projeto:
   ```bash
   git clone https://github.com/CodeMartell/model-checking.git
   cd model-checking
   ```
2.  Execute o código Python
   ```bash
   python first-code.py
   ```
3. Um arquivo cfg.dot será gerado no diretório atual.
4. Para visualizar o gráfico, use o Graphviz:
   ```bash
   dot -Tpng cfg.dot -o cfg.png
   ```
