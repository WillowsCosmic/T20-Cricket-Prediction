
# 🏏 T20 Cricket Score Predictor

A machine learning-powered web application that predicts T20 cricket match scores in real-time using historical match data and current game statistics.

🚀 **Live Demo**: [Try it now on Streamlit Cloud](https://willowscosmic-t20-cricket-prediction-app-ognnfi.streamlit.app/)

## ✨ Features

- **Real-time Score Prediction**: Predict final scores during live T20 matches
- **High Accuracy**: 2.19 runs MAE with 99.9% R² score
- **10 International Teams**: Australia, India, Bangladesh, New Zealand, South Africa, England, West Indies, Afghanistan, Pakistan, and Sri Lanka
- **90+ Venues**: Major cricket stadiums worldwide
- **User-Friendly Interface**: Clean, responsive Streamlit web interface
- **Fast Predictions**: Instant results with cached model loading
- **Cloud Deployment**: Hosted on Streamlit Cloud for 24/7 availability

## 📸 Screenshots
![image](https://github.com/user-attachments/assets/d198f085-efee-4f13-a1d8-7169d3b6ef61)

Prediction v/s Actual result for Australia batting in T20 Cricket World Cup 2K24 Against India

## 📦 Project Structure

```
t20-cricket-prediction/
│
├── app.py                    # Main Streamlit application
├── pipe.pkl                  # Trained XGBoost model
├── requirements.txt          # Python dependencies
├── README.md                 # Project documentation
│
├── static/
│   └── images/              # Team flag images
│       ├── india.png
│       ├── australia.png
│       └── ...
│
└── screenshots/             # App screenshots
    ├── main_interface.png
    └── prediction_result.png
```

## 🎮 Usage

### Online (Recommended)

Simply visit the live app: **[T20 Cricket Score Predictor](https://willowscosmic-t20-cricket-prediction-app-ognnfi.streamlit.app/)**

### Running Locally

1. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/t20-cricket-prediction.git
   cd t20-cricket-prediction
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the application**
   ```bash
   streamlit run app.py
   ```

4. **Open in browser**: `http://localhost:8501`

### Using the App

1. **Select Teams**: Choose batting and bowling teams from dropdowns
2. **Select Venue**: Pick the match stadium
3. **Enter Match Statistics**:
   - Current Score: Total runs scored
   - Overs Done: Completed overs (must be > 5.0)
   - Wickets Out: Number of wickets fallen (0-10)
   - Runs in Last 5 Overs: Recent scoring rate
4. **Get Prediction**: Click "Predict Score" to see final score prediction


## 🧠 Model Details

### Performance Metrics

| Metric | Value |
|--------|-------|
| **MAE (Final Score)** | 2.19 runs |
| **R² Score** | 99.91% |
| **Predictions within ±5 runs** | 90.7% |
| **Predictions within ±10 runs** | 96.3% |
| **Training Samples** | 39,054 |
| **Test Samples** | 12,778 |

### Performance by Innings Stage

| Stage | MAE | Avg Balls Remaining |
|-------|-----|---------------------|
| **Early Innings (0-6 overs)** | 4.15 runs | 101 balls |
| **Middle Innings (7-14 overs)** | 1.59 runs | 60 balls |
| **Death Overs (15-20 overs)** | 1.01 runs | 18 balls |

### Algorithm
- **Model**: XGBoost Regressor
- **Target**: Remaining runs in the innings
- **Calculation**: `Final Score = Current Score + Predicted Remaining Runs`
- **Deployment**: Model hosted on Streamlit Cloud, loaded on app startup

### Features

| Feature | Description |
|---------|-------------|
| `batting_team` | Team currently batting |
| `bowling_team` | Team currently bowling |
| `venue` | Cricket stadium |
| `current_score` | Runs scored so far |
| `balls_left` | Remaining deliveries |
| `wickets_left` | Wickets remaining |
| `current_run_rate` | Current scoring rate |
| `last_five` | Runs in last 5 overs |

### Data Preprocessing
- **One-Hot Encoding** for categorical features (teams, venues)
- **Feature Engineering** with rolling averages using `.shift(1)` to prevent data leakage
- **Train-Test Split** stratified by team-venue combinations (75-25 split)
- **Hyperparameter Tuning** for optimal XGBoost performance

### Dataset
- **Source**: T20i_info.csv


### Why XGBoost?

XGBoost was chosen for its:
- ✅ Superior handling of non-linear relationships
- ✅ Built-in regularization to prevent overfitting
- ✅ Fast prediction speed for real-time apps
- ✅ Excellent performance with mixed feature types
- ✅ Robust handling of missing values


**Built with ❤️ for cricket enthusiasts**

⭐ **Star this repo** if you found it useful!

