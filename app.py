import streamlit as st
import google.generativeai as genai
import os

# Set Google API Key
os.environ['GOOGLE_API_KEY'] = "AIzaSyDDTRFUeanEaGjtZm2iLzUuUAbZs7Bx1Ps"
genai.configure(api_key="AIzaSyDDTRFUeanEaGjtZm2iLzUuUAbZs7Bx1Ps")
model = genai.GenerativeModel("gemini-pro")

def main():
    # Set Page Configuration
    st.set_page_config(page_title="Content Generator", layout="wide")
    st.title("Headlines AI")

    st.sidebar.subheader("Platform and Content Type")
    platform_options = {
        "YouTube": ["Video Ideas", "Titles", "Descriptions", "Hashtags", "CTAs"],
        "Instagram": ["Photo Ideas", "Captions", "Hashtags", "CTAs"],
        "Tiktok": ["Trend Ideas", "Captions", "Hashtags", "CTAs"],
        "Medium": ["Article Ideas", "Titles", "Body Content", "CTAs"],
        "Reddit": ["Post Ideas", "Titles", "Post Content", "CTAs"],
        "Blog": ["Blog Post Ideas", "Titles", "Post Content", "CTAs"]
    }
    selected_platform = st.sidebar.selectbox("Select platform:", list(platform_options.keys()))
    selected_option = st.sidebar.radio("What do you want to generate?", platform_options[selected_platform])

    # Prompt Input
    st.subheader("Describe your idea:")
    prompt = st.text_input("Prompt:")

    # Button for Content Generation
    if st.button("Magic!"):
        try:
            # Generate Content
            response = model.generate_content(f"Generate a {selected_option.lower()} based on the following prompt: {prompt}")

            # Display Generated Content
            st.subheader(f"Generated {selected_option.title()} Content:")
            if response.parts:
                titles = [part.text.strip() for part in response.parts]
                for i, title in enumerate(titles, start=1):
                    st.write(f"{i}. {title}")
            else:
                st.write("No content generated.")
        except Exception as e:
            st.error(f"Error: {str(e)}")

if __name__ == "__main__":
    main()
