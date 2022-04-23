import streamlit as st
# To make things easier later, we're also importing numpy and pandas for
# working with sample data.
import numpy as np
import pandas as pd

from datetime import datetime
import pymysql

from charts import chart_CO2Country

#add an import to Hydralit
from hydralit import HydraHeadApp


#create a wrapper class
class MyCO2CountryApp(HydraHeadApp):

#wrap all your code in this method and you should be done
    def run(self):


        # connect to database and get data
        db=pymysql.connect(host="3.92.56.176",user="root",passwd="Hzpmark1996!",database="project")
        cursor=db.cursor()
        sql_CO2Country = "select b.country,a.years,a.cumulative_co2_emissions from cumulative_emissions_by_country a, country b where a.country_code=b.country_code"
        cursor.execute(sql_CO2Country)
        res = cursor.fetchall()
        frame_CountryCo2 = pd.DataFrame(list(res))
        # modify headers
        frame_CountryCo2.columns = ['Country','Year','Emission']
        # change world sum value to world average value
        all_Country = frame_CountryCo2.Country.unique()
        source = frame_CountryCo2
        # change 'Year' from int to string
        #source['Year'] = source['Year'].apply(str)
        #frame_world['Year']=pd.to_datetime(frame_world['Year'])


        def space(num_lines=1):
            """Adds empty lines to the Streamlit app."""
            for _ in range(num_lines):
                st.write("")


        #st.set_page_config(layout="centered", page_title="ENFO")


        # Data visualisation part
        title = '<p style="font-family:sans-serif; font-size: 55px;color:#008080;">ENFO🌲🌳🌴🌵</p>'
        st.markdown(title, unsafe_allow_html=True)
        subtitle = '<p style="font-family:sans-serif; font-size: 20px;color:#008080;">CO2 Emissions(Country)</p>'
        st.markdown(subtitle, unsafe_allow_html=True)


        countries = st.multiselect("Choose countries to visualize CO2 emissions",all_Country , all_Country[34:37])

        space(1)

        source = source[source.Country.isin(countries)]
        chart = chart_CO2Country.get_chart(source)
        st.altair_chart(chart, use_container_width=True)


        # some notations
        natation1 = '<p style="font-family:sans-serif; font-size: 16px;color:Black;">Data Source: </p>'
        st.markdown(natation1, unsafe_allow_html=True)
        st.write("CO2 Emissions [link](https://www.ucsusa.org/resources/each-countrys-share-co2-emissions)")

        # close database connections
        #cursor.close()
        #db.close()
