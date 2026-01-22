from langchain_ollama import ChatOllama
from langchain.agents import create_agent
from langgraph.checkpoint.memory import InMemorySaver
from .tools import available_tools


def build_agent():
    """Establishes the agent parameters and returns it."""
    
    llm = ChatOllama(model="llama3.1:8b", temperature=0)

    system_prompt = """
    You are a helpful and intelligent assistant
    Analyze the user's question and follow these rules:
        1. If the user wants the solution to some mathematical operation: use the 'calculator' tool.
        2. If it's a simple GENERAL KNOWLEDGE question or just a casual conversation: answer directly, based on your knowledge.

    Examples:
    User: "What is the capital of France?"
    You: "Paris." (NO CALLING TOOLS)

    User: "What is 10 + 10?"
    You: (CALL TOOL 'calculator')
    """

    memory = InMemorySaver()
    
    return create_agent(
        model=llm,
        tools=available_tools,
        system_prompt=system_prompt,
        checkpointer=memory
    )