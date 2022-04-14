import genanki
from ..notion.models import FlashCard
from .anki_model import my_model

my_note = genanki.Note(model=my_model, fields=["Capital of Argentina", "Buenos Aires"])

second_note = genanki.Note(
    model=my_model, fields=["Capital of the United States", "Washington D.C."]
)

my_deck = genanki.Deck(2059400110, "Country Capitals")

my_deck.add_note(my_note)

my_deck.add_note(second_note)

genanki.Package(my_deck).write_to_file("output.apkg")
