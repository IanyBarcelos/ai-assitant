# Assistente de IA com Ferramentas (Desafio Técnico - Vaga AI Engineer Júnior)

Este projeto é uma implementação de um agente de Inteligência Artificial capaz de conversar naturalmente e utilizar ferramentas externas quando necessário. 


## Funcionalidades:
O assistente possui os seguintes "superpoderes":

- Conversa Geral: Responde a perguntas de conhecimento geral usando o modelo de linguagem.

- Calculadora: Identifica operações matemáticas e executa o cálculo exato via código.


## Tecnologias Utilizadas:
- Python 3.10+

- LangChain & LangGraph: Frameworks para orquestração do agente.

- Ollama: Para rodar o LLM localmente de forma gratuita e privada.


## Pré-requisitos e Instalação:

Este projeto utiliza modelos locais para evitar custos. Por esse motivo, é necessário instalar o Ollama.

1. Instale o Ollama

Acesse o site: https://ollama.com/ e siga as intruções oficiais de instalação para o seu sistema operacional.

2. Baixe o modelo utilizado

No seu terminal, execute o comando abaixo para baixar o modelo Llama 3.1 (8B):

```Bash
ollama pull llama3.1:8b
```

3. Clone o repositório e instale as dependências

```
git clone <URL_DO_REPOSITORIO>
cd <NOME_DO_REPOSITORIO>
pip install -r requirements.txt
```


## Como Executar
Antes de iniciar a aplicação, certifique-se de que o serviço do Ollama está em execução em segundo plano.

1. Execute o script principal:

```Bash
python main.py
```
2. Interaja com o assistente via terminal

Após a inicialização, o assistente ficará aguardando entradas do usuário no CLI.

Para encerrar a execução, digite exit ou sair.


## Lógica de Implementação
Em síntese, a solução foi estruturada pensando no modelo como um "roteador" com a habilidade de Reasoning e action, interpretando a solicitação do usuário e definindo qual ferramenta utilizar para a resposta final.

Escolhi llama3.1:8b via Ollama por se tratar de um modelo local, com boa capacidade de seguir instruções e realizar chamadas de ferramentas de forma consistente. A temperatura foi configurada como zero para maximizar seu determinismo, especialmente no processo de decisão sobre quando utilizar ferramentas externas e evitar alucinações em suas respostas.

As ferramentas foram definidas como funções Python simples, decoradas com @tool, cada uma acompanhada de docstrings descritivas, permitindo que o modelo compreenda corretamente o propósito da função, seus parâmetros e em quais contextos ela deve ser acionada.

O prompt do sistema foi projetado para reforçar explicitamente que operações matemáticas devem ser delegadas à ferramenta de cálculo, evitando que o modelo tente inferir resultados.


## Aprendizados e Melhorias Futuras
Durante o desenvolvimento deste desafio, aprendi e reforcei conceitos importantes sobre LLMs e o uso de modelos pré-treinados. Especialmente no que se refere a importância de prompts de sistema bem definidos para evitar que o modelo ignore as ferramentas e induzi-lo a decidir corretamente quando delegar as tarefas a ferramentas externas, evitando tanto alucinações quanto o uso indevido dessas ferramentas.
Por exemplo, durante o desenvolvimento, tentei ainda integrar uma ferramenta de consulta à Wikipedia de forma condicional, apenas quando o modelo identificasse a necessidade de informações mais completas. Porém, ficou claro que ao trabalhar com modelos pré-treinados, controlar o comportamento do agente apenas por meio de prompt engineering pode ser complicado, especialmente em cenários que exigem decisões mais críticas sobre o uso de ferramentas.

Como melhorias futuras, com mais tempo de desenvolvimento, eu substituiria a CLI por uma interface gráfica mais amigável ao usuário, tornando o sistema mais acessível. Além disso, integraria uma ferramenta de consulta a notícias ou fontes atualizadas, permitindo que o assistente respondesse a eventos mais recentes.