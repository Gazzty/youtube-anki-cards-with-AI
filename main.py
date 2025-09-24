import json
from create_deck import create_deck, add_notes_to_deck, export_deck, json_to_notes
from send_video_ai import get_ai_anki

test_text = """
昨日友達と公園でサッカーをしました。  
とても楽しかったです。  
そのあと、一緒にレストランへ行ってカレーを食べました。
"""

def main():
	video_url = input("Input video URL you wigh to get anki cards from: ")
	
	notes_raw = get_ai_anki('spanish', test_text)
	notes = []
	for note in notes_raw:
		print(note)
		notes.append(note)

	deck = create_deck('Test')
	add_notes_to_deck(deck, notes)
	export_deck(deck)

if __name__ == '__main__':
	main()