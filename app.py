
import streamlit as st
import pandas as pd
import numpy as np

import streamlit as st
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
import joblib
model = joblib.load("model.pickle")

def predict(HOME_TEAM_ID, VISITOR_TEAM_ID, SEASON, TEAM_ID_home, TEAM_ID_away, 
           PTS_home, FG_PCT_home, FT_PCT_home, FG3_PCT_home, AST_home, REB_home,
           PTS_away, FG_PCT_away, FT_PCT_away, FG3_PCT_away, AST_away, REB_away):
    X_input = pd.DataFrame([[HOME_TEAM_ID, VISITOR_TEAM_ID, SEASON, TEAM_ID_home, TEAM_ID_away,
                           PTS_home, FG_PCT_home, FT_PCT_home, FG3_PCT_home, AST_home, REB_home,
                           PTS_away, FG_PCT_away, FT_PCT_away, FG3_PCT_away, AST_away, REB_away]])
    y_pred = model.predict(X_input)
    if y_pred == [0]:
        return "Home team loses"
    else:
        return "Home team wins"


st.title("Basketball Game Predictor")



HOME_TEAM_ID = st.selectbox("Home Team ID", [1610612739, 1610612752, 1610612756, 1610612757, 1610612749,
       1610612746, 1610612750, 1610612745, 1610612742, 1610612755,
       1610612753, 1610612747, 1610612764, 1610612760, 1610612762,
       1610612740, 1610612741, 1610612763, 1610612748, 1610612738,
       1610612751, 1610612759, 1610612754, 1610612758, 1610612766,
       1610612743, 1610612744, 1610612765, 1610612761, 1610612737])
VISITOR_TEAM_ID = st.selectbox("Visitor Team ID", [1610612739, 1610612752, 1610612756, 1610612757, 1610612749,
       1610612746, 1610612750, 1610612745, 1610612742, 1610612755,
       1610612753, 1610612747, 1610612764, 1610612760, 1610612762,
       1610612740, 1610612741, 1610612763, 1610612748, 1610612738,
       1610612751, 1610612759, 1610612754, 1610612758, 1610612766,
       1610612743, 1610612744, 1610612765, 1610612761, 1610612737])
SEASON = st.selectbox("Season", [2003, 2004, 2005, 2006, 2007, 2008, 2009, 2010, 2011, 2012, 2013,
       2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021])
TEAM_ID_home = st.selectbox("Team ID (Home)", [1610612739, 1610612752, 1610612756, 1610612757, 1610612749,
       1610612746, 1610612750, 1610612745, 1610612742, 1610612755,
       1610612753, 1610612747, 1610612764, 1610612760, 1610612762,
       1610612740, 1610612741, 1610612763, 1610612748, 1610612738,
       1610612751, 1610612759, 1610612754, 1610612758, 1610612766,
       1610612743, 1610612744, 1610612765, 1610612761, 1610612737])
TEAM_ID_away = st.selectbox("Team ID (Away)", [1610612739, 1610612752, 1610612756, 1610612757, 1610612749,
       1610612746, 1610612750, 1610612745, 1610612742, 1610612755,
       1610612753, 1610612747, 1610612764, 1610612760, 1610612762,
       1610612740, 1610612741, 1610612763, 1610612748, 1610612738,
       1610612751, 1610612759, 1610612754, 1610612758, 1610612766,
       1610612743, 1610612744, 1610612765, 1610612761, 1610612737])

PTS_home = st.number_input("Points (Home)")
FG_PCT_home = st.number_input("Field Goal Percentage (Home)")
FT_PCT_home = st.number_input("Free Throw Percentage (Home)")
FG3_PCT_home = st.number_input("3-Pointer Percentage (Home)")
AST_home = st.number_input("Assists (Home)")
REB_home = st.number_input("Rebounds (Home)")

PTS_away = st.number_input("Points (Away)")
FG_PCT_away = st.number_input("Field Goal Percentage (Away)")
FT_PCT_away = st.number_input("Free Throw Percentage (Away)")
FG3_PCT_away = st.number_input("3-Pointer Percentage (Away)")
AST_away =  st.number_input("Assists (Away)")
REB_away = st.number_input("Rebounds (Away)")





if st.button("Predict"):
    result = predict(HOME_TEAM_ID, VISITOR_TEAM_ID, SEASON, TEAM_ID_home, TEAM_ID_away, 
               PTS_home, FG_PCT_home, FT_PCT_home, FG3_PCT_home, AST_home, REB_home,
               PTS_away, FG_PCT_away, FT_PCT_away, FG3_PCT_away, AST_away, REB_away)
    st.write("The outcome of the game is:", result)