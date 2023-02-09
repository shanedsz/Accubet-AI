import pandas as pd
import plotly.express as px
import streamlit as st
from PIL import Image


# --- config ---
st.set_page_config(page_title="NBA Dashboard",
                   page_icon=":basketball:",
                   layout="wide"
                   )
df = pd.read_csv('NBA_Player_Stats_Regular.csv', delimiter=";", encoding="latin-1", index_col=0)
df.columns = df.columns.str.replace(' ', '_')
df.drop(df[df['Tm'] == 'TOT'].index, inplace=True)

# --- sidebar ---
st.sidebar.header("Please Filter Here:")
team = st.sidebar.selectbox(
    "Select the Team:",
    options=df["Tm"].unique(),
)
opponent_team = st.sidebar.selectbox(
    "Select opponent Team:",
    options=df["Tm"].unique(),
)

df_selection_home = df.query(
    "Tm == @team"
)
df_selection_away = df.query(
    "Tm == @opponent_team"
)
# --- main ---
st.title(":basketball: NBA 21/22 Dashboard ")
st.markdown("##")
image_home = Image.open('logos/'+team+'.png')
image_away = Image.open('logos/'+opponent_team+'.png')
left_column, right_column = st.columns(2)
# TOP Stats
most_points_home_name = df_selection_home.loc[df_selection_home.PTS == df_selection_home.PTS.max(), 'Player'].item()
most_points_home = round(df_selection_home["PTS"].max(), 3)
most_points_away = round(df_selection_away["PTS"].max(), 3)
most_points_away_name = df_selection_away.loc[df_selection_away.PTS == df_selection_away.PTS.max(), 'Player'].values[0]
average_assist_home = round(df_selection_home["AST"].max(), 3)
average_assist_home_name = df_selection_home.loc[df_selection_home.AST == df_selection_home.AST.max(), 'Player'].values[0]
average_assist_away = round(df_selection_away["AST"].max(), 3)
average_assist_away_name = df_selection_away.loc[df_selection_away.AST == df_selection_away.AST.max(), 'Player'].values[0]
blocks_home = round(df_selection_home["BLK"].max(), 3)
blocks_home_name = df_selection_home.loc[df_selection_home.BLK == df_selection_home.BLK.max(), 'Player'].values[0]
blocks_away = round(df_selection_away["BLK"].max(), 3)
blocks_away_name = df_selection_away.loc[df_selection_away.BLK == df_selection_away.BLK.max(), 'Player'].values[0]
steal_home = round(df_selection_home["STL"].max(), 3)
steal_home_name = df_selection_home.loc[df_selection_home.STL == df_selection_home.STL.max(), 'Player'].values[0]
steal_away = round(df_selection_away["STL"].max(), 3)
steal_away_name = df_selection_away.loc[df_selection_away.STL == df_selection_away.STL.max(), 'Player'].values[0]

# ----scatter-plot ----
# Offense
fig_scatter_home = px.scatter(df_selection_home, x="eFG%", y="PTS", text="Player", log_x=True, size_max=100, color="PTS")
fig_scatter_home.update_traces(textposition='top center')
fig_scatter_home.update_layout(title_text='eFG% Points Ratio', title_x=0.5)
fig_scatter_away = px.scatter(df_selection_away, x="eFG%", y="PTS", text="Player", log_x=True, size_max=100, color="PTS")
fig_scatter_away.update_traces(textposition='top center')
fig_scatter_away.update_layout(title_text='eFG% Points Ratio', title_x=0.5)
# Defense
fig_scatter_home_Defense = px.scatter(df_selection_home, x="BLK", y="PF", text="Player", log_x=True, size_max=100, color="PF")
fig_scatter_home_Defense.update_traces(textposition='top center')
fig_scatter_home_Defense.update_layout(title_text='Blocks Fouls Ratio', title_x=0.5)
fig_scatter_away_Defense = px.scatter(df_selection_away, x="BLK", y="PF", text="Player", log_x=True, size_max=100, color="PF")
fig_scatter_away_Defense.update_traces(textposition='top center')
fig_scatter_away_Defense.update_layout(title_text='Blocks Fouls Ratio', title_x=0.5)
# bar chart
pos_by_3p_home= df_selection_home.groupby(by=["Pos"]).mean()[["3P%"]]
fig_pos_3p_home = px.bar(
    pos_by_3p_home,
    x="3P%",
    y=pos_by_3p_home.index,
    orientation="h",
    title="<b>Position by 3P%<b>",
    template="plotly_dark",
)
pos_by_3p_away= df_selection_away.groupby(by=["Pos"]).mean()[["3P%"]]
fig_pos_3p_away = px.bar(
    pos_by_3p_away,
    x="3P%",
    y=pos_by_3p_away.index,
    orientation="h",
    title="<b>Position by 3P%<b>",
    template="plotly_dark",
)
age_by_mp_home= df_selection_home.groupby(by=["Age"]).mean()[["MP"]]
fig_age_mp_home = px.bar(
    age_by_mp_home,
    x="MP",
    y=age_by_mp_home.index,
    orientation="h",
    title="<b>Age by minutes per game<b>",
    template="plotly_dark",
)
age_by_mp_away= df_selection_away.groupby(by=["Age"]).mean()[["MP"]]
fig_age_mp_away = px.bar(
    age_by_mp_away,
    x="MP",
    y=age_by_mp_away.index,
    orientation="h",
    title="<b>Age by minutes per game<b>",
    template="plotly_dark",
)
with left_column:
    st.image(image_home)
    st.title("Offense")
    st.subheader(f"Most points per game : {most_points_home_name}")
    st.subheader(f"{most_points_home:,}")
    st.subheader(f"Most assists per game : {average_assist_home_name}")
    st.subheader(f"{average_assist_home}")
    st.plotly_chart(fig_scatter_home, use_container_width=True)
    st.plotly_chart(fig_pos_3p_home, use_container_width=True)
    st.markdown("##")
    st.title("Defense")
    st.subheader(f"Most blocks per game : {blocks_home_name}")
    st.subheader(f"{blocks_home:,}")
    st.subheader(f"Most steal per game : {steal_home_name}")
    st.subheader(f"{steal_home:,}")
    st.plotly_chart(fig_scatter_home_Defense, use_container_width=True)
    st.plotly_chart(fig_age_mp_home, use_container_width=True)
    st.dataframe(df_selection_home)
with right_column:
    st.image(image_away)
    st.title("Offense")
    st.subheader(f"Most points per game : {most_points_away_name}")
    st.subheader(f"{most_points_away:,}")
    st.subheader(f"Most assists per game : {average_assist_away_name}")
    st.subheader(f"{average_assist_away}")
    st.plotly_chart(fig_scatter_away, use_container_width=True)
    st.plotly_chart(fig_pos_3p_away, use_container_width=True)
    st.markdown("##")
    st.title("Defense")
    st.subheader(f"Most blocks per game : {blocks_away_name}")
    st.subheader(f"{blocks_away:,}")
    st.subheader(f"Most steal per game : {steal_away_name}")
    st.subheader(f"{steal_away:,}")
    st.plotly_chart(fig_scatter_away_Defense, use_container_width=True)
    st.plotly_chart(fig_age_mp_away, use_container_width=True)
    st.dataframe(df_selection_away)

st.markdown("---")

# HIDE STREAMLIT STYLE
hide_st_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            header {visibility: hidden;}
            </style>
            """
st.markdown(hide_st_style, unsafe_allow_html=True)
