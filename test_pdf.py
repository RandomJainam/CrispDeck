from backend.agents.extraction_agent import ExtractionAgent

agent = ExtractionAgent()

text = agent.run("sample.pdf")

print(text[:2000])  