import streamlit as st

st.set_page_config(page_title="Siva Prasad Story App", page_icon="📖")

st.title("🎬 నా కథలు - నా సొంత యాప్")
st.write("ఇది నా స్వంత క్రియేటివ్ ప్లాట్‌ఫాం. ఇక్కడ నా కథలకు సంబంధించిన వివరాలు ఉంటాయి!")

story_title = st.text_input("మీ కథ పేరు రాయండి:")
story_desc = st.text_area("మీ కథ యొక్క సారాంశం (Story Plot) ఇక్కడ రాయండి:")

if st.button("✨ కథను సేవ్ చేయి"):
    if story_title and story_desc:
        st.success(f"అద్భుతం! '{story_title}' విజయవంతంగా సేవ్ అయింది.")
        st.write("### కథ వివరాలు:")
        st.write(story_desc)
    else:
        st.warning("దయచేసి కథ పేరు మరియు వివరాలు పూర్తిగా రాయండి.")
