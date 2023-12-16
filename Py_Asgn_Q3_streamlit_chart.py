import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.set_option('deprecation.showPyplotGlobalUse', False)

def plot_graph(df):
    #st.header("Plotting the Histogram")
    #st.bar_chart(df, y=['age'])
    counts, edges, bars = plt.hist(df['age'], bins=20, color='skyblue', edgecolor='black')
    plt.xlabel('Age')
    plt.ylabel('Frequency')
    plt.title('Age Distribution')
    plt.bar_label(bars)
    st.pyplot()



uploaded_file = st.file_uploader("Choose a CSV file to upload ", accept_multiple_files=False, type=["csv"])
if uploaded_file is not None:
    dataframe = pd.read_csv(uploaded_file)
    cols = dataframe.columns
    cols_new = {x: x.lower().strip() for x in cols}
    dataframe.rename(columns=cols_new, inplace=True)
    dataframe = dataframe.convert_dtypes()
    
    selcted_col = ['name', 'age']
    if len([x for x in dataframe.columns if x in selcted_col])!=2:
        dataframe = None
        st.toast('Uploaded file does not have "name" and "age" column', icon="🔥")
    else:
        dataframe = dataframe[selcted_col]
        st.toast('File Validation Successful', icon='😍')
        st.divider()


        st.header("Name and Age data as per below")
        
        st.text("Data has "+ str(dataframe.shape[0])+" rows and 2 columns")
        st.text("Below are few samples")

        st.write(dataframe.head())
        st.divider()
        plot_graph(dataframe)



