import genanki
import random

def create_apkg(cards):

    model = genanki.Model(
        random.randrange(1 << 30, 1 << 31),

        'CrispDeck Model',

        fields=[
            {'name': 'Question'},
            {'name': 'Answer'}
        ],

        templates=[
            {
                'name': 'Card 1',
                'qfmt': '{{Question}}',
                'afmt': '{{FrontSide}}<hr>{{Answer}}'
            }
        ]
    )

    deck = genanki.Deck(
        random.randrange(1 << 30, 1 << 31),
        'CrispDeck Generated Deck'
    )

    for card in cards:

        note = genanki.Note(
            model=model,
            fields=[
                card["question"],
                card["answer"]
            ]
        )

        deck.add_note(note)

    output_file = "crispdeck_output.apkg"

    genanki.Package(deck).write_to_file(output_file)

    return output_file