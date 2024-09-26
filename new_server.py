# import streamlit as st
# # from streamlit_auth_component import login
# from groq import Groq
# import uuid

# # Title
# st.title("Ask Paul")

# # Initialize Groq client
# client = Groq(
#     api_key="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",
# )

# # Google Sign-In (User Authentication)
# # user = login('Google', 'Your_App_Name')

# # if user is None:
# #     st.warning("Please log in to continue.")
# #     st.stop()

# # st.success(f"Logged in as {user['name']}")

# # Chat sessions handling
# if "chat_sessions" not in st.session_state:
#     st.session_state.chat_sessions = {}  # Dictionary to store all chat sessions
#     st.session_state.current_chat_id = None  # To track current active chat session

# # Sidebar for chat session navigation and "New Chat" button
# st.sidebar.title("Chat Sessions")

# # Button to start a new chat session
# if st.sidebar.button("New Chat"):
#     new_chat_id = str(uuid.uuid4())  # Generate a unique ID for the new chat session
#     st.session_state.chat_sessions[new_chat_id] = [{"role": "assistant", "content": "Hello! How can I assist you today?"}]
#     st.session_state.current_chat_id = new_chat_id

# # Display existing chat sessions in the sidebar
# for chat_id in st.session_state.chat_sessions.keys():
#     chat_name = f"Chat {chat_id[:4]}"  # Give a short name to the chat session
#     if st.sidebar.button(chat_name):
#         st.session_state.current_chat_id = chat_id

# # Get current chat ID (if no chat session exists, start a new one)
# current_chat_id = st.session_state.current_chat_id
# if current_chat_id is None:
#     current_chat_id = str(uuid.uuid4())
#     st.session_state.chat_sessions[current_chat_id] = [{"role": "assistant", "content": "Hello! How can I assist you today?"}]
#     st.session_state.current_chat_id = current_chat_id

# # Current chat session (messages)
# current_chat = st.session_state.chat_sessions[current_chat_id]

# # Display the chat history for the selected chat session
# for message in current_chat:
#     with st.chat_message(message["role"]):
#         st.markdown(message["content"])

# # Input field for user input
# if prompt := st.chat_input("Ask a medical query"):
#     current_chat.append({"role": "user", "content": prompt})
#     with st.chat_message("user"):
#         st.markdown(prompt)

#     # Sending the system message and conversation history to the model
#     context2 = "You are a medical assistant answering the medical queries."
#     chat_completion = client.chat.completions.create(
#         messages=[{"role": "system", "content": context2}] + current_chat,
#         model="llama3-8b-8192",
#     )

#     # Extract the assistant's response
#     response = chat_completion.choices[0].message.content.encode("utf-8").decode()

#     # Append the assistant's response to the chat history and display it
#     current_chat.append({"role": "assistant", "content": response})
#     with st.chat_message("assistant"):
#         st.markdown(response)

import streamlit as st
from groq import Groq
import uuid

# Title
st.title("Ask Paul")
context2 = """You are a chatbot representing a person Paul Wan, helping answer queries of the user. anything asked to "you", answer as if you are Paul himself,
information of paul is given at the end which you can refer to, the user can ask 2 types of questions
1. any question that the user want to ask
2. questions for a person named Paul Wan, given below is the linkedin info of Paul Wan answer those questions for paul. 
Linkedin info of paul:
"Paul info starts"
Paul Wan

About
• Experienced professional with over 20 years of remarkable track record in banking, card payment and IT services industries.
• Excel at interfacing with others at all levels to ensure organizational goals are attained.
• Restorative approach has resulted in being chosen for newly defined roles where job descriptions and objectives might evolve over a period of time.
• Possess excellent interpersonal, analytical, and organizational skills.
• Excel within highly competitive environments where positive leadership style is one of the keys to success.
• An effective manager with the top strength of ‘inclusive’ to direct, train, and motivate staff to its fullest potential.


Experience

Standard Chartered
Regional Head, Asia TransformationRegional Head, Asia Transformation
Standard Chartered Bank · Full-time
Sep 2022 - Present · 2 yrs 1 mo
Location: Hong Kong SAR
Setting up Transformation and Data Management capability for major markets in Asia
Skills: Non Financial Risk Management · Operational Excellence · Project Management · Problem Solving · Data Management


Head, Risk & Controls, HK & Greater China and North Asia
Standard Chartered Bank (Hong Kong) Limited
May 2017 - Nov 2022 · 5 yrs 7 mos
locaton: Hong Kong

Standard Chartered Bank
7 yrs 10 mo
Interim CIO
Apr 2016 - Jun 2017 · 1 yr 3 mos
Hong Kong
Head, Governance & Controls, Technology & Operations
Jan 2011 - Jun 2017 · 6 yrs 6 mos
Hong Kong
Programme Director
Sep 2009 - Dec 2010 · 1 yr 4 mos
COO
Merchant Solutions Pte. Ltd.Merchant Solutions Pte. Ltd.
2007 - 2009 · 2 yrs

Senior Manager, Credit Card & Personal Loans
Standard Chartered Bank
Aug 2001 - Jun 2007 · 5 yrs 11 mos
Hong Kong


Member Services, Products and Emerging Technologies
Visa
1992 - 1999 · 7 yrs
Sydney, Australia; Hong Kong

Graduate Trainee
IBM
Jan 1990 - Jun 1992 · 2 yrs 6 mos
Sydney, Australia



Education
The University of Hong Kong
Master of Engineering Science, e-Commerce
1999 - 2003
Grade: Graduate with Distinction.Grade: Graduate with Distinction.

UNSW
Bachelor of Engineering (Electrical), Electrical and Electronics Engineering
1985 - 1989


Volunteering
Hong Kong Computer Society logo
Convenor, Cybersecurity Specialist Group
Hong Kong Computer Society
Jul 2022 - Present · 2 yrs 3 mos
Strive to promote cybersecurity awareness and development via connections among regulators, industries experts, thought leaders and IT professions. There is an expanded focus recently on promoting Hong Kong as a value added service hub for China and overseas markets in the area of AI, Data Management / Governance and Cyber Defense and Protection.
"Paul info ends"

"""
# Initialize Groq client
client = Groq(
    api_key="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",
)

# Chat sessions handling
if "chat_sessions" not in st.session_state:
    st.session_state.chat_sessions = {}  # Dictionary to store all chat sessions
    st.session_state.current_chat_id = None  # To track current active chat session
    st.session_state.chat_names = {}  # Store short names based on the first user message

# Sidebar for chat session navigation and "New Chat" button
st.sidebar.title("Chat Sessions")

# Button to start a new chat session
if st.sidebar.button("New Chat"):
    new_chat_id = str(uuid.uuid4())  # Generate a unique ID for the new chat session
    st.session_state.chat_sessions[new_chat_id] = [{"role": "assistant", "content": "Hello! How can I assist you today?"}]
    st.session_state.current_chat_id = new_chat_id
    st.session_state.chat_names[new_chat_id] = "New Chat"

# Display existing chat sessions in the sidebar
for chat_id, chat_name in st.session_state.chat_names.items():
    # Use the unique `chat_id` as the key to prevent DuplicateWidgetID errors
    if st.sidebar.button(chat_name, key=chat_id):
        st.session_state.current_chat_id = chat_id

# Get current chat ID (if no chat session exists, start a new one)
current_chat_id = st.session_state.current_chat_id
if current_chat_id is None:
    current_chat_id = str(uuid.uuid4())
    st.session_state.chat_sessions[current_chat_id] = [{"role": "assistant", "content": "Hello! How can I assist you today?"}]
    st.session_state.current_chat_id = current_chat_id
    st.session_state.chat_names[current_chat_id] = "New Chat"

# Current chat session (messages)
current_chat = st.session_state.chat_sessions[current_chat_id]

# Display the chat history for the selected chat session
for message in current_chat:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Input field for user input
if prompt := st.chat_input("Ask Paul anything ✍"):
    # Update the session name with the first user message (if it's a new chat)
    if st.session_state.chat_names[current_chat_id] == "New Chat":
        st.session_state.chat_names[current_chat_id] = prompt[:20] + "..." if len(prompt) > 20 else prompt
    
    current_chat.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    # Sending the system message and conversation history to the model
    # context2 = "You are a medical assistant answering the medical queries."
    chat_completion = client.chat.completions.create(
        messages=[{"role": "system", "content": context2}] + current_chat,
        model="llama3-8b-8192",
    )

    # Extract the assistant's response
    response = chat_completion.choices[0].message.content.encode("utf-8").decode()

    # Append the assistant's response to the chat history and display it
    current_chat.append({"role": "assistant", "content": response})
    with st.chat_message("assistant"):
        st.markdown(response)

