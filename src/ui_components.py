import streamlit as st
import tempfile
import os

class UIComponents:
    """Class responsible for rendering UI components"""
    
    def __init__(self, config):
        self.config = config
    
    def render_language_selector(self):
        """Render the language selection dropdown"""
        st.sidebar.header("Settings")
        return st.sidebar.selectbox("Select Language", list(self.config.languages.keys()))
    
    def render_text_input(self):
        """Render the text input area"""
        return st.text_area(
            "Enter text to convert to speech:", 
            "Hello, this is a voice cloning test. How does it sound?", 
            height=150
        )
    
    def render_voice_selector(self, tts):
        """Render the voice selection UI components"""
        voice_method = st.radio(
            "Choose voice method:",
            ["Use predefined speaker", "Upload your own voice"]
        )
        
        speaker_wav = None
        temp_file = None
        
        if voice_method == "Use predefined speaker":
            speaker_wav, temp_file = self._handle_predefined_speaker(tts)
        
        if voice_method == "Upload your own voice" or speaker_wav is None:
            speaker_wav, temp_file = self._handle_voice_upload()
        
        return voice_method, speaker_wav, temp_file
    
    def _handle_predefined_speaker(self, tts):
        """Handle selection of predefined speakers"""
        # Get available speakers
        available_speakers = getattr(tts, 'speakers', [])
        if available_speakers:
            selected_speaker = st.selectbox("Select a predefined speaker:", available_speakers)
            return selected_speaker, None
        else:
            st.warning("No predefined speakers available. Please upload your own voice.")
            return None, None
    
    def _handle_voice_upload(self):
        """Handle voice upload functionality"""
        st.info("Upload a clear audio file of your voice (WAV format recommended, 3-10 seconds)")
        uploaded_file = st.file_uploader("Upload your voice sample", type=["wav", "mp3"])
        
        if uploaded_file is not None:
            # Save the uploaded file to a temporary location
            temp_file = tempfile.NamedTemporaryFile(delete=False, suffix='.wav')
            temp_file.write(uploaded_file.getvalue())
            temp_file.close()  # Close the file before using it
            speaker_wav = temp_file.name
            st.audio(uploaded_file, format='audio/wav')
            return speaker_wav, temp_file
        
        return None, None
    
    def render_generate_button(self, disabled=False):
        """Render the generate speech button"""
        return st.button("Generate Speech", disabled=disabled)
    
    def render_app_info(self):
        """Render information about the app"""
        st.markdown("""
        ## About this app
        This app uses Coqui TTS's XTTS v2 model to generate speech from text. You can either:
        - Select from predefined speakers (if available)
        - Upload your own voice sample for voice cloning

        ## Tips for best results
        - Use clear audio samples without background noise
        - Samples of 5-10 seconds work best
        - Speak naturally in your sample
        - For languages other than English, use a voice sample in that language for better results
        """)
