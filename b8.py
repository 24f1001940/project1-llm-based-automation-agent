import os
import whisper

# Define output file
OUTPUT_FILE = "./data/audio_transcription.txt"

def run_task(audio_path: str):
    """Transcribes an audio file and saves the result to /data/audio_transcription.txt."""
    try:
        # Validate that audio path is within /data/
        if not audio_path.startswith("./data/"):
            return "❌ Access denied! Audio files must be inside /data/."

        # Check if the audio file exists
        if not os.path.exists(audio_path):
            return f"❌ Audio file not found: {audio_path}"

        # Load Whisper model
        model = whisper.load_model("base")

        # Transcribe audio
        result = model.transcribe(audio_path)

        # Save transcription
        with open(OUTPUT_FILE, "w", encoding="utf-8") as file:
            file.write(result["text"])

        return f"✅ Transcription completed and saved to {OUTPUT_FILE}"

    except Exception as e:
        return f"❌ Error processing audio file: {e}"

# Debugging (if running this script directly)
if __name__ == "__main__":
    path = input("Enter audio path (e.g., ./data/sample.mp3): ")
    print(run_task(path))
