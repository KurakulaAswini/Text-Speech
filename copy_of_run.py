# -*- coding: utf-8 -*-
"""Copy of run.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1iKjt5ZEbRqA-c6NYsP8JcUSlCuP3_zgU

# Gradio Demo: neon-tts-plugin-coqui
### This  demo converts text to speech in 14 languages.
"""

!pip install -q gradio neon-tts-plugin-coqui==0.4.1a9

# Downloading files from the demo repo
import os
!wget -q https://github.com/gradio-app/gradio/raw/main/demo/neon-tts-plugin-coqui/packages.txt

import tempfile
import gradio as gr
from neon_tts_plugin_coqui import CoquiTTS

LANGUAGES = list(CoquiTTS.langs.keys())
coquiTTS = CoquiTTS()

def tts(text: str, language: str):
    with tempfile.NamedTemporaryFile(suffix=".wav", delete=False) as fp:
        coquiTTS.get_tts(text, fp, speaker = {"language" : language})
        return fp.name

inputs = [gr.Textbox(label="Input", value=CoquiTTS.langs["en"]["sentence"], max_lines=3),
            gr.Radio(label="Language", choices=LANGUAGES, value="en")]
outputs = gr.Audio(label="Output")

demo = gr.Interface(fn=tts, inputs=inputs, outputs=outputs)

demo.launch()