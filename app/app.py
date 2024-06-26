import joblib
import pandas as pd
import streamlit as st
import joblib
from sklearn.base import BaseEstimator, TransformerMixin
from sklearn import set_config
set_config(transform_output="pandas")


class FeatureSelector(BaseEstimator, TransformerMixin):
    def __init__(self, features_to_drop):
        self.features_to_drop = features_to_drop
    
    def fit(self, X, y=None):
        return self
    
    def transform(self, X):
        return X.drop(columns=self.features_to_drop)

st.set_page_config(page_title='Churn Prediction', page_icon='img\dnc.webp')
st.title('Telco Previsão de Churn')

st.image('img\customer_churn.jpeg')

st.markdown("""
            A previsão de churn é um aspecto cruciar para qualquer negócio que queira reter os seus clientes.
            No contexto o aplicativo usa algoritmos de machine learning e dados históricos para aprender sobre os clientes e prever a possibilidade de churn.
            Usando estes algoritmos a companhia economiza tempo e recursos e fica mais informado sobre as decisões de negócio.
            """)

# Carregando o modelo
model = joblib.load('models/model_pipeline.pkl')

data = st.file_uploader('Upload your file')
if data:
    df_input = pd.read_csv(data)
    df_output = df_input.assign(
        churn = model.predict(df_input),
        churn_probability = model.predict_proba(df_input)[:,1]
    )

    st.markdown('Churn prediction:')
    st.write(df_output)
    st.download_button(
        label='Download CSV', data=df_output.to_csv(index=False).encode('utf-8'),
        mime='text/csv', file_name='predicted_insurance.csv'
    )