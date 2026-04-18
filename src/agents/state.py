from typing import TypedDict, Annotated, List, Optional
import operator

class AgentState(TypedDict):
    # Raw user inputs (BHK, City, etc.)
    property_input: dict
    
    # Data from your XGBoost model
    predicted_price: Optional[float]
    
    # Knowledge retrieved from your PDFs (RERA, Market Reports)
    market_context: Annotated[List[str], operator.add]
    
    # The final investment reasoning and report
    final_advisory: Optional[str]
    
    # To track which node is currently active
    current_step: str