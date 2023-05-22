import streamlit as st
from streamlit_option_menu import option_menu
from openai_sdk import askgpt
from PIL import Image

f = """<style>
footer {
    visibility:hidden
}
</style>
"""
image = Image.open('hl.png')
st.set_page_config(page_title="CodeConvertor", page_icon=image, layout="wide")
st.markdown(f, unsafe_allow_html=True)


def extract_code(answer, language):
    print(answer)
    if '```' not in answer:
        return answer
    code = f'```{language}\n'
    begin = answer.find(code) + len(code)
    end = answer[begin:].find(f'```')
    print(begin, end)
    print(answer[begin:end])
    return answer[begin:end]


def app():
    if not hasattr(st.session_state, 'message'):
        st.session_state.message = None
        st.session_state.language = ''
    # with st.sidebar:
    language = option_menu('', ['python', 'cpp', 'R', 'ruby', 'php', 'n4js'],
                           icons=['arrow-down'] * 6, default_index=1, orientation='horizontal')
    ol = st.sidebar.selectbox('original language', ['python', 'cpp', 'R', 'ruby', 'php', 'n4js'], 0)
    text = st.sidebar.text_area('write a code:')
    answer, st.session_state.message = askgpt(
        f'convert the following code from {ol} to {language}:' + text, st.session_state.message)
    if text and st.session_state.language != language:
        st.session_state.language = language
        st.write(answer)


if __name__ == '__main__':
    app()
