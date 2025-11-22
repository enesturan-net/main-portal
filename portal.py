import streamlit as st
import os

# --- SAYFA AYARLARI (Genişletilmiş ve Temiz) ---
st.set_page_config(
    page_title="TMCO Portal", 
    layout="wide", 
    page_icon="✨",
    initial_sidebar_state="collapsed"
)

# --- MODERN CSS TASARIMI ---
st.markdown("""
<style>
    /* 1. GENEL SAYFA YAPISI */
    .stApp {
        background-color: #f8f9fa; /* Çok hafif gri (Göz yormaz) */
        font-family: 'Inter', sans-serif;
    }
    
    /* Üstteki boşluğu kaldır */
    .block-container {
        padding-top: 2rem;
        padding-bottom: 5rem;
        max-width: 1200px; /* İçeriği ortada topla, çok yayılmasın */
    }

    /* 2. HEADER (ÜST ALAN) TASARIMI */
    .header-container {
        text-align: center;
        padding: 40px 20px;
        background: white;
        border-radius: 20px;
        box-shadow: 0 10px 30px rgba(0,0,0,0.04);
        margin-bottom: 40px;
        border-bottom: 4px solid #4ECDC4; /* Logonuzdaki o güzel Turkuaz */
    }
    
    .main-title {
        font-size: 2.8rem;
        font-weight: 800;
        color: #2d3436;
        letter-spacing: -1px;
        margin-top: 15px;
        margin-bottom: 5px;
    }
    
    .sub-title {
        font-size: 1.1rem;
        color: #636e72;
        font-weight: 400;
    }

    /* 3. KART (BUTTON) TASARIMI - GLASSMORPHISM & HOVER */
    div.stButton > button {
        width: 100%;
        height: 160px; /* Sabit yükseklik - Hepsi eşit dursun */
        background: white;
        border: 1px solid #eee;
        border-radius: 16px;
        box-shadow: 0 4px 6px rgba(0,0,0,0.02);
        transition: all 0.3s cubic-bezier(0.25, 0.8, 0.25, 1);
        display: flex;
        flex-direction: column;
        align-items: flex-start; /* Sola yaslı daha modern */
        justify-content: center;
        padding: 25px;
        position: relative;
        overflow: hidden;
    }

    /* Kartın Üzerine Gelince (Hover) */
    div.stButton > button:hover {
        transform: translateY(-7px);
        box-shadow: 0 15px 30px rgba(78, 205, 196, 0.2); /* Turkuaz gölge */
        border: 1px solid #4ECDC4;
    }

    /* Kart İçindeki Yazıların Stili */
    div.stButton > button p {
        font-size: 16px !important;
        color: #2d3436;
        text-align: left;
        line-height: 1.4;
    }
    
    /* İkonun Büyüklüğü */
    div.stButton > button p:first-child {
        font-size: 28px !important; /* İkon boyutu */
        margin-bottom: 10px;
    }

    /* Footer (Alt Bilgi) */
    .footer {
        text-align: center;
        margin-top: 50px;
        color: #b2bec3;
        font-size: 0.8rem;
    }
</style>
""", unsafe_allow_html=True)

# --- HEADER ALANI (LOGO + BAŞLIK) ---
# Burayı tek bir kutu gibi tasarladık
logo_path = "logo.png"

with st.container():
    st.markdown('<div class="header-container">', unsafe_allow_html=True)
    
    # Logo Ortada
    col1, col2, col3 = st.columns([4, 2, 4])
    with col2:
        if os.path.exists(logo_path):
            st.image(logo_path, use_container_width=True)
    
    # Başlıklar
    st.markdown('<div class="main-title">TMCO Otomasyon</div>', unsafe_allow_html=True)
    st.markdown('<div class="sub-title">İnsan Kaynakları ve Analiz Araçları Merkezi</div>', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

# --- UYGULAMA KARTLARI ---
# Kartların daha düzenli durması için boş olanları "Geliştiriliyor" olarak işaretledim.

uygulamalar = [
    {
        "ad": "Raven Zeka Testi",
        "ikon": "🧠",
        "aciklama": "Çocuk ve yetişkinler için otomatik yaş normu analizi ve raporlama.",
        "link": "https://raven-test-app-8vb5cu4nzr3cxgvuiwybus.streamlit.app/" 
    },
    {
        "ad": "Toplu Klasifikasyon",
        "ikon": "📋",
        "aciklama": "Test sonuçlarına göre toplu aday sınıflandırma.",
        "link": "https://toplu-klasifikasyon.streamlit.app/"
    },
    {
        "ad": "New App",
        "ikon": "🎯",
        "aciklama": "#.",
        "link": "#"
    },
    {
        "ad": "New App",
        "ikon": "📊",
        "aciklama": "#",
        "link": "#"
    },
    {
        "ad": "New App",
        "ikon": "📅",
        "aciklama": "#",
        "link": "#"
    },
    {
        "ad": "New App",
        "ikon": "📂",
        "aciklama": "#",
        "link": "#"
    }
]

# --- GRID SİSTEMİ (Daha Geniş ve Ferah) ---
# 2 Sütunlu bir yapı daha profesyonel durur (Kartlar daha geniş olur)
# Eğer 3 sütun istersen aşağıdaki 2 rakamını 3 yapabilirsin.
cols = st.columns(3, gap="large") 

for i, app in enumerate(uygulamalar):
    col = cols[i % 3]
    with col:
        st.link_button(
            label=f"{app['ikon']}  **{app['ad']}**\n\n{app['aciklama']}", 
            url=app['link'],
            use_container_width=True,
            help=f"{app['ad']} aracını başlat"
        )

# --- FOOTER ---
st.markdown('<div class="footer">© 2025 Talent Management Co. - Tüm Hakları Saklıdır</div>', unsafe_allow_html=True)

