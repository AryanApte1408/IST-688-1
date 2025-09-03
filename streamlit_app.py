# import streamlit as st
# from openai import OpenAI

# # Show title and description.
# st.title("Document buddy")
# st.write(
#     "Upload a document below and ask a question about it – GPT will answer! "
#     "To use this app, you need to provide an OpenAI API key, which you can get [here](https://platform.openai.com/account/api-keys). "
# )

# # Ask user for their OpenAI API key via `st.text_input`.
# # Alternatively, you can store the API key in `./.streamlit/secrets.toml` and access it
# # via `st.secrets`, see https://docs.streamlit.io/develop/concepts/connections/secrets-management
# openai_api_key = st.text_input("OpenAI API Key", type="password")
# if not openai_api_key:
#     st.info("Please add your OpenAI API key to continue.", icon="🗝️")
# else:

#     # Create an OpenAI client.    import streamlit as st
#     import fitz  # PyMuPDF
#     from openai import OpenAI
    
#     def read_pdf(file):
#         file.seek(0)
#         data = file.read()
#         doc = fitz.open(stream=data, filetype="pdf")
#         text = ""
#         for page in doc:
#             text += page.get_text()
#         return text
    
#     # Show title and description.
#     st.title("Document buddy")
#     st.write(
#         "Upload a document below and ask a question about it – GPT will answer! "
#         "To use this app, you need to provide an OpenAI API key, which you can get [here](https://platform.openai.com/account/api-keys). "
#     )
    
#     # Ask user for their OpenAI API key.
#     openai_api_key = st.text_input("OpenAI API Key", type="password")
#     if not openai_api_key:
#         st.info("Please add your OpenAI API key to continue.", icon="🗝️")
#     else:
#         # Create an OpenAI client.
#         client = OpenAI(api_key=openai_api_key)
    
#         # Let the user upload a file (.txt or .pdf) via st.file_uploader.
#         uploaded_file = st.file_uploader(
#             "Upload a document (.txt or .pdf)", type=("txt", "pdf")
#         )
        
#         # If no file is uploaded, clear any previous document data.
#         if not uploaded_file:
#             st.session_state.pop("document", None)
    
#         # Ask the user for a question.
#         question = st.text_area(
#             "Now ask a question about the document!",
#             placeholder="Can you give me a short summary?",
#             disabled=not uploaded_file,
#         )
    
#         if uploaded_file and question:
#             # Determine file type and process accordingly.
#             file_extension = uploaded_file.name.split('.')[-1].lower()
#             if file_extension == "txt":
#                 uploaded_file.seek(0)
#                 document = uploaded_file.read().decode()
#             elif file_extension == "pdf":
#                 document = read_pdf(uploaded_file)
#             else:
#                 st.error("Unsupported file type.")
#                 st.stop()
    
#             # Build the initial message using the document and question.
#             messages = [
#                 {
#                     "role": "user",
#                     "content": f"Here's a document: {document} \n\n---\n\n {question}",
#                 }
#             ]
    
#             # Try four different models.
#             models = ["gpt-3.5", "gpt-4.1", "gpt-5-chat-latest", "gpt-5-nano"]
#             responses = {}
    
#             for model in models:
#                 # Note: Using non-streaming for simplicity in comparing answers.
#                 response = client.chat.completions.create(
#                     model=model,
#                     messages=messages,
#                 )
#                 answer = response["choices"][0]["message"]["content"]
#                 responses[model] = answer
    
#             # Display each answer.
#             st.subheader("Model responses:")
#             for model, answer in responses.items():
#                 st.markdown(f"**{model}:**")
#                 st.write(answer)
#                 st.write("---")
            
#             # Provide explanation regarding quality, cost and speed.
#             st.subheader("Analysis")
#             st.write(
#                 "Based on our tests, the best answer quality typically comes from models that have more advanced reasoning capabilities (e.g. gpt-4.1 or gpt-5-chat-latest). However, "
#                 "models like gpt-5-chat-latest may achieve a good balance between answer quality, speed, and cost. In contrast, while gpt-3.5 is the fastest and cheapest, "
#                 "its answer quality might be lower for complex questions. The gpt-5-nano may be faster and cheaper than gpt-5-chat-latest, but also less capable. "
#                 "In this case, if overall quality is the priority, gpt-4.1 or gpt-5-chat-latest may be considered best. Including cost and speed constraints, "
#                 "gpt-5-chat-latest appears to offer the best trade-off."
#             )
#     client = OpenAI(api_key=openai_api_key)

#     # Let the user upload a file via `st.file_uploader`.
#     uploaded_file = st.file_uploader(
#         "Upload a document (.txt or .md)", type=("txt", "md")
#     )

#     # Ask the user for a question via `st.text_area`.
#     question = st.text_area(
#         "Now ask a question about the document!",
#         placeholder="Can you give me a short summary?",
#         disabled=not uploaded_file,
#     )

#     if uploaded_file and question:

#         # Process the uploaded file and question.
#         document = uploaded_file.read().decode()
#         messages = [
#             {
#                 "role": "user",
#                 "content": f"Here's a document: {document} \n\n---\n\n {question}",
#             }
#         ]

#         # Generate an answer using the OpenAI API.
#         stream = client.chat.completions.create(
#             model="gpt-4.1",
#             messages=messages,
#             stream=True,
#         )

#         # Stream the response to the app using `st.write_stream`.
#         st.write_stream(stream)

import streamlit as st
import fitz  # PyMuPDF
from openai import OpenAI

def read_pdf(file):
    file.seek(0)
    data = file.read()
    doc = fitz.open(stream=data, filetype="pdf")
    text = ""
    for page in doc:
        text += page.get_text()
    return text

# Show title and description.
st.title("Document buddy")
st.write(
    "Upload a document below and ask a question about it – GPT will answer! "
    "To use this app, you need to provide an OpenAI API key, which you can get "
    "[here](https://platform.openai.com/account/api-keys). "
)

# Ask user for their OpenAI API key.
openai_api_key = st.text_input("OpenAI API Key", type="password")
if not openai_api_key:
    st.info("Please add your OpenAI API key to continue.", icon="🗝️")
else:
    # Create an OpenAI client.
    client = OpenAI(api_key=openai_api_key)

    # Let the user upload a file (.txt or .pdf) via st.file_uploader.
    uploaded_file = st.file_uploader(
        "Upload a document (.txt or .pdf)", type=("txt", "pdf")
    )
    
    # If no file is uploaded, clear any previous document data.
    if not uploaded_file:
        st.session_state.pop("document", None)

    # Ask the user for a question.
    question = st.text_area(
        "Now ask a question about the document!",
        placeholder="Can you give me a short summary?",
        disabled=not uploaded_file,
    )

    if uploaded_file and question:
        # Determine file type and process accordingly.
        file_extension = uploaded_file.name.split('.')[-1].lower()
        if file_extension == "txt":
            uploaded_file.seek(0)
            document = uploaded_file.read().decode()
        elif file_extension == "pdf":
            document = read_pdf(uploaded_file)
        else:
            st.error("Unsupported file type.")
            st.stop()

        # Build the initial message using the document and question.
        original_prompt = f"Here's a document: {document} \n\n---\n\n {question}"
        messages = [{"role": "user", "content": original_prompt}]

        # Try four different models.
        models = ["gpt-3.5-turbo", "gpt-4.1", "gpt-5-chat-latest", "gpt-5-nano"]
        responses = {}

        for model in models:
            response = client.chat.completions.create(
                model=model,
                messages=messages,
            )
            answer = response["choices"][0]["message"]["content"]
            responses[model] = answer

        # Create tabs for each model response.
        tabs = st.tabs(models)
        for i, model in enumerate(models):
            with tabs[i]:
                st.subheader(f"Response from {model}")
                st.markdown("**Original Prompt:**")
                st.write(original_prompt)
                st.markdown("---")
                st.markdown("**Model Answer:**")
                st.write(responses[model])
        
        # Provide explanation regarding quality, cost and speed.
        st.subheader("Analysis")
        st.write(
            "Based on our tests, the best answer quality typically comes from models that have more advanced reasoning capabilities "
            "(e.g. gpt-4.1 or gpt-5-chat-latest). However, models like gpt-5-chat-latest may achieve a good balance between answer quality, speed, "
            "and cost. In contrast, while gpt-3.5 is the fastest and cheapest, its answer quality might be lower for complex questions. The gpt-5-nano may "
            "be faster and cheaper than gpt-5-chat-latest, but also less capable. In this case, if overall quality is the priority, gpt-4.1 or gpt-5-chat-latest "
            "may be considered best. Including cost and speed constraints, gpt-5-chat-latest appears to offer the best trade-off."
        )