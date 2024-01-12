import streamlit as st
from streamlit.logger import get_logger

LOGGER = get_logger(__name__)


def run():
    st.set_page_config(
        page_title="EMPLOFLATE",
        page_icon="📈",
    )

    st.write("# Welcome to Emploflate")
    st.image('img.png', use_column_width=True)
    st.sidebar.success("Select one option above.")

    st.markdown(
        """
        "*Exploring Malaysia's economic trends:* A detailed analysis of inflation and unemployment rates,
        shedding light on crucial factors shaping the nation's economic stability and workforce dynamics"

        ### Link 
        - Explore our [Github here](https://github.com/GROUP12PDS/GROUP12.git)
    """
    )


if __name__ == "__main__":
    run()
