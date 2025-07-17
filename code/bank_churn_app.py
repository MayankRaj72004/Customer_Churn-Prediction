# from pathlib import Path
# import pandas as pd
# import numpy as np
# import streamlit as st
# import predict


# def get_user_input(df_train):
#     left, right = st.columns(2)
#     with left:
#         # add element on the left side
#         st.write(f"**Customer's Personal Information**")
#         geography = st.radio('To which country does the customer belong?',
#                              df_train['Geography'].unique(), horizontal=True, index=1)
#         gender = st.radio('What is the gender of the customer?',
#                           df_train['Gender'].unique(), horizontal=True)
#         age = st.selectbox("What is the Age of the Customer?",
#                            np.arange(18, 101))
#         credit_score = st.slider("What is the customer's credit score?",
#                                  int(df_train['CreditScore'].min()),
#                                  int(df_train['CreditScore'].max()),
#                                  int(df_train['CreditScore'].mean()))
#         estimated_salary = st.slider("What is Customer Estimated Salary?",
#                                      0,
#                                      200000,
#                                      int(df_train['EstimatedSalary'].mean()))
#     with right:
#         # add element on the right side
#         st.write(f"**Customer's Relationship with Bank**")
#         tenure = st.selectbox("What is the customer's tenure with bank?",
#                               sorted(df_train['Tenure'].unique()), index=5)

#         balance = st.slider("What is the balance of the customer's bank account?",
#                             float(df_train['Balance'].min()),
#                             float(df_train['Balance'].max()),
#                             float(df_train['Balance'].mean()))
#         num_of_products = st.radio('How many bank products does the customer have?',
#                                    sorted(df_train['NumOfProducts'].unique()), horizontal=True, index=1)
#         has_credit_card = st.selectbox('Does the customer have a credit card?',
#                                        ["Yes", 'No'])
#         has_credit_card = 1 if has_credit_card == "Yes" else 0
#         is_active = st.selectbox('Is the customer actively engaged in bank activities?',
#                                  ["Yes", 'No'])
#         is_active = 1 if is_active == "Yes" else 0

#     X = pd.DataFrame({
#         'CreditScore': credit_score,
#         'Geography': geography,
#         'Gender': gender,
#         'Age': age,
#         'Tenure': tenure,
#         'Balance': balance,
#         'NumOfProducts': num_of_products,
#         'HasCrCard': has_credit_card,
#         'IsActiveMember': is_active,
#         'EstimatedSalary': estimated_salary
#     }, index=[0])
#     return X


# if __name__ == "__main__":
#     hide_default_format = """
#            <style>
#            #MainMenu {visibility: hidden; }
#            footer {visibility: hidden;}
#            </style>
#            """

#     st.set_page_config(page_title="Bank Customer Churn Prediction", page_icon=None, layout="centered",
#                        initial_sidebar_state="auto")
#     st.markdown(hide_default_format, unsafe_allow_html=True)

#     df_train = pd.read_csv(str(Path(__file__).parents[1] / 'data/churn_data.csv'))

#     # Displaying text
#     st.title("Bank Customer Churn Prediction")
#     # Displaying an image
#     st.image(str(Path(__file__).parents[1] / 'img/customer_churn.png'), width=700)

#     st.write("""  
#              Customer churn, refers to customers discontinuing their relationship with a business or organization. In the banking industry, predicting customer churn is of great importance as it allows banks to address customer needs, improve retention strategies, and save costs associated with acquiring new customers.\n
#              A machine learning model has been developed as part of this project to predict customer churn. Please provide the following inputs to utilize the churn model.
#              """)

#     st.header("Input Fields")
#     input_df = get_user_input(df_train)  # get user input from sidebar

#     st.header("Prediction")
#     customer_churn = predict.predict(input_df)[0]  # get predicitions
#     if customer_churn == 0:
#         st.subheader("_:green[Customer is not likely to churn.]_")
#     else:
#         st.subheader("_:red[Customer is likely to churn.]_")



from pathlib import Path
import pandas as pd
import numpy as np
import streamlit as st
import predict


def get_user_input(df_train):
    st.markdown("### 🧍‍♂️ Customer's Personal Information")
    with st.container():
        col1, col2 = st.columns(2)

        with col1:
            geography = st.radio('🌍 Country',
                                 df_train['Geography'].unique(),
                                 horizontal=True, index=1)
            gender = st.radio('👤 Gender',
                              df_train['Gender'].unique(),
                              horizontal=True)
            age = st.selectbox("🎂 Age",
                               np.arange(18, 101))

        with col2:
            credit_score = st.slider("💳 Credit Score",
                                     int(df_train['CreditScore'].min()),
                                     int(df_train['CreditScore'].max()),
                                     int(df_train['CreditScore'].mean()))
            estimated_salary = st.slider("💼 Estimated Salary (₹)",
                                         0, 200000,
                                         int(df_train['EstimatedSalary'].mean()))

    st.markdown("### 🏦 Customer's Relationship with Bank")
    with st.container():
        col3, col4 = st.columns(2)

        with col3:
            tenure = st.selectbox("📅 Tenure (years)",
                                  sorted(df_train['Tenure'].unique()), index=5)
            balance = st.slider("🏦 Account Balance (₹)",
                                float(df_train['Balance'].min()),
                                float(df_train['Balance'].max()),
                                float(df_train['Balance'].mean()))

        with col4:
            num_of_products = st.radio('📦 Number of Products',
                                       sorted(df_train['NumOfProducts'].unique()), horizontal=True, index=1)
            has_credit_card = st.selectbox('💳 Has Credit Card?', ["Yes", 'No'])
            has_credit_card = 1 if has_credit_card == "Yes" else 0
            is_active = st.selectbox('🔥 Active Member?', ["Yes", 'No'])
            is_active = 1 if is_active == "Yes" else 0

    # Combine inputs into dataframe
    X = pd.DataFrame({
        'CreditScore': credit_score,
        'Geography': geography,
        'Gender': gender,
        'Age': age,
        'Tenure': tenure,
        'Balance': balance,
        'NumOfProducts': num_of_products,
        'HasCrCard': has_credit_card,
        'IsActiveMember': is_active,
        'EstimatedSalary': estimated_salary
    }, index=[0])

    # Display summary metrics
    st.markdown("### 📋 Summary of Inputs")
    col5, col6, col7 = st.columns(3)
    col5.metric("Credit Score", credit_score)
    col6.metric("Balance (₹)", f"{balance:,.0f}")
    col7.metric("Age", age)

    return X


# Streamlit App
if __name__ == "__main__":
    st.set_page_config(page_title="🏦 Bank Customer Churn Prediction", layout="centered")
    
    # Hide default streamlit footer
    st.markdown("""
        <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            .reportview-container .main .block-container{padding-top: 2rem;}
        </style>
        """, unsafe_allow_html=True)

    # Load data
    df_train = pd.read_csv(str(Path(__file__).parents[1] / 'data/churn_data.csv'))

    # Header
    st.title("🔮 Bank Customer Churn Prediction")
    st.image(str(Path(__file__).parents[1] / 'img/customer_churn.png'), width=700)

    # Info section
    st.info("""\
**Customer churn** refers to customers discontinuing their relationship with a bank.  
This app uses a machine learning model to predict the likelihood of customer churn based on user input.  
Provide the information below to generate a prediction.""")

    # Input
    st.header("📝 Input Fields")
    input_df = get_user_input(df_train)

    # Prediction
    st.header("📊 Prediction Result")
    prediction = predict.predict(input_df)[0]

    if prediction == 0:
        st.success("✅ _Customer is **not likely** to churn._ 😊")
    else:
        st.error("⚠️ _Customer is **likely** to churn._ 😟")

