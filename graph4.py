from langgraph.graph import StateGraph , START, END
from typing import Dict, TypedDict , List
from IPython.display import Image , display

class AgentState(TypedDict):
    number1: int
    number2: int
    finalNumber: int
    operation: str

def adder(state:AgentState)->AgentState:
    """ this is addition node of the graph and it will add the both number"""
    state['finalNumber']= state['number1']+state['number2']
    return state

def subtracter(state:AgentState)-> AgentState:
    """this node subtract the the both numbers"""
    state['finalNumber']= state['number1']-state['number2']
    return state

def decide_next_node(state:AgentState)->AgentState:
    """ this node will decide what will be the next node implemented"""
    if state['operation']=="+":
        return "addition operation"
    elif state['operation']=="-":
        return "subtraction operation"
    else:
        print("invalid operation")
        return "invalid"

graph = StateGraph(AgentState)
graph.add_node("add_node", adder)
graph.add_node("subtract_node",subtracter)
graph.add_node("router",lambda state:state)

graph.add_edge(START,"router")
graph.add_conditional_edges(
    "router",
    decide_next_node,
    {
        "addition operation": "add_node",
        "subtraction operation": "subtract_node"
    }
)
graph.add_edge("add_node",END)
graph.add_edge("subtract_node",END)

app = graph.compile()
try:
    img_byte = app.get_graph().draw_mermaid_png()
    display(Image(img_byte))
except Exception as e:
    print("not available visualization", e)

user_input = {"number1":30, "number2":20,"operation":"+"}
response = app.invoke(user_input)
print(response)