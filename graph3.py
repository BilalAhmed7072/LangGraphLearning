from langgraph.graph import StateGraph
from IPython.display import Image , display
from typing import Dict, TypedDict, List 

class AgentState(TypedDict):
    name: str
    age: str
    result: str

def first_node(state: AgentState)->AgentState:
    """this is our first node of the graph"""
    state['result']= f"hi {state['name']}"
    return state

def second_node(state:AgentState)->AgentState:
    """this is our second node of the graph"""
    state['result']= state['name']+ f" you are {state['age']} years old"
    return state

graph = StateGraph(AgentState)
graph.add_node("first node", first_node)
graph.add_node("second node", second_node)
graph.set_entry_point("first node")
graph.add_edge("first node", "second node")
graph.set_finish_point("second node")

app = graph.compile()

try:
    img_byte = app.get_graph().draw_mermaid_png()
    display(Image(img_byte))

except Exception as e:
    print("no visualization")


input={"name":"Bilal", "age":"twenty two"}
result = app.invoke()
print(result)
