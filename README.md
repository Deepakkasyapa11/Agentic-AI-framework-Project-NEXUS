# Nexus-Agent Hub 

Nexus-Agent Hub is a modular framework for building and deploying intelligent agents. It decouples core logic, tool execution, and knowledge retrieval into a unified system, moving away from monolithic script architectures.

<img width="363" height="255" alt="crewai" src="https://github.com/user-attachments/assets/4fb4663e-a899-42d4-9599-772ba74fdf4a" />

# Architecture
- **Core:** Centralized prompt management and persona-driven templates.
- **Agents:** Specialized tools (e.g., Weather API integration) for real-world interaction.
- **Knowledge Base:** Vector-store implementation for RAG (Retrieval-Augmented Generation) using PDF indexing.
- **API:** FastAPI gateway for serving agentic workflows as a microservice.

# Key Features
- **Multi-Tool Orchestration:** Dynamically switches between internal knowledge (RAG) and external tools (APIs).
- **Advanced Prompt Engineering:** Implements few-shot, persona, and Chain-of-Thought (CoT) methodologies.
- **Local & Cloud LLM Support:** Optimized for Ollama (local) and Gemini/HuggingFace (cloud) integrations.

# Setup & Installation
 Clone the repository:

