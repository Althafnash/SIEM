import streamlit as st 
from Elastic import Failed_Logins, Security

st.set_page_config(page_title="SIEMui",  layout="wide")
st.title("SIEMui")
tabs = st.tabs(["MainContent","Failed Logins", "Security Events"])

with st.sidebar:
    st.title("SIEMui")
    st.write("Features of SIEMui:")
    st.write("Failed Logins")
    st.write("Security Events")

with tabs[0]:
    st.title("SIEMui")
    st.write("Welcome to the SIEMui interface!")

with tabs[1]:
    st.title("Failed Logins")
    st.write("This section displays failed login attempts in the last 24 hours.")
    result , messages = Failed_Logins()
    st.html(f"<h1>{result}</h1>")
    for message in messages:
        st.html(f"<h2 style='color: green;'>{message}</h2>")

with tabs[2]:
    st.title("Security Events")
    st.write("This section displays security events in the last 24 hours.")
    result, messages = Security()
    st.html(f"<h1>{result}</h1>")
    for message in messages:
        st.html(f"<h2 style='color: green;'>{message}</h2>")