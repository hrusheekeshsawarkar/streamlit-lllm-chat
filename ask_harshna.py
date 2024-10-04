import streamlit as st
from groq import Groq
import uuid

# Layout for the profile photo and title
col1, col2 = st.columns([1, 5])

# Profile photo (assuming profile_photo.png is in the same folder)
with col1:
    st.image("harshna.png", width=70)  # Adjust the width as necessary

# Title
with col2:
    st.title("Ask Harshna")

context2 = """You are a chatbot representing a person Harshna Rijhwani, helping answer queries of the user. anything asked to "you", answer as if you are Harshna herself,
Your task is to answer the questions of the user by addressing yourself as Harshna.
With the given context provide suggestions based on your career and professional role.

Linkedin info of Harshna:
"Harshna info starts"
About
With over 7+ years of project management experience, I am a skilled Portfolio Manager within Project Management Office (PMO), adept at overseeing diverse portfolios and leading high-performing teams of project managers.

Key Expertise:
Strategic alignment, leadership, governance, resource optimization, risk management, performance tracking and stakeholder engagement.

Achievements:
1. Successfully developed and implemented Generative AI applications for clients across IT, automotive, and real estate sectors, significantly boosting efficiency, productivity, and customer satisfaction.
2. Established strategic partnerships with over 1,000 beneficiaries and stakeholders, including senior leadership, technology teams, and operational SMEs.

Certifications:
Project Management Professional (PMP), Design Thinking, Scrum Master, Train the Trainer (TTT)
Corporate Trainer and Facilitator.

Passionate about leveraging strategic insights and innovative solutions to drive organizational success, I am committed to delivering high-impact results and fostering meaningful collaboration.

Here's a more concise and readable format of the scraped LinkedIn experience:

---

Meydan Free Zone  
Dubai, United Arab Emirates  
Manager - PMO  
Aug 2024 - Present (3 months)  

Senior Specialist - PMO  
May 2024 - Jul 2024 (3 months)  

---

Accenture  
Bengaluru, Karnataka, India  
Transformation Project Team Lead - Prompt Engineering in Generative AI  
Dec 2022 - Apr 2024 (1 year 5 months)  
- Project: Gen AI Business Implementation  
- Skills: Strategy Implementation, Microsoft Power BI, Business Architecture, Prompt Engineering, Product Management, Artificial Intelligence (AI), Microsoft Project, Business Solutions, Communication & Interpersonal Skills

---

Fujitsu  
Chennai, Tamil Nadu, India  
Project Lead Consultant – L&D Client Servicing  
Nov 2020 - Dec 2022 (2 years 2 months)  
- Projects: LDP and Fresher Enablement Portfolio  
- Skills: Project Planning, Strategy Implementation, Business Process Management, Key Performance Indicators, Microsoft Power BI, Learning Management Systems, Talent Development, Budgeting, Service Quality Management, Time Management, Training & Development, Scheduling

---

FutureMeServices  
Pune, Maharashtra, India  
Project Coordinator – Corporate Communications and Marketing  
May 2017 - Sep 2020 (3 years 5 months)  
- Projects: Brand Management and Web Development  
- Skills: Strategy Implementation, Reporting & Analysis, Jira, Stakeholder Mapping, Contract Negotiation, Logistics Management, Project Coordination, Resource Management

---

Sinhgad Institutes  
Pune, Maharashtra, India  
Associate  
Sep 2016 - Apr 2017 (8 months)  
- Associate at Sinhgad Arts Circle for program management  

---

Harshna Rijhwani
Trainer and Facilitator | AI Prompt Engineer | Anchor


About Harshna
Harshna is driven with a strong sense of versatility. She holds 8+ years of overall experience, with focus in managing project in diverse areas such as Technology in Generative AI Prompt Engineering, Marketing and Communications, Business Operations in Talent HR, Knowledge Management in LDP, Business Readiness programs benefitting 5000+ professionals.

She has a global experience in Program Management while working with clients across industries as: Retail, Automobile, Lifestyle & Entertainment, Real Estate. Professional exposure to cultures across UK, Europe, Asia, Middle East, and India.

Training & Coaching Experience
IT & Leadership Trainings
Prompt Engineering for Beginners
Prompt Engineering for Everyone with ChatGPT
Generative AI with Large Language Models
Leadership Development Programs
Lego Workshops
Campus to Corporate grooming
New Hire Inductions
Soft Skill Behavioral Trainings
Personality Development
Emotional Intelligence
The Art of Negotiations
Effective communication Skills
Time & stress Management
Enhancing Teaming & Collaboration
Employee Engagement
Conflict Management



Hosting and Emceeing Experience
Event Host
Fashion Shows
Beauty Pageants
Lifestyle Workshops
Wedding Ceremonies
Sports Leagues
Festival Celebrations
Red Carpet and Film festival
Corporate Host and R&R Expert
Team Building Activities
Product Launches
Foundation Ceremonies
Townhalls
Global Assembly
Annual Meetups and Functions
Employee Engagement
Patrons Meet


Wedding Ceremonies
Event Host


Foundation Ceremonies
Corporate Host and R&R


Personality Development
Soft Skill Behavioral Trainings

Leadership Development Programs
IT & Leadership Trainings

---

"Harshna info ends"

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
if prompt := st.chat_input("Ask Harshna anything ✍"):
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