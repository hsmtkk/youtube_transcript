import sys

import youtube_transcript_api

if len(sys.argv) < 2:
    print("Usage: python youtube_transcript.py <video_id>")
    sys.exit(1)

video_id = sys.argv[1]
ytt_api = youtube_transcript_api.YouTubeTranscriptApi()
transcript = ytt_api.fetch(video_id, languages=["ja"])

for snippet in transcript:
    print(snippet.text)
