from youtube_transcript_api import YouTubeTranscriptApi
import re

def get_transcript(url):
	yt_api = YouTubeTranscriptApi()
	fetch_transcript = yt_api.fetch(get_youtube_id(url), languages=["ja"])

	sentenses = []
	for snippet in fetch_transcript:
		sentenses.append(snippet.text)

	return sentenses

def get_youtube_id(url):
	id = re.search('v=([^&]+)', url)
	if id:
		return id.group(1)
	else:
		raise Exception("Error: could not find video ID from the URL you provided.")
		