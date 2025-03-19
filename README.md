# CloTTS

CloTTS is a Python-based text-to-speech application that leverages the Coqui-TTS library to generate high-quality speech from text locally on your machine.

## Features

- Local text-to-speech conversion without relying on external APIs
- Built with Coqui-TTS for high-quality voice synthesis
- Simple Python interface for easy integration into your projects

## Requirements

- Python 3.9 (recommended)
- uv package manager (for easier dependency management)

## Installation

### Installing uv

First, install the uv package manager, which will help manage Python versions and dependencies:

**For macOS and Linux:**
```bash
curl -LsSf https://astral.sh/uv/install.sh | sudo sh
```

**For Windows (using PowerShell with administrator privileges):**
```powershell
powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
```

**Via Homebrew:**
```bash
brew install uv
```

Verify the installation:
```bash
uv version
```

### Setting up Python 3.9

Install Python 3.9 using uv:
```bash
uv python install 3.9
```

### Installing CloTTS

1. Clone the repository:
```bash
git clone https://github.com/Wanderer0074348/CloTTS.git
cd CloTTS
```

2. Create a virtual environment with Python 3.9:
```bash
uv venv --python 3.9
```

3. Activate the virtual environment:
   - On Windows: `.venv\Scripts\activate`
   - On macOS/Linux: `source .venv/bin/activate`

4. Install the required dependencies:
```bash
uv pip install -r requirements.txt
```

5. Install Coqui-TTS (make sure to use coqui-tts, not TTS):
```bash
uv pip install coqui-tts
```

## Usage

Run the main application:
```bash
python main.py
```

## Project Structure

- `src/` - Source code for the application
- `main.py` - Entry point for the application
- `requirements.txt` - List of Python dependencies

## Development

To contribute to this project:

1. Fork the repository
2. Create a new branch for your feature
3. Make your changes
4. Submit a pull request

## License

This project is open-source.

## Acknowledgements

- [Coqui-TTS](https://github.com/idiap/coqui-ai-TTS) for providing the text-to-speech technology
- [uv](https://github.com/astral-sh/uv) for the efficient Python package management
