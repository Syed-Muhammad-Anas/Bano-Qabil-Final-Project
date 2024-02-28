import streamlit as st
from currency_converter import CurrencyConverter

def main():
    st.title("Currency Converter")

    # Input fields for amount and currency codes
    amount = st.number_input("Enter amount here:")
    cur1 = st.text_input("Enter currency:")
    cur2 = st.text_input("Enter target currency:")

    # Button to trigger the conversion
    if st.button("Convert"):
        result = convert_currency(amount, cur1, cur2)
        st.write(f"Converted amount: {result}")

def convert_currency(amount, cur1, cur2):
    # Initialize the currency converter
    c = CurrencyConverter()
    # Convert the currency
    converted_amount = c.convert(amount, cur1, cur2)
    return converted_amount

if __name__ == "__main__":
    main()