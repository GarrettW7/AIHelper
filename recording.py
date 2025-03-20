import pyaudio
import wave
import threading

# Recording Parameters
FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 44100
CHUNK = 1024
OUTPUT_FILENAME = "output.wav"

# Global Variables
audio = pyaudio.PyAudio()
stream = None
frames = []
is_recording = False

def start_recording():
    """Start recording audio."""
    global is_recording, stream, frames
    if is_recording:
        return  # Prevent multiple recordings

    print("Recording started... Press 'Shift' to stop.")
    is_recording = True
    frames = []
    
    stream = audio.open(format=FORMAT, channels=CHANNELS, rate=RATE,
                        input=True, frames_per_buffer=CHUNK)

    def record():
        while is_recording:
            data = stream.read(CHUNK)
            frames.append(data)

    # Run in a separate thread to avoid blocking
    threading.Thread(target=record, daemon=True).start()
    # record()

def stop_recording():
    """Stop recording and save audio file."""
    global is_recording, stream
    if not is_recording:
        return
    
    is_recording = False
    stream.stop_stream()
    stream.close()
    
    # Save to a file
    with wave.open(OUTPUT_FILENAME, 'wb') as wf:
        wf.setnchannels(CHANNELS)
        wf.setsampwidth(audio.get_sample_size(FORMAT))
        wf.setframerate(RATE)
        wf.writeframes(b''.join(frames))

    print(f"Audio saved as {OUTPUT_FILENAME}")
    audio.terminate()
    stream.stop_stream()
    stream.close()
    audio.terminate()

def recording():
    # Restart PyAudio to avoid issues with multiple recordings
    restart_pyaudio()

    # Listen for key presses
    print("Press 'Enter' to start recording, 'Enter' to stop.")
    # thread = threading.Thread(target=start_recording, daemon=True)
    key =  input("Press 'Enter' to start!  " )
    while True:
        if key == '':
            break
        else:
            print("Press Enter to start recording.")
    # thread.start()
    start_recording()
    key = input("Press 'Enter' to stop!  ")
    while True:
        if key == '':
            break
        else:
            print("Press Enter to stop recording.")
    stop_recording()
    # print("Recording stopped.")
    # close the script
    # keyboard.unhook_all()
    return

def restart_pyaudio():
    global audio
    audio.terminate()  # Ensure previous instance is closed
    audio = pyaudio.PyAudio()  # Restart PyAudio
