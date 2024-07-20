import streamlit as st
import pandas as pd

st.subheader("Drought in Odisha")
st.markdown("Odisha faces frequent droughts, particularly in western districts like Bolangir and Kalahandi. These dry spells can significantly impact agriculture, the main source of income for many residents. The state government and disaster management authorities work together to monitor droughts, provide assistance to farmers, and implement mitigation strategies.")
st.divider()
df=pd.read_excel("drought.xlsx")
d=pd.DataFrame(df)
st.map(d)

st.divider()

st.subheader("Statistical Data")
st.markdown("Lacking water supply in Odisha has led to significant crop losses, severely impacting the agricultural sector. Farmers, dependent on consistent irrigation, face dwindling yields as droughts and erratic rainfall disrupt growth cycles. This water scarcity not only diminishes the quantity of produce but also its quality, affecting the livelihood of countless farmers. Consequently, the economic stability of the region is threatened, exacerbating poverty and food insecurity.")
x,space,y=st.columns((1,0.6,1))
df2=pd.read_csv("fdata.csv")
d2=pd.DataFrame(df2)
selec=d2[['Crop_Year','Production']]
se=d2[['Area','Production']]
s=[['area']]
x.line_chart(selec)
y.line_chart(se)
x.area_chart(se)
y.bar_chart(selec)
st.divider()
st.markdown("The charts above illustrate the impact of water scarcity on crop production in Odisha. The line chart shows the production of various crops over the years, while the bar chart compares the production of different crops in the state. The area chart displays the area under cultivation for different crops. These visualizations highlight the challenges faced by farmers due to water shortages and the resulting decline in agricultural output.But for more statistical data you can go for the tabular data")
st.write(df2)
st.toast("Water crisis page is all about the drought and its impact on agriculture")

