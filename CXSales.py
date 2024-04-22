import time
import streamlit as st

st.set_page_config(
    page_title="Oracle CX Sales Chat",
    layout="wide",                      # "centered" or "wide"
    initial_sidebar_state="collapsed",   #"auto", "expanded", or "collapsed"
)
st.markdown(
    """
    <style>
    .reportview-container {
        background-color: #FBF9F8;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# st.title("Hello")

if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

if prompt := st.chat_input("Enter a prompt for analysis eg: Summarize the sales data by month"):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):
        if st.session_state.messages[-1]["content"]=="What is the distribution of deal values across different quarters?":
            bot_response = """The dataset includes opportunities from various quarters, including Q1 2023, Q3 2021, Q4 2023, and Q1 2024. The distribution of deal values across these quarters varies. For example, in Q1 2023, there are deals ranging from $27,000 to $243,900, while in Q3 2021, the deals range from $212,542 to $297,126. The dataset also includes a few outliers, such as a $0 deal in Q1 2024 and a $100 deal in Q3 2021.  \nTo visualize the distribution of deal values across different quarters, a box plot or a histogram could be created, grouping the data by the quarter and displaying the range, median, and potential outliers for each quarter."""
            with st.spinner('Analyzing...'):
                time.sleep(3)
            st.write(bot_response)
        elif st.session_state.messages[-1]["content"]=="show the visualization":
            bot_response = """Here's a box plot showing the distribution of deal values across different quarters:  \nThe box plot provides insights into the distribution of deal values for each quarter included in the dataset. The boxes represent the interquartile range (IQR), with the line in the middle indicating the median value. The whiskers extend to show the range of values, excluding any outliers, which are represented as individual points.  \nFrom the visualization, we can observe that:  \n- Q3 2021 had the highest median deal value, followed by Q1 2023 and Q2 2023.
- Q1 2024 had the lowest median deal value, with a relatively narrow range.
- Q3 2021 had the widest range of deal values, with some outliers on the higher end.
- Q4 2023 and Q2 2024 seem to have similar distributions, with Q4 2023 having a slightly higher median."""
            with st.spinner('Analyzing...'):
                time.sleep(3)
            st.write(bot_response)
        elif st.session_state.messages[-1]["content"]=="What actions can be taken based on the above visualizations?":
            bot_response = """Based on the visualizations and the dataset provided, here are some possible actions that could be considered:


- __Focus on High-Value Opportunities__: The visualizations highlight the variation in deal values across different quarters and owners. It might be beneficial to focus on high-value opportunities, especially those owned by Sophia Sales Rep and Jane Solis, as they seem to have consistently higher deal values.
- __Sales Strategies and Training__: Analyzing the distribution of deal values can help identify areas for improvement in sales strategies and training. For instance, the low median deal value in Q1 2024 could prompt a review of the sales approach for that quarter.
- __Resource Allocation__: Understanding the distribution of deal values can aid in allocating resources effectively. Owners with higher deal values, such as Sophia Sales Rep and Jane Solis, may require additional support or resources to maximize their potential.
- __Sales Target Setting__: The visualizations can assist in setting realistic sales targets for future quarters. For example, based on the median and range of deal values, sales targets can be adjusted to align with historical trends and expectations.
- __Performance Evaluation__: The data and visualizations can be used to evaluate the performance of different sales owners and identify top performers. This information can then be used to recognize successful strategies and share best practices across the team.
- __Customer Segmentation__: Analyzing deal values can help identify customer segments that tend to have higher or lower deal values. This information can be used to tailor sales and marketing strategies accordingly, focusing on the most valuable customer segments."""
            with st.spinner('Analyzing...'):
                time.sleep(3)
            st.write(bot_response)
        elif st.session_state.messages[-1]["content"]=="Create an opportunity dashboard summary for current quarter":
            bot_response = """Here's an opportunity dashboard for the current quarter (Q2 2024):


__Summary Statistics:__

- Total Opportunities: 4
- Total Value: $2,375,096.64
- Average Value per Opportunity: $593,774.16
- Median Value per Opportunity: $244,800

__Opportunity Stage Breakdown:__

- Open: 2 opportunities, $1,960,000 total value
- Negotiation: 1 opportunity, $269,804.79 total value
- Agreement: 1 opportunity, $198,450.35 total value

__Opportunities by Owner:__

- Sara Sales Rep: 3 opportunities, $1,748,250.35 total value
- Sales Admin: 1 opportunity, $620,000 total value

__Opportunities by Customer:__

- United States: 4 opportunities, $2,375,096.64 total value"""
            with st.spinner('Analyzing...'):
                time.sleep(3)
            st.write(bot_response)






        st.session_state.messages.append({"role": "assistant", "content": bot_response})
