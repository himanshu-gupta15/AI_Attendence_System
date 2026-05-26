import streamlit as st


def subject_card(name, code, section, stats=None, footer_callback=None):

    html = f"""
    <div style="
        background:white;
        border-left:8px solid #EB459E;
        border:1px solid #e2e8f0;
        padding:25px;
        margin-bottom:20px;
        border-radius:10px;
        box-shadow:0 2px 8px rgba(0,0,0,0.05);
    ">

        <h3 style="
            margin:0;
            color:#1e293b;
            font-size:1.5rem;
        ">
            {name}
        </h3>

        <p style="
            color:#64748b;
            margin:10px 0;
        ">

            Code:

            <span style="
                background:#E0E3FE;
                color:#5865F2;
                padding:2px 8px;
                border-radius:5px;
                font-weight:600;
            ">
                {code}
            </span>

            | Section: {section}

        </p>
    """

    if stats:

        html += """
        <div style="
            display:flex;
            gap:8px;
            flex-wrap:wrap;
            margin-top:10px;
        ">
        """

        for icon, label, value in stats:

            html += f"""
            <div style="
                background:#EB459E10;
                padding:5px 12px;
                border-radius:12px;
                font-size:0.9rem;
                color:#1e293b;
            ">
                {icon} <b>{value}</b> {label}
            </div>
            """

        html += "</div>"

    html += "</div>"

    # FINAL FIX
    st.html(html)

    if footer_callback:
        footer_callback()