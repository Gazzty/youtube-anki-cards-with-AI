from youtube_transcript_api import YouTubeTranscriptApi

def get_transcript(url):
	yt_api = YouTubeTranscriptApi()
	fetch_transcript = yt_api.fetch("yYNWwH2GlB0", languages=["ja"])

	sentenses = []
	for snippet in fetch_transcript:
		sentenses.append(snippet.text)

	return sentenses