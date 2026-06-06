from backend.agents.extraction_agent import ExtractionAgent
from backend.agents.concept_agent import ConceptAgent
from backend.agents.generation_agent import GenerationAgent

extractor = ExtractionAgent()
concept_agent = ConceptAgent()
generation_agent = GenerationAgent()

text = extractor.run("sample.pdf")

concepts = concept_agent.run(text)

flashcards = generation_agent.run(concepts)

print(flashcards)