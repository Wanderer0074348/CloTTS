import streamlit as st
from TTS.api import TTS


class TTSModelManager:

    def __init__(self):
        self.model_name = "tts_models/multilingual/multi-dataset/xtts_v2"

    def load_model(self):

        return self._load_model_cached(self.model_name)

    @staticmethod
    @st.cache_resource
    def _load_model_cached(model_name):

        import torch
        device = "cuda" if torch.cuda.is_available() else "cpu"
        st.info(f"Using device: {device}")

        tts = TTS(model_name).to(device)
        return tts

    def generate_speech(self, tts, text, speaker_wav, language, output_path, type):
        if type == "Use predefined speaker":
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