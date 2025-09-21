import genanki

# Create a deck model
model_test = genanki.Model(
	1182953384,	# This is a unique ID generated with python3 -c "import random; print(random.randrange(1 << 30, 1 << 31))"
	'Test model',
	fields=[
		{'name': 'Question'},
		{'name': 'Answer'}
	],
	templates=[
		{
      'name': 'Card 1',
      'qfmt': '{{Question}}',
      'afmt': '{{FrontSide}}<hr id="answer">{{Answer}}',
    },
	]
)

# Create a note
note_test = genanki.Note(
	model=model_test,
	fields=['これ質問',
		 	'これ答え']
)

# Create a deck
deck_test = genanki.Deck(
	1716667060,
	'Deck test'
)

# Add note to deck
deck_test.add_note(note_test)

# Export deck
genanki.Package(deck_test).write_to_file('test_deck.apkg')
print("Anki deck 'my_awesome_deck.apkg' created successfully!")