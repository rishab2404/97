# Import modules
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st

# Write your code to filter streamlit warnings 
st.set_option('deprecation.showPyplotGlobalUse', False)

def app(census_df):
	# Write the code to design the web app
	st.title("Census Data Set")
	# Write the code to design the web app

	# Add title on the main page and in the sidebar.
	st.title("Census Data Visualisation Web App")
	st.sidebar.title("Census Data Visualisation")

	# Using the 'if' statement, display raw data on the click of the checkbox.
	if st.sidebar.checkbox("Show Raw Data"):
	  st.subheader("Census Data Set")
	  st.dataframe(census_df)
	  st.write("Number of Rows: ",census_df.shape[0])
	  st.write("Number of Column: ",census_df.shape[1])

	# Add a multiselect widget to allow the user to select multiple visualisations.
	# Add a subheader in the sidebar with the label "Visualisation Selector"
	st.sidebar.subheader("Visualisation Selector")

	# Add a multiselect in the sidebar with label 'Select the Charts/Plots:'
	# Store the current value of this widget in a variable 'plot_list'.
	plot_list= st.sidebar.multiselect("Select Plot/Chart",("Pie Chart","Box Plot","Count Plot"))

	# Display pie plot using matplotlib module and 'st.pyplot()'
	if 'Pie Chart' in plot_list :
	  st.subheader('Pie Chart')
	  pie_data = census_df['income'].value_counts()
	  plt.figure(figsize=(5,5))
	  plt.pie(pie_data, labels=pie_data.index, autopct='%1.2f%%', startangle=30,explode = np.linspace(.06, .12, 2))
	  plt.title('Distribution of records for the income-group feature.')
	  st.pyplot()

	  pie_data = census_df['gender'].value_counts()
	  plt.figure(figsize=(5,5))
	  plt.pie(pie_data, labels=pie_data.index, autopct='%1.2f%%', startangle=30,explode = np.linspace(.06, .12, 2))
	  plt.title('Distribution of records for the gender feature.')
	  st.pyplot()

	# Display box plot using matplotlib module and 'st.pyplot()'
	if 'Box Plot' in plot_list :
	  st.subheader('Box Plot')
	  plt.figure(figsize=(9,5))
	  plt.title('Box plot for difference in the range of values for the hours-per-week feature for different income groups.')
	  sns.boxplot('hours-per-week', 'income', data=census_df)
	  st.pyplot()
	  
	  plt.figure(figsize=(9,5))
	  plt.title('Box plot for difference in the range of values for the hours-per-week feature for different gender groups.')
	  sns.boxplot('hours-per-week', 'gender', data=census_df)
	  st.pyplot() 


	# Display count plot using seaborn module and 'st.pyplot()' 
	if 'Count Plot' in plot_list :
	  st.subheader('Count Plot')
	  plt.figure(figsize=(9,5))
	  plt.title('Count plot for distribution of records for unique workclass groups')
	  sns.countplot('workclass', data=census_df, hue = 'income')
	  st.pyplot()