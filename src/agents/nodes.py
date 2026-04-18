from src.tools.ml_model import RealEstatePredictor
from src.tools.search_rag import market_researcher
from src.agents.state import AgentState

# Initialize the predictor
predictor = RealEstatePredictor()

def valuation_node(state: AgentState):
    """Triggers the XGBoost model to get the base market value."""
    print("--- 🤖 NODE: Valuation ---")
    data = state["property_input"]
    
    # Call the ML tool we verified
    price = predictor.predict_market_price_func(
        Property_Type=data['Property_Type'],
        BHK=data['BHK'],
        Furnished_Status=data['Furnished_Status'],
        Size_sqft=data['Size_in_SqFt'],
        Bathrooms=data['Bathrooms'],
        Public_Transport_Accessibility=data['Public_Transport_Accessibility'],
        Facing=data['Facing'],
        Security=data['Security'],
        City=data['City'],
        State=data['State']
    )
    
    return {"predicted_price": price, "current_step": "Valuation Complete"}

def research_node(state: AgentState):
    """Searches PDFs for trends and laws related to the property city."""
    print("--- 📚 NODE: Market Research ---")
    city = state["property_input"].get("City", "India")
    
    # Query the RAG tool for city-specific trends and RERA rules
    query = f"Real estate market trends and RERA legal guidelines for {city}"
    context = market_researcher.run(query)
    
    return {"market_context": [context], "current_step": "Research Complete"}