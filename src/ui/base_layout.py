import streamlit as st


def style_background_home():

    st.markdown("""
        <style>

                .stApp {
                    background: #0F172A !important;
                }

                .stApp div[data-testid="stColumn"]{
                    background-color:#1E293B !important;
                    padding:2.5rem !important;
                    border-radius: 5rem !important;
                    }
        </style>  

                """
            ,unsafe_allow_html=True)
    

def style_background_dashboard():

    st.markdown("""
        <style>

                .stApp {
                    background: #0F172A !important;
                }

        </style>  

                """
            ,unsafe_allow_html=True)
    

    

def style_base_layout():
    st.markdown("""
        <style>
        @import url('https://fonts.googleapis.com/css2?family=Climate+Crisis:YEAR@1979&display=swap');
        @import url('https://fonts.googleapis.com/css2?family=Outfit:wght@100..900&display=swap');

                
         /* Hide Top Bar of streamlit */
                
            #MainMenu, footer, header {
                visibility: hidden;
            }
                
            .block-container {
                padding-top:1.5rem !important;    
            }

            h1 {
                font-family: 'Climate Crisis', sans-serif !important;
                font-size: 3.5rem !important;
                line-height:1.1 !important;
                margin-bottom:0rem !important;
                color: #F8FAFC !important;
            }
                

            h2 {
                font-family: 'Outfit', sans-serif !important;
                font-size: 1.8rem !important;
                font-weight: 700 !important;
                line-height: 1.2 !important;
                margin-bottom: 0rem !important;
                color: #F8FAFC !important;
            }
                
            h3, h4, p, label {
                font-family: 'Outfit', sans-serif;
                color: #CBD5E1 !important;
            }

            /* General text color for dashboard */
            .stApp, .stMarkdown, div[data-testid="stText"] {
                color: #CBD5E1 !important;
            }

            /* Input fields */
            .stTextInput input, .stSelectbox select {
                background-color: #1E293B !important;
                color: #F8FAFC !important;
                border: 1px solid #334155 !important;
                border-radius: 0.5rem !important;
            }

            /* Primary button — bright teal/cyan accent */
            button[kind="primary"] {
                border-radius: 1.5rem !important;
                background-color: #0EA5E9 !important;
                color: white !important;
                padding: 10px 20px !important;
                border: none !important;
                transition: transform 0.25s ease-in-out !important;
            }

            /* Secondary button — slate/neutral */
            button[kind="secondary"] {
                border-radius: 1.5rem !important;
                background-color: #334155 !important;
                color: #F8FAFC !important;
                padding: 10px 20px !important;
                border: none !important;
                transition: transform 0.25s ease-in-out !important;
            }

            /* Tertiary button — dark muted */
            button[kind="tertiary"] {
                border-radius: 1.5rem !important;
                background-color: #1E293B !important;
                color: #94A3B8 !important;
                padding: 10px 20px !important;
                border: 1px solid #334155 !important;
                transition: transform 0.25s ease-in-out !important;
            }

            button:hover {
                transform: scale(1.05);
            }

            /* Divider */
            hr {
                border-color: #334155 !important;
            }

            /* Cards / containers */
            div[data-testid="stContainer"] {
                border-color: #334155 !important;
            }

            /* Dataframe */
            .stDataFrame {
                background-color: #1E293B !important;
            }

            /* Selectbox */
            div[data-baseweb="select"] {
                background-color: #1E293B !important;
                border-color: #334155 !important;
            }

            /* Tabs */
            .stTabs [data-baseweb="tab"] {
                color: #94A3B8 !important;
            }
            .stTabs [aria-selected="true"] {
                color: #38BDF8 !important;
                border-bottom-color: #38BDF8 !important;
            }

        </style>  

                """
            ,unsafe_allow_html=True)
