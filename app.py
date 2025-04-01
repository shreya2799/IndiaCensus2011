import streamlit as st
import numpy as np
import pandas as pd
import plotly.express as px

st.set_page_config(layout='wide')
st.sidebar.title("India's Data Visualisation")

df=pd.read_csv('india_alldata.csv')
list_of_states=list(df['State'].unique())
list_of_states.insert(0,'Overall India')

selected_state=st.sidebar.selectbox('Select a state',list_of_states)
primary=st.sidebar.selectbox("Select Primary feature",sorted(df.columns[5:]))
secondary=st.sidebar.selectbox("Select Secondary feature",sorted(df.columns[5:]))


plot=st.sidebar.button('Plot Graph')

if plot:
    st.text('Color represents primary paramter.'
            'Size represents secondary parameter.')
    if selected_state=='Overall India':
        fig=px.scatter_mapbox(df,lat="Latitude", lon="Longitude",color=primary,size=secondary,zoom=4,color_discrete_sequence=["fuchsia"],mapbox_style='carto-positron',width=1200,height=700,hover_name='District')
        st.plotly_chart(fig,use_container_width=True)
        #plot for entire india

    else:
        temp=df[df['State']==selected_state]
        fig = px.scatter_mapbox(temp, lat="Latitude", lon="Longitude", color=primary, size=secondary, zoom=4,color_discrete_sequence=["fuchsia"],mapbox_style='carto-positron',width=1200,height=700,hover_name='District')
        st.plotly_chart(fig)
        #plot for selected state
