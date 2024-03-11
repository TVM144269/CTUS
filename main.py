import streamlit
streamlit.set_page_config("SMS TO US")
streamlit.success("NAME :")
name = streamlit.text_input(".")
streamlit.success("মেইল :")
email = streamlit.text_input("..")
streamlit.success("SMS :")
message = streamlit.text_area("...")
ww = len(name) >= 1  and len(email) >= 1 and len(message) >= 1
file = open("D BASE.txt", "a")


if streamlit.button("SUBMIT>") and len(name) >= 1  and len(email) >= 1 and len(message) >= 1:
    streamlit.success("MESSAGE টি গ্রহণ করা হয়েছে")
    file.write(name+"  "+email+"   "+message)
    file.close()
elif ww == False:
    streamlit.warning("")
else:
    streamlit.warning("")