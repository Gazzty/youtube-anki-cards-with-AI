import genanki

# Create a deck model
model_fields = ['Expression', 'Reading', 'Meaning', 'Notes']
model_test = genanki.Model(
	1182953384,	# This is a unique ID generated with python3 -c "import random; print(random.randrange(1 << 30, 1 << 31))"
	'Test model',
	fields=[{'name': field} for field in model_fields],
	templates=[
		{
      'name': '日本語 template',
      'qfmt': '<div class="center"><span style="font-family: irohamaru mikami; font-size: 50px;">{{Expression}}</span></div>',
      'afmt': '<div class="card-content center"><div class="center"><span style="font-family: irohamaru mikami; font-size: 50px;">{{Expression}}</span></div><hr id="answer" class="separator" /><span style="font-size: 50px;">{{furigana:Reading}}</span><hr id="answer" class="separator" /><div class="left"><span style="font-size: 30px;">{{furigana:Meaning}}</span></div><hr id="answer" class="separator" /><div class="left"><span style="font-size: 30px;">{{furigana:Notes}}</span></div><div class="card-tags-container"><div class="bottom">{{Tags}}</div></div></div>',
    },
	]
)

# Create a deck
deck_test = genanki.Deck(
	1716667060,
	'Deck test'
)

# Create a note
notes = [
	['Expression', 'Reading', 'Meaning', 'Notes'],
	['Expression', 'Reading', 'Meaning', 'Notes'],
	['Expression', 'Reading', 'Meaning', 'Notes'],
	['Expression', 'Reading', 'Meaning', 'Notes']
]

# Add note to deck
for note in notes:
	deck_test.add_note(genanki.Note(
		model=model_test,
		fields=note
	))


# Export deck
print('Creating deck...')
genanki.Package(deck_test).write_to_file('test_deck.apkg')
print('Deck created successfully!')