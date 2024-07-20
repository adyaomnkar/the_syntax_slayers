import streamlit as st
import numpy as np
import pandas as pd


st.set_page_config(
    page_title="Water Supply and resource",
    page_icon="🌊",
    layout="centered",
    initial_sidebar_state="auto",
)
st.header("🚰 Aquatic Infrastructure and Resource Management")
st.subheader("Ensuring sustainable management of Odisha's abundant water resources for agriculture, industry, and daily life.")

st.divider()
slide=st.selectbox('Water resources of Odisha',options=['Hydrogeology','Natural Topography','Groundwater Utilisation','River Basin'])
if slide=='Hydrogeology':
    st.write("Odisha is endowed with rich water resources in the form of rivers, lakes, ponds, and groundwater. The state has 11 major rivers, 11000 km of waterways, 480 km of coastline, 5 major river basins, 3 major reservoirs, and 61 minor reservoirs. The state has a total of 1,92,000 water bodies, including 1,10,000 ponds, 1,000 lakes, 5 major rivers, and 11,000 km of waterways. The state has a total of 1,92,000 water bodies, including 1,10,000 ponds, 1,000 lakes, 5 major rivers, and 11,000 km of waterways.")
    st.image("hydro.png")
elif slide=='Natural Topography':
    st.write("The state of Odisha has a diverse topography, with the Eastern Ghats, the Central Plateau, and the Coastal Plains. The Eastern Ghats are a mountain range that runs parallel to the coast of the Bay of Bengal, while the Central Plateau is a hilly region that lies between the Eastern Ghats and the Coastal Plains. The Coastal Plains are a low-lying region that stretches along the coast of the Bay of Bengal.")
    st.image("topo.png")
elif slide=='Groundwater Utilisation':
    st.write("Groundwater is an important source of water for agriculture, industry, and daily life in Odisha. The state has a total of 3,000 million cubic meters of groundwater, with an annual recharge of 2,000 million cubic meters. The state has a total of 3,000 million cubic meters of groundwater, with an annual recharge of 2,000 million cubic meters. The state has a total of 3,000 million cubic meters of groundwater, with an annual recharge of 2,000 million cubic meters.")
    st.image("gw1.jpeg")
elif slide=='River Basin':
    st.write("Odisha has 5 major river basins, including the Mahanadi, Brahmani, Baitarani, Subarnarekha, and Rushikulya. The Mahanadi is the largest river basin in the state, with a total length of 851 km and a catchment area of 1,41,600 sq km. The Brahmani is the second-largest river basin in the state, with a total length of 799 km and a catchment area of 39,033 sq km. The Baitarani is the third-largest river basin in the state, with a total length of 360 km and a catchment area of 12,000 sq km.")
    st.image("basin.jpg")
    
st.divider()

c, space, d = st.columns((1, 0.4, 1))

c.write("𝘛𝘩𝘪𝘴 𝘤𝘢𝘯𝘢𝘭 𝘴𝘺𝘴𝘵𝘦𝘮 𝘴𝘦𝘳𝘷𝘦𝘴 𝘢𝘴 𝘢 𝘷𝘪𝘵𝘢𝘭 𝘸𝘢𝘵𝘦𝘳 𝘴𝘶𝘱𝘱𝘭𝘺 𝘧𝘰𝘳 𝘵𝘩𝘦 𝘴𝘵𝘢𝘵𝘦 𝘰𝘧 𝘖𝘥𝘪𝘴𝘩𝘢. 𝘐𝘵 𝘦𝘯𝘴𝘶𝘳𝘦𝘴 𝘵𝘩𝘦 𝘥𝘪𝘴𝘵𝘳𝘪𝘣𝘶𝘵𝘪𝘰𝘯 𝘰𝘧 𝘸𝘢𝘵𝘦𝘳 𝘳𝘦𝘴𝘰𝘶𝘳𝘤𝘦𝘴 𝘧𝘰𝘳 𝘢𝘨𝘳𝘪𝘤𝘶𝘭𝘵𝘶𝘳𝘢𝘭, 𝘪𝘯𝘥𝘶𝘴𝘵𝘳𝘪𝘢𝘭, 𝘢𝘯𝘥 𝘥𝘰𝘮𝘦𝘴𝘵𝘪𝘤 𝘶𝘴𝘦. 𝘛𝘩𝘪𝘴 𝘪𝘯𝘧𝘳𝘢𝘴𝘵𝘳𝘶𝘤𝘵𝘶𝘳𝘦 𝘪𝘴 𝘤𝘳𝘶𝘤𝘪𝘢𝘭 𝘧𝘰𝘳 𝘵𝘩𝘦 𝘳𝘦𝘨𝘪𝘰𝘯'𝘴 𝘥𝘦𝘷𝘦𝘭𝘰𝘱𝘮𝘦𝘯𝘵 𝘢𝘯𝘥 𝘴𝘶𝘴𝘵𝘢𝘪𝘯𝘢𝘣𝘪𝘭𝘪𝘵𝘺")
st.empty()
st.empty()
c.image("drain.png")

ele=st.empty()

d.write("𝘛𝘩𝘦 𝘯𝘢𝘵𝘶𝘳𝘢𝘭 𝘸𝘢𝘵𝘦𝘳 𝘳𝘦𝘴𝘰𝘶𝘳𝘤𝘦𝘴 𝘪𝘯 𝘖𝘥𝘪𝘴𝘩𝘢, 𝘪𝘯𝘤𝘭𝘶𝘥𝘪𝘯𝘨 𝘳𝘪𝘷𝘦𝘳𝘴, 𝘭𝘢𝘬𝘦𝘴, 𝘢𝘯𝘥 𝘨𝘳𝘰𝘶𝘯𝘥𝘸𝘢𝘵𝘦𝘳, 𝘢𝘳𝘦 𝘢𝘣𝘶𝘯𝘥𝘢𝘯𝘵 𝘢𝘯𝘥 𝘥𝘪𝘷𝘦𝘳𝘴𝘦. 𝘛𝘩𝘦𝘴𝘦 𝘳𝘦𝘴𝘰𝘶𝘳𝘤𝘦𝘴 𝘢𝘳𝘦 𝘤𝘳𝘶𝘤𝘪𝘢𝘭 𝘧𝘰𝘳 𝘢𝘨𝘳𝘪𝘤𝘶𝘭𝘵𝘶𝘳𝘦, 𝘪𝘯𝘥𝘶𝘴𝘵𝘳𝘺, 𝘢𝘯𝘥 𝘥𝘢𝘪𝘭𝘺 𝘭𝘪𝘧𝘦, 𝘮𝘢𝘬𝘪𝘯𝘨 𝘦𝘧𝘧𝘦𝘤𝘵𝘪𝘷𝘦 𝘮𝘢𝘯𝘢𝘨𝘦𝘮𝘦𝘯𝘵 𝘦𝘴𝘴𝘦𝘯𝘵𝘪𝘢𝘭 𝘧𝘰𝘳 𝘴𝘶𝘴𝘵𝘢𝘪𝘯𝘢𝘣𝘭𝘦 𝘥𝘦𝘷𝘦𝘭𝘰𝘱𝘮𝘦𝘯𝘵 𝘢𝘯𝘥 𝘦𝘤𝘰𝘭𝘰𝘨𝘪𝘤𝘢𝘭 𝘣𝘢𝘭𝘢𝘯𝘤𝘦 𝘪𝘯 𝘵𝘩𝘦 𝘳𝘦𝘨𝘪𝘰𝘯.")
d.image("river.png")
st.toast("Home page is all about knowledge")


tab1, tab2 = st.tabs(["News", "Blogs"])
tab1.subheader("Odisha Launches Major Water Conservation Initiative")
p1="""
Bhubaneswar, June 14, 2024 – The Odisha government has unveiled a comprehensive water conservation initiative aimed at tackling the state's perennial water scarcity issues. The program, named "Jala Suraksha Abhiyan," focuses on rainwater harvesting, rejuvenation of traditional water bodies, and the introduction of efficient irrigation practices.

Chief Minister Naveen Patnaik announced the initiative, emphasizing its importance in ensuring sustainable water management for the state's agrarian economy. "We are committed to making Odisha water-sufficient. This initiative will not only conserve water but also enhance agricultural productivity," he stated.

The initiative includes the construction of over 1,000 check dams, the renovation of existing ponds and tanks, and community awareness programs on water conservation practices. The state government has allocated Rs 500 crore for the project, with support from central government schemes and international agencies.


"""
tab1.write(p1)
tab1.subheader("Mahanadi River Basin Faces Severe Water Crisis Amidst Rising Temperatures")
p2="""
Cuttack, June 14, 2024 – The Mahanadi River Basin is experiencing an unprecedented water crisis, exacerbated by soaring temperatures and delayed monsoon rains. The water levels in Hirakud Dam, a critical reservoir in the region, have dropped to historic lows, raising alarms among farmers and residents dependent on the river.

Experts attribute the crisis to a combination of climate change, over-extraction of groundwater, and inefficient water management practices. "The situation is dire. We need immediate measures to manage the existing water resources and long-term plans to mitigate the impacts of climate change," said Dr. Ramesh Chandra, a hydrologist at Utkal University.

The state government has urged farmers to adopt water-saving irrigation techniques and has expedited the release of funds for water conservation projects. Meanwhile, relief measures, including water tankers and emergency supplies, are being deployed in the most affected areas.



"""
tab1.write(p2)
tab1.subheader("Odisha's Groundwater Levels Decline, Prompting Urgent Action Plans")
p3="""
Bhubaneswar, June 14, 2024 – Recent studies have shown a significant decline in groundwater levels across Odisha, prompting the state government to draft urgent action plans to address the issue. The Central Ground Water Board's report indicates that the depletion is particularly severe in the western and southern districts.

In response, the government has announced a series of measures including strict regulation of borewell drilling, promotion of rainwater harvesting systems, and the rejuvenation of dried-up wells and ponds. "Groundwater is a critical resource for our state. We need to implement these measures swiftly to prevent further depletion," said Minister of Water Resources, Raghunandan Das.

The state is also seeking assistance from the World Bank and other international organizations to fund large-scale water recharge projects. Additionally, a statewide awareness campaign on water conservation practices is set to be launched to engage communities in the preservation efforts.

"""
tab1.write(p3)
tab1.subheader("Odisha's Chilika Lake Under Threat: Urgent Need for Water Management Reforms")
p4="""
Puri, June 14, 2024 – Chilika Lake, Asia's largest brackish water lagoon, is facing serious ecological threats due to water mismanagement and pollution. A recent study by the Chilika Development Authority (CDA) highlights alarming levels of salinity fluctuations and contamination from industrial and agricultural runoff.

The lake, which supports a diverse range of wildlife and serves as a vital source of livelihood for local fishing communities, is at risk of losing its ecological balance. "Immediate action is required to control pollution and manage the water resources feeding into Chilika. We are working on a comprehensive plan to restore the health of the lake," said CDA Chief Executive Officer, Dr. Ajit Patnaik.

The proposed plan includes stricter regulation of industries along the lake's periphery, promotion of organic farming practices in the surrounding areas, and the construction of treatment plants to filter out pollutants. Community involvement and continuous monitoring will be key components of the lake's restoration strategy.
"""
tab1.write(p4)

p5="""
Odisha, with its vast network of rivers including the Mahanadi, Brahmani, and Baitarani, boasts a rich water resource landscape that is crucial for the state's economy and ecology. These rivers are not only lifelines for agricultural and domestic needs but also hold immense potential for sustainable development. This blog explores the significance of Odisha’s rivers, the opportunities they present, and the challenges that need to be addressed for optimal management.

The Lifeblood of Odisha: Importance of Rivers

Rivers in Odisha play a pivotal role in supporting agriculture, which is the backbone of the state's economy. They provide essential irrigation to farmlands, enabling the cultivation of various crops. Additionally, these rivers are vital for fisheries, which support the livelihoods of many local communities. Urban centers like Cuttack and Bhubaneswar rely heavily on river water for their domestic and industrial needs, underscoring the importance of these water bodies in everyday life.

Opportunities: Maximizing the Potential

Hydropower Generation

Odisha’s rivers hold significant potential for hydropower generation. The Hirakud Dam on the Mahanadi River is a prime example of how hydropower can be harnessed. Expanding such projects, particularly with small-scale, decentralized hydropower plants, can provide a sustainable and clean energy source, reducing dependence on fossil fuels.

Irrigation Projects

Enhancing and modernizing the irrigation infrastructure can boost agricultural productivity. There is a need to develop new irrigation canals and improve existing ones. Advanced irrigation techniques like drip and sprinkler systems can ensure efficient water use, reducing wastage and ensuring that water reaches more areas effectively.

Ecotourism

The scenic beauty and biodiversity of Odisha’s rivers offer excellent opportunities for ecotourism. River cruises, wildlife safaris, and cultural tours can attract tourists, generating revenue and promoting conservation. Ecotourism can also raise awareness about the importance of preserving river ecosystems.

Challenges: Addressing the Issues

Pollution

Pollution is a major threat to Odisha’s rivers. Industrial discharge, agricultural runoff, and domestic sewage are the primary pollutants. To combat this, stringent pollution control measures are necessary. Establishing efficient waste management systems and treatment plants can significantly reduce the pollution levels in these rivers.

Climate Change

Climate change poses a significant challenge to river management in Odisha. Altered rainfall patterns and increased frequency of extreme weather events such as floods and droughts affect river flows and water availability. Developing climate-resilient infrastructure and adaptive management practices can help mitigate these impacts.

Conflict Over Water Use

With agriculture, industry, and domestic sectors all vying for water, conflicts over water use are inevitable. An integrated water resource management framework is needed to balance these competing demands. This involves coordinated efforts among various stakeholders to ensure equitable and sustainable use of water resources.

Conclusion

Harnessing the potential of Odisha's rivers offers immense opportunities for sustainable development. However, it also requires addressing significant challenges. By implementing a holistic approach that includes technological innovations, stringent pollution control, adaptive management practices, and community involvement, Odisha can ensure that its rivers continue to support the state's economy and ecology. This balance is crucial for the prosperity and well-being of future generations.



"""

tab2.subheader("Harnessing the Potential of Odisha’s Rivers: Opportunities and Challenges")
tab2.write(p5)