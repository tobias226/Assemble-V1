# Assemble — Employee Voice, Community & Workforce Risk Platform (Prototype)

A green-and-black themed Streamlit prototype built for an ESG project. Assemble
brings together employee voice, community engagement and workforce risk
monitoring in one place:

- 🔧 **Engineering Exchange** — technical skills learning, mentors, skill-swap requests
- 🌍 **Culture Connect** — communities based on culture, language and interests
- 🌸 **Women in Motion** — women's network, mentorship, events, resources
- 🗣️ **Speak Up** — confidential reporting channel
- 📋 **Monthly Survey** — a lightweight monthly pulse survey
- 📊 **Management Dashboard** — KPIs incl. turnover trend and an engagement heatmap

All data in this prototype is **simulated** — nothing here is a real employee
record, and no submitted form data leaves your browser session (it's stored
in Streamlit's `session_state` only, and disappears when the session ends).

---

## 1. Project structure

```
assemble_app/
├── app.py                          # Home page / entry point
├── requirements.txt                # Python dependencies
├── .streamlit/
│   └── config.toml                 # Green/black theme config
├── utils/
│   ├── __init__.py
│   ├── styling.py                  # Shared CSS, fade-transitions, header/footer
│   └── data_generator.py           # Seeded dummy data generators
└── pages/
    ├── 1_Engineering_Exchange.py
    ├── 2_Culture_Connect.py
    ├── 3_Women_in_Motion.py
    ├── 4_Speak_Up.py
    ├── 5_Monthly_Survey.py
    └── 6_Management_Dashboard.py
```

Streamlit automatically turns everything in `pages/` into a sidebar
navigation menu — the leading number controls ordering, and the display name
is generated from the filename.

## 2. Run it locally

```bash
python -m venv venv
source venv/bin/activate        # Windows: venv\Scripts\activate
pip install -r requirements.txt
streamlit run app.py
```

The app opens at `http://localhost:8501`.

## 3. Push to GitHub

```bash
git init
git add .
git commit -m "Initial Assemble prototype"
git branch -M main
git remote add origin https://github.com/<your-username>/<your-repo>.git
git push -u origin main
```

## 4. Deploy on Streamlit Community Cloud

1. Go to [share.streamlit.io](https://share.streamlit.io) and sign in with GitHub.
2. Click **"New app"**.
3. Select your repository, branch (`main`), and set the main file path to
   `app.py`.
4. Click **Deploy**. Streamlit Cloud will read `requirements.txt` and
   `.streamlit/config.toml` automatically — no extra configuration needed.
5. Your app will be live at a URL like
   `https://<your-app-name>.streamlit.app`.

Whenever you push new commits to `main`, Streamlit Cloud redeploys
automatically.

## 5. Customising

- **Theme colours**: edit `.streamlit/config.toml` and the palette constants
  at the top of `utils/styling.py` (`GREEN`, `BLACK`, `PANEL`, etc.).
- **Dummy data**: all charts pull from `utils/data_generator.py`. Each
  function is `@st.cache_data`-decorated and seeded, so numbers stay
  consistent between reruns. Swap these out for real data sources (HRIS
  exports, survey platform APIs, case management systems) when moving beyond
  prototype stage.
- **Adding a new module**: create a new file in `pages/`, prefixed with the
  next number (e.g. `7_New_Module.py`), and call `apply_style()` +
  `page_header()` at the top for a consistent look.

## 6. Notes on the Speak Up module

This is a **prototype only**. It demonstrates UX for confidential reporting
(anonymity toggle, severity flagging, reference numbers, a clear process
explainer) but does **not** implement real encryption, secure storage, or
case management — those would be required before handling genuine
whistleblowing reports in production, alongside legal review against local
whistleblower protection law.

---

Built as an ESG / People & Culture concept prototype. All figures shown are
illustrative and randomly generated.
