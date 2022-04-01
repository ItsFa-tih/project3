from io import StringIO
import streamlit as st
from dataclasses import dataclass
from datetime import datetime
from typing import List
import hashlib

# NEWLY ADDED CODE

# New import list to connect streamlit, contract and Ganache
import os
import json
from web3 import Web3
from dotenv import load_dotenv
from pathlib import Path

# Loading env variable
load_dotenv()

# Define and connect a new Web3 provider
w3 = Web3(Web3.HTTPProvider(os.getenv("WEB3_PROVIDER_URI")))

#---------------------------------------------------------------#
# Contract Helper function:
# 1. Loads the contract once using cache
# 2. Connects to the contract using the contract address and ABI
#---------------------------------------------------------------#

# Cache the contract on load
@st.cache(allow_output_mutation=True)
# Define the load_contract function
def load_contract():

    # Load Resume ABI
    with open(Path('./contracts/compiled/resume_abi.json')) as f:
        resume_abi = json.load(f)

    # Set the contract address (this is the address of the deployed contract)
    contract_address = os.getenv("SMART_CONTRACT_ADDRESS")

    # Connecting our Ganache and get the contract
    contract = w3.eth.contract(
        address=contract_address,
        abi=resume_abi
    )
    # Return the contract from the function
    return contract

# Load the contract
contract = load_contract()

#------------------------#
# Streamlit Title & Header
#------------------------#
st.markdown("# Welcome to My Block Chain Resume")
st.markdown("## Start by uploading your resume then hit ' Add your resume to the block button' ")

#----------------#
# Uploading Resume
#----------------#
accounts = w3.eth.accounts

account = accounts[0]

candidate_account = st.selectbox("Select Candiate Account", options=accounts)

uploaded_file:str = st.file_uploader("Choose a file")
# if uploaded_file:
#     for line in uploaded_file:
#         st.write(line)
resume_details = st.text_input("Resume Details", value="My Block Chain Resume Upload for: ")

  
if st.button("Add your resume to the Block"):
      contract.functions.uploadResume(candidate_account, resume_details).transact({'from': account, 'gas': 1000000})
    
    # new_block=Block(uploaded_file=Block, creator_id=10)
    # st.write(new_block)
