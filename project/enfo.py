from hydralit import HydraApp
import streamlit as st
import hydralit as hy

from apps.app_Intro import MyIntroApp
from apps.app_CO2Region import MyCO2RegionApp
from apps.app_CO2Country import MyCO2CountryApp
from apps.app_AgriRegion import MyAgriRegionApp
from apps.app_AgriCountry import MyAgriCountryApp
from apps.app_ForestRegion import MyForestRegionApp
from apps.app_Forestcountry import MyForestCountryApp
from apps.app_Pole import MyPoleApp
#from apps.app_Temp import MyTempApp



if __name__ == '__main__':

    #this is the host application, we add children to it and that's it!
    app = HydraApp(title='ENFO',favicon="🌳",layout='centered')
              
    #add all your application classes here

    app.add_app("Introduction Page",icon="", app=MyIntroApp())
    app.add_app("CO2 Emissions(Region)", icon="💨", app = MyCO2RegionApp())
    app.add_app("CO2 Emissions(Country)", icon="💨", app = MyCO2CountryApp())
    app.add_app("Agricultural Land(Region)", icon="🌾", app = MyAgriRegionApp())
    app.add_app("Agricultural Land(Country)", icon="🌾", app = MyAgriCountryApp())
    app.add_app("Forest(Region)", icon="🌲", app = MyForestRegionApp())
    app.add_app("Forest(Country)", icon="🌲", app = MyForestCountryApp())
    app.add_app("Pole Data", icon="💧", app = MyPoleApp())
    #app.add_app("Temperature Data", icon="💧", app = MyTempApp())

    #run the whole lot
    app.run()

