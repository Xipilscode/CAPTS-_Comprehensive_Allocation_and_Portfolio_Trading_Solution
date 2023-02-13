# Import dependencies
import streamlit as st
from PIL import Image
import datetime

# create the navigation menu
def navigation():
    page = st.sidebar.selectbox("Choose a page to continue", ["Home", "Step 1", "Step 2", "Step 3"])
    if page == "Home":
        home()
    elif page == "Step 1":
        step_1()
    elif page == "Step 2":
        step_2()
    elif page == "Step 3":
        step_3()

# # Create containers
# st.container(home)
# st.container(step_1)
# st.container(step_2)
# st.container(step_3)

# Define home page container 
def home():
    with st.spinner("Loading Home page..."):
         # Heder image 
        img_header = Image.open("data/images/main_page_1.jpeg")
        st.image(img_header, width=None)

        # Header name of the project w/description
        st.markdown(
        """
        <h2 style="text-align: center;">
        CAPTS: Comprehensive Allocation and Portfolio Trading Solution</h2>
        
        <div style="text-align:justify;">
        This project aims to provide a comprehensive and integrated solution for 
        portfolio allocation, financial analysis and algorithmic trading of three 
        asset classes (crypto, commodities, stocks), consisting of the following 
        3 steps:
        <br/>
        <br/>
        """,
        unsafe_allow_html=True,
        )

        # Header name of Step 1  w/description
        st.markdown(
        """
        <h3 style="text-align: left;">
        Step 1: Capital Allocation Optimization:</h3>
        
        <div style="text-align:justify;">
        The objective of this step is to gather, clean, and analyze data for 3 assets : cryptocurrencies , commodities, and stocks, leveraging financial API such as Yahoo Finance with Pandas. The data will be structured and saved in JSON format, and analyzed and visualized with Numpy and PyViz. The analyzed data will be stored in SQL for future use.
        <br/>
        <br/>
        """,
        unsafe_allow_html=True,
        )
        
        # Header name of Step 2  w/description
        st.markdown(
        """
        <h3 style="text-align: left;">
        Step 2: Machine Learning for Portfolio Optimization: </h3>
        
        <div style="text-align:justify;">
        In this step, machine learning algorithms will be applied to analyze and optimize the portfolio. Techniques such as linear regression, decision trees, and clustering will be used to identify patterns and make predictions about future price movements. Financial metrics, such as Sharpe ratio and Sortino ratio, will also be employed to evaluate and optimize the portfolio.
        <br/>
        <br/>
    
        """,
        unsafe_allow_html=True,
        )

        # Header name of Step 3  w/description
        st.markdown(
        """
        <h3 style="text-align: left;">
        Step 3: GRID Bot for Backtesting and Trading: </h3>
        
        <div style="text-align:justify;">
        In this step , a GRID bot will be developed for backtesting and bug fixing using a paper trading platform. The bot will use the data collected in the first project and insights from the second project to make trades based on various financial strategies, including mean reversion and trend following. The bot's performance will be optimized through algorithmic trading strategies.
        <br/>
        <br/>
        """,
        unsafe_allow_html=True,
        )



# Step 1 page
def step_1():
    with st.spinner("Loading Home page..."):
         # Heder image 
        img_header = Image.open("data/images/main_page_2.jpeg")
        st.image(img_header, width=None)

        # Header name of Step 1  w/description
        st.markdown(
        """
        <h3 style="text-align: left;">
        Step 1: Capital Allocation Optimization:</h3>
        
        <div style="text-align:justify;">
        The objective of this step is to gather, clean, and analyze data for 3 assets : cryptocurrencies , commodities, and stocks, leveraging financial API such as Yahoo Finance with Pandas. The data will be structured and saved in JSON format, and analyzed and visualized with Numpy and PyViz. The analyzed data will be stored in SQL for future use.
        <br/>
        <br/>
        """,
        unsafe_allow_html=True,
        )
        # Prompt user to input capital allocation amount
        capital_sum = st.text_input("How much capital would you like to allocate?")


        # Prompt user to choose assets in asset classes 
        crypto = st.multiselect("Choose cryptocurencies:", options=['BTC-USD', 'ETH-USD', 'DOGE-USD', 'MATIC-USD', 'AVAX-USD', 'SOL-USD', 'TRX-USD', 'ATOM-USD', 'UNI7083-USD', 'LINK-USD'])
        stocks = st.multiselect("Choose stocks:", options=['AMZN', 'AAPL', 'TSLA', 'GOOGL', 'NVDA', 'MSFT', 'TSM', 'META','XOM', 'LAC'])
        comodities = st.multiselect("Choose comodities:", options=['GC=F', 'SI=F', 'CL=F', 'HG=F', 'LBS=F', 'ZS=F', 'GF=F', 'KE=F', 'CT=F', 'ZR=F'])
   
        # Prompt user to choose time period 
        st.write("Please choose the analysis period:" 
                "Please note that you can choose the period only begining forn Jan 1st 2019")

        # Get the current date
        today = datetime.datetime.now().date()

        # Set the earliest allowed start date to January 1st, 2019
        earliest_start_date = datetime.date(2019, 1, 1)

        # Get the user selected start and end dates
        selected_start_date = st.date_input("Select the start date", earliest_start_date)

        # If the selected start date is earlier than the earliest allowed start date, set it to the earliest start date
        if selected_start_date < earliest_start_date:
            selected_start_date = earliest_start_date

        selected_end_date = st.date_input("Select the end date", today)

        # If the selected end date is later than the current date, set it to the current date
        if selected_end_date > today:
            selected_end_date = today

        # If the selected end date is earlier than the selected start date, set the end date to the start date
        if selected_end_date < selected_start_date:
            selected_end_date = selected_start_date

        # Display the selected dates
        st.write("Selected start date:", selected_start_date)
        st.write("Selected end date:", selected_end_date)
       
       
        # st.dadframe(data.pct_change,width=500, height=500)
        # start_date = st.date_input("Start date", min_date, max_date, default_start)
        # end_date = st.date_input("End date", min_date, max_date, default_end)
        # if start_date and end_date:
        #     show_df(start_date, end_date)


        # Prompt user to choose number of simulations
        num_of_simulations = st.slider("Please choose number of simulations:", min_value=5000, max_value=10000, step=1000)

# create a function to show the data frame for the selected period
def show_df(start, end):
    filtered_df = df[start:end]
    return st.dataframe(filtered_df)

# Step 2 page
def step_2():
    st.write("Step 2: Choose the analysis method")
    st.write("Coming soon!")

# Step 3 page
def  step_3():
    st.write("Step 3: View the results")
    st.write("Coming soon!")


# Main function to run the app
def main():
    navigation()
    
    # st.set_page_config(page_title="Data Analysis", page_icon=":chart_with_upwards_trend:", layout="wide")
    # st.title("Data Analysis App")
    # menu = ["Home", "Step 1", "Step 2", "Step 3"]
    # choice = st.sidebar.selectbox("Select a page", menu)
    # if choice == "Home":
    #     home()
    # elif page == "Step 1":
    #     step_1()
    # elif page == "Step 2":
    #     step_2()
    # elif page == "Step 3":
    #     step_3()
# run the app
if __name__ == "__main__":
    main()



