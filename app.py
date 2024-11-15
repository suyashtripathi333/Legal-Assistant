import streamlit as st
from google.cloud import aiplatform
import os
import vertexai 
vertexai.init(project="legalify-441709", location="us-central1")
import openai

import google.generativeai as genai
from google.generativeai.types import HarmCategory, HarmBlockThreshold

# Set Google Cloud authentication key (ensure the path to your .json key is correct)
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "legalify-441709-ba2d68a1b491.json"  # Update with actual file path

# Initialize Google Vertex AI
aiplatform.init(project="legalify-441709", location="us-central1")

# List of legal document types (same as before)
document_types = [
    "Lease Deed (for a term of years)",
    "Rent Agreement",
    "Agreement for Sale of a House (Sale Agreement)",
    "Agreement between Independent Contractor and Service Provider",
    "Shareholders Agreement",
    "Joint Venture / Share Holder’s Agreement",
    "Franchise Agreement",
    "Employee Service Agreement",
    "Business Services Agreement",
    "Loan Agreement with Security",
    "Loan Agreement",
    "Retainership Agreement",
    "Hire Purchase Agreement",
    "Agreement of License to Publish on Royalty Basis",
    "Confidential Information and Non-Disclosure Agreement (NDA)",
    "Deed of Family Trust",
    "Simple Will",
    "Deed of Gift of Moveable Property / Immovable Property",
    "Partition Deed",
    "Memorandum Recording Family Settlement",
    "Deed of Adoption",
    "Deed of Hypothecation (HP)",
    "Deed of Guarantee",
    "Deed of Lease (for a term in perpetuity)",
    "Licence to use Copyright",
    "Power of Attorney",
    "Irrevocable Power of Attorney",
    "Revocation of the Power of Attorney",
    "General Power of Attorney (GPA)",
    "Legal Notice for Cancellation of Power of Attorney",
    "Legal Notice for Recovery of Friendly Loan",
    "Legal Notice for Non-Payment of Invoice",
    "Legal Notice for Non-Payment of Salary",
    "Legal Notice for Recovery of Money",
    "Cheque Bounce Notice Format",
    "Legal Notice for Recovery of Security Deposit",
    "Legal Notice for Breach of Trust",
    "Legal Notice for Cancellation of Sale Agreement",
    "Legal Notice for Trespassing",
    "Legal Notice for Wrongful Termination",
    "Legal Notice for Defamation",
    "Legal Notice for Property Partition",
    "Legal Notice for Non-performance of a Contract",
    "Legal Notice to Wife for Restitution of Conjugal Rights",
    "Legal Notice for Insurance Claim",
    "Writ Petition",
    "Bail Application Format",
    "Consumer Court Petition Format",
    "Draft Criminal Complaint for Harassment Sample",
    "Mutual Divorce Petition",
    "Application for Suit for Damages for Breach of Contract",
    "Public Interest Litigation",
    "Restraining Order",
    "Public Charitable Trust",
    "Deed of Family Trust",
    "Memorandum of Settlement of Industrial Dispute between Employer and Employees",
    "Security Bond for Grant of Succession Certificate",
    "Security Bond by a Surety",
    "Bond to Secure the Performance of a Contract",
    "Employee Bond for Non-Compete",
    "Bond and Bail Bond under CrPC 1973 after Arrest under a Warrant",
    "Simple Money Bond",
    "Simple Mortgage Deed",
    "Formation Agreement to Convert a Partnership into a Limited Company",
    "Articles of Association for Public Companies",
    "Memorandum of Understanding (MOU)",
    "Sample Letter to Builder for Delay in Handing Over the Possession",
    "Sample Complaint Letter to Police for Life Threat",
    "Separation Agreement between Husband and Wife",
    "Deed of Family Settlement for Division of Properties Left by a Deceased Between Son and Daughters Where Son Pays Money to Daughters",
    "Affidavit and Indemnity"
]

# Function to generate the legal draft using PaLM API
# def generate_draft(name, dob, address, issue, document_type):
#     """
#     Generate a personalized legal draft using Google Vertex AI's PaLM model.
#     """
#     endpoint = aiplatform.Endpoint(endpoint_name="projects/legal-441716/locations/asia-south1/endpoints/legal-441716")  # Replace with your actual endpoint ID

#     # Prepare a detailed prompt including user details
#     prompt = (f"Generate a {document_type} based on the following details:\n"
#               f"Name: {name}\n"
#               f"Date of Birth: {dob}\n"
#               f"Address: {address}\n"
#               f"Issue: {issue}\n\n"
#               f"Create a professional legal draft incorporating these details.")
    
#     # Call the PaLM API for text generation
#     response = endpoint.predict(instances=[{"content": prompt}])

#     # Extract and return the generated draft text
#     draft = response.predictions[0]['content']
#     return draft

# def generate_draft(name, dob, address, issue, document_type):
#     """
#     Generate a personalized legal draft using the Gemini 1.5 Pro model.
#     """
#     openai.api_key = "AIzaSyBpfhs6WtNRInvYeJhpfUtA18HYpjQZ600"
#     prompt = (f"Generate a {document_type} based on the following details:\n"
#               f"Name: {name}\n"
#               f"Date of Birth: {dob}\n"
#               f"Address: {address}\n"
#               f"Issue: {issue}\n\n"
#               f"Create a professional legal draft incorporating these details.")
    
#     response = openai.Completion.create(
#         engine="gemini-1.5-pro",
#         prompt=prompt,
#         max_tokens=1024,
#         n=1,
#         stop=None,
#         temperature=0.7,
#     )
    
#     draft = response.choices[0].text
#     return draft



# import google.generativeai as genai
# from google.generativeai.types import HarmCategory, HarmBlockThreshold

# API_KEY = "AIzaSyBpfhs6WtNRInvYeJhpfUtA18HYpjQZ600"

# def generate_draft(name, dob, address, issue, document_type):
#     genai.configure(api_key=API_KEY)

#     generation_config = {
#         "temperature": 0.1,
#         "top_p": 1,
#         "top_k": 32,
#         "max_output_tokens": 2048,
#     }

#     safety_settings = [
#         {"category": HarmCategory.HARM_CATEGORY_HATE_SPEECH, "threshold": HarmBlockThreshold.BLOCK_MEDIUM_AND_ABOVE},
#         {"category": HarmCategory.HARM_CATEGORY_DANGEROUS_CONTENT, "threshold": HarmBlockThreshold.BLOCK_MEDIUM_AND_ABOVE},
#         {"category": HarmCategory.HARM_CATEGORY_SEXUALLY_EXPLICIT, "threshold": HarmBlockThreshold.BLOCK_MEDIUM_AND_ABOVE},
#         {"category": HarmCategory.HARM_CATEGORY_HARASSMENT, "threshold": HarmBlockThreshold.BLOCK_MEDIUM_AND_ABOVE},
#     ]

#     model = genai.GenerativeModel(
#         model_name="gemini-1.5-flash",
#         generation_config=generation_config,
#         safety_settings=safety_settings
#     )

#     prompt_template = f"Generate a {document_type} draft based on the following details:\nName: {name}\nDOB: {dob}\nAddress: {address}\nIssue: {issue}\n"

#     try:
#         response = model.generate_content(prompt_template)
#         # Extract the draft content
#         draft = response['result']['candidates'][0]['content']['parts'][0]['text']
#         return draft
#     except Exception as e:
#         return f"An error occurred: {e}"



# API_KEY = "AIzaSyBpfhs6WtNRInvYeJhpfUtA18HYpjQZ600"

# def generate_draft(name, dob, address, issue, document_type):
#     genai.configure(api_key=API_KEY)

#     generation_config = {
#         "temperature": 0.1,
#         "top_p": 1,
#         "top_k": 32,
#         "max_output_tokens": 2048,
#     }

#     safety_settings = [
#         {"category": HarmCategory.HARM_CATEGORY_HATE_SPEECH, "threshold": HarmBlockThreshold.BLOCK_MEDIUM_AND_ABOVE},
#         {"category": HarmCategory.HARM_CATEGORY_DANGEROUS_CONTENT, "threshold": HarmBlockThreshold.BLOCK_MEDIUM_AND_ABOVE},
#         {"category": HarmCategory.HARM_CATEGORY_SEXUALLY_EXPLICIT, "threshold": HarmBlockThreshold.BLOCK_MEDIUM_AND_ABOVE},
#         {"category": HarmCategory.HARM_CATEGORY_HARASSMENT, "threshold": HarmBlockThreshold.BLOCK_MEDIUM_AND_ABOVE},
#     ]

#     model = genai.GenerativeModel(
#         model_name="gemini-1.5-flash",
#         generation_config=generation_config,
#         safety_settings=safety_settings
#     )

#     prompt_template = f"Generate a {document_type} draft based on the following details:\nName: {name}\nDOB: {dob}\nAddress: {address}\nIssue: {issue}\n"

#     try:
#         response = model.generate_content(prompt_template)
#         print(response)
        
#         # Access the generated content using dot notation
#         draft = response.result.candidates[0].content.parts[0].text
#         print("....",draft)
#         return draft
#     except Exception as e:
#         return f"An error occurred: {e}"


API_KEY = os.getenv('KEY')

def generate_draft(name, dob, address, issue, document_type):
    genai.configure(api_key=API_KEY)

    generation_config = {
        "temperature": 0.1,
        "top_p": 1,
        "top_k": 32,
        "max_output_tokens": 2048,
    }

    safety_settings = [
        {"category": HarmCategory.HARM_CATEGORY_HATE_SPEECH, "threshold": HarmBlockThreshold.BLOCK_MEDIUM_AND_ABOVE},
        {"category": HarmCategory.HARM_CATEGORY_DANGEROUS_CONTENT, "threshold": HarmBlockThreshold.BLOCK_MEDIUM_AND_ABOVE},
        {"category": HarmCategory.HARM_CATEGORY_SEXUALLY_EXPLICIT, "threshold": HarmBlockThreshold.BLOCK_MEDIUM_AND_ABOVE},
        {"category": HarmCategory.HARM_CATEGORY_HARASSMENT, "threshold": HarmBlockThreshold.BLOCK_MEDIUM_AND_ABOVE},
    ]

    model = genai.GenerativeModel(
        model_name="gemini-1.5-flash",
        generation_config=generation_config,
        safety_settings=safety_settings
    )

    prompt_template = f"Generate a {document_type} draft based on the following details:\nName: {name}\nDOB: {dob}\nAddress: {address}\nIssue: {issue}\n"

    try:
        response = model.generate_content(prompt_template)
        print("R",response)
        draft = response.candidates[0].content.parts[0].text
        print("D",draft)
        
        # Access the generated content using dot notation
        # draft = response.result.candidates[0].content.parts[0].text

        # draft = response.result.candidates[0].content.parts[0].get_text()
        return draft
    
    except Exception as e:
        return f"An error occurred: {e}"

# Example usage:
# name = "John Doe"
# dob = "01/01/1980"
# address = "123 Main St, Cityville"
# issue = "Vehicle rental agreement"
# document_type = "Vehicle Rental Agreement"

# generated_draft = generate_draft(name, dob, address, issue, document_type)
# print(generated_draft)

# # Example usage:
# name = "John Doe"
# dob = "01/01/1980"
# address = "123 Main St, Cityville"
# issue = "Vehicle rental agreement"
# document_type = "Vehicle Rental Agreement"

# generated_draft = generate_draft(name, dob, address, issue, document_type)
# print(generated_draft)

# Streamlit App UI
st.title("Legal Document Draft Generator")

# Form to take user input
with st.form(key='legal_form'):
    name = st.text_input("Enter your name:")
    dob = st.date_input("Enter your Date of Birth:")
    address = st.text_area("Enter your address:")
    issue = st.text_area("Describe your legal issue:")
    document_type = st.selectbox("Select the document type based on your issue:", document_types)
    submit_button = st.form_submit_button(label="Generate Legal Draft")

# Process user input
if submit_button:
    if not name or not dob or not address or not issue:
        st.error("Please fill out all fields")
    else:
        # Generate the legal draft based on the user's information and selected document type
        draft_output = generate_draft(name, dob, address, issue, document_type)

        # Display the generated draft
        st.subheader(f"Generated {document_type}:")
        st.write(draft_output)
