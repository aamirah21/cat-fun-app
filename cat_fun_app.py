import streamlit as st
import requests

st.set_page_config(page_title="🐱 Cat Fun App", page_icon="🐱")

st.title("🐱 Cat Fun App")
st.write("Click the button to get a random cat fact and see a random cat picture!")

if st.button("Show me a cat! 😻"):
    # Get a random cat fact
    fact_resp = requests.get("https://catfact.ninja/fact")
    fact = fact_resp.json().get("fact", "No fact available right now 😿")
    
    # Get a random cat image
    img_resp = requests.get("https://api.thecatapi.com/v1/images/search")
    img_url = img_resp.json()[0].get("url", "")

    st.subheader("🐾 Cat Fact:")
    st.write(fact)

    st.subheader("📸 Random Cat Image:")
    if img_url:
        st.image(img_url, use_column_width=True)
    else:
        st.write("Couldn’t fetch a cat image 😿")
else:
    st.write("Press the button to start! 🐾")

