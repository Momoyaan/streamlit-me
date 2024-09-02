import streamlit as st

EVA_LOGO = "images/eva-logo.png"
st.logo(EVA_LOGO, link=None, icon_image=None)
st.markdown(
    """
    <style>
    [data-testid=stSidebar] {
        border-right: 1px solid #39393B !important;}
    }
    a {
        text-decoration: none;
    }
    a:link {
        text-decoration: none;
    }
    a:hover {
        color: #DC2626;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

with open("styles.css") as css:
    st.markdown(f"<style>{css.read()}</style>", unsafe_allow_html=True)

pg = st.navigation([
    st.Page("page/autobiography.py", title="AUTOBIOGRAPHY"),
    st.Page("page/portfolio.py", title="PORTFOLIO"),
])

pg.run()
