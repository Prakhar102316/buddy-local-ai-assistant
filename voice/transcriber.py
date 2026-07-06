from faster_whisper import WhisperModel


class VoiceTranscriber:

    def __init__(self, model_size="base"):

        print("🧠 Loading Faster-Whisper model...")

        self.model = WhisperModel(
            model_size,
            device="cpu",
            compute_type="int8"
        )

        print("✅ Whisper loaded!")

    def transcribe(self, audio_path):

        segments, info = self.model.transcribe(audio_path)

        text = ""

        for segment in segments:
            text += segment.text

        return text.strip()