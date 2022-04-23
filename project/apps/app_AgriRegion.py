import streamlit as st
# To make things easier later, we're also importing numpy and pandas for
# working with sample data.
import numpy as np
import pandas as pd

from datetime import datetime
import pymysql

#from charts import chart_AgriRegion

#add an import to Hydralit
from hydralit import HydraHeadApp
import hydralit as hy

#create a wrapper class
class MyAgriRegionApp(HydraHeadApp):

#wrap all your code in this method and you should be done
    def run(self):

       hy.info('a')
