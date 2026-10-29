import streamlit as st
import pandas as pd
import plotly.express as px
from pathlib import Path

st.set_page_config(page_title='Airwise | Air Pollution Dashboard', page_icon='🌿', layout='wide')
BG, INK, MUTED = '#F4F7F6', '#183B3A', '#6B807E'
TEAL, MINT, AMBER, CORAL, RED, PURPLE = '#167D78', '#63B89C', '#E7B84B', '#E98262', '#C95454', '#8C6BB1'
GRID = '#E7EEEB'
st.markdown(f'''<style>
@import url('https://fonts.googleapis.com/css2?family=DM+Sans:wght@400;500;600;700&family=Manrope:wght@500;600;700;800&display=swap');
html,body,[class*="css"]{{font-family:'DM Sans',sans-serif}} .stApp{{background:{BG};color:{INK}}}
.block-container{{padding-top:1.2rem;padding-bottom:2rem;max-width:1500px}}
h1,h2,h3{{font-family:'Manrope',sans-serif!important;color:{INK}!important}}
div[data-testid="stVerticalBlockBorderWrapper"]{{background:white;border:1px solid #E3EBE7;border-radius:16px;box-shadow:0 4px 14px rgba(24,59,58,.035)}}
div[data-testid="stMetricLabel"] p{{color:{MUTED}!important;font-size:12px!important}} div[data-testid="stMetricValue"]{{color:{INK}!important;font-family:'Manrope',sans-serif}}
.hero{{background:linear-gradient(115deg,#153F3D,#176D68 62%,#29978A);border-radius:22px;padding:24px 28px;color:white;margin-bottom:18px;box-shadow:0 10px 30px rgba(22,80,74,.12)}}
.hero h1{{color:white!important;font-size:29px;margin:0 0 5px}} .hero p{{color:#D8EFEB;margin:0;font-size:14px}}
.pill{{display:inline-block;background:rgba(255,255,255,.13);color:#E5F6F2;border:1px solid rgba(255,255,255,.2);border-radius:999px;padding:7px 12px;font-size:11px;letter-spacing:.08em;font-weight:700}}
.section-title{{font-family:'Manrope',sans-serif;color:{INK};font-size:16px;font-weight:800;margin-bottom:2px}} .section-subtitle{{color:{MUTED};font-size:12px;margin-bottom:12px}}
div[data-baseweb="select"]>div{{border-radius:10px;border-color:#DCE7E2}} .stButton button{{border-radius:10px;border:1px solid #DCE7E2}}
</style>''', unsafe_allow_html=True)

@st.cache_data
def load_data(file_bytes=None):
    if file_bytes is not None:
        import io
        df = pd.read_csv(io.BytesIO(file_bytes))
    else:
        paths = [Path('air_pollution_dashboard_50000_rows.csv'), Path('/mnt/data/air_pollution_dashboard_50000_rows.csv')]
        path = next((p for p in paths if p.exists()), None)
        if path is None: return None
        df = pd.read_csv(path)
    if 'DateTime' in df:
        df['DateTime'] = pd.to_datetime(df['DateTime'], errors='coerce')
        df['Year'] = df['DateTime'].dt.year
    aliases = {'PM2.5':'PM2_5_ug_m3','PM10':'PM10_ug_m3','AQI Category':'AQI_Category','Station Type':'Station_Type'}
    for old,new in aliases.items():
        if new not in df and old in df: df[new] = df[old]
    for c in ['AQI','PM2_5_ug_m3','PM10_ug_m3']:
        if c in df: df[c] = pd.to_numeric(df[c], errors='coerce')
    return df

st.markdown('''<div class="hero"><div style="display:flex;justify-content:space-between;align-items:flex-start;gap:16px;flex-wrap:wrap"><div><div style="font-size:12px;font-weight:700;letter-spacing:.14em;color:#A8DED3;margin-bottom:7px">AIRWISE · ENVIRONMENTAL INTELLIGENCE</div><h1>Air Pollution Dashboard</h1><p>A clear snapshot of air quality across Indian cities</p></div><div class="pill">● SAMPLE DATA</div></div></div>''', unsafe_allow_html=True)
with st.expander('📂 Load your data', expanded=False):
    uploaded = st.file_uploader('Upload your air pollution CSV', type=['csv'])
    st.caption('The app also auto-loads air_pollution_dashboard_50000_rows.csv when it is in the same folder.')
df = load_data(uploaded.getvalue() if uploaded else None)
if df is None:
    st.info('Upload your air pollution CSV above, or put air_pollution_dashboard_50000_rows.csv beside this app file.')
    st.stop()
if not {'City','AQI'}.issubset(df.columns):
    st.error('CSV must contain at least City and AQI columns.'); st.stop()

with st.container(border=True):
    f1,f2,f3,f4 = st.columns([1.2,1,1.2,.7])
    cities = sorted(df.City.dropna().astype(str).unique())
    chosen_cities = f1.multiselect('City', cities, placeholder='All cities')
    years = sorted(df.Year.dropna().astype(int).unique().tolist()) if 'Year' in df else []
    chosen_years = f2.multiselect('Year', years, placeholder='All years')
    cats = sorted(df.AQI_Category.dropna().astype(str).unique()) if 'AQI_Category' in df else []
    chosen_cats = f3.multiselect('AQI category', cats, placeholder='All categories')
    f4.markdown('<div style="height:29px"></div>', unsafe_allow_html=True)
    reset = f4.button('↺ Reset filters', use_container_width=True)
if reset: st.rerun()
filtered = df.copy()
if chosen_cities: filtered = filtered[filtered.City.astype(str).isin(chosen_cities)]
if chosen_years and 'Year' in filtered: filtered = filtered[filtered.Year.isin(chosen_years)]
if chosen_cats and 'AQI_Category' in filtered: filtered = filtered[filtered.AQI_Category.astype(str).isin(chosen_cats)]

avg = filtered.AQI.mean() if len(filtered) else 0
max_aqi = filtered.AQI.max() if len(filtered) else 0
k1,k2,k3,k4 = st.columns(4)
for col,label,value,accent,caption in [
    (k1,'AVERAGE AQI',f'{avg:,.1f}',TEAL,'Across selected readings'),
    (k2,'PEAK READING',f'{max_aqi:,.0f}',CORAL,'Highest recorded sample'),
    (k3,'MONITORING VOLUME',f'{len(filtered):,}',AMBER,'Readings in current selection'),
    (k4,'COVERAGE',f'{filtered.City.nunique():,}',MINT,'Cities in current selection')]:
    with col:
        with st.container(border=True):
            st.markdown(f'<div style="color:{accent};font-size:11px;font-weight:700;letter-spacing:.08em">{label}</div>',unsafe_allow_html=True)
            st.metric(label, value)
            st.caption(caption)

base = dict(paper_bgcolor='rgba(0,0,0,0)',plot_bgcolor='rgba(0,0,0,0)',font=dict(family='DM Sans',color=INK,size=11),margin=dict(l=8,r=8,t=12,b=8))
cat_colors = {'Good':MINT,'Satisfactory':'#A6BE63','Moderate':AMBER,'Poor':CORAL,'Very Poor':RED,'Severe':'#8B4F65'}
left,mid,right = st.columns([1.55,1,1],gap='medium')
with left:
    with st.container(border=True):
        st.markdown('<div class="section-title">Average AQI by City</div><div class="section-subtitle">Compare air quality across locations</div>',unsafe_allow_html=True)
        summary = filtered.groupby('City',as_index=False).AQI.mean().sort_values('AQI',ascending=False)
        if not summary.empty:
            summary['Severity'] = summary.AQI.map(lambda x:'Good' if x<=50 else 'Satisfactory' if x<=100 else 'Moderate' if x<=200 else 'Poor' if x<=300 else 'Very Poor' if x<=400 else 'Severe')
            fig = px.bar(summary,x='City',y='AQI',color='Severity',color_discrete_map=cat_colors,hover_data={'AQI':':.1f','Severity':True},text_auto='.0f')
            fig.update_traces(marker_line_width=0,textposition='outside',cliponaxis=False)
            fig.update_layout(**base,height=355,showlegend=False,xaxis_title=None,yaxis_title='Average AQI',xaxis=dict(tickangle=-40,showgrid=False,tickfont=dict(size=9)),yaxis=dict(gridcolor=GRID,zeroline=False,rangemode='tozero'))
            st.plotly_chart(fig,use_container_width=True,config={'displayModeBar':False})
            st.caption('Bar colours indicate AQI severity.')
        else: st.info('No data matches these filters.')
with mid:
    with st.container(border=True):
        st.markdown('<div class="section-title">Air Quality Categories</div><div class="section-subtitle">Share of readings by AQI level</div>',unsafe_allow_html=True)
        if 'AQI_Category' in filtered and len(filtered):
            cat = filtered.AQI_Category.fillna('Unknown').value_counts().rename_axis('Category').reset_index(name='Readings')
            fig = px.pie(cat,names='Category',values='Readings',color='Category',color_discrete_map=cat_colors)
            fig.update_traces(textposition='inside',textinfo='percent',marker=dict(line=dict(color='white',width=2)),hovertemplate='<b>%{label}</b><br>%{value:,} readings<br>%{percent}<extra></extra>')
            fig.update_layout(**base,height=355,showlegend=True,legend=dict(font=dict(size=10),orientation='h',y=-.12,x=0))
            st.plotly_chart(fig,use_container_width=True,config={'displayModeBar':False})
        else: st.info('AQI_Category is not available in this dataset.')
with right:
    with st.container(border=True):
        st.markdown('<div class="section-title">Monitoring Station Types</div><div class="section-subtitle">Where readings were collected</div>',unsafe_allow_html=True)
        if 'Station_Type' in filtered and len(filtered):
            stations = filtered.Station_Type.fillna('Unknown').value_counts().rename_axis('Station Type').reset_index(name='Readings')
            fig = px.pie(stations,names='Station Type',values='Readings',hole=.62,color='Station Type',color_discrete_sequence=[TEAL,AMBER,CORAL,'#7295C7',PURPLE,MINT])
            fig.update_traces(textinfo='none',marker=dict(line=dict(color='white',width=2)),hovertemplate='<b>%{label}</b><br>%{value:,} readings<br>%{percent}<extra></extra>')
            fig.add_annotation(text=f'<b>{len(filtered):,}</b><br><span style="font-size:11px">records</span>',x=.5,y=.5,showarrow=False,font=dict(size=19,color=INK))
            fig.update_layout(**base,height=355,showlegend=True,legend=dict(font=dict(size=10),orientation='h',y=-.12,x=0))
            st.plotly_chart(fig,use_container_width=True,config={'displayModeBar':False})
        else: st.info('Station_Type is not available in this dataset.')
with st.expander('View filtered data preview'):
    st.dataframe(filtered.head(100),use_container_width=True,hide_index=True)
    st.caption(f'Showing up to 100 of {len(filtered):,} filtered rows.')
st.markdown(f'<div style="text-align:center;color:{MUTED};font-size:11px;padding:14px 0 0">Airwise Dashboard · Sample data may be simulated. Use verified monitoring data for public reporting.</div>',unsafe_allow_html=True)
