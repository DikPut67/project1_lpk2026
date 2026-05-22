import streamlit as st

st.title("Project Kel.12")
import streamlit as kl

kl.markdown("*Streamlit* is **really** ***cool***.")
kl.markdown('''
    :red[Streamlit] :orange[can] :green[write] :blue[text] :violet[in]
    :gray[pretty] :rainbow[colors] and :blue-background[highlight] text.''')
kl.markdown("Here's a bouquet &mdash;\
            :tulip::cherry_blossom::rose::hibiscus::sunflower::blossom:")
import streamlit as pa

pages = {
    "Your account": [
        pa.Page("create_account.py", title="Create your account"),
        pa.Page("manage_account.py", title="Manage your account"),
    ],
    "Resources": [
        pa.Page("learn.py", title="Learn about us"),
        pa.Page("trial.py", title="Try it out"),
    ],
}

pg = pa.navigation(pa)
pg.run()
