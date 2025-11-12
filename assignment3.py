from langgraph.graph import StateGraph
from IPython.display import Image , display
from typing import Dict , List , TypedDict


class AgentState(TypedDict):
    name: str
    age: str
    skills: list
    final_result: str


def first_node(state:AgentState)->AgentState:
    """  this is the first node """
    state['final_result']= f"hi i am {state['name']}"
    return state

def second_node(state:AgentState)->AgentState:
    """ this is the second node """
    state['final_result'] = state['final_result'] + f"you are {state['age']} years old."
    return state

def third_node(state:AgentState)->AgentState:
    """this is the third node of the graph"""
    state['final_result']= state['final_result']+ f" you have skills : {",".join(state['skills'])}"
    return state 

graph = StateGraph(AgentState)
graph.add_node("first node", first_node)
graph.add_node("second node", second_node)
graph.add_node("third node", third_node)
graph.set_entry_point("first node")
graph.add_edge("first node", "second node")
graph.add_edge("second node","third node")
graph.set_finish_point("third node")

app = graph.compile()
try:
    img_byte = app.get_graph().draw_mermaid_png()
    display(Image(img_byte))
except Exception as e:
    print("invalid visyualization")


input= {"name":"Bilal","age":"thirty","skills":["python","ML","langgraph"]}
response = app.invoke(input)
print(response)