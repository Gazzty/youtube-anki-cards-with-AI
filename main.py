from create_deck import create_deck, add_notes_to_deck, export_deck

def main():
	notes = [
		['Expression', 'Reading', 'Meaning', 'Notes'],
		['Expression', 'Reading', 'Meaning', 'Notes'],
		['Expression', 'Reading', 'Meaning', 'Notes'],
		['Expression', 'Reading', 'Meaning', 'Notes']
	]

	deck = create_deck('Test')
	add_notes_to_deck(deck, notes)
	export_deck(deck)
	

if __name__ == '__main__':
	main()