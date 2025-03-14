# # Import necessary tools/libraries
# import streamlit as st  # type: ignore # Imports Streamlit for making web apps
# import random  # Imports random number generator
# import time  # Imports time-related functions
# import requests  # type: ignore # Imports tool for making web requests

# # Set the title of our web app
# st.title("Money Making Machine")


# # Function to create random amount of money
# def generate_money():
#     return random.randint(1, 1000)  # Gives random number between 1 and 1000


# # Create a section for generating money
# st.subheader("Instant Cash Generator")
# if st.button("Generate Money"):  # When user clicks the button
#     st.write("Counting your money...")  # Show loading message
#     time.sleep(5)  # Wait for 5 seconds
#     amount = generate_money()  # Get random amount
#     st.success(f"You made ${amount}!")  # Show success message with amount


# # Function to get side hustle ideas from a server
# def fetch_side_hustle():
#     try:
#         # Try to get data from local server or deployed server
#         response = requests.get(
#             "https://fastapi-api.vercel.app/side_hustles"
#         )
#         if response.status_code == 200:  # If request successful
#             hustles = response.json()  # Convert response to JSON
#             return hustles["side_hustle"]  # Return the hustle idea
#         else:
#             return "Freelancing"  # Default response if server fails

#     except:
#         return "Something went wrong!"  # Error message if request fails


# # Create a section for side hustle ideas
# st.subheader("Side Hustle Ideas")
# if st.button("Generate Hustle"):  # When user clicks button
#     idea = fetch_side_hustle()  # Get a hustle idea
#     st.success(idea)  # Show the idea


# # Function to get money-related quotes from server
# def fetch_money_quote():
#     try:
#         # Try to get quote from local server or deployed server
#         response = requests.get(
#             "https://fastapi-api.vercel.app/money_quotes"
#         )
#         if response.status_code == 200:  # If request successful
#             quotes = response.json()  # Convert response to JSON
#             return quotes["money_quote"]  # Return the quote
#         else:
#             return "Money is the root of all evil!"  # Default quote if server fails
#     except:
#         return "Something went wrong!"  # Error message if request fails


# # Create a section for motivation quotes
# st.subheader("Money-Making Motivation")
# if st.button("Get Inspired"):  # When user clicks button
#     quote = fetch_money_quote()  # Get a quote
#     st.info(quote)  # Show the quote






import streamlit as st  # Imports Streamlit for making web apps
import random  # Imports random number generator
import time  # Imports time-related functions
import requests  # Imports tool for making web requests

# ---- Set Page Configuration ----
st.set_page_config(page_title="Money Making Machine", page_icon="💰", layout="wide")



# ---- App Title ----
st.title("💰 Money Making Machine")
st.markdown("### Generate money, find side hustles, and get inspired!")

# ---- Function to Create Random Money ----
def generate_money():
    return random.randint(50, 5000)  # Generates random amount between 50 and 5000

# ---- Instant Cash Generator Section ----
st.subheader("🤑 Instant Cash Generator")
if st.button("Generate Money 💵"):
    with st.spinner("Counting your money..."):
        time.sleep(3)  # Simulate processing time
        amount = generate_money()
        st.success(f"🎉 You made **${amount}**!")

# ---- Function to Get Side Hustle Ideas ----
def fetch_side_hustle():
    try:
        response = requests.get("https://fastapi-api.vercel.app/side_hustles")
        if response.status_code == 200:
            hustles = response.json()
            return hustles.get("side_hustle", "Freelancing")
        else:
            return "Try Blogging or Online Courses!"
    except:
        return "Could not fetch side hustles, try again later!"

# ---- Side Hustle Ideas Section ----
st.subheader("💼 Side Hustle Ideas")
if st.button("Generate Hustle 💡"):
    with st.spinner("Finding the best hustle for you..."):
        time.sleep(2)
        idea = fetch_side_hustle()
        st.success(f"🚀 Your next hustle: **{idea}**")

# ---- Function to Get Money Quotes ----
def fetch_money_quote():
    try:
        response = requests.get("https://fastapi-api.vercel.app/money_quotes")
        if response.status_code == 200:
            quotes = response.json()
            return quotes.get("money_quote", "Wealth is the ability to fully experience life!")
        else:
            return "Money grows on the tree of persistence!"
    except:
        return "Could not fetch quote, try again later!"

# ---- Money-Making Motivation Section ----
st.subheader("📢 Money-Making Motivation")
if st.button("Get Inspired ✨"):
    with st.spinner("Fetching a powerful quote..."):
        time.sleep(2)
        quote = fetch_money_quote()
        st.info(f"💡 **{quote}**")