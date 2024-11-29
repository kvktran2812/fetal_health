import streamlit as st

# Setup pages
overview_page = st.Page("streamlit_pages/overview.py", title="1. Overview")
eda_page = st.Page("streamlit_pages/eda.py", title="2. EDA")
pca_page = st.Page("streamlit_pages/pca.py", title="3. PCA")
predictive_models_page = st.Page("streamlit_pages/models.py", title="4. Models")



# Setup main pages 
pg = st.navigation([overview_page, eda_page, pca_page, predictive_models_page])
st.set_page_config(page_title="Stock Prediction Project")
pg.run()