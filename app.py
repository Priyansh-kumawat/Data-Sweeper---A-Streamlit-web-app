#Importing the libraries 

import pandas as pd
import streamlit as st
import os 
from io import BytesIO # used to create buffer for our files and store the data in form of binary digits 
                       # which make easier to convert them into different format.

#set up our app
st.set_page_config(page_title=" Data Sweeper", layout='wide')
st.title("Data Sweeper")
st.write("Transform your files like CSV and Excel formats with built-in techniques like data cleaning , Feature Engineering and Data Visualization")

#Uploading 
uploaded_files = st.file_uploader("Upload your files (CSV or Excel):", type=["csv","xlsx"],accept_multiple_files=True)


if uploaded_files:
    for file in uploaded_files:
        file_ext=os.path.splitext(file.name)[-1].lower()

        if file_ext ==".csv":
            df=pd.read_csv(file)

        elif file_ext==".xlsx":
            df=pd.read_excel(file)
        else:
            st.error(f"Unsuppoerted file format:{file_ext}")
            continue

        #Displaying info of file
        st.write(f"**File Name:** {file.name}")
        st.write(f"**File Size:** {file.size/1024}")

        #Showing the head of dataset
        st.write("Preview the Head of the Dataframe")
        st.dataframe(df.head())
        
        #Showing the shape of dataset
        st.write("Preview the shape of Dataframe")
        st.dataframe(df.shape)

        #Showing the summary of dataset
        st.write("Preview the summary of Dataframe")
        st.dataframe(df.describe())

        #Options for Data Cleaning
        st.subheader("Data Cleaning")
        if st.checkbox(f"Clean Data for {file.name}"):
            col1,col2=st.columns(2)
            
            #With is the context manager which open something do it and close it again
            with col1:
                if st.button(f"Remove Duplicates from {file.name} "):
                    df.drop_duplicates(inplace=True)
                    st.write("Duplicates Removed!")

            with col1:
                if st.button(f"Filling Missing Values for {file.name} "):
                    numeric_cols = df.select_dtypes(include=['number']).columns
                    df[numeric_cols]=df[numeric_cols].fillna(df[numeric_cols].mean())
                    st.write("Missing Values replaced with the mean!")

        #Choose specific columns to Keep only relevant columns and convert the dataset
        st.subheader("Feature Engineering ")
        columns =st.multiselect(f"Choose only the relevant columns to be used for study and conversion for {file.name}",df.columns,default=df.columns)
        df = df[columns]

        #Create some visualizations
        st.subheader("Data Visualization")
        if st.checkbox(f"Show Visuals for {file.name}"):
            st.bar_chart(df.select_dtypes(include='number').iloc[:,:2])

        #Convert the file type
        st.subheader("Conversion Options")
        conversion_type=st.radio(f"Convert {file.name} to :",["CSV","EXCEL"],key=file.name)
        if st.button(f"Convert {file.name}"):
            buffer=BytesIO()
            if conversion_type =="CSV":
                df.to_csv(buffer,index=False)
                file_name = file.name.replace(file_ext,".csv")
                mime_type = "text/csv"

            elif conversion_type =="Excel":
                df.to_excel(buffer,index=False)
                file_name = file.name.replace(file_ext,".xlsx")
                mime_type = "application/vnd.ms-excel"
            buffer.seek(0)

            #Download Button
            st.download_button(label=f"Download {file_name} as {conversion_type}",
                               data=buffer,
                               file_name=file_name,
                               mime="mime_type")
            
st.success("Hope it help")
                
            
            
