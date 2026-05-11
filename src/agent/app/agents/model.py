from langchain_groq import ChatGroq
from dotenv import load_dotenv
import os

from tools.registry import tools
load_dotenv()

llm = ChatGroq(model="openai/gpt-oss-20b")


tools_by_name = {tool.name: tool for tool in tools}

llm_with_tools = llm.bind_tools(tools) 