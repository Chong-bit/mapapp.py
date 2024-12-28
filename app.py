!pip install pyngrok
from pyngrok import ngrok

# Start ngrok tunnel
public_url = ngrok.connect(port='8501') # Default Streamlit port
print(f"Public URL: {public_url}")

# Run Streamlit app
!streamlit run app.py &
