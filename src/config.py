class AppConfig:

    def __init__(self):

        self.languages = {
            "English": "en",
            "Spanish": "es",
            "French": "fr",
            "German": "de",
            "Italian": "it",
            "Portuguese": "pt",
            "Polish": "pl",
            "Turkish": "tr",
            "Russian": "ru",
            "Dutch": "nl",
            "Czech": "cs",
            "Arabic": "ar",
            "Chinese": "zh-cn",
            "Japanese": "ja",
            "Korean": "ko",
            "Hindi": "hi"
        }

        self.model_name = "tts_models/multilingual/multi-dataset/xtts_v2"

        self.output_dir = "output"
        self.default_output_file = "generated_speech.wav"