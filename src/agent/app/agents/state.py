from typing import List, Optional, Dict
from typing_extensions import TypedDict, Annotated
from langchain_core.messages import AnyMessage
import operator


class AgentState(TypedDict):
    messages: Annotated[List[AnyMessage], operator.add]
    user_id: Optional[str]