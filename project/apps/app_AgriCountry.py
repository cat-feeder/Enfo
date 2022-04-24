import streamlit as st
# To make things easier later, we're also importing numpy and pandas for
# working with sample data.
import numpy as np
import pandas as pd

from datetime import datetime
import pymysql

from charts import chart_AgriCountry

#add an import to Hydralit
from hydralit import HydraHeadApp
import hydralit as hy

#create a wrapper class
class MyAgriCountryApp(HydraHeadApp):

#wrap all your code in this method and you should be done
    def run(self):

        # connect to database and get data
        db=pymysql.connect(host="3.92.56.176",user="root",passwd="Hzpmark1996!",database="project")
        cursor=db.cursor()
        sql = sql = "select b.country,a.years,a.percentage from agricultural_by_country a, country b where a.country_code=b.country_code"
        cursor.execute(sql)
        res = cursor.fetchall()
        frame = pd.DataFrame(list(res))
        # modify headers
        frame.columns = ['Country','Year','Percentage'] 
        all_country = frame.Country.unique()
        # convert percentage
        frame['Percentage'] = frame['Percentage'].apply(lambda x:x/100)
        source = frame
        #change 'Year' from int to string
        #source['Year'] = source['Year'].apply(str)
        #frame_world['Year']=pd.to_datetime(frame_world['Year'])


        def space(num_lines=1):
            """Adds empty lines to the Streamlit app."""
            for _ in range(num_lines):
                st.write("")


        #st.set_page_config(layout="centered", page_title="ENFO")


        # Data visualisation part
        title = '<p style="font-family:sans-serif; font-size: 55px;color:#008080;">ENFO🌲🌳</p>'
        st.markdown(title, unsafe_allow_html=True)
        subtitle = '<p style="font-family:sans-serif; font-size: 20px;color:#008080;">Agricultural Land(Country)</p>'
        st.markdown(subtitle, unsafe_allow_html=True)


        countries = st.multiselect("Choose countries to visualize agricultural land percentage",all_country , all_country[-15:-13])

        space(1)

        source = source[source.Country.isin(countries)]
        chart = chart_AgriCountry.get_chart(source)
        st.altair_chart(chart, use_container_width=True)


        # some notations
        natation1 = '<p style="font-family:sans-serif; font-size: 16px;color:Black;">Data Source: </p>'
        st.markdown(natation1, unsafe_allow_html=True)
        st.write("Agricultural Land [link](https://databank.worldbank.org/reports.aspx?source=2&series=AG.LND.AGRI.ZS&country=#)")

        # close database connections
        #cursor.close()
        #db.close()
