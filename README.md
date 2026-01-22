# IA assistant with tools (Desafio Técnico - Vaga AI Engineer Júnior)

This project implements an Artificial Intelligence agent capable of engaging in a natural conversation and invoking external tools when necessary.


## Features:
The assistant has the following “superpowers”:

- General Conversation: Answers general knowledge questions directly using the language model.

- Calculator: Detects mathematical operations and performs exact calculations through code execution.


## Used technologies:
- Python 3.10+

- LangChain & LangGraph: Frameworks for agent orchestration.

- Ollama: Used to run the LLM locally, providing a free and privacy-preserving setup.


## Requirements and Installation:

This project uses local language models to avoid external API costs. For this reason, it is necessary to install Ollama.

1. Install Ollama

Visit the official website: https://ollama.com/ and follow the installation instructions for your operating system.

2. Download the required model

In your terminal, run the command below to download the Llama 3.1 (8B) model:

```Bash
ollama pull llama3.1:8b
```

3. Clone the repository and install dependencies

```
git clone <REPOSITORY_URL>
cd <REPOSITORY_NAME>
pip install -r requirements.txt
```


## How to Run
Before starting the application, make sure that the Ollama service is running in the background.

1. Run the main script

```Bash
python main.py
```
2. Interact with the assistant via the terminal

After initialization, the assistant will wait for user input through the CLI.

To exit the application, type exit or sair.


## Implementation Logic
In summary, the solution was structured by treating the model as a router with reasoning and action capabilities, responsible for interpreting the user’s request and deciding which tool should be used to produce the final response.

The llama3.1:8b model was chosen via Ollama because it is a local model with a strong ability to follow instructions and perform tool calls in a consistent manner. The temperature was set to zero to maximize determinism, particularly during the decision-making process of whether to invoke external tools, and to reduce hallucinations in the responses.

The tools were implemented as simple Python functions decorated with @tool, each accompanied by descriptive docstrings. This allows the model to correctly understand the purpose of each function, its parameters, and the contexts in which it should be invoked.

The system prompt was carefully designed to explicitly enforce that mathematical operations must be delegated to the calculator tool, preventing the model from attempting to infer numerical results on its own.


## Lessons Learned and Future Improvements
During the development of this challenge, I learned and reinforced important concepts related to LLMs and the use of pretrained models, particularly the importance of well-defined system prompts to prevent the model from ignoring tools and to guide it in correctly deciding when to delegate tasks to external tools. This helps reduce both hallucinations and improper tool usage.

For example, during the development I attempted to integrate a Wikipedia query tool in a conditional manner, so that it would only be used when the model identified the need for more comprehensive information. However, this made it clear that when working with pretrained models, controlling agent behavior solely through prompt engineering can be challenging, especially in scenarios that require more critical decisions regarding tool usage.

As future improvements, with additional development time, I would replace the CLI with a more user-friendly graphical interface, making the system more accessible. In addition, I would integrate a news or up-to-date information tool, enabling the assistant to respond to more recent events.
