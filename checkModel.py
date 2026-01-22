import google.generativeai as genai
import os

# --- PASTE YOUR API KEY HERE ---
api_key = "AIzaSyCIBmlxSFmeUJgCWWxHMWwqjphmcT_dcWM" 

genai.configure(api_key=api_key)

print("Listing available models for your key...")
try:
    for m in genai.list_models():
        if 'generateContent' in m.supported_generation_methods:
            print(f"- {m.name}")
except Exception as e:
    print(f"Error: {e}")