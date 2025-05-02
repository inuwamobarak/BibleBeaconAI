import uuid
from dotenv import load_dotenv
from langchain_core.messages import HumanMessage
from langchain_openai import ChatOpenAI
from langgraph.checkpoint.memory import MemorySaver
from langgraph.prebuilt import create_react_agent
from langchain.tools import tool

load_dotenv()

# Initialize memory and the model
memory = MemorySaver()
model = ChatOpenAI(model="gpt-4o-mini", temperature=0.7)

@tool
def say_hello(name: str) -> str:
    """Greets a person by name."""
    return f"Hello, {name}!"

@tool
def get_user_age(name: str) -> str:
    """Use this tool to find the user's age."""
    if "bob" in name.lower():
        return "42 years old"
    return "41 years old"

@tool
def suggest_bible_verses(topic: str) -> list:
    """
    Suggests relevant Bible verses based on a topic or text input.
    Returns a list of dictionaries formatted for API consumption.
    """
    # In a real app, this could call a search service.
    # Here's a hardcoded example for demonstration:
    if "Jesus" in topic and "son of God" in topic:
        return [
            {
                "translation": "YLT",
                "book": 19,  # Psalms
                "chapter": 145,
                "verses": [14, 15, 16]
            },
            {
                "translation": "KJV",
                "book": 19,  # Psalms
                "chapter": 91,
                "verses": [1, 2, 3]
            }
        ]
    return [
        {
            "translation": "KJV",
            "book": 43,  # John
            "chapter": 3,
            "verses": [16]
        }
    ]


# Create a react agent with the model, tools, and memory
app = create_react_agent(
    model,
    tools=[say_hello, get_user_age, suggest_bible_verses],
    checkpointer=memory,
)

# The thread id is a unique key that identifies this conversation.
thread_id = uuid.uuid4()
config = {"configurable": {"thread_id": thread_id}}

# Send an initial message asking the AI about the user's age
input_message = HumanMessage(content="Say hello to Benjamin")
for event in app.stream({"messages": [input_message]}, config, stream_mode="values"):
    event["messages"][-1].pretty_print()

# Ask the AI if it remembers the user's name
input_message = HumanMessage(content="do you remember my name?")
for event in app.stream({"messages": [input_message]}, config, stream_mode="values"):
    event["messages"][-1].pretty_print()