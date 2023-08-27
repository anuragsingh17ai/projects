# Import libraries
import numpy as np
import librosa
import soundfile as sf
import random

# Define parameters
sample_rate = 22050 # Sampling rate in Hz
duration = 30 # Duration of the song in seconds
n_mels = 128 # Number of mel-frequency bins
n_fft = 2048 # Length of the FFT window
hop_length = 512 # Number of samples between successive frames
fmin = 0 # Minimum frequency in Hz
fmax = sample_rate / 2 # Maximum frequency in Hz

# Define a function to generate a random melody
def generate_melody():
    # Define the notes and their frequencies in Hz
    notes = ["C4", "D4", "E4", "F4", "G4", "A4", "B4", "C5"]
    freqs = [261.63, 293.66, 329.63, 349.23, 392.00, 440.00, 493.88, 523.25]

    # Define the duration of each note in seconds
    durations = [0.25, 0.5, 1]

    # Initialize an empty list to store the melody
    melody = []

    # Generate a random number of notes between 10 and 20
    n_notes = random.randint(10, 20)

    # Loop over the number of notes
    for i in range(n_notes):
        # Choose a random note and its frequency
        note = random.choice(notes)
        freq = freqs[notes.index(note)]

        # Choose a random duration for the note
        duration = random.choice(durations)

        # Append the note and its duration to the melody list
        melody.append((note, freq, duration))

    # Return the melody list
    return melody

# Define a function to synthesize a sine wave for a given frequency and duration
def synthesize_sine(freq, duration):
    # Generate a time array from 0 to duration
    t = np.linspace(0, duration, int(duration * sample_rate))

    # Generate a sine wave for the given frequency
    x = np.sin(2 * np.pi * freq * t)

    # Return the sine wave array
    return x

# Define a function to convert lyrics to a sequence of phonemes using CMUdict
def lyrics_to_phonemes(lyrics):
    # Import the CMUdict module
    import nltk
    nltk.download('cmudict')
    from nltk.corpus import cmudict

    # Initialize an empty list to store the phonemes
    phonemes = []

    # Split the lyrics into words and loop over them
    words = lyrics.split()
    for word in words:
        # Convert the word to lowercase and strip any punctuation
        word = word.lower().strip(".,!?")

        # Check if the word is in the CMUdict
        if word in cmudict.dict():
            # Choose a random pronunciation for the word from the CMUdict
            pronunciation = random.choice(cmudict.dict()[word])

            # Append the pronunciation to the phonemes list
            phonemes.extend(pronunciation)

            # Append a pause symbol to separate words
            phonemes.append("-")

        else:
            # If the word is not in the CMUdict, skip it
            pass

    # Return the phonemes list
    return phonemes

# Define a function to map phonemes to frequencies using a simple heuristic
def phonemes_to_freqs(phonemes):
    # Define a dictionary of phonemes and their corresponding frequencies in Hz
    phoneme_freqs = {
        "AA": 600,
        "AE": 500,
        "AH": 400,
        "AO": 700,
        "AW": 800,
        "AY": 900,
        "B": 200,
        "CH": 300,
        "D": 250,
        "DH": 350,
        "EH": 450,
        "ER": 550,
        "EY": 650,
        "F": 150,
        "G": 300,
        "HH": 100,
        "IH": 500,
        "IY": 600,
        "JH": 400,
        "K": 350,
        "L": 200,
        "M": 100,
        "N": 150,
        "NG": 250,
        "OW": 750,
        "OY": 850,
        "P": 200,
        "R": 300,
        "S": 100,
        "SH": 200,
        "T": 250,
        "TH": 350,
        "UH": 400,
        "UW": 500,
        "V": 150,
        "W": 100,
        "Y": 200,
        "Z": 100,
        "ZH": 200,
        "-": 0 # Pause symbol
    }

    # Initialize an empty list to store the frequencies
    freqs = []

    # Loop over the phonemes and map them to frequencies
    for phoneme in phonemes:
        # Check if the phoneme is in the dictionary
        if phoneme in phoneme_freqs:
            # Get the frequency for the phoneme
            freq = phoneme_freqs[phoneme]

            # Append the frequency to the freqs list
            freqs.append(freq)

        else:
            # If the phoneme is not in the dictionary, skip it
            pass

    # Return the freqs list
    return freqs

# Define a function to synthesize a vocal sound for a given frequency and duration
def synthesize_vocal(freq, duration):
    # Generate a time array from 0 to duration
    t = np.linspace(0, duration, int(duration * sample_rate))

    # Generate a random amplitude between 0.5 and 1
    amp = random.uniform(0.5, 1)

    # Generate a random phase between 0 and 2 pi
    phase = random.uniform(0, 2 * np.pi)

    # Generate a vocal sound using a sawtooth wave with some noise
    x = amp * np.sign(np.sin(2 * np.pi * freq * t + phase)) + 0.1 * np.random.randn(len(t))

    # Return the vocal sound array
    return x

# Define a function to generate a song audio from lyrics and melody
def generate_song_audio(lyrics, melody):
    # Convert the lyrics to a sequence of phonemes
    phonemes = lyrics_to_phonemes(lyrics)

    # Map the phonemes to a sequence of frequencies
    freqs = phonemes_to_freqs(phonemes)

    # Initialize an empty array to store the song audio
    song_audio = np.array([])

    # Loop over the melody and the frequencies
    for (note, note_freq, note_duration), vocal_freq in zip(melody, freqs):
        # Synthesize a sine wave for the note frequency and duration
        note_audio = synthesize_sine(note_freq, note_duration)

        # Synthesize a vocal sound for the vocal frequency and duration
        vocal_audio = synthesize_vocal(vocal_freq, note_duration)

        # Mix the note audio and the vocal audio with equal weights
        mixed_audio = 0.5 * note_audio + 0.5 * vocal_audio

        # Append the mixed audio to the song audio array
        song_audio = np.append(song_audio, mixed_audio)

    # Normalize the song audio to have values between -1 and 1
    song_audio = song_audio / np.max(np.abs(song_audio))

    # Return the song audio array
    return song_audio

# Define some sample lyrics for testing
lyrics = """
Twinkle twinkle little star
How I wonder what you are
Up above the world so high
Like a diamond in the sky"""

# Generate a random melody for testing
melody = generate_melody()

# Generate a song audio from the lyrics and melody
song_audio = generate_song_audio(lyrics, melody)

# Save the song audio as a wav file
sf.write("song.wav", song_audio, sample_rate)
