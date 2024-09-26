# from openai import OpenAI
# import streamlit as st
# from groq import Groq

# st.title("Ask Paul")


# context2="""You are a medical assistant answering the medical queries."""

# # client = OpenAI(api_key=st.secrets["OPENAI_API_KEY"])
# # openai = OpenAI(
# #     api_key="K5P_f+Dy9Z_lzs3.R_6XklzW",
# #     base_url="https://cloud.olakrutrim.com/v1",
# # )

# client = Groq(
#     api_key= "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",
# )

# # if "openai_model" not in st.session_state:
# #     st.session_state["openai_model"] = "gpt-3.5-turbo"

# if "messages" not in st.session_state:
#     # st.session_state.messages = []
#     st.session_state.messages = [{"role":"system", "content": context2}]

# for message in st.session_state.messages:
#     with st.chat_message(message["role"]):
#         st.markdown(message["content"])

# if prompt := st.chat_input("What is up?"):
#     st.session_state.messages.append({"role": "user", "content": prompt})
#     with st.chat_message("user"):
#         st.markdown(prompt)

#     with st.chat_message("assistant"):
#         # stream = client.chat.completions.create(
#         #     model=st.session_state["openai_model"],
#         #     messages=[
#         #         # {"role":"system", "content": "You are a hospital feedback Chatbot, asking the user about the feedback for the hospital, ask the user one question at a time only in kannada lnaguage, make sure you interact only in kannada language and notin english"},
#         #         {"role": m["role"], "content": m["content"]}
#         #         for m in st.session_state.messages
#         #     ],
#         #     stream=True,
#         # )
#         # chat_completion = openai.chat.completions.create(
#         #     model="Krutrim-spectre-v2",
#         #     messages=[
#         #         {"role": m["role"], "content": m["content"]}
#         #         for m in st.session_state.messages
#         #     ],
#         #     max_tokens= 2048,
#         #     # stream= True, # Optional, Defaults to false
#         #     temperature= 0, # Optional, Defaults to 1. Range: 0 to 2
#         # )

#         chat_completion = client.chat.completions.create(
#         messages=[
#             {"role": m["role"], "content": m["content"]}
#             for m in st.session_state.messages
#         ],
#         model="llama3-8b-8192",
#         )

#         print(chat_completion.choices[0].message.content.encode("utf-8").decode())
#         stream = chat_completion.choices[0].message.content.encode("utf-8").decode()

#         print(st.session_state.messages)
#         # for m in st.session_state.messages:
#         #     print(m["role"],m["content"])
#         # response = st.write_stream(stream)
#         response = st.write(stream)
#     st.session_state.messages.append({"role": "assistant", "content": response})



import streamlit as st
from groq import Groq

st.title("Ask Paul")

context2 = """You are a chatbot answering queries of the user. the user can ask 2 types of questions
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

# client initialization with API key
client = Groq(
    api_key="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",
)

# Initial session state setup
if "messages" not in st.session_state:
    st.session_state.messages = [{"role": "system", "content": context2}]
    st.session_state.chat_display = [{"role": "assistant", "content": "Hello! How can I assist you today with your medical queries?"}]

# Displaying chat history (without the system message)
for message in st.session_state.chat_display:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Handling user input
if prompt := st.chat_input("Ask Paul anything ✍"):
    st.session_state.chat_display.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    # Sending the system message along with the conversation to the model
    chat_completion = client.chat.completions.create(
        messages=[
            {"role": m["role"], "content": m["content"]}
            for m in st.session_state.messages  # using full history with system message
        ] + [{"role": "user", "content": prompt}],  # add the user input for the current completion
        model="llama3-8b-8192",
    )

    # Extracting the response
    response = chat_completion.choices[0].message.content.encode("utf-8").decode()

    # Displaying the assistant's response in the chat
    with st.chat_message("assistant"):
        st.markdown(response)

    # Update the state with the assistant's response
    st.session_state.chat_display.append({"role": "assistant", "content": response})

    # Store the complete conversation with the system message
    st.session_state.messages.append({"role": "user", "content": prompt})
    st.session_state.messages.append({"role": "assistant", "content": response})
