import streamlit as st
import pickle
import pandas as pd

@st.cache_resource
def load_model():
    return pickle.load(open('pipe.pkl', 'rb'))

pipe = load_model()

teams = [
    'Australia', 'India', 'Bangladesh', 'New Zealand', 'South Africa',
    'England', 'West Indies', 'Afghanistan', 'Pakistan', 'Sri Lanka'
]
venue = ['AMI Stadium', 'Adelaide Oval', 'Arnos Vale Ground, Kingstown', 'Arun Jaitley Stadium', 'Barabati Stadium', 'Bay Oval', 'Beausejour Stadium, Gros Islet', 'Bellerive Oval', 'Bharat Ratna Shri Atal Bihari Vajpayee Ekana Cricket Stadium', 'Boland Park', 'Brabourne Stadium', 'Brisbane Cricket Ground, Woolloongabba', 'Buffalo Park', 'Carrara Oval', 'Central Broward Regional Park Stadium Turf Ground', 'County Ground', 'Darren Sammy National Cricket Stadium, St Lucia', 'Dr. Y.S. Rajasekhara Reddy ACA-VDCA Cricket Stadium', 'Dubai International Cricket Stadium', 'Eden Gardens', 'Eden Park', 'Edgbaston', 'Feroz Shah Kotla', 'Gaddafi Stadium', 'Green Park', 'Greenfield International Stadium', 'Gymkhana Club Ground', 'Hagley Oval', 'Harare Sports Club', 'Himachal Pradesh Cricket Association Stadium', 'Holkar Cricket Stadium', 'JSCA International Stadium Complex', 'Jade Stadium', 'Kennington Oval', 'Kensington Oval, Bridgetown', 'Kingsmead', "Lord's", 'M Chinnaswamy Stadium', 'M.Chinnaswamy Stadium', 'MA Chidambaram Stadium, Chepauk', 'Maharashtra Cricket Association Stadium', 'Mahinda Rajapaksa International Cricket Stadium, Sooriyawewa', 'Mangaung Oval', 'Manuka Oval', 'Maple Leaf North-West Ground', 'McLean Park', 'Melbourne Cricket Ground', 'Moses Mabhida Stadium', 'National Stadium', 'New Wanderers Stadium', 'Newlands', 'Old Trafford', 'Pallekele International Cricket Stadium', 'Perth Stadium', 'Providence Stadium', 'Providence Stadium, Guyana', 'Punjab Cricket Association IS Bindra Stadium, Mohali', 'Punjab Cricket Association Stadium, Mohali', "Queen's Park Oval, Port of Spain", 'R Premadasa Stadium', 'R.Premadasa Stadium, Khettarama', 'Rajiv Gandhi International Cricket Stadium', 'Rajiv Gandhi International Stadium, Uppal', 'Riverside Ground', 'Sabina Park, Kingston', 'Sardar Patel Stadium, Motera', 'Saurashtra Cricket Association Stadium', 'Saxton Oval', 'Seddon Park', 'Senwes Park', 'Sharjah Cricket Stadium', 'Sheikh Zayed Stadium', 'Shere Bangla National Stadium', 'Shere Bangla National Stadium, Mirpur', 'Simonds Stadium, South Geelong', 'Sir Vivian Richards Stadium, North Sound', 'Sophia Gardens', "St George's Park", 'Stadium Australia', 'Subrata Roy Sahara Stadium', 'SuperSport Park', 'Sydney Cricket Ground', 'Sylhet International Cricket Stadium', 'The Rose Bowl', 'The Wanderers Stadium', 'Trent Bridge', 'Vidarbha Cricket Association Stadium, Jamtha', 'Wankhede Stadium', 'Warner Park, Basseterre', 'Warner Park, St Kitts', 'Western Australia Cricket Association Ground', 'Westpac Stadium', 'Windsor Park, Roseau', 'Zahur Ahmed Chowdhury Stadium'
]

st.set_page_config(
    page_title="Cricket Score Predictor",
    page_icon="🏏",
    layout="wide"
)

st.title("🏏 T20 Cricket Score Predictor 🏏")
st.markdown("""
    <style>
    /* Main title */
    .main-title {
        text-align: center;
        font-size: 2.5rem;
        font-weight: 600;
        color: #333;
        margin-bottom: 30px;
        margin-top: 20px;
    }
    
    /* Remove streamlit padding */
    .block-container {
        padding-top: 2rem;
        padding-bottom: 2rem;
    }
    
    stSelectbox label, .stNumberInput label {
        color: white !important;
        font-size: 0.95rem;
        font-weight: 500;
    }
    
    /* Input fields - dark theme */
    .stSelectbox > div > div {
        background-color: #2d3139;
        color: white;
        border: 1px solid #404552;
    }
    
    .stNumberInput > div > div > input {
        background-color: #2d3139;
        color: white;
        border: 1px solid #404552;
    }
    
    .stButton>button {
        background-color: #0d6efd;
        color: white;
        height: 45px;
        font-size: 16px;
        font-weight: 600;
        border-radius: 5px;
        border: none;
        padding: 0 30px;
        margin-top: 10px;
    }
    
    .stButton>button:hover {
        background-color: #0b5ed7;
    }
    
    .prediction-box {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        padding: 30px;
        border-radius: 10px;
        text-align: center;
        color: white;
        font-size: 2.5rem;
        font-weight: bold;
        margin-top: 30px;
    }
    </style>
""", unsafe_allow_html=True)


flag_col1, form_col, flag_col2 = st.columns([2, 6, 2])


team_col1, team_col2 = st.columns(2)
with team_col1:
    batting_team = st.selectbox(
        "Select batting team",
        options=teams,
        index=teams.index('India') if 'India' in teams else 0
    )

with team_col2:
    bowling_team = st.selectbox(
        "Select bowling team",
        options=teams,
        index=teams.index('Pakistan') if 'Pakistan' in teams else 1
    )

with flag_col1:
    st.markdown('<div class="team-container">', unsafe_allow_html=True)
    try:
        batting_image = f"static/images/{batting_team.lower().replace(' ', '_')}.png"
        st.image(batting_image, use_container_width=True)
    except:
        st.markdown("<p style='text-align: center; font-size: 80px;'>🏏</p>", unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

with flag_col2:
    st.markdown('<div class="team-container">', unsafe_allow_html=True)
    try:
        bowling_image = f"static/images/{bowling_team.lower().replace(' ', '_')}.png"
        st.image(bowling_image, use_container_width=True)
    except:
        st.markdown("<p style='text-align: center; font-size: 80px;'>⚾</p>", unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)
    with form_col:
    
        venue_col1, venue_col2 = st.columns(2)
    
        with venue_col1:
            venue = st.selectbox("Select venue", options=sorted(venue))
        
        with venue_col2:
            current_score = st.number_input(
                "Current Score",
                min_value=0,
                max_value=500,
                value=0,
                step=1
            )
        
        input_col1, input_col2, input_col3 = st.columns(3)
        
        with input_col1:
            overs = st.number_input(
                "Overs Done (works for over > 5)",
                min_value=5.1,
                max_value=20.0,
                value=5.1,
                step=0.1,
                format="%.1f"
            )
        
        with input_col2:
            wickets = st.number_input(
                "Wickets Out",
                min_value=0,
                max_value=10,
                value=0,
                step=1
            )
        
        with input_col3:
            last_five = st.number_input(
                "Runs scored in last 5 overs",
                min_value=0,
                max_value=150,
                value=0,
                step=1
            )
        
predict_clicked = st.button("Predict Score")

if predict_clicked:
    if batting_team == bowling_team:
        st.error("⚠️ Batting and Bowling teams cannot be the same!")
    else:
        balls_left = 120 - (int(overs) * 6 + int((overs % 1) * 10))
        wickets_left = 10 - wickets
        crr = current_score / overs if overs > 0 else 0
        
        # Create input dataframe
        input_df = pd.DataFrame({
            'batting_team': [batting_team],
            'bowling_team': [bowling_team],
            'venue': [venue],
            'current_score': [current_score],
            'balls_left': [balls_left],
            'wicket_left': [wickets_left], 
            'current_run_rate': [crr], 
            'last_five': [last_five]
        })

        try:
            result = pipe.predict(input_df)
            prediction = int(result[0])
 
            st.markdown(
                f'<div class="prediction-box">🏆 Predicted Score: {prediction}</div>',
                unsafe_allow_html=True
            )
                
        except Exception as e:
            st.error(f"❌ Prediction failed: {str(e)}")
            st.info("Please check your input values.")

