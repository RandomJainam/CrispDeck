from backend.agents.extraction_agent import ExtractionAgent
from backend.agents.concept_agent import ConceptAgent

extractor = ExtractionAgent()
concept_agent = ConceptAgent()

text = extractor.run("sample.pdf")

concepts = concept_agent.run(text)

print(concepts)