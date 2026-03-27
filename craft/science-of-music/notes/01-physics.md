# S1: The Physics of Sound — Notes

## Core Concepts

### Frequency, Amplitude, Timbre
- **Frequency**: vibrations per second (Hz); determines pitch. A4 = 440 Hz standard (ISO 16:1975)
- **Amplitude**: strength of vibration; determines loudness. Measured in decibels (logarithmic scale)
- **Timbre**: the "color" of sound; determined by the relative amplitudes of overtones. Why a trumpet and violin at the same pitch sound different

### The Overtone Series
- A vibrating string produces frequencies at integer multiples of the fundamental: f, 2f, 3f, 4f, 5f...
- 2f = octave above fundamental
- 3f = octave + fifth (the origin of consonance)
- 4f = two octaves
- 5f = two octaves + major third
- Higher harmonics produce increasingly complex intervals
- The relative strength of each harmonic defines the instrument's timbre

### Standing Waves and Resonance
- Standing waves form when reflected waves interfere constructively
- Nodes (zero displacement) and antinodes (maximum displacement)
- String instruments: both ends fixed → harmonics at n × (v/2L)
- Open tubes (flute): all harmonics
- Closed tubes (clarinet): odd harmonics only → distinctive hollow timbre
- Resonance: when driving frequency matches natural frequency, amplitude increases dramatically

### Fourier Analysis
- Joseph Fourier (1768-1830): any periodic waveform = sum of sine waves
- Fast Fourier Transform (FFT): computational algorithm for real-time spectral analysis
- Spectrogram: visual representation of frequency content over time
- Applications: audio engineering, speech recognition, instrument synthesis, noise cancellation
- The mathematical bridge between physics and music perception

### Speed of Sound
- Air at 20°C: 343 m/s (varies with temperature, medium)
- Water: ~1,480 m/s; steel: ~5,960 m/s
- Wavelength = speed / frequency → A4 at 440 Hz has wavelength ~0.78 m
- Relevant to concert hall design: travel time creates reflections

### Concert Hall Acoustics
- Wallace Clement Sabine (1868-1919): father of architectural acoustics
- RT60 (reverberation time): time for sound to drop 60 dB
- Sabine equation: RT60 = 0.161 × V / A (V = volume in m³, A = total absorption in sabins)
- Optimal RT60: ~2.0-2.25s for orchestral music; ~1.0s for speech
- Absorption coefficient: 0 (total reflection) to 1 (total absorption)
- Materials: concrete ~0.02; carpet ~0.5; acoustic panels ~0.8+
- Famous halls: Vienna Musikverein (RT60 ~2.0s), Boston Symphony Hall (Sabine's design, ~1.8s)

## Key Sources
- HyperPhysics (GSU): canonical web resource for acoustics fundamentals
- Romano PHYS 1406: undergraduate physics of sound lecture notes
- Sabine/Thermaxx: history of architectural acoustics
- Scientific Reports 2025: modern computational acoustics

## Connections to Other Sections
- Overtone series → S2 (why simple ratios sound consonant)
- Fourier analysis → S7 (mathematical basis of digital audio and AI music)
- Timbre perception → S4 (brainstem reflex in BRECVEMA responds to timbral features)
