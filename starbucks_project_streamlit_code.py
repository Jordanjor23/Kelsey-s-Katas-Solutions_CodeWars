

"""## Homepage ⭐


"""

# Home Page
if page == "Home":
    st.title("📊 Starbucks Data Analysis Project")
    st.subheader("Welcome to my Starbucks Data Analysis Project app!")
    st.write("""
        This app provides an interactive platform to explore the Starbucks dataset.
        You can visualize the distribution of data, explore relationships between different columns and rows in the dataset, and even learn nutritional facts about the
        delicious Starbucks menu.
    """)
    st.image('https://images.app.goo.gl/GGNuLB4K1p2w8Laz6', caption="Starbucks Drinks")

import streamlit as st
import pandas as pd
import plotly.express as px

# Set page title and icon
st.set_page_config(page_title="Home", page_icon="🌸")

import streamlit as st

# Sidebar for navigation
page = st.sidebar.selectbox("Select a Page", ["Home", "Overview of the Data", "EDA", "Data Visualizations","Final Thoughts"])

# Display different pages based on selection
if page == "Home":
    st.title("Welcome to the Home Page")
    st.write("Welcome to the Home Page of my steamlit. The focus of this app is to complete a data analysis of a Starbucks dataset that covers nutritional information. Enjoy!")

elif page == "Overview of the Data":
    st.title("Overview of the Data")
    st.write("This page provides an Overview of the Dataset.")

elif page == "EDA":
    st.title("Exploratory Data Analysis (EDA)")
    st.write("This page provides elements of the Exploratory Data Analysis (EDA) for the Starbucks data project.")

elif page == "Data Visualizations":
    st.title("Data Visualizations")
    st.write("This page is home to the Data Visualizations for the Starbucks Data Analysis Project.")


elif page == "Final Thoughts":
    st.title("Final Thoughts")
    st.write("This page will discuss Final Thoughts about the Starbucks Data Analysis project.")

"""## Overview of the Data 📊"""

# Data Overview
if page == "Home":
    st.title("Welcome to the Homepage")
elif page == "Overview of the Data":
    st.title("🔢 Overview of the Data")
    st.subheader("About the Data")

    st.subheader("About the Data")
    st.write("""
        The Starbucks dataset provides nuturiontal information about the famous Starbucks menu.
        It contains 240 rows of Starbucks menu items ranging from (Frappuccino® Blended Coffee, Tazo® Tea Drinks, and  Classic Espresso Drinks).
        For each drink on the menu, the dataset includes nutritional information like calories, vitamin count, and cafeine level.
    """)
    st.image('https://images.app.goo.gl/GGNuLB4K1p2w8Laz6', caption="Starbucks Drinks")

    # Dataset Display

    starbucks = pd.read_csv('/gdrive/MyDrive/M8-Mini-Project-Starbucks-EDA/data/Copy of cleaned_starbucks.csv')
    st.subheader("Quick Glance at the Data")
    if st.checkbox("Show DataFrame"):
        st.dataframe(starbucks)


    # Shape of Dataset
    if st.checkbox("Show Shape of Data"):
        st.write(f"The dataset contains {starbucks.shape[240]} rows and {starbucks.shape[18]} columns.")

  ##info
starbucks.info()

# Create a sample DataFrame
starbucks = pd.DataFrame(starbucks.info())

# Title
st.title("Starbucks Dataset: Info")

# About the Dataset
st.write("The following dataframe illustrates the different Columns, Non-Null Count, and Dtypes for the data set. This information is very useful when exploring the data set. The 'info' view alows the data analyst to see the different types of columns and data types that can be utilized for the analysis.")
st.dataframe(starbucks)
starbucks.head()


# Describe the Dataset
st.title("Starbucks Dataset: Describe")
st.write("The following dataframe illustrates the description of the dataset. The attribute '.describe' is used with libraries like Pandas to display relevant information about the rows and columns in the dataset.")

starbucks_data = pd.read_csv('/gdrive/MyDrive/M8-Mini-Project-Starbucks-EDA/data/Copy of cleaned_starbucks.csv')

# Display the Description of the Dataset
st.title("Starbucks Dataset: Describe")
st.write("The following dataframe illustrates the description of the dataset. The attribute '.describe' is used with libraries like Pandas to display relevant information about the rows and columns in the dataset.")
st.dataframe(starbucks_data.describe())

import pandas as pd

starbucks = pd.read_csv('/gdrive/MyDrive/M8-Mini-Project-Starbucks-EDA/data/Copy of cleaned_starbucks.csv')

import streamlit as st

# Create a sample DataFrame
starbucks = pd.DataFrame(starbucks.head(240))

# Title
st.title("Starbucks Dataset")

# About the Dataset
st.write("The following dataframe illustrates information about the Starbucks menu the name of the beverage, the calorie amount, and other dietary information.")
st.dataframe(starbucks)
starbucks.head()

#info
starbucks.info()

import streamlit as st

# Create a sample DataFrame
starbucks = pd.DataFrame(starbucks.info())

# Title
st.title("Starbucks Dataset: Info")

# About the Dataset
st.write("The following dataframe illustrates the different Columns, Non-Null Count, and Dtypes for the data set. This information is very useful when exploring the data set. The 'info' view alows the data analyst to see the different types of columns and data types that can be utilized for the analysis.")
st.dataframe(starbucks)
starbucks.head()

import pandas as pd
import streamlit as st
starbucks_data = pd.read_csv('/gdrive/MyDrive/M8-Mini-Project-Starbucks-EDA/data/Copy of cleaned_starbucks.csv')

# Display the descriptive statistics
st.title("Starbucks Dataset: Describe")
st.write("The following dataframe illustrates the description of the dataset. The attribute '.describe' is used with libraries like Pandas to display relevant information about the rows and columns in the dataset.")
st.dataframe(starbucks_data.describe())

"""## Exploratory Data Analysis (EDA) 📊

## Data Visualizations 📊

## Final Thoughts 📊
"""

