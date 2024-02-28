import streamlit as st
from currency_converter import CurrencyConverter

def main():
    page = st.sidebar.selectbox("Select a page", ["Converter", "Menu", "Contact"])
    
    if page == "Converter":
        currency_converter()
    elif page == "Menu":
        menu_page()
    elif page == "Contact":
        contact_page()

def currency_converter():
    st.title("Currency Converter")

    # Input fields for amount and currency codes
    amount = st.number_input("Enter amount here:")
    cur1 = st.text_input("Enter currency:")
    cur2 = st.text_input("Enter target currency:")

    # Button to trigger the conversion
    if st.button("Convert"):
        result = convert_currency(amount, cur1, cur2)
        st.write(f"Converted amount: {result}")

def menu_page():
    st.title("Menu Page")
    # Add content for the menu page here
    st.write("This is the menu page.")
    st.write("Welcome to the Menu Page! Here are the available options:")
    
    st.markdown("- **Currency Converter:** Convert currencies using the currency converter tool.")
    st.markdown("- **Exchange Rates:** View current exchange rates for different currencies.")
    st.markdown("- **Settings:** Customize settings for the currency converter.")


def contact_page():
    st.title("Contact Page")
    # Add content for the contact page here
    st.write("This is the contact page.")
    st.write("Feel free to reach out to us for any questions, feedback, or support!")
    
    st.subheader("Contact Information:")
    st.markdown("- **Email:** dijaskhan467@gmail.com")
    st.markdown("- **Phone:** +923190372796")
    st.markdown("- **Address:** Bano Qabil korangi Campus, Karachi, Pakistan")
    
    st.subheader("Our Team:")
    st.markdown("LEADER: Sajid Khan")
    st.markdown("1st MEMBER: Abdullah Javed")
    st.markdown("2nd MEMBER: Syed Muhammad Anas")
    
    st.subheader("Send us a Message:")
    message = st.text_area("Enter your message here:")
    if st.button("Send"):
        # Code to handle message submission goes here
        st.success("Message sent successfully!")


import streamlit as st
from currency_converter import CurrencyConverter

def main():
    page = st.sidebar.selectbox("Select a page", ["Converter", "Menu", "Contact"])
    
    if page == "Converter":
        currency_converter()
    elif page == "Menu":
        menu_page()
    elif page == "Contact":
        contact_page()

def currency_converter():
    st.title("Currency Converter")

    # Input fields for amount and currency codes
    amount = st.number_input("Enter amount here:")
    cur1 = st.text_input("Enter currency:")
    cur2 = st.text_input("Enter target currency:")

    # Button to trigger the conversion
    if st.button("Convert"):
        result = convert_currency(amount, cur1, cur2)
        st.write(f"Converted amount: {result}")

def menu_page():
    st.title("Menu Page")
    # Add content for the menu page here
    st.write("This is the menu page.")
    st.write("Welcome to the Menu Page! Here are the available options:")
    
    st.markdown("- **Currency Converter:** Convert currencies using the currency converter tool.")
    st.markdown("- **Exchange Rates:** View current exchange rates for different currencies.")
    st.markdown("- **Settings:** Customize settings for the currency converter.")


def contact_page():
    st.title("Contact Page")
    # Add content for the contact page here
    st.write("This is the contact page.")
    st.write("Feel free to reach out to us for any questions, feedback, or support!")
    
    st.subheader("Contact Information:")
    st.markdown("- **Email:** dijaskhan467@gmail.com")
    st.markdown("- **Phone:** +923190372796")
    st.markdown("- **Address:** Bano Qabil korangi Campus, Karachi, Pakistan")
    
    st.subheader("Our Team:")
    st.markdown("LEADER: Sajid Khan")
    st.markdown("1st MEMBER: Abdullah Javed")
    st.markdown("2nd MEMBER: Syed Muhammad Anas")
    
    st.subheader("Send us a Message:")
    message = st.text_area("Enter your message here:")
    if st.button("Send"):
        # Code to handle message submission goes here
        st.success("Message sent successfully!")


def convert_currency(amount, cur1, cur2):
    # Initialize the currency converter
    c = CurrencyConverter()

    # Convert the currency
    try:
        result = c.convert(amount, cur1.upper(), cur2.upper())
        return result
    except ValueError as e:
        return str(e)
