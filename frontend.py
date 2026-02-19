from rag_pipline import answer_query,retrieve_docs,llm_model
#part1 uplod pdf funtionality
import streamlit as st

upload_file=st.file_uploader("upload PDF",type="pdf",accept_multiple_files=False)
#part 2 chatbot conversion(question answer)
user_query=st.text_area("enter your prompt",height=150,placeholder="ask your question here")

ask_questiom=st.button("ask Ai Lawer")
if ask_questiom:
    if upload_file:
        st.chat_message("user").write(user_query)
    #rag Pipline
    retrieved_docs=retrieve_docs(user_query)
    response=answer_query(documents=retrieved_docs, model=llm_model, query=user_query)
    # fixed_response="hi,this is your Ai Lawer,how can i help you?"
    st.chat_message("AI Lawer").write(response)
else:
    st.error("please upload a PDF file")
    