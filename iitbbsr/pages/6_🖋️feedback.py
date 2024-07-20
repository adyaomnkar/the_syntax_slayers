import streamlit as st

def main():
    st.title("📄 Feedback Form")

    # User details section
    st.header("Your Details")
    
    # column layout for first name and last name
    col1, col2 = st.columns(2)
    with col1:
       first_name = st.text_input("First Name")
    with col2:
       last_name = st.text_input("Last Name")
    
    # email section
    email = st.text_input("Email")

    # Feedback section
    st.header("Your Feedback")
    comment = st.text_area("Comments", height=150)

    # Additional feedback options
    st.subheader("Additional Information 📝")
    rating = st.selectbox("Rate your experience ⭐", options=[1, 2, 3, 4, 5])
    would_recommend = st.radio("Would you recommend our model?", ("Yes", "No"))
    improvements = st.text_input("What areas can we improve on?")

    # Submit button
    if st.button("Submit", key="submit_button", help="Click to submit your feedback"):
        if not first_name or not last_name or not email or not comment:
            st.error("Please fill out all fields before submitting.")
        else:
            st.success("Thank you for your feedback!")

if __name__ == "__main__":
    main()