from langgraph.graph import StateGraph
from typing import Dict, TypedDict, List
from IPython.display import display, Image 

class AgentState(TypedDict):
    values: list[int]
    name: str
    result: str

def process_data(state:AgentState)->AgentState:
    """ process the data of multiple inout"""
    state['result'] = f"you are {state['name']} and your sum = {sum(state['values'])}"
    return state

graph = StateGraph(AgentState)
graph.add_node("processor",process_data)
graph.set_entry_point("processor")
graph.set_finish_point("processor")

app = graph.compile()
try:
    img_byte = app.get_graph().draw_mermaid_png()
    display(Image(img_byte))
except Exception as e:
    print("visualization is disabled", e)
input_value = {"values":[1,2,2,4], "name":"Bilal"}
result = app.invoke(input_value)
print(result)