import streamlit as st
from util import *

# Page configuration options
page_title = "FAQs"
page_icon = "💬"
st.set_page_config(page_title=page_title, page_icon=page_icon, layout="wide", initial_sidebar_state="expanded")

st.title('FAQs')

expand_all = st.toggle("Expand all", value=True)

# Display footer in the sidebar
display_footer()

tokenizer_table = '''
<table>
        <tr>
            <th>Tokenizer Name</th>
            <th>Description</th>
        </tr>
        <tr>
            <td>BERT BASE CASED</td>
            <td>Tokenizer based on Case-sensitive version of BERT Base</td>
        </tr>
        <tr>
            <td>BERT BASE UNCASED</td>
            <td>Tokenizer based on Case-insensitive version of BERT Base</td>
        </tr>
        <tr>
            <td>GPT-4</td>
            <td>Tokenizer based on OpenAI’s latest large language model</td>
        </tr>
        <tr>
            <td>GPT-2</td>
            <td>Tokenizer based on Older version of OpenAI’s language model</td>
        </tr>
        <tr>
            <td>FLAN T5 SMALL</td>
            <td>Tokenizer based on Small-sized FLAN-T5 model for fine-tuned tasks</td>
        </tr>
        <tr>
            <td>PHI-3</td>
            <td>Tokenizer based on Microsoft small language model</td>
        </tr>
        <tr>
            <td>STARCODER 2</td>
            <td>Tokenizer based on  StarCoder 2 -- LLM optimized for code generation</td>
        </tr>
        <tr>
            <td>QWEN2</td>
            <td>Tokenizer based on Alibaba’s open-source LLM</td>
        </tr>
    </table>
'''

faq_data = {
        'What this Application is about?':
            '<p>A web app that let you explore and compare different LLM tokenizers in real time! .</p>',

        'Which Tokenizers are supported by this application?':
            'Following table list the supported Tokenizers by this app.'
            f'{tokenizer_table}',

        'I want to make modification in the application. Can I get the application source code?':
            '<p>Yes, Source code of this application is available at: '
            '<a href="https://github.com/mzeeshanaltaf/llm_tokenizer">GitHub</a></p>',

    }

# Display expandable boxes for each question-answer pair
for question, answer in faq_data.items():
    with st.expander(r"$\textbf{\textsf{" + question + r"}}$", expanded=expand_all):  # Use LaTeX for bold label
        st.markdown(f'<div style="text-align: justify;"> {answer} </div>', unsafe_allow_html=True)