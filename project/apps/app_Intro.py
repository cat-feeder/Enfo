import streamlit as st
# To make things easier later, we're also importing numpy and pandas for
# working with sample data.
import numpy as np
import pandas as pd

from datetime import datetime
import pymysql

#from charts import chart_Intro

#add an import to Hydralit
from hydralit import HydraHeadApp


class MyIntroApp(HydraHeadApp):

    def run(self):

        def space(num_lines=1):
            """Adds empty lines to the Streamlit app."""
            for _ in range(num_lines):
                st.write("")

        #st.set_page_config(layout="centered", page_title="ENFO")

        # title and subtitle
        title = '<p style="font-family:sans-serif; font-size: 55px;color:#008080;">ENFO🌲🌳</p>'
        st.markdown(title, unsafe_allow_html=True)
        subtitle = '<p style="font-family:sans-serif; font-size: 20px;color:#008080;">Environment Information</p>'
        st.markdown(subtitle, unsafe_allow_html=True)
        space(1)

        # text part
        subtitle2 = '<p style="font-family:sans-serif; font-size: 16px;color:black;">Motivation and Introduction</p>'
        st.markdown(subtitle2, unsafe_allow_html=True)
        st.write("In the past few decades, heavy industrial activity has caused great environmental pressure on the earth, fundamentally changing our ecosystem and global climate. Environmental protection could be a huge issue, but it could also be specific to the daily life of every individual. In fact, our generations have witnessed colossal changes in the global environment, but not every one of us is truly aware of the severity of the problem. Therefore we aim to develop a website (and app also) that literally speaks with data, which intuitively displays the global climate- and environment-related data fluctuations in the past decades. In conclusion, our motivation is to arouse people’s focus on environmental issues by displaying global changes intuitively with data and graphs.")

        space(2)

