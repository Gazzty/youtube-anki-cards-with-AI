import genanki, random, os, os.path

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

def json_to_notes(notes_json):
	notes = []
	for note in notes_json:
		current_note = []
		for field in note:
			current_note.append(field)
		notes.append(current_note)

	return notes

# Create a deck
def create_deck(name):
	deck = genanki.Deck(
		random.randrange(1 << 30, 1 << 31),
		name
	)

	return deck

# Add note to deck
def add_notes_to_deck(deck, notes):
	for note in notes:
		deck.add_note(genanki.Note(
			model=model_test,
			fields=note
		))


def export_deck(deck):
	print('Creating deck...')
	genanki.Package(deck).write_to_file('./decks/test_deck.apkg')
	print('Deck created successfully!')