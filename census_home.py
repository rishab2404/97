# Show complete dataset and summary in 'census_home.py'
# Import necessary modules.
import numpy as np
import pandas as pd
import streamlit as st
# Define a function 'app()' which accepts 'census_df' as an input.
def app(census_df):
  # View Dataset Configuration

  # Add an expander and display the dataset as a static table within the expander.
  st.subheader("View Data")
  with st.beta_expander("View Dataset"):
    st.dataframe(census_df)

  # Create three beta_columns.
  beta_col1, beta_col2, beta_col3 = st.beta_columns(3)
  # Add a checkbox in the first column. Display the column names of 'census_df' on the click of checkbox.
  with beta_col1:
    if st.checkbox("Show all Column names"):
      st.table(list(census_df.columns))

  # Add a checkbox in the second column. Display the column data-types of 'census_df' on the click of checkbox.
  with beta_col2:
    if st.checkbox("View column data-type"):
      cols_name = st.selectbox("Select Column for data-type",list(census_df.columns))
      st.text(census_df[cols_name].dtype)

  # Add a checkbox in the third column followed by a selectbox which accepts the column name whose data needs to be displayed.
  with beta_col3:
    if st.checkbox("view Column Data"):
      col_name = st.selectbox("Select Column for Data",list(census_df.columns))
      st.table(census_df[col_name])


  # Display summary of the dataset on the click of checkbox.
  if st.checkbox("Show Summary"):
    st.table(census_df.describe())