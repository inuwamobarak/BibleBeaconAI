import json
import re
import uuid
from app.services.http_client import bolls_life_client
from dotenv import load_dotenv
from langchain_core.messages import HumanMessage
from langchain_core.tools import tool
from langchain_openai import ChatOpenAI
from langgraph.checkpoint.memory import MemorySaver
from langgraph.prebuilt import create_react_agent
from .tools import say_hello, get_user_age, suggest_bible_verses
from langchain_core.messages import AIMessage, ToolMessage, HumanMessage

load_dotenv()

# Initialize memory and the model
memory = MemorySaver()
model = ChatOpenAI(model="gpt-4o-mini", temperature=0.7)

# Create a react agent with the model, tools, and memory
app = create_react_agent(
    model,
    tools=[say_hello, get_user_age, suggest_bible_verses],
    checkpointer=memory,
)

# The thread id is a unique key that identifies this conversation.
thread_id = uuid.uuid4()
config = {"configurable": {"thread_id": thread_id}}

class BibleAgent():
    # Ask the Bible agent about a theological concept
    messages = []
    def human_message(self, content):
        input_message = HumanMessage(content=content)
        
        responses = []
        
        for event in app.stream({"messages": [input_message]}, config, stream_mode="values"):
            message = event["messages"][-1]
            message.pretty_print()
            
            if isinstance(message, ToolMessage):
                responses.append({
                    "type": "tool",
                    "name": message.name,
                    "content": json.loads(message.content) if message.content else None
                })

        bible_data = bolls_life_client(responses[0]['content'])
        bible_data = re.sub(r'<S>\d+</S>', '', bible_data[0][0]['text']).strip()
        
        return {"responses": responses, "bible_data": bible_data}