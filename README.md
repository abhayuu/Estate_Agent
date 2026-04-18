# Real Estate AI Agent

A comprehensive AI-powered real estate analysis system built with LangGraph, LLMs, and machine learning. This agent provides property price predictions, market analysis, and investment recommendations for the Indian real estate market.

---

## Folder Structure

```
real-estate-ai-agent/
├── app/                        # Streamlit UI & Frontend Logic
│   └── main.py                 # Entry point for the UI
├── src/                        # Core AI Logic (Hidden from UI)
│   ├── agents/                 # LangGraph Definitions
│   │   ├── graph.py            # Workflow & State management
│   │   ├── nodes.py            # Individual AI reasoning steps
│   │   └── state.py            # Pydantic state definitions
│   ├── tools/                  # Function calling tools
│   │   ├── ml_model.py         # Wrapper for your joblib model
│   │   └── search_rag.py       # ChromaDB / RAG retrieval logic
│   └── utils/                  # Data cleaning & helpers
├── data/                       # Local Knowledge Base
│   ├── raw_reports/            # PDFs/Text for RAG (Indian market trends)
│   └── vector_store/           # Persisted ChromaDB/FAISS index
├── models/                     # ML Artifacts
│   ├── model.pkl               # Your trained XGBoost/RF model
│   └── encoder.pkl             # Label encoders or scalers
├── tests/                      # Testing the ML output accuracy
├── requirements.txt            # Dependencies
├── .env                        # API Keys (OpenAI/Gemini/Anthropic)
└── README.md                   # System Architecture & Documentation
```

---

## Component Details

### `app/` - Streamlit Interface
- **main.py**: Contains the Streamlit application that serves as the user-facing interface.
  - Handles user queries about properties
  - Displays predictions and recommendations
  - Manages session state for conversation history

### `src/agents/` - AI Workflow (LangGraph)
- **state.py**: Defines the shared state schema using Pydantic models
  - Tracks conversation context, property details, and agent decisions
  - Ensures type safety across the workflow
  
- **nodes.py**: Individual AI reasoning steps/nodes
  - Data validation and preprocessing
  - LLM-based reasoning and analysis
  - Tool execution handlers
  
- **graph.py**: Main workflow orchestration
  - Defines the DAG (Directed Acyclic Graph) connecting nodes
  - Implements decision logic (conditional edges)
  - Manages the overall agent flow

### `src/tools/` - Function Calling Integration
- **ml_model.py**: ML model wrapper for property price prediction
  - Loads trained XGBoost/Random Forest model from `models/model.pkl`
  - Handles input validation with Pydantic schemas
  - Returns formatted price predictions for agent consumption
  
- **search_rag.py**: RAG (Retrieval-Augmented Generation) system
  - Embeds market reports and trends into ChromaDB/FAISS
  - Retrieves relevant market context for the agent
  - Enhances LLM reasoning with domain knowledge

### `src/utils/` - Utilities & Helpers
- Data cleaning functions
- Feature engineering utilities
- Common helper functions

### `data/` - Knowledge Base
- **raw_reports/**: Original documents (PDFs, CSVs, text files)
  - Indian real estate market trends
  - Historical data and reports
  
- **vector_store/**: Persisted vector embeddings
  - ChromaDB or FAISS indices
  - Enables fast semantic search

### `models/` - ML Artifacts
- **model.pkl**: Serialized trained ML model (XGBoost/Random Forest)
- **encoder.pkl**: Feature encoders/scalers for data transformation

### `tests/` - Quality Assurance
- Unit tests for ML model accuracy
- Integration tests for agent workflow
- End-to-end testing

---

## Setup & Installation

### 1. Prerequisites
- Python 3.10+
- pip or conda

### 2. Install Dependencies
```bash
pip install -r requirements.txt
```

### 3. Environment Configuration
Create a `.env` file in the root directory:
```
OPENAI_API_KEY=your_openai_key_here
GEMINI_API_KEY=your_gemini_key_here
ANTHROPIC_API_KEY=your_anthropic_key_here
```

### 4. Prepare ML Model
- Place your trained model in `models/model.pkl`
- Place your encoder in `models/encoder.pkl`

### 5. Populate Knowledge Base
- Add Indian market reports/PDFs to `data/raw_reports/`
- Run RAG indexing to build vector store

---

## Running the Application

### Start the Streamlit UI
```bash
streamlit run app/main.py
```

The application will be available at `http://localhost:8501`

---

## Key Technologies

- **LangGraph**: Multi-agent workflow orchestration
- **LangChain**: LLM integration and tool calling
- **Streamlit**: Web interface for user interaction
- **ChromaDB/FAISS**: Vector database for RAG
- **Scikit-learn / XGBoost**: Machine learning models
- **Pydantic**: Data validation and schema definition

---

## Workflow Overview

1. **User Input** → Streamlit captures property details
2. **State Initialization** → Creates initial request state
3. **Graph Execution** → LangGraph orchestrates AI reasoning
4. **Tool Invocation** → ML model predicts price, RAG retrieves market context
5. **LLM Reasoning** → Agent synthesizes information
6. **Output** → Recommendations and insights returned to UI

---

## Development Notes

- Keep business logic in `src/agents/` and `src/tools/`, UI logic in `app/`
- All tool inputs should use Pydantic schemas for validation
- Vector store should be periodically updated with fresh market data
- Model retraining pipeline should be documented separately

---

## License

MIT License



We will use LangChain’s RecursiveCharacterTextSplitter. We'll set a chunk size of around 1000 characters with an overlap of 200. This ensures that context (like the city name mentioned at the start of a paragraph) carries over into the next chunk.

