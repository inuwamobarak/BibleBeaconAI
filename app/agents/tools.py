from langchain.tools import tool

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
    Returns only a list of dictionaries formatted for API consumption.
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