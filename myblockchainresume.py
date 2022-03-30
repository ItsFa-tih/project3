from io import StringIO
import streamlit as st
from dataclasses import dataclass
from datetime import datetime
from typing import List
import hashlib
st.markdown("# Welcome to MyBlockChainResume")
st.markdown("## Start by uploading your resume then hit ' Add your resume to the block button' ")

uploaded_file:str = st.file_uploader("Choose a file")
if uploaded_file:
        for line in uploaded_file:
            st.write(line)
  
if st.button("Add your resume to the Block"):
    new_block=Block(uploaded_file=Block, creator_id=10)
    st.write(new_block)
