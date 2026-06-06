from backend.agents.extraction_agent import ExtractionAgent
from backend.agents.concept_agent import ConceptAgent
from backend.agents.generation_agent import GenerationAgent
from backend.agents.validation_agent import ValidationAgent

from backend.services.apkg_service import create_apkg

extractor = ExtractionAgent()
concept_agent = ConceptAgent()
generation_agent = GenerationAgent()
validation_agent = ValidationAgent()

text = extractor.run("sample.pdf")

concepts = concept_agent.run(text)

flashcards = generation_agent.run(concepts)

cards = validation_agent.run(flashcards)

output = create_apkg(cards)

print("Generated:", output)
print("Cards:", len(cards))