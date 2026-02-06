import os
from dotenv import load_dotenv
from agents.weather_tool import WeatherAgent
from knowledge_base.vector_store import RAGManager
from core.prompt_templates import get_persona

load_dotenv()

class NexusOrchestrator:
    def __init__(self):
        self.rag = RAGManager(doc_path="data/docs/sample.pdf")
        self.weather = WeatherAgent()
        self.persona = get_persona("expert_assistant")

    def handle_query(self, query: str):
        # Professional logic: Route the query
        if "weather" in query.lower():
            return self.weather.run(query)
        elif "document" in query.lower() or "pdf" in query.lower():
            return self.rag.query(query)
        else:
            return "General LLM processing with persona..."

if __name__ == "__main__":
    nexus = NexusOrchestrator()
    print(nexus.handle_query("What does the document say about nodejs?"))