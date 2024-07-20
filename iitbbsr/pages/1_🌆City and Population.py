import streamlit as st
import pandas as pd
import numpy as np

st.header("Population Vs Water Resources")
st.markdown("The population of a city is a crucial factor in determining its water requirements. As urban areas grow, the demand for water increases, leading to potential shortages and resource management challenges. Understanding the relationship between population growth and water resources is essential for sustainable development and effective urban planning. The visualizations below compare the population and water resources of different cities in Odisha.")
st.divider()
x,space,y=st.columns((1,0.6,1))
df=pd.read_csv("pop.csv")
d=pd.DataFrame(df)
sel=d[['Urban[51]','Population[50]']]
x.line_chart(sel)
y.area_chart(sel)
data = np.random.rand(10, 2)
d3=pd.DataFrame(data, columns=["Population", "Rain Consistency"])
x.bar_chart(sel)
y.bar_chart(d3)
y.area_chart(d3)
x.line_chart(d3)
st.divider()
st.markdown("The line chart above compares the population and urban water resources of different cities in Odisha. The area chart illustrates the distribution of water resources across these cities. These visualizations provide insights into the water requirements of urban areas and the challenges associated with meeting the growing demand for water. For more detailed information, refer to the table below.")
st.write(df)
x.image('wc1.jpg')
y.image('wc2.jpeg')
st.toast("Population vs Water Resources page is all about the comparison of population and water resources")