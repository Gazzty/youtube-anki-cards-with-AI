import os, json
from google import genai
from dotenv import load_dotenv

load_dotenv()
GEMINI_API_KEY = os.getenv('GEMINI_API_KEY')
client = genai.Client(api_key=GEMINI_API_KEY)

def get_context(lang):
	context = f"""
		I want you to act as an Anki flashcard generator from Japanese text.  
		I will provide you with a fragment of Japanese text, and your task is:  

		1. Select complete sentences or useful expressions from the text (not just single words), appropriate for a Japanese learner at the N4 level.  
		2. For each sentence, generate a card with these fields:  
			- Expression: the original sentence in Japanese.  
			- Reading: the sentence with furigana or hiragana if the kanji is difficult.  
			- Meaning: a natural translation into {lang}.  
			- Notes: a short explanation of grammar, context, or usage (in simple {lang}).  

		3. Return the result in the following structure:
			['Expression', 'Reading', 'Meaning', 'Notes']

		[
			["勉強する", "べんきょうする", "to study", "Verb 勉強する (study) in masu form."],
			["本", "ほん", "book", "Can also mean origin or main"],
			["大丈夫", "だいじょうぶ", "okay; fine", "Often used to reassure someone"]
		]

		DO NOT ADD THE JSON OR THE `

		Here is the text: 
	"""
	return context


def get_ai_anki(lang, text):
	context = get_context(lang)
	response = client.models.generate_content(
    	model="gemini-2.5-flash",
		contents=context + text
	)
	
	return json.loads(response.text)