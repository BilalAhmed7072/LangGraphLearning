from langgraph.graph import StateGraph , END, START
from typing import Dict, TypedDict, List
from IPython.display import display,Image

class AgentState(TypedDict):
    number1: int
    number2: int
    number3: int
    number4: int
    operation: str
    operation2: str
    finalnumber: int
    finalnumber2: int

def adder(state:AgentState)->AgentState:
    """ this will add the two numbers"""
    state['finalnumber']= state['number1']+state['number2']
    return state

def subtracter(state:AgentState)->AgentState:
    """ this will subtract the two numbers"""
    state['finalnumber'] = state['number1']-state['number2']
    return state

def decide_node(state:AgentState)->AgentState:
    """this will select the which node to implement the next"""
    if state['operation']== "+":
        return "addition_ooperation"
    elif state['operation']=="-":
        return "subtraction_ooperration"
    else:
        return "invalid"
    
def adder2(state:AgentState)->AgentState:
    """this will add the numbers"""
    state['finalnumber2']= state['number3']+ state['number4']
    return state

def subtracter2(state:AgentState)->AgentState:
    """ this will subtract the two numbers"""
    state['finalnumber2']= state['number3']-state['number4']
    return state

def decide2_node(state:AgentState)->AgentState:
    """ this also decide which node to be implemented """
    if state['operation2']== "+":
        return "addition_operation"
    elif state['operation2']=="-":
        return "subtraction_operation"
    else:
        return "invalid"

graph = StateGraph(AgentState)
graph.add_node("add1_node",adder)
graph.add_node("subtract1_node", subtracter)
graph.add_node("add2_node",adder2)
graph.add_node("subtract2_node",subtracter2)
graph.add_node("router1",lambda state:state)
graph.add_node("router2",lambda state:state)

graph.add_edge(START, "router1")
graph.add_conditional_edges(
    "router1",
    decide_node,
    {
        "addition_ooperation": "add1_node" ,
        "subtraction_ooperation": " subtract1_node"
    }
)
graph.add_edge("add1_node", "router2")
graph.add_edge("subtract1_node", "router2")
graph.add_conditional_edges(
    "router2",
    decide2_node,
    {
        "addition_operation":"add2_node",
        "subtraction_operation":"subtract2_node"
    }
)
graph.add_edge("add2_node",END)
graph.add_edge("subtract2_node",END)

app  = graph.compile()
try:
    img_byte = app.get_graph().draw_mermaid_png()
    display(Image(img_byte))
except Exception as e: 
    print("invalid ", e)


initial_state = AgentState(number1=10, number2= 20, number3= 30, number4=40,
                           operation="+", operation2="-", finalnumber=0, finalnumber2=0)

response = app.invoke(initial_state)

print(response)
