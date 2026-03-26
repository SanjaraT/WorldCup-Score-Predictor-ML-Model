import streamlit as st
import requests

API_URL = "https://cricket-score-predictor-system.onrender.com"

st.markdown(
    """
    <h1 style='text-align: center; color: #58C65C;'>
    🏏 T20 Score Predictor
    </h1>
    <p style='text-align: center; color: gray;'>
    Predict the final score based on current match situation
    </p>
    """,
    unsafe_allow_html=True
)

# Main data
teams = [
    'Australia','India','Zimbabwe','Bangladesh','New Zealand',
    'South Africa','England','West Indies','Afghanistan',
    'Pakistan','Sri Lanka'
]

cities = [
     'Guwahati', 'Brighton', 'Kolkata', 'Rajkot', 'Dubai', 'Bridgetown',
       'Barbados', 'Mirpur', 'Wellington', 'Durban', 'Providence',
       'Christchurch', 'Centurion', 'Canberra', 'East London', 'London',
       'Sharjah', 'Johannesburg', 'Abu Dhabi', 'Gros Islet', 'Karachi',
       'Dambulla', "St George's", 'Colombo', 'Birmingham', 'Cape Town',
       'Cardiff', 'Melbourne', 'Hamilton', 'Delhi', 'Chittagong',
       'Dharamsala', 'Harare', 'Basseterre', 'Mumbai', 'Mount Maunganui',
       'Manchester', 'Hangzhou', 'Brisbane', 'Lauderhill', 'Paarl',
       'Bristol', 'Auckland', 'Taunton', 'Kingston', 'Navi Mumbai',
       'Potchefstroom', 'North Sound', 'Trinidad', 'Dhaka', 'Chelmsford',
       'Sydney', 'Dunedin', 'St Lucia', 'Lahore', 'Chandigarh', 'Lucknow',
       'Sylhet', 'Hambantota', 'Guyana', 'Chennai', 'Southampton',
       'Derby', 'Rawalpindi', 'Kuala Lumpur', 'Chattogram', 'Nagpur',
       'Gqeberha', 'Chester-le-Street', 'Bangalore', 'Hobart', 'Tarouba',
       'Perth', 'Benoni', 'Nelson', 'Nottingham', 'Napier',
       'Thiruvananthapuram', 'Ahmedabad', 'Kandy', 'Northampton',
       'Antigua', 'Carrara', 'Visakhapatnam', 'Pune', 'Adelaide'
]


col1, col2 = st.columns(2)

with col1:
    batting_team = st.selectbox(" Batting Team", teams)
    bowling_team = st.selectbox("Bowling Team", teams)
    city = st.selectbox("City", cities)

with col2:
    overs = st.number_input("Overs Completed", min_value=0.1, max_value=20.0, step=0.1)
    wickets = st.slider("Wickets Lost", 0, 10, 2)
    current_score = st.number_input("Current Score", min_value=0, step=1)
    last_5_overs_runs = st.number_input("Runs in Last 5 Overs", min_value=0, step=1)



st.markdown("""
    <style>
    div.stButton > button {
        background-color: #7DAEDE;
        color: black;
        font-size: 18px;
        padding: 10px 30px;
        border-radius: 10px;
        border: none;
        transition: 0.3s;
    }

    div.stButton > button:hover {
        background-color: #58C65C;
        color: white;
    }
    </style>
""", unsafe_allow_html=True)

col_center = st.columns([1, 2, 1])

with col_center[1]:
    predict_clicked = st.button("Predict Score", use_container_width=True)

if predict_clicked:

    payload = {
        "batting_team": batting_team,
        "bowling_team": bowling_team,
        "city": city,
        "overs": overs,
        "wickets": wickets,
        "current_score": current_score,
        "last_5_overs_runs": last_5_overs_runs
    }

    try:
        response = requests.post(API_URL, json=payload)

        if response.status_code == 200:
            result = response.json()

            predicted_score = result["predicted_score"]

            st.markdown(
                f"""
                <div style="
                    background-color:#7DAEDE;
                    padding:5px;
                    border-radius:5px;
                    text-align:center;
                ">
                    <h5 style="color:#030302;">Predicted Score</h5>
                    <h4 style="color:white;">{predicted_score}</h4>
                </div>
                """,
                unsafe_allow_html=True
            )

        else:
            st.error("Error from API")

    except Exception as e:
        st.error(f"Backend not running: {e}")
