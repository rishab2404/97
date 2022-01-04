# Open Sublime text editor, create a new Python file, copy the following code in it and save it as 'census_main.py'.

# Import Streamlit and other required modules
import numpy as np
import pandas as pd
import streamlit as st

@st.cache()
def load_data():
	# Load the Adult Income dataset into DataFrame.

	cenus_df = pd.read_csv('adult.csv', header=None)
	cenus_df.head()

	# Rename the column names in the DataFrame using the list given above. 

	# Create the list
	column_name =['age', 'workclass', 'fnlwgt', 'education', 'education-years', 'marital-status', 'occupation', 'relationship', 'race','gender','capital-gain', 'capital-loss', 'hours-per-week', 'native-country', 'income']

	# Rename the columns using 'rename()'
	for i in range(cenus_df.shape[1]):
	  cenus_df.rename(columns={i:column_name[i]},inplace=True)

	# Print the first five rows of the DataFrame
	cenus_df.head()

	# Replace the invalid values ' ?' with 'np.nan'.

	cenus_df['native-country'] = cenus_df['native-country'].replace(' ?',np.nan)
	cenus_df['workclass'] = cenus_df['workclass'].replace(' ?',np.nan)
	cenus_df['occupation'] = cenus_df['occupation'].replace(' ?',np.nan)

	# Delete the rows with invalid values and the column not required 

	# Delete the rows with the 'dropna()' function
	cenus_df.dropna(inplace=True)

	# Delete the column with the 'drop()' function
	cenus_df.drop(columns='fnlwgt',axis=1,inplace=True)

	return cenus_df

census_df=load_data()

# Create the Page Navigator for 'Home' and 'Visualise Data' web pages in 'census_main.py'
# Import 'census_home.py' and 'census_plots.py' .
import census_home
import census_plots
# Adding a navigation in the sidebar using radio buttons
# Create a dictionary.
pages_dict={"Home":census_home,"Visualise Data": census_plots}

# Add radio buttons in the sidebar for navigation and call the respective pages based on user selection.
st.sidebar.subheader("Navigation")
user_choice=st.sidebar.radio("Go to",(pages_dict.keys()))

if user_choice=="Home":
  census_home.app(census_df)
else:
  census_plots.app(census_df) 