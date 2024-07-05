import streamlit as st


def BMI_calculator():
    st.title("**BMI** Calculator")
    with st.form(key='form'):
        col1,col2,col3=st.columns(3)

        with col1:
            weight= st.number_input('Enter you body weight',min_value=0,max_value=400,step=1)
        with col2:
            height=st.number_input('Enter you height in meters')
        with col3:
            submit=st.form_submit_button("Calculate")

        if submit:
            BMI=(weight/(height)**2)
            if BMI <=18.5:
                st.error("Under weight")
            if BMI>18.5 and BMI<=24.9:
                st.success("Healthy")
            if BMI>24.9 and BMI <=29.9:
                st.warning ("Overweight")
            if BMI>29.9:
                st.error("Unhealthy")
        return

def rate_yourself():
        st.title('Rate Yourself')
        languages = st.text_input('Enter the programming languages you know with comma separation', )
        languages = [i.strip() for i in languages.split(',')]

        st.subheader('How would you rate your experience in the following programming languages & tools?')

        for language in languages:
            # st.write(language)
            st.slider(language, min_value=0., max_value=10., step=1.0)

choice=st.sidebar.selectbox('Menu',['BMI',"Rate_Yourself"])

if choice=='BMI':
    BMI_calculator()
elif choice=='Rate_Yourself':
    rate_yourself()





















