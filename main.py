from langchain_core.messages import HumanMessage
from app.agent import build_agent

def start_chat():
    agent_executor = build_agent()
    config = {"configurable": {"thread_id": "sessao_1"}}

    print("Hello, I'm your interactive AI Assistant! Type 'exit' to quit or type your question.")
    
    while True:
        try:
            user_input = input("\nUser: ")
            
            if user_input.lower() in ["sair", "exit", "quit"]:
                print("Ending chat. See you later!")
                break
            
            print("Assistant: Thinking...")
            response = agent_executor.invoke(
                {"messages": [("user", user_input)]}, 
                config=config
            )

            print(f"Assistant: {response['messages'][-1].content}")
            
        except Exception as e:
            print(f"Error: {e}")



if __name__ == "__main__":
    start_chat()