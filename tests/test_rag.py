import sys
import os

# Add project root to Python path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.tools.search_rag import market_researcher

def verify_system():
    print("🔍 Testing Local RAG Retrieval...")
    
    # Test 1: Market Trends
    query = "What is the residential market update for Bengaluru in 2024?"
    print(f"\nQuery: {query}")
    result = market_researcher.run(query)
    print(f"Result Preview: {result[:300]}...")

    # Test 2: Legal/RERA
    query = "What does RERA say about project registration?"
    print(f"\nQuery: {query}")
    result = market_researcher.run(query)
    print(f"Result Preview: {result[:300]}...")

if __name__ == "__main__":
    verify_system()