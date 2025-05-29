from dotenv import load_dotenv
from pydantic_ai.agent import Agent
from pydantic_ai.models.gemini import GeminiModel

load_dotenv()

model = GeminiModel(model_name="gemini-2.0-flash")


# Emulate a tool function
def say_hello(name: str) -> str:
    """Greet to my good friend."""
    return f"Hello, my good friend {name}! -- From the agent-demo"


agent = Agent(
    model=model,
    system_prompt="You are an expert in Python programming.",
    tools=[say_hello],  # Add your tools here, generally a list of functions
    # history=history_messages,
)


def main():
    history_messages = []
    while True:
        user_input = input("Input: ")
        if user_input.lower() in ["exit", "quit"]:
            print("Exiting the agent.")
            break
        response = agent.run_sync(user_input, message_history=history_messages)
        history_messages = list(response.all_messages())
        print(response.output)


if __name__ == "__main__":
    main()
