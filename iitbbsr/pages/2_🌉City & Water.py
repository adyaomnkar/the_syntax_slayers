import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# City data (replace with your actual data)
data = {
    "City": [
        "Bolangir", "Bargarh", "Nuapada", "Kalahandi", "Nabarangpur", "Angul",
        "Gajapati", "Kandhamal", "Sundargarh", "Bhawanipatna (Kalahandi)",
        "Junagarh (Kalahandi)", "Nuapada Town", "Khariar (Nuapada)",
        "Paralakhemundi (Gajapati)", "Rayagada (Gajapati)", "Phulbani (Kandhamal)",
        "Boudh (Kandhamal)", "Sundargarh Town", "Rourkela (Sundargarh)"
    ],
    "Population": [
        768549, 657828, 316158, 1245762, 874657, 1017980,
        532413, 660285, 2076937, 154621, 89342, 71509, 44789,
        107384, 105562, 102845, 75946, 109586, 538845
    ],
    "Water Needed (Liters per Day)": [
        115282350, 98674200, 47423700, 186864300, 131198550, 152697000,
        79862950, 99042750, 311540550, 23193150, 13401300, 10726350,
        6718350, 16107600, 15834300, 15426750, 11391900, 16437900, 80826750
    ]
}

df = pd.DataFrame(data)

# Chart title
st.title("City Water Needs in Odisha (Drought Area)")

# Selectbox for city selection
selected_city = st.selectbox("Select a City:", df["City"].unique())

# Filter data for selected city
filtered_df = df[df["City"] == selected_city]

# Display population and water needs for selected city
st.subheader(f"Selected City: {selected_city}")
population = filtered_df["Population"].values[0]
water_need = filtered_df["Water Needed (Liters per Day)"].values[0]
st.write(f"Population: {population:,}")  # Use comma separator for readability
st.write(f"Water Needed (Liters per Day): {water_need:,}")

# Optional: Line chart for water needed over time (replace with your data)
# Comment out if not needed
water_need_data = [100000, 120000, 135000, 150000, 148000]  # Sample data (replace)
st.line_chart(water_need_data)

# Optional customization using Matplotlib (explained earlier)
# Comment out the following lines if you don't need customization

# Create a Matplotlib figure and axis for the line chart (optional)
fig, ax = plt.subplots()
ax.plot(water_need_data)  # Assuming water_need_data represents time series

# Set labels and title (optional)
ax.set_xlabel('Time')
ax.set_ylabel('Water Needed (Liters)')
ax.set_title('Water Needed Over Time (Sample)')

# Customize grid and appearance (optional)
ax.grid(True)

# Display the Matplotlib chart in Streamlit (requires additional setup)
st.pyplot(fig)

st.toast("This page is for water supplying officers")
a,space,b=st.columns((1,0.6,1))
st.divider()

