import streamlit as st

# 1. Configuration de la page (Toujours en premier)
st.set_page_config(page_title="Portfolio Nianguiri Dembele", layout="wide")

# 2. CSS pour la couleur GRIS de la sidebar (#b0bec5)
st.markdown("""
    <style>
        [data-testid="stSidebar"] {
            background-color: #b0bec5;
        }
        /* On change la couleur du texte en noir pour la lisibilité sur le gris clair */
        [data-testid="stSidebar"] * {
            color: #000000 !important;
        }
        /* Style pour arrondir la photo de profil */
        .stImage img {
            border-radius: 10px;
        }
    </style>
""", unsafe_allow_html=True)

# 3. BARRE LATÉRALE (SIDEBAR)
with st.sidebar:
    # On vérifie si l'image existe pour éviter les erreurs au lancement
    try:
        st.image("DEMBELE.JPG", caption="Nianguiri Dembele", width=200)
    except:
        st.info("Image 'DEMBELE.JPG' non trouvée (placez-la dans le même dossier que le script).")
        
    st.title("NIANGUIRI DEMBELE")
    st.write("📧 *Email :* bdembele981@gmail.com")
    st.write("🎓 *Poste :* Technicien supérieur en Géomatique")
    st.write("📍 *Localisation :* Pikine, Dakar - Sénégal")
    st.markdown("---")
    st.write("Projet : Port de Ndayane")

# 4. CONTENU PRINCIPAL
st.title("🎓 ÉTUDIANT EN GÉOMATIQUE")

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
