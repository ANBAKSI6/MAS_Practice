"""
Confirmation Agent: Wires the confirmation agent node into a LangGraph StateGraph. This graph will be used to confirm
appointment details with the user before finalizing the booking.
"""
from langgraph.graph import StateGraph, MessagesState, START
from langgraph.prebuilt import ToolNode, tools_condition
from agents.confirmation_agent import create_confirmation_node
from tools.mcp_tools import get_gmail_tools, get_mcp_client

# async def build_confirmation_graph():
#     """Build and return the confirmation graph with MCP Gmail tool."""
#     client = get_mcp_client()
#     gmail_tools = await get_gmail_tools(client)

#     if not gmail_tools:
#         raise RuntimeError("No Gmail tools found. Is Composio MCP server running?")

#     confirmation_node, gmail_tool = create_confirmation_node(gmail_tools[0])

#     builder = StateGraph(MessagesState)
#     builder.add_node("confirmation_agent", confirmation_node)
#     builder.add_node("gmail", ToolNode(gmail_tools))

#     builder.add_edge(START, "confirmation_agent")
#     builder.add_conditional_edges("confirmation_agent", tools_condition)
#     builder.add_edge("gmail", "confirmation_agent")

#     return builder.compile(), client

# async def build_confirmation_graph():
#     """Build and return the confirmation graph with MCP Gmail tool."""
#     client = get_mcp_client()
#     gmail_tools = await get_gmail_tools(client)

#     if not gmail_tools:
#         raise RuntimeError("No Gmail tools found. Is Composio MCP server running?")

#     confirmation_node, tools = create_confirmation_node(gmail_tools)

#     builder = StateGraph(MessagesState)
#     builder.add_node("confirmation_agent", confirmation_node)
#     builder.add_node("gmail", ToolNode(tools))

#     builder.add_edge(START, "confirmation_agent")
#     builder.add_conditional_edges("confirmation_agent", tools_condition)
#     builder.add_edge("gmail", "confirmation_agent")

#     return builder.compile(), client
async def build_confirmation_graph():
    """Build and return the confirmation graph with MCP Gmail tool."""
    client = get_mcp_client()
    gmail_tools = await get_gmail_tools(client)

    if not gmail_tools:
        raise RuntimeError("No Gmail tools found. Is Composio MCP server running?")

    confirmation_node, tools = create_confirmation_node(gmail_tools)

    builder = StateGraph(MessagesState)
    builder.add_node("confirmation_agent", confirmation_node)
    builder.add_node("tools", ToolNode(tools))   # ✅ FIXED

    builder.add_edge(START, "confirmation_agent")
    builder.add_conditional_edges("confirmation_agent", tools_condition)
    builder.add_edge("tools", "confirmation_agent")

    return builder.compile(), client