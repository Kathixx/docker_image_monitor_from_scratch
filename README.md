# Docker Image Monitor
This repository builds the core components of a agentic docker image monitor from scratch using LangGraph. 
This code is based on the tutorial [Deep research agent with Langchain](https://academy.langchain.com/courses/deep-research-with-langgraph).

## Repository Structure
The 3 notebooks demonstrate different components.

```
docker_image_monitor/
├── notebooks/              
│   ├── 1_version_agent.ipynb     # AI agent to search for the latest version
│   ├── 2_research_agent.ipynb    # AI agent to research for changelogs
│   ├── 3_docker_monitor.ipynb    # Agent process
│   └── utils.py                  # Shared utilities for notebooks
├── src/docker_image_monitor/  # Generated source code 
│   ├── prompts.py
│   ├── research_agent.py
│   ├── state_version_research.py
│   ├── utils_research.py
│   ├── utils_version.py
│   └── version_agent.py
└── README.md              # Comprehensive documentation
```

## Quickstart

### Prerequisites
- Ensure **Node.js** and **npx* is installed
- Ensure you're using **Python 3.11** or later.
- Ensure **uv package manager** is installed.


### Installation

1. Install the package and dependencies (this automatically creates and manages the virtual environment):
```bash
uv sync
```

2. Create a `.env` file in the project root with your API keys:
```bash
# Create .env file
touch .env
```

Add your API keys to the `.env` file:
```env
# Required for agents with external search
TAVILY_API_KEY=your_tavily_api_key_here

# Required for model usage
OPENAI_API_KEY=your_openai_api_key_here
ANTHROPIC_API_KEY=your_anthropic_api_key_here
```

4. Run notebooks or code using uv:
```bash
# Run Jupyter notebooks directly
uv run jupyter notebook

# Or activate the virtual environment if preferred
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
jupyter notebook
```
