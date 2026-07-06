from voice.recorder import VoiceRecorder
from voice.transcriber import VoiceTranscriber
from voice.speaker import VoiceSpeaker


class VoiceManager:

    def __init__(self):

        self.recorder = VoiceRecorder()
        self.transcriber = VoiceTranscriber()
        self.speaker = VoiceSpeaker()

    def listen(self):

        print("Recording...")

        audio_path = self.recorder.record(duration=5)

        print(f"Audio saved: {audio_path}")

        print("Starting transcription...")

        text = self.transcriber.transcribe(audio_path)

        print(f"Transcribed text: {text}")

        return text