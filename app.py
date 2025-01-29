import streamlit as st

# Set page configuration for Arabic layout
st.set_page_config(page_title="الباحث القرآني", page_icon="🌙", layout="centered")

# Simulated results
results = [
    {
        "_id": {"$oid": "67974cb35e8e7e6047695ee3"},
        "surah_no": 2,
        "surah_name_ar": "البقرة",
        "ayah_no_surah": 9,
        "ayah_ar": "يُخَٰدِعُونَ ٱللَّهَ وَٱلَّذِينَ ءَامَنُوا۟ وَمَا يَخْدَعُونَ إِلَّآ أَنفُسَهُمْ وَمَا يَشْعُرُونَ",
        "ayah_en": "They seek to deceive Allah and the believers, yet they only deceive themselves, but they fail to perceive it.",
        "juz_no": 1,
        "place_of_revelation": "مدنية",
    }
]

# Quran-themed CSS with dark colors
st.markdown("""
    <style>
    /* General styling */
    .stApp {
        background-color: #0D0D0D;
        color: #F0F0F0;
        direction: rtl;
        font-family: 'Amiri Quran', 'Noto Naskh Arabic', serif;
        max-width: 800px;
        margin: 0 auto;
    }

    /* Quranic color palette */
    :root {
        --quran-green: #0A5F2F;
        --islamic-gold: #D4AF37;
        --deep-blue: #1A365F;
        --arabic-red: #8A2B32;
    }

    /* Search input styling */
    .stTextInput>div>input {
        background-color: #1A1A1A;
        color: #F0F0F0;
        border: 2px solid var(--islamic-gold);
        border-radius: 8px;
        height: 60px;
        font-size: 20px;
        padding: 10px 20px;
        text-align: right;
        width: 100%;
        font-family: 'Amiri Quran', serif;
    }

    /* Arabic fonts */
    @import url('https://fonts.googleapis.com/css2?family=Amiri+Quran&family=Noto+Naskh+Arabic:wght@400;600&display=swap');

    /* Results container */
    .results-container {
        margin-top: 40px;
        padding: 20px;
        background-color: #1A1A1A;
        border-radius: 12px;
        border: 1px solid var(--quran-green);
    }

    .result-bubble {
        background-color: #0A5F2F20;
        color: #F0F0F0;
        border-radius: 8px;
        padding: 25px;
        margin: 20px 0;
        border-left: 5px solid var(--islamic-gold);
    }

    .ayah-arabic {
        font-size: 28px;
        font-weight: bold;
        margin-bottom: 20px;
        color: var(--islamic-gold);
        line-height: 2.5;
        text-align: justify;
        text-justify: inter-word;
    }

    /* Header styling */
    .header-container {
        background: linear-gradient(135deg, var(--quran-green) 0%, var(--deep-blue) 100%);
        padding: 40px;
        border-radius: 12px;
        margin-bottom: 40px;
        border-bottom: 4px solid var(--islamic-gold);
    }

    .header-title {
        font-size: 42px;
        font-family: 'Noto Naskh Arabic', serif;
        color: var(--islamic-gold);
        text-shadow: 2px 2px 4px rgba(0,0,0,0.3);
    }

    .header-description {
        font-size: 20px;
        color: #C0C0C0;
        margin-top: 15px;
    }

    /* Button styling */
    .stButton>button {
        background-color: var(--quran-green);
        color: var(--islamic-gold) !important;
        border: 2px solid var(--islamic-gold) !important;
        border-radius: 8px;
        padding: 18px 45px;
        font-size: 20px;
        font-family: 'Noto Naskh Arabic', serif;
        transition: all 0.3s ease;
        margin-top: 20px;
    }

    .stButton>button:hover {
        background-color: var(--deep-blue) !important;
        transform: translateY(-2px);
        box-shadow: 0 4px 15px rgba(212, 175, 55, 0.3);
    }

    /* Metadata styling */
    .metadata {
        font-family: 'Noto Naskh Arabic', serif;
        color: #C0C0C0;
        font-size: 16px;
        border-top: 1px solid var(--quran-green);
        padding-top: 15px;
        margin-top: 20px;
    }
    </style>
""", unsafe_allow_html=True)

# Quranic Header
st.markdown("""
    <div class="header-container">
        <h1 class="header-title">الباحث القرآني</h1>
        <p class="header-description">الْقُرْآنُ هُدًى لِّلنَّاسِ وَبَيِّنَاتٍ مِّنَ الْهُدَىٰ وَالْفُرْقَانِ</p>
    </div>
""", unsafe_allow_html=True)

# Search Form
with st.form("search_form"):
    user_query = st.text_input("اكتب كلمات البحث هنا:", placeholder="﴿وَٱبْتَغُوا۟ فِيمَآ ءَاتَىٰكُمُ ٱللَّهُ﴾ [النساء:٣٤]...")
    submit_button = st.form_submit_button(label="ابحث في القرآن")

# Display Results
if submit_button and user_query:
    st.markdown("<div class='results-container'>", unsafe_allow_html=True)
    if results:
        for verse in results:
            st.markdown(f"""
                <div class='result-bubble'>
                    <div class='ayah-arabic'>{verse['ayah_ar']}</div>
                    <div class='metadata'>
                        <span>سورة {verse['surah_name_ar']} - الآية {verse['ayah_no_surah']}</span><br>
                        <span>الجزء {verse['juz_no']} | {verse['place_of_revelation']}</span>
                    </div>
                </div>
            """, unsafe_allow_html=True)
    else:
        st.error("لم يتم العثور على نتائج")
    st.markdown("</div>", unsafe_allow_html=True)