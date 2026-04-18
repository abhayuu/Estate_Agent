import sys
import os

# Add project root to Python path so we can import src modules
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.agents.nodes import valuation_node, research_node

def test_node_flow():
    print("🚀 Testing Node Transitions...")
    
    # Initial State
    initial_state = {
        "property_input": {
            'Property_Type': 'Apartment', 'BHK': 3, 'Furnished_Status': 'Semi-furnished',
            'Size_in_SqFt': 1800, 'Bathrooms': 3, 'Public_Transport_Accessibility': 'High',
            'Facing': 'East', 'Security': 'Yes', 'City': 'Mumbai', 'State': 'Maharashtra'
        },
        "market_context": []
    }

    # 1. Test Valuation Node
    val_result = valuation_node(initial_state)
    print(f"✅ Valuation Node Result: {val_result['predicted_price']} Lakhs")

    # 2. Test Research Node (Pass the city from state)
    res_result = research_node(initial_state)
    print(f"✅ Research Node found context (chars): {len(res_result['market_context'][0])}")

if __name__ == "__main__":
    test_node_flow()