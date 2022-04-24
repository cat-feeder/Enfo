import streamlit as st
# To make things easier later, we're also importing numpy and pandas for
# working with sample data.
import numpy as np
import pandas as pd

from datetime import datetime
import pymysql

from charts import chart_ForestRegion

#add an import to Hydralit
from hydralit import HydraHeadApp
import hydralit as hy

#create a wrapper class
class MyForestRegionApp(HydraHeadApp):

#wrap all your code in this method and you should be done
    def run(self):

        # connect to database and get data
        db=pymysql.connect(host="3.92.56.176",user="root",passwd="Hzpmark1996!",database="project")
        cursor=db.cursor()
        sql = "select region,years,percentage from forest_by_region"
        cursor.execute(sql)
        res = cursor.fetchall()
        frame = pd.DataFrame(list(res))
        # modify headers
        frame.columns = ['Region','Year','Percentage'] 
        all_regions = frame.Region.unique()
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
        subtitle = '<p style="font-family:sans-serif; font-size: 20px;color:#008080;">Forest Land(Region)</p>'
        st.markdown(subtitle, unsafe_allow_html=True)


        regions = st.multiselect("Choose regions to visualize forest land percentage",all_regions , all_regions[2:5])

        space(1)

        source = source[source.Region.isin(regions)]
        chart = chart_ForestRegion.get_chart(source)
        st.altair_chart(chart, use_container_width=True)


        # some notations
        natation1 = '<p style="font-family:sans-serif; font-size: 16px;color:Black;">Data Source: </p>'
        st.markdown(natation1, unsafe_allow_html=True)
        st.write("Forest Land [link](https://databank.worldbank.org/reports.aspx?source=2&series=AG.LND.FRST.ZS&country=#)")

        # close database connections
        #cursor.close()
        #db.close()
