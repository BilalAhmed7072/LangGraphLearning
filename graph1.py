from typing import Dict, TypedDict
from langgraph.graph import StateGraph

class AgentState(TypedDict):
    message: str


def greeting_node(state:AgentState)->AgentState:
    """say greeting to the user in polite manner"""
    state['message'] = "hey" + state['message'] + "how are you?"
    return state


graph = StateGraph(AgentState)
graph.add_node("greeter",greeting_node)
graph.set_entry_point("greeter")
graph.set_finish_point("greeter")

app =  graph.compile()

from IPython.display import Image, display
display(Image(app.get_graph().draw_mermaid_png()))

result = app.invoke({'message':'bob'})
print(result)