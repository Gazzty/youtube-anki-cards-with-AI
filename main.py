import json
from create_deck import create_deck, add_notes_to_deck, export_deck, json_to_notes
from send_video_ai import get_ai_anki
from get_text_youtube import get_transcript

# https://www.youtube.com/watch?v=duZfbMbpY9g&list=PL56n09cSLKei30pFhk7Y4BVl31lE0QA7d&index=2

test_mode = False

def main():
	if test_mode:
		video_url = "https://www.youtube.com/watch?v=duZfbMbpY9g&list=PL56n09cSLKei30pFhk7Y4BVl31lE0QA7d&index=2"
		lang = "spanish"
		deck_name = "Hana podcast"
	else:
		video_url = input("Input video URL you wigh to get anki cards from: ")
		lang = input("Input the translation language: ")
		deck_name = input("Input the deck name you want: ")

	transcript = " ".join(map(str, get_transcript(video_url))) # This is to get a single string for all the transcript
	print("Get transcript from youtube -> OK!")

	print("Sending transcript to AI, please wait...")
	notes_raw = get_ai_anki(lang, transcript)
	notes = []
	for note in notes_raw:
		notes.append(note)

	deck = create_deck(deck_name)
	add_notes_to_deck(deck, notes)
	export_deck(deck, deck_name)

if __name__ == '__main__':
	main()