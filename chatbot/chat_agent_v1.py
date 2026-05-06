from langchain.agents import create_agent
from dotenv import load_dotenv
from rich.console import Console

load_dotenv()
console = Console()


def main():
    chat_history = []
    console.print("Starting simple chatbot. Type 'exit' or 'quit' to stop.")
    agent = create_agent(
        model="openai:gpt-5.2",
        tools=[],
        system_prompt="You are a helpful chat assistant. Be clear, concise and polite. Understand the user's intent and stay professional and safe",
    )

    while True:
        user_input = input("You ".strip())
        console.print("\n")
        if user_input.lower() in ["exit", "quit"]:
            console.print("Assistant: Goodbye 👋")
            break

        message = chat_history + [{"role": "user", "content": user_input}]
        result = agent.invoke({"messages": message})

        # extract reply
        reply = result["messages"][-1].content
        console.print(f"Assistant: {reply}\n")
        console.print("_" * 60)

        # update chat history
        chat_history.append({"role": "user", "content": user_input})
        chat_history.append({"role": "assistant", "content": reply})
    # result = agent.invoke(
    #     {
    #         "messages": [
    #             {"role": "user", "content": "Explain machine learning in detail"}
    #         ]
    #     }
    # )
    # pprint.pprint(result["messages"][1].content)


if __name__ == "__main__":
    main()
