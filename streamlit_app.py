import streamlit as st

st.set_page_config(page_title="Maykoll Rocha - Portifolio Pessoal",
            page_icon=None ,
            layout="wide",
            initial_sidebar_state="expanded",
        )

st.write("Hello Word")
st.text("Hello Word")
st.latex(r"P(n, k) = \frac{1}{k!} \sum_{j=1}^{k} (-1)^{k-j} \binom{k}{j} j^n ")
st.markdown(r"""

            $$ P(n, k) = \frac{1}{k!} \sum_{j=1}^{k} (-1)^{k-j} \binom{k}{j} j^n $$
            """)