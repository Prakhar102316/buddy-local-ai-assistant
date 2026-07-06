from voice.recorder import VoiceRecorder
from voice.transcriber import VoiceTranscriber

recorder = VoiceRecorder()

transcriber = VoiceTranscriber()

audio_path = recorder.record(duration=5)

print("\n🧠 Transcribing...\n")

text = transcriber.transcribe(audio_path)

print("Buddy heard:")

print(text)
