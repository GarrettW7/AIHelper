import whisper
import subprocess
import warnings

# Suppress the FP16 warning
warnings.filterwarnings("ignore", message="FP16 is not supported on CPU; using FP32 instead")

def translateAudio(inputFile):
    model = whisper.load_model("base")
    result = model.transcribe(inputFile)
    print(result["text"])
    return result["text"]

