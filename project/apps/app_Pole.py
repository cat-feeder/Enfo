import streamlit as st
# To make things easier later, we're also importing numpy and pandas for
# working with sample data.
import numpy as np
import pandas as pd

from datetime import datetime
import pymysql

from charts import chart_Pole

#add an import to Hydralit
from hydralit import HydraHeadApp
import hydralit as hy

#create a wrapper class
class MyPoleApp(HydraHeadApp):

#wrap all your code in this method and you should be done
    def run(self):

        # connect to database and get data
        db=pymysql.connect(host="3.92.56.176",user="root",passwd="Hzpmark1996!",database="project")
        cursor=db.cursor()
        sql = "select years,months,region,area from pole_data"
        # min data of evey year
        cursor.execute(sql)
        res = cursor.fetchall()
        frame= pd.DataFrame(list(res))
        frame.columns = ['Year','Month','Region','Minimal_area']
        frame.drop(frame[frame.Year==1987].index,inplace=True) 
        frame.drop(frame[(frame.Region=='N') & (frame.Month!=9)].index,inplace=True) 
        frame.drop(frame[(frame.Region=='S') & (frame.Month!=2)].index,inplace=True) 
        frame = frame.replace('N','North Pole')
        frame = frame.replace('S','South Pole')
        source_overall = frame
        all_categories = source_overall.Region.unique()


        def space(num_lines=1):
            """Adds empty lines to the Streamlit app."""
            for _ in range(num_lines):
                st.write("")


        #st.set_page_config(layout="centered", page_title="ENFO")


        # Data visualisation part
        title = '<p style="font-family:sans-serif; font-size: 55px;color:#008080;">ENFO🌲🌳</p>'
        st.markdown(title, unsafe_allow_html=True)
        subtitle = '<p style="font-family:sans-serif; font-size: 20px;color:#008080;">Pole Area Data (of Year)</p>'
        st.markdown(subtitle, unsafe_allow_html=True)


        Categories = st.multiselect("Choose regions to visualize Pole data (minimal pole area of evey year)",all_categories , all_categories[0:2])

        space(1)

        source = source_overall[source_overall.Region.isin(Categories)]
        chart = chart_Pole.get_chart_overall(source)
        st.altair_chart(chart, use_container_width=True)

        space(1)

        # second chart: month as x axis, year in the selection box:
        frame_N= pd.DataFrame(list(res))
        frame_N.columns = ['Year','Month','Region','area']
        frame_N.drop(frame_N[frame_N.Year==1987].index,inplace=True) 
        frame_N.drop(frame_N[frame_N.Region=='S'].index,inplace=True)
        frame_N = frame_N.replace('N','North Pole')
        frame_N['Year'] = frame_N['Year'].apply(str)
        source_N = frame_N
        all_N = source_N.Year.unique()
        subtitle2 = '<p style="font-family:sans-serif; font-size: 20px;color:#008080;">North Pole Area Data (of Year & Month)</p>'
        st.markdown(subtitle2, unsafe_allow_html=True)  
        N = st.multiselect("Choose years to visualize North Pole area data",all_N , all_N[-3:-1])
        space(1)
        sourceN = source_N[source_N.Year.isin(N)]
        chart = chart_Pole.get_chart_north(sourceN)
        st.altair_chart(chart, use_container_width=True)      

        space(1)

        # third chart: month as x axis, year in the selection box:
        frame_S= pd.DataFrame(list(res))
        frame_S.columns = ['Year','Month','Region','area']
        frame_S.drop(frame_S[frame_S.Year==1987].index,inplace=True) 
        frame_S.drop(frame_S[frame_S.Region=='N'].index,inplace=True)
        frame_S = frame_S.replace('S','South Pole')
        frame_S['Year'] = frame_S['Year'].apply(str)
        source_S = frame_S
        all_S = source_S.Year.unique()
        subtitle3 = '<p style="font-family:sans-serif; font-size: 20px;color:#008080;">South Pole Area Data (of Year & Month)</p>'
        st.markdown(subtitle3, unsafe_allow_html=True)  
        S = st.multiselect("Choose years to visualize South Pole area data",all_S , all_S[-3:-1])
        space(1)
        sourceS = source_S[source_S.Year.isin(S)]
        chart = chart_Pole.get_chart_south(sourceS)
        st.altair_chart(chart, use_container_width=True)      

        space(1)

        # some notations
        natation1 = '<p style="font-family:sans-serif; font-size: 16px;color:Black;">Data Source: </p>'
        st.markdown(natation1, unsafe_allow_html=True)
        st.write("Pole Data [link](https://masie_web.apps.nsidc.org/pub/DATASETS/NOAA/G02135/north/monthly/data/)")

        # close database connections
        #cursor.close()
        #db.close()
