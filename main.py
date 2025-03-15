import streamlit as st
import torch
import os

# Set torch classes path to avoid warnings
torch.classes.__path__ = []

# Import our components
from src.tts_model import TTSModelManager
from src.ui_components import UIComponents
from src.audio_processor import AudioProcessor
from src.config import AppConfig

def main():
    # Set up page configuration
    st.set_page_config(
        page_title="Voice Cloning TTS App",
        page_icon="🎙️",
        layout="wide"
    )
    
    st.title("🎙️ Voice Cloning Text-to-Speech App")
    
    # Initialize components
    config = AppConfig()
    tts_manager = TTSModelManager()
    ui = UIComponents(config)
    audio_processor = AudioProcessor()
    
    # Load TTS model
    try:
        tts = tts_manager.load_model()
        st.success("TTS model loaded successfully!")
    except Exception as e:
        st.error(f"Error loading TTS model: {e}")
        st.stop()
    
    # Get language selection
    selected_language = ui.render_language_selector()
    language_code = config.languages[selected_language]
    
    # Get text input
    text_input = ui.render_text_input()
    
    # Get voice selection
    voice_method, speaker_wav, temp_file = ui.render_voice_selector(tts)
    print(voice_method)
    
    # Generate speech button
    if ui.render_generate_button(speaker_wav is None):
        if not text_input.strip():
            st.error("Please enter some text to convert to speech.")
        else:
            with st.spinner("Generating speech..."):
                try:
                    # Create output directory if it doesn't exist
                    os.makedirs("output", exist_ok=True)
                    output_path = "output/generated_speech.wav"
                    
                    # Generate speech
                    tts_manager.generate_speech(
                        tts,
                        text_input,
                        speaker_wav,
                        language_code,
                        output_path,
                        voice_method
                    )
                    
                    # Display and offer download of the audio
                    audio_processor.display_audio(output_path)
                    
                except Exception as e:
                    st.error(f"Error generating speech: {e}")
    
    # Clean up temporary file if created
    if temp_file:
        audio_processor.cleanup_temp_file(temp_file)
    
    # Display app information
    ui.render_app_info()

if __name__ == "__main__":
    main()
