import streamlit as st
from util import *

# Page title of the application
page_title = "Tokenizer Lab"
page_icon = "🔢"
st.set_page_config(page_title=page_title, page_icon=page_icon, layout="centered")

# Tokenizer dictionary to map the name with tokenizer
tokenizer_map = {'BERT BASE CASED': 'bert-base-cased', 'BERT BASE UNCASED': 'bert-base-uncased','GPT-4': 'Xenova/gpt-4',
                 'GPT-2': 'gpt2','FLAN T5 SMALL': 'google/flan-t5-small', 'PHI-3': 'microsoft/Phi-3-mini-4k-instruct',
                 'STARCODER 2': 'bigcode/starcoder2-15b', 'QWEN2': 'Qwen/Qwen2-VL-7B-Instruct'}


sample_text = """
English and CAPITALIZATION 🎵 鸟
show_tokens False None elif == >= else: two tabs:"    " Three tabs: "       " 12.0*50=600
"""

# Application Title and description
st.title(f'{page_title}🔢')
st.write('***:blue[Decode Text, Compare Tokenizers! 🚀]***')
st.write("""
*Tokenizer Lab lets you explore and compare different LLM tokenizers in real time! 🧩 Choose a tokenizer, input text, 
and see how it gets tokenized. Perfect for AI enthusiasts, researchers, and developers optimizing for efficiency! ⚡*
""")

# Display footer in the sidebar
display_footer()

col1, col2 = st.columns([2, 1], border=True)
with col1:
    input_text = st.text_area("Enter the text to tokenize:", value=sample_text.strip(), help='Enter the Text to Tokenize')
with col2:
    tokenizer_selection = st.selectbox('Select the Tokenizer', ['BERT BASE CASED', 'BERT BASE UNCASED','GPT-4','GPT-2','FLAN T5 SMALL',
                                          'PHI-3','STARCODER 2', 'QWEN2'], placeholder='Select the Tokenizer',
                                       help='Select the Tokenizer from the list')
tokenize = st.button("Tokenize", type='primary', disabled=(not tokenizer_selection or not input_text))

if tokenize:
    with st.spinner('Tokenizing ...'):
        t_name = tokenizer_map[tokenizer_selection]
        show_tokens(sample_text, t_name)
