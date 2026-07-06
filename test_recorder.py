from voice.recorder import VoiceRecorder

recorder = VoiceRecorder()

audio_path = recorder.record(duration=5)

print("\nSaved to:")
print(audio_path)
