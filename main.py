import streamlit
streamlit.set_page_config("CLOSEO")
link = streamlit.text_input(" ")
if streamlit.button("OPEN"):
    streamlit.video(link)
else:
    streamlit.success(" ")
