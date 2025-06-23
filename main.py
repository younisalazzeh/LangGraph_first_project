from dotenv import load_dotenv
from typing import Annotated, Literal
from langgraph.graph import StateGraph, START, END
from langgraph.graph.message import add_messages
from langchain_openai import ChatOpenAI
from pydantic import BaseModel, Field
from typing_extensions import TypedDict

# Load environment variables from .env
load_dotenv()

# Initialize OpenAI chat model
llm = ChatOpenAI(
    model="gpt-4o",  # You can switch to "gpt-3.5-turbo" if needed
    temperature=0.7
)

# Schema for message classification
class MessageClassifier(BaseModel):
    message_type: Literal["emotional", "logical"] = Field(
        ...,
        description="Classify if the message requires an emotional (therapist) or logical response."
    )

# State object used in LangGraph
class State(TypedDict):
    messages: Annotated[list, add_messages]
    message_type: str | None

# Node: classify the message type
def classify_message(state: State):
    last_message = state["messages"][-1]
    classifier_llm = llm.with_structured_output(MessageClassifier)

    result = classifier_llm.invoke([
        {
            "role": "system",
            "content": """Classify the user message as either:
            - 'emotional': if it asks for emotional support, therapy, deals with feelings, or personal problems
            - 'logical': if it asks for facts, information, logical analysis, or practical solutions."""
        },
        {
            "role": "user",
            "content": last_message.content
        }
    ])
    return {"message_type": result.message_type}

# Node: route the message to the right agent
def router(state: State):
    message_type = state.get("message_type", "logical")
    return {"next": "therapist" if message_type == "emotional" else "logical"}

# Node: handle emotional messages
def therapist_agent(state: State):
    last_message = state["messages"][-1]

    messages = [
        {"role": "system",
         "content": """You are a compassionate therapist. Focus on the emotional aspects of the user's message.
         Show empathy, validate their feelings, and help them process their emotions.
         Ask thoughtful questions to help them explore their feelings more deeply.
         Avoid giving logical solutions unless explicitly asked."""},
        {"role": "user", "content": last_message.content}
    ]
    reply = llm.invoke(messages)
    return {"messages": [{"role": "assistant", "content": reply.content}]}

# Node: handle logical messages
def logical_agent(state: State):
    last_message = state["messages"][-1]

    messages = [
        {"role": "system",
         "content": """You are a purely logical assistant. Focus only on facts and information.
         Provide clear, concise answers based on logic and evidence.
         Do not address emotions or provide emotional support."""},
        {"role": "user", "content": last_message.content}
    ]
    reply = llm.invoke(messages)
    return {"messages": [{"role": "assistant", "content": reply.content}]}

# Build the graph
graph_builder = StateGraph(State)

graph_builder.add_node("classifier", classify_message)
graph_builder.add_node("router", router)
graph_builder.add_node("therapist", therapist_agent)
graph_builder.add_node("logical", logical_agent)

graph_builder.add_edge(START, "classifier")
graph_builder.add_edge("classifier", "router")
graph_builder.add_conditional_edges(
    "router",
    lambda state: state.get("next"),
    {
        "therapist": "therapist",
        "logical": "logical"
    }
)
graph_builder.add_edge("therapist", END)
graph_builder.add_edge("logical", END)

graph = graph_builder.compile()

# Chat loop
def run_chatbot():
    state = {"messages": [], "message_type": None}

    while True:
        user_input = input("Message: ")
        if user_input.lower() == "exit":
            print("Bye!")
            break

        state["messages"] += [{"role": "user", "content": user_input}]
        state = graph.invoke(state)

        if state.get("messages"):
            print(f"Assistant: {state['messages'][-1].content}")

if __name__ == "__main__":
    run_chatbot()
