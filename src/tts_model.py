import streamlit as st
from TTS.api import TTS

class TTSModelManager:
    """Class responsible for loading and managing the TTS model"""
    
    def __init__(self):
        self.model_name = "tts_models/multilingual/multi-dataset/xtts_v2"
    
    def load_model(self):
        """Load the TTS model with caching for efficiency"""
        # Use the cached loader function instead of caching the method directly
        return self._load_model_cached(self.model_name)
    
    @staticmethod
    @st.cache_resource
    def _load_model_cached(model_name):
        """Static cached method to load the model"""
        # Get device
        import torch
        device = "cuda" if torch.cuda.is_available() else "cpu"
        st.info(f"Using device: {device}")
        
        # Initialize TTS
        tts = TTS(model_name).to(device)
        return tts
    
    def generate_speech(self, tts, text, speaker_wav, language, output_path, type):
        """Generate speech using the TTS model"""
        if type=="Use predefined speaker":
            tts.tts_to_file(
                text=text,
                speaker=speaker_wav,
                language=language,
                file_path=output_path
            )
        else:
            tts.tts_to_file(
                text=text,
                speaker_wav=speaker_wav,
                language=language,
                file_path=output_path
            )
        return output_path
