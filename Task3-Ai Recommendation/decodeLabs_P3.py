import streamlit as st
import pandas as pd
import plotly.express as px
import time

# ---------------- PAGE ----------------
st.set_page_config(page_title="Smart Civic AI", layout="wide")

# ---------------- SIDEBAR ----------------
st.sidebar.title("🏙️ Civic AI Dashboard")
page = st.sidebar.radio("Navigate", ["🏠 Home", "📊 Dashboard", "🕒 History"])

# ---------------- SESSION ----------------
if "history" not in st.session_state:
    st.session_state.history = []

# ---------------- PREDICT FUNCTION ----------------
def predict(text):
    text = text.lower()

    dept_keywords = {
        "Roads": ["road", "pothole", "street", "damage", "crack"],
        "Water": ["water", "leak", "pipe", "flood", "drainage"],
        "Electricity": ["electric", "electricity", "wire", "pole", "line", "current"],
        "Sanitation": ["garbage", "waste", "dirty", "drain", "sewage"],
        "Traffic": ["traffic", "signal", "jam", "accident"],
        "Health": ["hospital", "injury", "sick", "ambulance"],
        "Police": ["theft", "robbery", "fight", "crime"]
    }

    scores = {dept: 0 for dept in dept_keywords}

    for dept, words in dept_keywords.items():
        for word in words:
            if word in text:
                scores[dept] += 1

    dept = max(scores, key=scores.get)

    # ---------------- PRIORITY ----------------
    high_risk = ["danger", "shock", "accident", "injury", "fire", "fell", "storm"]

    if any(w in text for w in high_risk):
        priority = "High"
    elif scores[dept] >= 2:
        priority = "Medium"
    else:
        priority = "Low"

    # ---------------- ACTIONS ----------------
    citizen_actions = {
        "Roads": "Avoid damaged road area and use alternate routes 🚧",
        "Water": "Avoid using contaminated water and report to authorities 💧",
        "Electricity": "Stay away from electric lines and avoid contact ⚡",
        "Sanitation": "Avoid polluted area and maintain hygiene 🗑️",
        "Traffic": "Follow traffic rules and avoid congested areas 🚦",
        "Health": "Seek medical help immediately 🏥",
        "Police": "Stay safe and report incident to police 🚓"
    }

    gov_actions = {
        "Roads": "Deploy repair team and fix road damage 🚧",
        "Water": "Send team to repair pipeline and restore supply 💧",
        "Electricity": "Dispatch electrical team urgently ⚡",
        "Sanitation": "Schedule cleaning and waste removal 🗑️",
        "Traffic": "Manage traffic and clear congestion 🚦",
        "Health": "Send ambulance and medical staff 🏥",
        "Police": "Dispatch police team and investigate 🚓"
    }

    return dept, priority, citizen_actions.get(dept), gov_actions.get(dept)

# ---------------- HOME ----------------
if page == "🏠 Home":

    st.title("🏙️ Smart Complaint Analyzer")

    complaint = st.text_area("✍️ Enter Complaint")
    location = st.text_input("📍 Location")

    if st.button("🚀 Analyze Complaint"):

        if complaint.strip() == "":
            st.warning("Enter complaint")
        else:
            dept, priority, citizen_action, gov_action = predict(complaint)

            st.subheader("🤖 AI Processing Steps")

            # STEP 1
            with st.spinner("Step 1: Reading complaint..."):
                time.sleep(1)
            st.success(f"Step 1: Complaint received")

            # STEP 2
            with st.spinner("Step 2: Understanding issue..."):
                time.sleep(1)
            st.info("Step 2: Analyzing context and problem type")

            # STEP 3
            with st.spinner("Step 3: Assigning department..."):
                time.sleep(1)
            st.success(f"Step 3: Department → {dept}")

            # STEP 4
            with st.spinner("Step 4: Evaluating risk level..."):
                time.sleep(1)
            st.warning(f"Step 4: Priority → {priority}")

            # STEP 5
            with st.spinner("Step 5: Generating actions..."):
                time.sleep(1)

            st.success("Step 5: Recommended Actions")

            st.markdown(f"👤 **Citizen Action:** {citizen_action}")
            st.markdown(f"🏢 **Government Action:** {gov_action}")

            # SAVE HISTORY
            st.session_state.history.append({
                "Complaint": complaint,
                "Department": dept,
                "Priority": priority,
                "Location": location
            })

# ---------------- DASHBOARD ----------------
elif page == "📊 Dashboard":

    st.title("📊 Complaint Dashboard")

    if len(st.session_state.history) > 0:

        df = pd.DataFrame(st.session_state.history)

        col1, col2, col3 = st.columns(3)

        col1.metric("Total Complaints", len(df))
        col2.metric("Top Department", df['Department'].mode()[0])
        col3.metric("High Priority", len(df[df['Priority']=="High"]))

        col1, col2 = st.columns(2)

        counts = df['Department'].value_counts().reset_index()
        counts.columns = ['Department', 'Count']

        with col1:
            fig1 = px.pie(counts, names='Department', values='Count')
            st.plotly_chart(fig1, use_container_width=True)

        with col2:
            fig2 = px.bar(counts, x='Department', y='Count')
            st.plotly_chart(fig2, use_container_width=True)

    else:
        st.info("No data yet")

# ---------------- HISTORY ----------------
elif page == "🕒 History":

    st.title("🕒 Complaint History")

    if len(st.session_state.history) > 0:

        df = pd.DataFrame(st.session_state.history)

        search = st.text_input("🔍 Search complaints")

        if search:
            df = df[df['Complaint'].str.contains(search, case=False)]

        st.dataframe(df)

        csv = df.to_csv(index=False).encode('utf-8')
        st.download_button("📥 Download", csv, "complaints.csv")

        if st.button("🗑️ Clear History"):
            st.session_state.history = []
            st.success("Cleared")

    else:
        st.info("No history")
