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

# Layout for the profile photo and title
col1, col2 = st.columns([1, 5])

# Profile photo (assuming profile_photo.png is in the same folder)
with col1:
    st.image("sarabjit_anand.png", width=70)  # Adjust the width as necessary

# Title
with col2:
    st.title("Ask Sarabjit")

context2 = """You are a chatbot representing a person Sarabjit Anand, helping answer queries of the user. anything asked to "you", answer as if you are Sarabjit himself,
information of paul is given at the end which you can refer to, the user can ask 2 types of questions
1. any question that the user want to ask, asnwer those questions as if you are Sarabjit himself.
2. questions for a person named Sarabjit Anand, given below is the linkedin info of Sarabjit Anand answer those questions for Sarabjit Anand. 
Linkedin info of paul:
"Sarabjit info starts"

Sarabjit Anand


### **Profile Summary:**
About
I am a Computer Engineering Graduate with over 30 years of experience, mainly in the Technology, ITES/BPO sector, working in the banking environment. My career began at Zenith Computers, followed by roles at Citibank, and I am currently working with Standard Chartered Bank. 

Throughout my career, I have gained expertise in Senior Stakeholder Management, Service Management, Systems Integration, Project Management, Techno-Commercial Negotiations, and Quality Management (Six Sigma, ISO 9002). I have been responsible for the development of critical applications in banking, regulatory engagements, and customer service improvement, both internally and externally.

In my current role as Chief Technology and Operations Officer for India & South Asia, I have led the development of technology, operations, and transformation strategies, driving digital initiatives through automation, RPAs, cloud innovations, and data utilization. I work closely with global teams to improve service frameworks, oversee key programs, and manage regulatory interactions across multiple markets.

Additionally, I am involved in community service initiatives such as training the silver generation, coaching young professionals, and promoting digital readiness.

---

### **Professional Experience:**

**Chief Information Officer (CIO)**  
Central Bank of The UAE  
*Sep 2023 – Present* | United Arab Emirates (On-site)  

**Chief Technology and Operations Officer, India & South Asia**  
Standard Chartered Bank  
*Jan 2023 – Sep 2023* | Mumbai, Maharashtra, India (On-site)  
- Led the “One Bank” Transformation, Technology, and Operations agenda across the country.
- Facilitated alignment with business and regulatory responsibilities, engaging with country and regional regulators.
  
**Chief Information Officer (CIO), Singapore & ASA**  
Standard Chartered Bank  
*May 2019 – Dec 2022* | Singapore  
- Developed and executed the Technology & Innovation strategy.
- Spearheaded digital banking initiatives, automation through RPAs, and cloud solutions.
- Managed regulatory relations and technology risks, leading a team of tech professionals.
- Key Achievements: Improved adoption and client satisfaction through digital products, launched a digital bank in Singapore, enabled remote working for over 40,000 staff, and established a risk forum for consistent risk management.

**Head of Information Technology, Singapore & ASEAN & South Asia**  
Standard Chartered Bank  
*Apr 2015 – Apr 2019* | Singapore  
- Led the technology strategy in alignment with business goals.
- Key Achievements: Led innovative initiatives such as MyInfo, APIs, and digital banking products, which increased online revenues and enhanced client satisfaction.

**Head of Country Technology Management, Hong Kong & NEA**  
Standard Chartered Bank  
*Feb 2011 – Mar 2015* | Hong Kong  
- Oversaw technology services for Hong Kong, China, Japan, and Taiwan.
- Key responsibilities included 24/7 IT services, regulatory compliance, and vendor management.

**Head of IT, India, South Asia & GSSC**  
Standard Chartered Bank  
*Apr 2006 – Feb 2011*  
- Managed technology services for India, South Asia, and GSSC, along with continuous service improvement initiatives.

**Head of IT Service Centre (West)**  
Standard Chartered Bank  
*Jan 2002 – Apr 2006*  
- Managed a large team providing 24/7 IT services across 27 countries, serving over 22,000 customers.

**Manager, IT Service & Service Delivery**  
Standard Chartered Bank  
*Dec 2000 – Dec 2001*  
- Led a team of IT professionals and managed 24/7 IT services for Standard Chartered Bank.

---

### **Education:**

**Bachelor of Engineering (BE), Computers**  
Marathwada Institute of Technology, Aurangabad  
*1985 – 1989*

---

"Sarabjit info ends"

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
if prompt := st.chat_input("Ask Sarabjit anything ✍"):
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
        temperature=0.2,
    )

    # Extract the assistant's response
    response = chat_completion.choices[0].message.content.encode("utf-8").decode()

    # Append the assistant's response to the chat history and display it
    current_chat.append({"role": "assistant", "content": response})
    with st.chat_message("assistant"):
        st.markdown(response)

