try:
    import streamlit as st
    import google.genai as genai
    
    google_api_key = st.secrets["google"]["api_key"]
    client = genai.Client(api_key = google_api_key)
    
    st.title("Your Personalised AI Investment Assistant")
    
    st.title("_AI_ is :blue[cool] :sunglasses:")
    # Input fields for height and weight
    name = st.text_input("* Enter Your name", key="name")
    inv = st.slider("Enter Your investment amount",  min_value=100000, max_value= 100000000, step=100000)
    age = st.slider("Enter your Age:", min_value=18, max_value= 60, step=1)
    time = st.slider("Enter your time horizon:", min_value=5, max_value= 30, step=1)

    inv2 = st.number_input()
    

    # Calculate BMI
    if st.button("Share Stratigy"):
        if not name.strip():
            st.error("Please enter your name.")
        
        else:
            # bmi = wt / (ht ** 2)
            # st.write(f"Your BMI is: {bmi:.2f}")
            prompt = f"Greet {name} and Act like an investment expert, share the investment stratagy based on the amount {inv}, over {time} horizon depending on the age {age}"
        
            # Generate content from Gemini
            response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents= prompt)
            st.write(response.text)
except Exception as e:
    st.error(f"An error occurred: {e}")
