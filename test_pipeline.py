from backend.agents.extraction_agent import ExtractionAgent
from backend.agents.concept_agent import ConceptAgent
from backend.agents.generation_agent import GenerationAgent
from backend.agents.validation_agent import ValidationAgent

from backend.services.csv_service import export_csv

extractor = ExtractionAgent()
concept_agent = ConceptAgent()
generation_agent = GenerationAgent()
validation_agent = ValidationAgent()

text = extractor.run("sample.pdf")

concepts = concept_agent.run(text)

flashcards = generation_agent.run(concepts)

validated_cards = validation_agent.run(flashcards)

file = export_csv(validated_cards)

print("Generated:", file)
print("Cards:", len(validated_cards))