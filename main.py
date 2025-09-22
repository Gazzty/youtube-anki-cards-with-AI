from create_deck import create_deck, add_notes_to_deck, export_deck, json_to_notes
from send_video_ai import get_ai_anki

test_text = """
昨日友達と公園でサッカーをしました。  
とても楽しかったです。  
そのあと、一緒にレストランへ行ってカレーを食べました。
"""

def main():
	notes_json = get_ai_anki('spanish', test_text)
	notes = json_to_notes(notes_json)

	deck = create_deck('Test')
	add_notes_to_deck(deck, notes)
	export_deck(deck)

if __name__ == '__main__':
	main()