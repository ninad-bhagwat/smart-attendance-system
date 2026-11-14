import streamlit as st

def subject_card(name, code, section, stats=None, footer_callback=None):
    html = f"""
        <div style="background:#1E293B; border-left: 4px solid #0EA5E9; padding:25px; border-radius: 20px; border: 1px solid #334155; margin-bottom:8px;">
        <h3 style="margin:0; color: #F8FAFC; font-size: 1.4rem; font-family: 'Outfit', sans-serif; font-weight:600;">{name}</h3>
        <p style="color:#94A3B8; margin:10px 0; font-family: 'Outfit', sans-serif;">Code : <span style="background:#0EA5E920; color:#38BDF8; padding:2px 8px; border-radius:5px; font-weight:600;">{code}</span> | Section : {section}</p>
        """

    if stats:
        html += """
        <div style="display:flex; gap:8px; flex-wrap:wrap; margin-top:8px;">
        """
        for icon, label, value in stats:
            html += f'<div style="background:#0F172A; border:1px solid #334155; padding:5px 12px; border-radius:12px; font-size:0.9rem; color:#CBD5E1; font-family:\'Outfit\', sans-serif;">{icon} <b style="color:#F8FAFC;">{value}</b> {label}</div>'
        html += "</div>"

    html += "</div>"
    st.markdown(html, unsafe_allow_html=True)

    if footer_callback:
        footer_callback()
