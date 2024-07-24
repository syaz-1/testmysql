import streamlit as st
import pandas as pd
import requests
from sqlalchemy.sql import text

conn=st.connection('mysql',type='sql')

# import mysql.connector
# from oci.config import from_file
# from oci.signer import Signer
# config = from_file()
# auth = Signer(
# tenancy=config['tenancy'],
# user=config['user'],
# fingerprint=config['fingerprint'],
# private_key_file_location=config['key_file'],
# pass_phrase=config['pass_phrase']
# )

# endpoint='https://sql.dbtools.us-chicago-1.oci.oraclecloud.com/20201005/ords/ocid1.databasetoolsconnection.oc1.us-chicago-1.amaaaaaaxc7u3kianrg7kpoftbqvafpy5eghxszddftbnwbao2ze5x6hemiq/_/sql'
# headers={'Content-Type': 'application/sql'}

# def sql_rest_query(data, resp_format='table'):
#     response = requests.post(endpoint, data=data, headers=headers, auth=auth)
#     if response.status_code == 200:
#         if resp_format == 'table':
#             columnName = response.json()['items'][0]['resultSet']['metadata'][0]['jsonColumnName']
#             columnValues = response.json()['items'][0]['resultSet']['items']
#             resp_df = pd.DataFrame(data=columnValues)
#         elif resp_format == 'raw':
#             resp_df = response.text
#         else:
#             resp_df = response.json()['items'][0]['response']
#     else:
#         resp_df = response.json()
#     return resp_df


# data='show databases'
# ml_model="call sys.ML_MODEL_LOAD('mistral-7b-instruct-v1', NULL);"
# ml = requests.post(endpoint, data=ml_model, headers=headers, auth=auth)
# response = requests.post(endpoint, data=data, headers=headers, auth=auth)
# print(ml)
# print(ml.text)
# print(response)
# print(response.text)

st.title("🎈 MySQL GEN ai Test")
st.write(
    "Let's start building! For help and inspiration, head over to [docs.streamlit.io](https://docs.streamlit.io/)."
)

question = st.text_area("Enter you question:")
if st.button("Ask"):
    q=f"call sys.heatwave_chat('{question}')"
    qtest="call sys.heatwave_chat('what is heatwave auto ml')"
    # query=f"SET @query ='{question}';  SET @options = JSON_Object('vector_store',JSON_ARRAY('vectordb.demo_embedding'));call sys.ML_RAG(@query,@output,@options);SELECT JSON_UNQUOTE(JSON_EXTRACT(@output, '$.text')) as output;"
    query=f"set @query='{question}';set @options = JSON_OBJECT('vector_store', JSON_ARRAY('vectordb.demo_embeddings'));call sys.ML_RAG(@query,@output,@option);"
    # answer = sql_rest_query(query, resp_format='json')
    # answer = sql_rest_query('show tables in vectordb')
    # answer = sql_rest_query(query,resp_format='table')
    q1="set @options = JSON_OBJECT('vector_store', JSON_ARRAY('vectordb.demo_embeddings'));"
    # a1=a1=requests.post(endpoint, data=q1, headers=headers, auth=auth)
    q2=f"set @query='{question}'"
    # a2=requests.post(endpoint, data=q2, headers=headers, auth=auth)
    q3="call sys.ML_RAG(@query,@output,@options);"
    # a3=requests.post(endpoint, data=q3, headers=headers, auth=auth)
    q4="SELECT JSON_UNQUOTE(JSON_EXTRACT(@output, '$.text')) as output;"
    # a4=requests.post(endpoint, data=q4, headers=headers, auth=auth)
    # answer=requests.post(endpoint, data=query, headers=headers, auth=auth)
    # df1 = conn.query(f'{query}', ttl=600)
    test_query="select JSON_PRETTY(@output); as output"
    with conn.session as session:
        session.execute(text(query))
    df1 = conn.query(f'{q4}', ttl=600) 
    if df1 is not None:
        for row in df1.itertuples():
            st.write(f"{row.output}:")
        # st.write(df1)    
        # st.write(answer)
        # st.write(answer[6])
    else:
        st.write("DB connection error")