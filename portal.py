import streamlit as st

# --- SAYFA AYARLARI ---
st.set_page_config(page_title="TMCO Otomasyon", layout="wide", page_icon="🚀")

# --- TASARIM VE CSS ---
st.markdown("""
<style>
    /* Ana Başlık Stili */
    .main-title {
        text-align: center;
        font-size: 3rem;
        font-weight: 800;
        color: #2c3e50;
        margin-bottom: 10px;
    }
    .sub-title {
        text-align: center;
        font-size: 1.2rem;
        color: #7f8c8d;
        margin-bottom: 50px;
    }
    
    /* Kart Tasarımı */
    div.stButton > button {
        width: 100%;
        height: auto;
        padding: 20px;
        background-color: white;
        border: 1px solid #e0e0e0;
        border-radius: 15px;
        box-shadow: 0 4px 6px rgba(0,0,0,0.05);
        transition: all 0.3s ease;
        text-align: left;
        display: flex;
        flex-direction: column;
        align-items: center;
    }
    
    /* Kart Hover Efekti (Üzerine gelince) */
    div.stButton > button:hover {
        transform: translateY(-5px);
        box-shadow: 0 10px 20px rgba(0,0,0,0.1);
        border-color: #FF4B4B;
        background-color: #fff5f5;
    }
    
    /* İkon ve Yazı Stilleri */
    .card-icon {
        font-size: 3rem;
        margin-bottom: 15px;
    }
    .card-title {
        font-size: 1.2rem;
        font-weight: bold;
        color: #333;
        margin-bottom: 5px;
    }
    .card-desc {
        font-size: 0.9rem;
        color: #666;
        font-weight: normal;
    }
</style>
""", unsafe_allow_html=True)

# --- BAŞLIK ALANI ---
st.markdown('<div class="main-title">TMCO Otomasyon Araçları</div>', unsafe_allow_html=True)
st.markdown('<div class="sub-title">Tüm analiz ve raporlama araçlarına tek noktadan erişim</div>', unsafe_allow_html=True)

# --- UYGULAMA LİSTESİ (BURAYI DÜZENLEYECEKSİN) ---
# Yeni uygulama yaptıkça buraya ekleyebilirsin.
uygulamalar = [
    {
        "ad": "Raven Yaş ve Ülke Analizi",
        "ikon": "🧠",
        "aciklama": "Çocuk ve yetişkinler için zeka testi skorlama ve raporlama aracı.",
        "link": "https://raven-test-app-8vb5cu4nzr3cxgvuiwybus.streamlit.app/#raven-testi-otomatik-analiz-ve-raporlama"  # BURAYA SENİN RAVEN UYGULAMANIN LİNKİNİ YAPIŞTIR
    },
    {
        "ad": "New App",
        "ikon": "📊",
        "aciklama": "#",
        "link": "#" 
    },
    {
        "ad": "New App",
        "ikon": "🎯",
        "aciklama": "#",
        "link": "#"
    },
    {
        "ad": "Profilleme & Aday Değerlendirme",
        "ikon": "📝",
        "aciklama": "Profill oluştur & aday değerlendir",
        "link": "https://tmco-profiler.streamlit.app/"
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

# --- KARTLARI IZGARA (GRID) ŞEKLİNDE DİZME ---
cols = st.columns(3) # Yan yana 3 kutu olsun (Mobil uyumludur, telefonda alt alta iner)

for i, app in enumerate(uygulamalar):
    col = cols[i % 3] # Sırayla sütunlara dağıt
    with col:
        # Streamlit'in yeni link_button özelliği (Çok daha stabil çalışır)
        st.link_button(
            label=f"{app['ikon']} {app['ad']}\n\n{app['aciklama']}", 
            url=app['link'],
            use_container_width=True,
            help=f"{app['ad']} uygulamasını açmak için tıklayın"
        )

        st.write("") # Kartlar arası boşluk bırak







