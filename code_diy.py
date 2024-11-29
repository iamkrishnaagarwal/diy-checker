from streamlit_option_menu import option_menu
import google.generativeai as genai
from dotenv import load_dotenv
import streamlit as st
import base64
import os

load_dotenv('.env')
genai_key = os.getenv("GOOGLE_API_KEY")

st.set_page_config(page_title="DIY Tester || Skin Formulator", page_icon=":moon:", layout="wide")
st.image("img\logo.png", width=300)
st.markdown("<style> .element-container { display: flex; justify-content: center; } </style>", unsafe_allow_html=True)

st.markdown("""<style>.stApp {background-color: #0E1117;color: white;}</style>""",unsafe_allow_html=True,)

selected2 = option_menu(None, ["DIY's", "About", "Contact"],  
    menu_icon="cast", default_index=0, orientation="horizontal")

if selected2 == "DIY's":
    st.title("🫧 DIY Checker")
    # Create a large text input box
    col1, col2 = st.columns(2)
    with col1:
        options_l = ["English", "Hindi"]
        selected_option_l = st.selectbox("Select Your Prefered Output Language:", options_l)
        # language = st.select_slider
    with col2:
        options_s = ["Vasanta (Spring) Mid-March to May", "Grishma (Summer) May to Mid-July", 
        "Varsha (Monsoon) Mid-July to September", "Sharad (Autumn) October to November", 
        "Hemant (Pre-Winter) December to Mid-January", "Shishir (Winter) Mid-January to March"]
        selected_option_s = st.selectbox("Select Your Prefered Season:", options_s)
        season = st.select_slider
    options_skin = ["Normal Skin (Samanya Twacha)", "Oily Skin (Tikti Twacha)", 
    "Dry Skin (Rukha Twacha)", "Combination Skin (Sanyukt Twacha)", "Sensitive Skin (Samvedansheel Twacha)", 
    "Pigmented Skin (Rang Dhanik Twacha)", "Acne-Prone Skin (Dhooshan Rupi Twacha)"]
    selected_option_skin = st.selectbox("Select Your Prefered Season:", options_skin)
    skin_type = st.select_slider
    user_input = st.text_area("Enter your DIY Recipe (in max 100 words):", height=200)
    # Function to count words
    def count_words(text):
        return len(text.split())
    # Create a submit button
    if st.button("Check Your Recipe Now"):
        if not user_input.strip():
            st.warning("Please enter a detailed DIY recipe.")
        if user_input:
            word_count = count_words(user_input)
            if word_count > 100:
                st.warning("You have exceeded the word limit of 100 words.")
            elif word_count <= 100:
                genai.configure(api_key = genai_key)
                model = genai.GenerativeModel("gemini-1.5-flash")
                user_input = f"Especially for {selected_option_skin}, used in {selected_option_s} season in {selected_option_l} tell me to use it or not especially for my skin type and things to remeber before using the below recipe {user_input} "
                # st.write(user_input)
                response = model.generate_content(user_input)
                st.write(response.text)
                st.markdown("""<div style="text-align: center;">
                            <a href="https://skin-formulator.mini.site" target="_blank" style="text-decoration: none; color: #FAF9F6; font-size: 14px;">
                            Note: This advice is AI-generated. It's always recommended to consult with a dermatologist for personalized skincare advice.
                            </a></div>""",unsafe_allow_html=True)

if selected2 == "About":
    about_col1, about_col2 = st.columns(2)
    with about_col1:
        st.image('img\word_c.png')
    with about_col2:
        st.title("🚀 Who we are")
        st.markdown("""<div style= text-align:left;">
            At Skin Formulator, we understand that skincare goes beyond the surface—it's a ritual of self-care, confidence, and well-being. Our philosophy is rooted in the belief that every individual’s skin is unique, deserving personalized care that aligns with their specific needs. That's why we are committed to transparency, education, and empowerment, providing not only exceptional products but also the knowledge behind the ingredients.
            ### **Our Approach: Science Meets Nature**  
We believe in harmonizing the power of nature with the precision of science. Every product is a testament to our dedication to quality, safety, and innovation. From potent plant extracts and nourishing oils to clinically tested actives, we ensure each ingredient serves a purpose—delivering visible results while being gentle on the skin. Our team of dermatologists and chemists collaborates to craft formulations that are dermatologically tested, cruelty-free, and free from harmful additives.

### **Personalized Skincare Solutions**  
At Skin Formulator, we celebrate individuality. Our customizable DIY face wash kits, SkinFormulator, offer a hands-on approach to skincare, allowing you to tailor your face wash based on your unique skin type and concerns. With easy-to-understand instructions and fun, interactive modules, we guide you through the process of creating your own skincare—because who knows your skin better than you?

### **Sustainability & Responsibility**  
We are deeply committed to minimizing our ecological footprint. Our sustainable practices include sourcing raw materials responsibly, using biodegradable or recyclable packaging, and supporting fair trade suppliers. We believe in creating beauty that not only nurtures the skin but also protects the environment for future generations.

### **Educational Commitment**  
Education is at the heart of Skin Formulator. Through our courses, workshops, and online resources, we empower you to understand the science behind skincare. From learning about different skin types to exploring the chemistry of natural and synthetic ingredients, we ensure you have the tools to make informed choices.

### **Our Promise to You**  
1. **Quality First**: We use only premium-grade ingredients tested for safety and efficacy.  
2. **Customizable Care**: Skincare designed by you, for you.  
3. **Sustainability Focus**: Ethical sourcing, eco-friendly packaging, and conscious production methods.  
4. **Transparency**: Clear labeling, honest marketing, and full ingredient disclosure.  
5. **Inclusivity**: Products crafted to cater to all skin types, tones, and concerns.

### **Join the Skin Formulator Community**  
Whether you're a skincare novice or a seasoned enthusiast, Skin Formulator invites you to embark on a journey of discovery, creativity, and transformation. Together, let's redefine skincare—where science, art, and sustainability unite to reveal your most radiant self.
            </div>""", unsafe_allow_html=True)
    # Embed the video in an HTML iframe with custom width and height
    st.markdown(
        f"""
        <center><iframe width="400" height="250" src="https://www.youtube.com/embed/zZImFU7K1R4" frameborder="1" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe></center>
        """, 
        unsafe_allow_html=True
    )


if selected2 == "Contact":
    c1, c2 = st.columns(2)
    with c1:
        st.image('img\carousel-3.png')
    with c2:
        # st.markdown("<style> .element-container { display: flex; justify-content: center; } </style>", unsafe_allow_html=True)
        c2_1, c2_2 = st.columns(2)
        with c2_1:
            st.markdown("""<a href="https://www.instagram.com/skinformulator.in/">
                        <img src="data:image/png;base64,{}" width="250"></a>""".format(
                            base64.b64encode(open("img\insta_logo.png", "rb").read()).decode()),unsafe_allow_html=True)
            
            st.markdown("""<a href="https://skin-formulator.mini.site">
                        <img src="data:image/png;base64,{}" width="250"></a>""".format(
                            base64.b64encode(open("img\web_logo.png", "rb").read()).decode()),unsafe_allow_html=True)
            st.markdown("<style> .element-container { display: flex; justify-content: center; } </style>", unsafe_allow_html=True)



        with c2_2:
            st.markdown("""<a href="https://wa.me/message/H224ZTDRTT6TC1">
                        <img src="data:image/png;base64,{}" width="250"></a>""".format(
                            base64.b64encode(open("img\whatsapp_logo.png", "rb").read()).decode()),unsafe_allow_html=True)
            
            st.markdown("""<a href="https://skin-formulator.mini.site">
            <img src="data:image/png;base64,{}" width="250"></a>""".format(
                base64.b64encode(open("img/note.png", "rb").read()).decode()),unsafe_allow_html=True)
st.write('')
st.write('')
st.write('')
st.write('')

st.markdown(
    """
    <div style="text-align: center;">
        <a href="https://skin-formulator.mini.site" target="_blank" style="text-decoration: none; color: #FAF9F6; font-size: 20px;">
            SHOP SKINCARE NOW WITH SKINFORMULATOR
        </a>
    </div>
    """,
    unsafe_allow_html=True
)