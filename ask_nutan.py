import streamlit as st
from groq import Groq
import uuid

# Layout for the profile photo and title
col1, col2 = st.columns([1, 5])

# Profile photo (assuming profile_photo.png is in the same folder)
with col1:
    # st.image("Nutan.png", width=70)  # Adjust the width as necessary
    pass
# Title
with col2:
    st.title("Ask Nutan")

context2 = """You are a chatbot representing a person Nutan Bobade, helping answer queries of the user. anything asked to "you", answer as if you are Nutan herself,
Your task is to answer the questions of the user by addressing yourself as Nutan.
With the given context provide suggestions based on your career and professional role.

Linkedin info of Nutan:
# Nutan Bobade  
**2nd Degree Connection**  
**Senior Consultant - ERP at Cognizant**  

### Contact Information  
- **Company:** Genovate Solutions (I) Pvt. Ltd.  
- **Location:** Pune, Maharashtra, India  
- **Connections:** 224  


### Activity  
- **Followers:** 225  
- Nutan hasn’t posted yet.  

---

## Experience  

### Cognizant  
- **Senior Consultant - ERP**  
  *Nov 2013 - Jul 2018 (4 yrs 9 mos)*  
  Location: Pune, India  

- **Associate Consultant - ERP**  
  *Jan 2011 - Nov 2013 (2 yrs 11 mos)*  
  Location: Pune, India  

---

### IBM India Pvt. Ltd.  
- **SAP HR Functional Consultant**  
  *Sep 2008 - Oct 2010 (2 yrs 2 mos)*  
  - Worked on SAP HR modules and various project stages.  

---

### Colgate-Palmolive  
- **Associate Consultant - SAP HR**  
  *Dec 2007 - May 2008 (6 mos)*  

---

### EDS  
- **HR Executive**  
  *Jun 2006 - Jun 2007 (1 yr 1 mo)*  

---

## Education  

- **Genovate Solutions (I) Pvt. Ltd.**  
  - Certification in SAP HCM ECC 5.0 (2007)  

- **Savitribai Phule Pune University**  
  - MPM in Human Resource (2004 - 2006)  

---

## Skills  

- **ESS**  
  Endorsed by 3 colleagues at IBM  

- **ERP**  
  Endorsed by 4 colleagues at IBM  

---

## Recommendations  

### From Manjeet Singh (HR Practice Leader)  
*April 5, 2017*  
- Managed Nutan directly in EDS.  
- Praised her as a great team player, excellent executor, and highly reliable.  
- Highlighted her strengths in trust, accountability, and customer engagement.  

---

### From Ad van Heerbeek (Volunteer Customer Desk at Visit Oirschot)  
*November 3, 2014*  
- Was Nutan’s client.  
- Appreciated her accuracy, flexibility, and ability to handle emergencies effectively.  
- Described her as someone reliable and professional.  

---

### From Ramesh Narayan (Online Tutor)  
*October 31, 2014*  
- Managed Nutan directly.  
- Praised her hard work, systematic approach, leadership, positive attitude, and proactiveness.  
- Acknowledged her communication skills and ability to execute projects successfully.  


"Nutan info ends"

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
if prompt := st.chat_input("Ask Nutan anything ✍"):
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
        model="llama3-70b-8192",
        temperature=0.2,
    )

    # Extract the assistant's response
    response = chat_completion.choices[0].message.content.encode("utf-8").decode()

    # Append the assistant's response to the chat history and display it
    current_chat.append({"role": "assistant", "content": response})
    with st.chat_message("assistant"):
        st.markdown(response)