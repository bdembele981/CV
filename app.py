import streamlit as st

# 1. Configuration de la page
st.set_page_config(page_title="Portfolio Nianguiri Dembele", layout="wide")

# 2. CSS pour la couleur bleu foncé de la sidebar
st.markdown("""
    <style>
        [data-testid="stSidebar"] {
            background-color: #b0bec5;
            color: white;
        }
        [data-testid="stSidebar"] * {
            color: white !important;
        }
    </style>
""", unsafe_allow_html=True)

# 3. BARRE LATÉRALE (SIDEBAR - Environ 30% de l'écran par défaut)
with st.sidebar:
    st.image("DEMBELE.JPG", caption="Nianguiri Dembele", width=150)
    st.title("NIANGUIRI DEMBELE")
    st.write("📧 bdembele981@gmail.com")
    st.write("🎓 Technicien supérieur en Géomatique")
    st.write("📍 Pikine, Dakar - Sénégal")

# 4. CONTENU PRINCIPAL
st.title("🎓 ETUDIANT EN GEOMATIQUE")

st.write("""
Technicien supérieur en géomatique, je suis en mesure de fournir des cartes thématiques, topographiques et SIG. 
Passionné par la programmation et l’analyse géographique, je m’intéresse particulièrement 
à la gestion territoriale et aux applications environnementales.
""")

st.header("🛠 Compétences")
st.markdown("""
- *Cartographie numérique et analyse spatiale* (SIG : ArcGIS, QGIS)
- *Collecte et gestion de données* (GPS, QField)
- *Analyse Python* & Bases de données spatiales
- *Réalisation de cartes* thématiques et analytiques
- *Notions en MMNT* & Entrepreneuriat
""")

st.header("📚 Projets académiques") 
# Correction ici : ajout de st.markdown
st.markdown("""
- *Cartographie SIG* : Collecte, traitement et visualisation de données géospatiales  
- *Programmation Python* : Développement d’applications et analyse de données  
- *Dessin de plan* : Conception d’un plan architectural complet  
- *Géographie appliquée* : Réalisation de cartes thématiques sous ArcGIS
""")

st.header("📖 Formation")
st.markdown("""
- *BTS Géomatique* — Technicienne supérieure en Géomatique  
- *MNT* : Méthodes et Moyens Numériques de Travail  
- *SIG* : Systèmes d’Information Géographique  
- *Entrepreneuriat* : Initiation à la gestion de projets
""")                                                                                                                                                              

st.header("🎯 Objectif professionnel")
st.info("""
Mettre mes compétences au service du *Port de Ndayane* pour réaliser les infrastructures routières et ferroviaires.
""")
