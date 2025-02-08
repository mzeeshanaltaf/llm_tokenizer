import streamlit as st
from transformers import AutoTokenizer

# A list of colors in HEX for representing the tokens
colors = [
    '#66C2A5', '#FC8D62', '#8DA0CB',
    '#E78AC3', '#A6D854', '#FFD92F'
]

def show_tokens(sentence: str, tokenizer_name: str):
    """ Show the tokens each separated by a different color """

    # Load the tokenizer and tokenize the input
    tokenizer = AutoTokenizer.from_pretrained(tokenizer_name)
    token_ids = tokenizer(sentence).input_ids

    st.subheader('Tokenizer Vocabulary Size:', divider='gray')
    # Extract vocabulary length
    # st.metric(f"Vocab length: {len(tokenizer)}")
    st.metric('Vocabulary Length', f'{len(tokenizer):,}', label_visibility='collapsed')

    # Display the tokenized sentence with colors
    colored_tokens = []
    for idx, t in enumerate(token_ids):
        token_text = tokenizer.decode(t)
        color = colors[idx % len(colors)]
        colored_tokens.append(
            f'<span style="background-color: {color}; padding: 5px; border-radius: 5px; color: black; margin: 2px;">{token_text}</span>')

    st.subheader('Token List:', divider='gray')
    st.markdown(" ".join(colored_tokens), unsafe_allow_html=True)

    st.subheader('Details:', divider='gray')
    token_id_str = ", ".join(map(str, token_ids)) # Convert the list to a string
    st.write(f"Total Tokens: {len(token_ids)}")
    st.write(f"Token IDs: {token_id_str}")

def display_footer():
    footer = """
    <style>
    /* Ensures the footer stays at the bottom of the sidebar */
    [data-testid="stSidebar"] > div: nth-child(3) {
        position: fixed;
        bottom: 0;
        width: 100%;
        text-align: center;
    }

    .footer {
        color: grey;
        font-size: 15px;
        text-align: center;
        background-color: transparent;
    }
    </style>
    <div class="footer">
    Made with ❤️ by <a href="mailto:zeeshan.altaf@gmail.com">Zeeshan</a>.
    </div>
    """
    st.sidebar.markdown(footer, unsafe_allow_html=True)