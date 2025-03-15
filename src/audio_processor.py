import streamlit as st
import os
import numpy as np
from scipy.io.wavfile import write as write_wav


class AudioProcessor:

    def display_audio(self, audio_path):
        st.success("Speech generated successfully!")
        st.audio(audio_path, format='audio/wav')

        with open(audio_path, "rb") as file:
            st.download_button(
                label="Download Audio",
                data=file,
                file_name="generated_speech.wav",
                mime="audio/wav"
            )

    def cleanup_temp_file(self, temp_file):
        try:
            if hasattr(temp_file, 'close'):
                temp_file.close()

            if hasattr(temp_file, 'name') and os.path.exists(temp_file.name):
                os.unlink(temp_file.name)
        except Exception as e:

            print(f"Error cleaning up temporary file: {e}")