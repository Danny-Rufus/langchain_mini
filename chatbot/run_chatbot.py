import sys
from rich.console import Console
from dotenv import load_dotenv
from chatbot import ChatBot

load_dotenv()

console = Console()


def main():
    console.print("Starting simple chatbot. Type 'exit' or 'quit' to stop.")
    bot = ChatBot()

    if not bot.use_openai:
        console.print(
            "[yellow]No OPENAI_API_KEY detected in environment. Running local fallback.[/yellow]"
        )

    while True:
        try:
            message = console.input("[bold green]You> [/bold green]")
        except (KeyboardInterrupt, EOFError):
            console.print("\nExiting.")
            sys.exit(0)

        if message.strip().lower() in ("exit", "quit"):
            console.print("Goodbye.")
            break

        reply = bot.send_message(message)
        console.print(f"[bold cyan]Bot>[/bold cyan] {reply}\n")


if __name__ == "__main__":
    main()
