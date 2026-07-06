import sounddevice as sd
from scipy.io.wavfile import write
from pathlib import Path
import tempfile


class VoiceRecorder:

    def __init__(self, sample_rate=16000):

        self.sample_rate = sample_rate

    def record(self, duration=5):

        print("🎤 Listening...")

        recording = sd.rec(
            int(duration * self.sample_rate),
            samplerate=self.sample_rate,
            channels=1,
            dtype="int16",
        )

        sd.wait()

        print("✅ Recording complete.")

        temp_dir = Path(tempfile.gettempdir())

        output_file = temp_dir / "buddy_recording.wav"

        write(output_file, self.sample_rate, recording)

        return str(output_file)