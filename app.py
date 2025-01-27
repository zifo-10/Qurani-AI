import streamlit as st

# Set page configuration for Arabic layout
st.set_page_config(page_title="بحث القرآن", page_icon="📖", layout="centered")

# Simulated results (full details of ayah)
results = [
    {
        "_id": {"$oid": "67974cb35e8e7e6047695ee3"},
        "surah_no": 2,
        "surah_name_en": "The Cow",
        "surah_name_ar": "البقرة",
        "surah_name_roman": "Al-Baqarah",
        "ayah_no_surah": 9,
        "ayah_no_quran": 16,
        "ayah_ar": "يُخَٰدِعُونَ ٱللَّهَ وَٱلَّذِينَ ءَامَنُوا۟ وَمَا يَخْدَعُونَ إِلَّآ أَنفُسَهُمْ وَمَا يَشْعُرُونَ",
        "ayah_en": "They seek to deceive Allah and the believers, yet they only deceive themselves, but they fail to perceive it.",
        "ruko_no": 3,
        "juz_no": 1,
        "manzil_no": 1,
        "hizb_quarter": 1,
        "total_ayah_surah": 286,
        "place_of_revelation": "Medinan",
        "sajah_ayah": False,
        "no_of_word_ayah": 10,
        "list_of_words": ["يُخَٰدِعُونَ", "ٱللَّهَ", "وَٱلَّذِينَ", "ءَامَنُوا۟", "وَمَا", "يَخْدَعُونَ", "إِلَّآ",
                          "أَنفُسَهُمْ", "وَمَا", "يَشْعُرُونَ"],
        "Ayah_without_tashkil": "يخادعون الله والذين آمنوا وما يخدعون إلا أنفسهم وما يشعرون"
    }
]

# Custom CSS for a dark theme with Arabic font and professional header box
st.markdown("""
    <style>
    /* General styling */
    .stApp {
        background-color: #121212;
        color: #E0E0E0;
        direction: rtl;
        font-family: 'Amiri Quran', serif; /* Ensure Amiri Quran font is applied */
        max-width: 800px; /* Restrict the width of the content */
        margin: 0 auto; /* Center the content */
    }

    .stTextInput>div>input {
        background-color: #333;
        color: #fff;
        border: 1px solid #444;
        border-radius: 8px;
        height: 50px;
        font-size: 16px;
        padding-left: 15px;
        text-align: right;
        width: 100%;  /* Make the search input take full width */
    }

    /* Arabic font and styling */
    @import url('https://fonts.googleapis.com/css2?family=Amiri+Quran&display=swap'); /* Correct font import */

    /* Styling for the search results container */
    .results-container {
        margin-top: 40px;
        padding: 30px;
        background-color: #1F1F1F;
        border-radius: 12px;
        box-shadow: 0px 6px 18px rgba(0, 0, 0, 0.5);
        width: 100%;  /* Match the width of the search input */
    }

    .result-bubble {
        background-color: #333333;
        color: white;
        border-radius: 12px;
        padding: 15px;
        margin: 10px 0;
        max-width: 100%;
        word-wrap: break-word;
    }

    .result-header {
        font-size: 18px;
        font-weight: bold;
        margin-bottom: 10px;
        background-color: #9C27B0;
        padding: 10px;
        border-radius: 10px;
        text-align: center;
    }

    .result-body {
        font-size: 14px;
        margin-bottom: 8px;
    }

    /* Larger font for Ayah in Arabic */
    .ayah-arabic {
        font-size: 20px;
        font-weight: bold;
        margin-bottom: 15px;
    }

    /* Styling for the header (title) */
    .header-container {
        background-color: #333;
        color: #fff;
        padding: 30px;
        border-radius: 12px;
        box-shadow: 0px 6px 18px rgba(0, 0, 0, 0.5);
        text-align: center;
        margin-bottom: 40px;
    }

    .header-title {
        font-size: 36px;
        font-weight: bold;
        color: #9C27B0;
    }

    .header-description {
        font-size: 18px;
        margin-top: 10px;
        color: #B0B0B0;
    }

    /* Specific color for the Surah and Ayah */
    .surah-ayah-header {
        font-size: 22px;
        font-weight: bold;
        color: #4CAF50; /* Green color, associated with the Quran */
        text-align: center;
        margin-bottom: 15px;
    }
    </style>
""", unsafe_allow_html=True)

# Professional header (box with gray background)
st.markdown("""
    <div class="header-container">
        <h1 class="header-title">بحث في القرآن الكريم</h1>
        <p class="header-description">اكتب سؤالك للبحث عن الآيات ذات الصلة.</p>
    </div>
""", unsafe_allow_html=True)

# Collect user input in Arabic
with st.form("search_form"):
    user_query = st.text_input("أدخل سؤالك عن القرآن:", placeholder="على سبيل المثال: رحمة، صلاة، خلق...")
    submit_button = st.form_submit_button(label="بحث", help="اضغط للبحث عن الآيات ذات الصلة.")

# Display results (simulated)
if submit_button and user_query:
    st.markdown("<div class='results-container'>", unsafe_allow_html=True)
    if results:
        for verse in results:
            st.markdown(f"""
                <div class='result-bubble'>
                    <div class='surah-ayah-header'>سورة {verse['surah_name_ar']} - آية {verse['ayah_no_surah']}</div>
                    <div class='ayah-arabic'>{verse['ayah_ar']}</div>
                    <div class='result-body'>
                        <strong>الترجمة إلى الإنجليزية:</strong> {verse['ayah_en']}
                    </div>
                    <div class='result-body'>
                        <strong>رقم الجزء:</strong> {verse['juz_no']} <br>
                        <strong>مكان النزول:</strong> {verse['place_of_revelation']}
                    </div>
                </div>
            """, unsafe_allow_html=True)
    else:
        st.error("لم يتم العثور على نتائج.")
    st.markdown("</div>", unsafe_allow_html=True)
