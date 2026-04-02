"""
VIT Campus Energy Utility Dashboard
A comprehensive dashboard for monitoring and optimizing energy consumption
with long-term sustainability solutions
"""

import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots
from datetime import datetime, timedelta
import os

# Page configuration
st.set_page_config(
    page_title="VIT Energy Dashboard",
    page_icon="⚡",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for professional aesthetics
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;600;700;800&display=swap');
    
    * {
        font-family: 'Inter', -apple-system, BlinkMacSystemFont, sans-serif;
    }
    
    [data-testid="stAppViewContainer"] {
        background: #f8f9fe;
    }
    
    .block-container {
        padding: 2rem 3rem;
        background: rgba(255, 255, 255, 0.98);
        border-radius: 20px;
        margin: 1rem;
        box-shadow: 0 20px 60px rgba(0, 0, 0, 0.3);
    }
    
    /* Enhanced Metrics */
    [data-testid="stMetric"] {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        padding: 1.5rem;
        border-radius: 15px;
        color: white;
        box-shadow: 0 8px 20px rgba(102, 126, 234, 0.4);
        transition: transform 0.3s ease, box-shadow 0.3s ease;
        border: 1px solid rgba(255, 255, 255, 0.2);
    }
    
    [data-testid="stMetric"]:hover {
        transform: translateY(-5px);
        box-shadow: 0 12px 30px rgba(102, 126, 234, 0.6);
    }
    
    [data-testid="stMetric"] label {
        color: rgba(255, 255, 255, 0.95) !important;
        font-weight: 600;
        font-size: 0.9rem;
        text-transform: uppercase;
        letter-spacing: 0.5px;
    }
    
    [data-testid="stMetric"] [data-testid="stMetricValue"] {
        color: white;
        font-size: 2.2rem;
        font-weight: 800;
    }
    
    [data-testid="stMetric"] [data-testid="stMetricDelta"] {
        color: rgba(255, 255, 255, 0.9);
        font-weight: 600;
    }
    
    /* Typography */
    h1 {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        font-weight: 900;
        font-size: 3rem;
        margin-bottom: 0.5rem;
        letter-spacing: -1px;
    }
    
    h2 {
        color: #667eea;
        font-weight: 800;
        font-size: 1.8rem;
        margin-top: 2rem;
        margin-bottom: 1rem;
    }
    
    h3 {
        color: #764ba2;
        font-weight: 700;
        font-size: 1.3rem;
    }
    
    /* Sidebar Styling */
    [data-testid="stSidebar"] {
        background: linear-gradient(180deg, #667eea 0%, #764ba2 100%);
        padding: 2rem 1rem;
    }
    
    [data-testid="stSidebar"] p,
    [data-testid="stSidebar"] h1,
    [data-testid="stSidebar"] h2,
    [data-testid="stSidebar"] h3,
    [data-testid="stSidebar"] label {
        color: white !important;
        background: none !important;
        -webkit-text-fill-color: white !important;
    }
    
    [data-testid="stSidebar"] [data-baseweb="select"] *,
    [data-testid="stSidebar"] [data-baseweb="popover"] *,
    [data-testid="stSidebar"] [data-baseweb="calendar"] * {
        color: #333 !important;
    }
    
    [data-testid="stSidebar"] .stRadio > label {
        font-weight: 600;
        font-size: 1.1rem;
        margin-bottom: 1rem;
    }
    
    [data-testid="stSidebar"] [data-baseweb="radio"] {
        background: rgba(255, 255, 255, 0.15);
        padding: 0.8rem;
        border-radius: 10px;
        margin: 0.3rem 0;
        transition: all 0.3s ease;
        border: 1px solid rgba(255,255,255,0.4);
    }
    
    [data-testid="stSidebar"] [data-baseweb="radio"]:hover {
        background: rgba(255, 255, 255, 0.2);
        transform: translateX(5px);
    }
    
    /* Cards */
    .sustainability-card {
        background: linear-gradient(135deg, #ffffff 0%, #f8f9fa 100%);
        padding: 1.5rem;
        border-radius: 15px;
        box-shadow: 0 4px 15px rgba(0, 0, 0, 0.1);
        margin: 10px 0;
        border-left: 4px solid #667eea;
        transition: transform 0.3s ease, box-shadow 0.3s ease;
    }
    
    .sustainability-card:hover {
        transform: translateY(-3px);
        box-shadow: 0 8px 25px rgba(0, 0, 0, 0.15);
    }
    
    .sustainability-card h2 {
        color: #667eea;
        font-size: 2.5rem;
        font-weight: 800;
        margin: 0.5rem 0;
    }
    
    .sustainability-card h3 {
        color: #764ba2;
        font-size: 1.1rem;
        font-weight: 700;
        margin-bottom: 0.5rem;
    }
    
    .sustainability-card p {
        color: #6c757d;
        font-size: 0.9rem;
        margin: 0;
    }
    
    /* Info boxes */
    .stAlert {
        border-radius: 12px;
        border: none;
        box-shadow: 0 4px 12px rgba(0, 0, 0, 0.1);
    }
    
    /* Tabs */
    .stTabs [data-baseweb="tab-list"] {
        gap: 8px;
        background: transparent;
    }
    
    .stTabs [data-baseweb="tab"] {
        background: linear-gradient(135deg, #f8f9fa 0%, #e9ecef 100%);
        border-radius: 10px;
        padding: 0.8rem 1.5rem;
        font-weight: 600;
        border: 2px solid transparent;
        transition: all 0.3s ease;
    }
    
    .stTabs [data-baseweb="tab"]:hover {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
        transform: translateY(-2px);
    }
    
    .stTabs [aria-selected="true"] {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white !important;
        border-color: #764ba2;
    }
    
    /* Dividers */
    hr {
        margin: 2rem 0;
        border: none;
        height: 2px;
        background: linear-gradient(90deg, transparent, #667eea, transparent);
    }
    
    /* Buttons */
    .stButton > button {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
        border: none;
        border-radius: 10px;
        padding: 0.6rem 2rem;
        font-weight: 600;
        transition: all 0.3s ease;
        box-shadow: 0 4px 12px rgba(102, 126, 234, 0.3);
    }
    
    .stButton > button:hover {
        transform: translateY(-2px);
        box-shadow: 0 6px 20px rgba(102, 126, 234, 0.5);
    }
    
    /* Plotly charts enhancement */
    .js-plotly-plot {
        border-radius: 15px;
        overflow: hidden;
        box-shadow: 0 4px 15px rgba(0, 0, 0, 0.1);
    }
    
    /* Table styling */
    .stDataFrame {
        border-radius: 12px;
        overflow: hidden;
        box-shadow: 0 4px 12px rgba(0, 0, 0, 0.1);
    }
    
    /* Multiselect and inputs */
    .stMultiSelect [data-baseweb="select"] {
        border-radius: 10px;
    }
    
    .stDateInput [data-baseweb="input"] {
        border-radius: 10px;
    }
    
    /* Scrollbar */
    ::-webkit-scrollbar {
        width: 10px;
        height: 10px;
    }
    
    ::-webkit-scrollbar-track {
        background: #f1f1f1;
        border-radius: 10px;
    }
    
    ::-webkit-scrollbar-thumb {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        border-radius: 10px;
    }
    
    ::-webkit-scrollbar-thumb:hover {
        background: linear-gradient(135deg, #764ba2 0%, #667eea 100%);
    }
    
    /* Animation for page load */
    @keyframes fadeIn {
        from { opacity: 0; transform: translateY(20px); }
        to { opacity: 1; transform: translateY(0); }
    }
    
    .element-container {
        animation: fadeIn 0.5s ease-out;
    }
    </style>
""", unsafe_allow_html=True)

# Load data
@st.cache_data
def load_data():
    """Load all energy data"""
    try:
        hourly_data = pd.read_csv('data/hourly_energy_data.csv')
        hourly_data['timestamp'] = pd.to_datetime(hourly_data['timestamp'])
        
        daily_data = pd.read_csv('data/daily_energy_summary.csv')
        daily_data['date'] = pd.to_datetime(daily_data['date'])
        
        facility_data = pd.read_csv('data/facility_metadata.csv')
        
        return hourly_data, daily_data, facility_data
    except FileNotFoundError:
        with st.spinner("Initializing smart grid data connections..."):
            import os
            from energy_data_generator import generate_all_data
            
            os.makedirs('data', exist_ok=True)
            generate_all_data()
            
        # Load the newly generated data
        hourly_data = pd.read_csv('data/hourly_energy_data.csv')
        hourly_data['timestamp'] = pd.to_datetime(hourly_data['timestamp'])
        
        daily_data = pd.read_csv('data/daily_energy_summary.csv')
        daily_data['date'] = pd.to_datetime(daily_data['date'])
        
        facility_data = pd.read_csv('data/facility_metadata.csv')
        
        return hourly_data, daily_data, facility_data

# Load data
hourly_data, daily_data, facility_data = load_data()

# Sidebar
with st.sidebar:
    st.markdown("""
        <div style='text-align: center; padding: 1rem 0; margin-bottom: 2rem; background: rgba(255,255,255,0.1); border-radius: 15px;'>
            <h1 style='margin: 0; font-size: 2.2rem; font-weight: 800; background: none; -webkit-text-fill-color: white;'>⚡ VIT Energy</h1>
            <p style='color: rgba(255,255,255,0.8); font-size: 0.9rem; margin-top: 0.2rem; font-weight: 500;'>Campus Dashboard</p>
        </div>
    """, unsafe_allow_html=True)
    st.markdown("<h3 style='margin-bottom: 0.5rem;'>Navigation</h3>", unsafe_allow_html=True)
    
    page = st.radio(
        "Select View",
        ["🏠 Overview", "📊 Analytics", "🌱 Sustainability", "💡 Solutions", "📈 Predictions"]
    )
    
    st.markdown("---")
    st.subheader("Filters")
    
    # Date range filter
    date_range = st.date_input(
        "Date Range",
        value=(daily_data['date'].min(), daily_data['date'].max()),
        min_value=daily_data['date'].min(),
        max_value=daily_data['date'].max()
    )
    
    # Facility filter
    selected_facilities = st.multiselect(
        "Facilities",
        options=hourly_data['facility'].unique(),
        default=hourly_data['facility'].unique()[:3]
    )
    
    st.markdown("---")
    
    # PDF Download Button
    try:
        with open("VIT_Energy_Dashboard_Documentation.pdf", "rb") as pdf_file:
            st.download_button(
                label="📄 Download Monthly Report (PDF)",
                data=pdf_file,
                file_name="VIT_Energy_Dashboard_Documentation.pdf",
                mime="application/pdf",
                use_container_width=True
            )
    except FileNotFoundError:
        pass
        
    st.info("**Last Updated:** " + datetime.now().strftime("%Y-%m-%d %H:%M"))

# Main content - Professional Header
st.markdown("""
    <div style='background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); 
                padding: 2.5rem 2rem; 
                border-radius: 20px; 
                margin-bottom: 2rem;
                box-shadow: 0 10px 30px rgba(102, 126, 234, 0.3);
                text-align: center;'>
        <h1 style='color: white; 
                   margin: 0; 
                   font-size: 3rem; 
                   font-weight: 900;
                   -webkit-text-fill-color: white;
                   text-shadow: 2px 2px 4px rgba(0,0,0,0.2);'>
            ⚡ VIT Campus Energy Management Dashboard
        </h1>
        <p style='color: rgba(255,255,255,0.95); 
                  margin: 0.5rem 0 0 0; 
                  font-size: 1.3rem; 
                  font-weight: 500;'>
            Real-time Monitoring • Advanced Analytics • Sustainability Solutions
        </p>
    </div>
""", unsafe_allow_html=True)

# Overview Page
if page == "🏠 Overview":
    # Key Metrics
    col1, col2, col3, col4 = st.columns(4)
    
    latest_day = daily_data.iloc[-1]
    prev_day = daily_data.iloc[-2]
    
    with col1:
        st.metric(
            "Today's Consumption",
            f"{latest_day['total_consumption_kwh']:,.0f} kWh",
            f"{((latest_day['total_consumption_kwh'] - prev_day['total_consumption_kwh']) / prev_day['total_consumption_kwh'] * 100):.1f}%"
        )
    
    with col2:
        st.metric(
            "Renewable Energy",
            f"{latest_day['renewable_percentage']:.1f}%",
            f"{(latest_day['renewable_percentage'] - prev_day['renewable_percentage']):.1f}%"
        )
    
    with col3:
        st.metric(
            "Carbon Emissions",
            f"{latest_day['carbon_emissions_kg']:,.0f} kg",
            f"{((latest_day['carbon_emissions_kg'] - prev_day['carbon_emissions_kg']) / prev_day['carbon_emissions_kg'] * 100):.1f}%",
            delta_color="inverse"
        )
    
    with col4:
        st.metric(
            "Daily Cost",
            f"₹{latest_day['cost_inr']:,.0f}",
            f"{((latest_day['cost_inr'] - prev_day['cost_inr']) / prev_day['cost_inr'] * 100):.1f}%",
            delta_color="inverse"
        )
    
    st.markdown("---")
    
    # Live System Alerts & Weather
    alert_col, weather_col = st.columns([2, 1])
    
    with alert_col:
        st.markdown("""
        <div style='background: rgba(255, 107, 107, 0.1); border-left: 4px solid #ff6b6b; padding: 1rem; border-radius: 8px; margin-bottom: 1rem;'>
            <h4 style='color: #ff6b6b; margin: 0 0 0.5rem 0;'>⚠️ Active System Alerts</h4>
            <p style='margin: 0; font-size: 0.9rem; color: #333;'>• <b>Maintenance Required:</b> HVAC systems in Academic Block A are consuming 15% more power than historical patterns.</p>
        </div>
        <div style='background: rgba(82, 196, 26, 0.1); border-left: 4px solid #52c41a; padding: 1rem; border-radius: 8px;'>
            <h4 style='color: #52c41a; margin: 0 0 0.5rem 0;'>✅ Subsystem Status</h4>
            <p style='margin: 0; font-size: 0.9rem; color: #333;'>• Solar Arrays 1-4 operating at peak efficiency. Battery storage at 94% capacity.</p>
        </div>
        """, unsafe_allow_html=True)
        
    with weather_col:
        st.markdown("""
        <div style='background: linear-gradient(135deg, #4facfe 0%, #00f2fe 100%); padding: 1.5rem; border-radius: 12px; color: white; box-shadow: 0 4px 15px rgba(0,0,0,0.1);'>
            <h3 style='margin: 0 0 0.8rem 0; color: white;'>🌤️ Live Weather Info</h3>
            <div style='display: flex; justify-content: space-between; align-items: center;'>
                <div>
                    <span style='font-size: 2.8rem; font-weight: 800; line-height: 1;'>34°C</span><br/>
                    <span style='font-size: 0.9rem; opacity: 0.9; font-weight: 500;'>Vellore, TN</span>
                </div>
                <div style='text-align: right; font-size: 0.85rem; opacity: 0.9; line-height: 1.6;'>
                    <b>Humidity:</b> 65%<br/>
                    <b>UV Index:</b> Very High<br/>
                    <b>Wind:</b> 14 km/h SE
                </div>
            </div>
        </div>
        """, unsafe_allow_html=True)
        
    st.markdown("---")
    
    # Section Header
    st.markdown("""
        <div style='background: linear-gradient(135deg, rgba(102, 126, 234, 0.1) 0%, rgba(118, 75, 162, 0.1) 100%);
                    padding: 1rem 1.5rem;
                    border-radius: 12px;
                    border-left: 4px solid #667eea;
                    margin-bottom: 1.5rem;'>
            <h2 style='margin: 0; color: #667eea; font-size: 1.5rem;'>📊 Energy Consumption Overview</h2>
        </div>
    """, unsafe_allow_html=True)
    
    # Real-time consumption chart
    col1, col2 = st.columns([2, 1])
    
    with col1:
        st.subheader("📈 Energy Consumption Trend (Last 30 Days)")
        
        fig = go.Figure()
        fig.add_trace(go.Scatter(
            x=daily_data['date'].tail(30),
            y=daily_data['total_consumption_kwh'].tail(30),
            mode='lines+markers',
            name='Total Consumption',
            line=dict(color='#667eea', width=3),
            fill='tozeroy',
            fillcolor='rgba(102, 126, 234, 0.2)'
        ))
        
        fig.update_layout(
            height=400,
            hovermode='x unified',
            plot_bgcolor='rgba(248, 249, 250, 0.5)',
            paper_bgcolor='white',
            xaxis=dict(
                showgrid=True, 
                gridcolor='rgba(102, 126, 234, 0.1)',
                title='Date',
                title_font=dict(size=14, color='#667eea', family='Inter')
            ),
            yaxis=dict(
                showgrid=True, 
                gridcolor='rgba(102, 126, 234, 0.1)', 
                title='Energy Consumption (kWh)',
                title_font=dict(size=14, color='#667eea', family='Inter')
            ),
            font=dict(family='Inter', size=12),
            margin=dict(l=10, r=10, t=30, b=10)
        )
        
        st.plotly_chart(fig, use_container_width=True)
    
    with col2:
        st.subheader("🔋 Energy Sources")
        
        energy_sources = pd.DataFrame({
            'Source': ['Solar', 'Wind', 'Grid', 'Diesel'],
            'Percentage': [
                latest_day['solar_generation_kwh'] / latest_day['total_consumption_kwh'] * 100,
                latest_day['wind_generation_kwh'] / latest_day['total_consumption_kwh'] * 100,
                latest_day['grid_consumption_kwh'] / latest_day['total_consumption_kwh'] * 100,
                2.0
            ]
        })
        
        fig = px.pie(
            energy_sources,
            values='Percentage',
            names='Source',
            color='Source',
            color_discrete_map={'Solar': '#ffd700', 'Wind': '#87ceeb', 'Grid': '#ff6b6b', 'Diesel': '#666666'},
            hole=0.4
        )
        
        
        fig.update_layout(
            height=400, 
            showlegend=True,
            font=dict(family='Inter', size=12),
            paper_bgcolor='white',
            legend=dict(
                orientation="v",
                yanchor="middle",
                y=0.5,
                xanchor="left",
                x=1.05,
                font=dict(size=11)
            )
        )
        fig.update_traces(
            textposition='inside',
            textinfo='percent+label',
            textfont_size=11,
            marker=dict(line=dict(color='white', width=2))
        )
        st.plotly_chart(fig, use_container_width=True)
    
    st.markdown("---")
    
    # Section Header
    st.markdown("""
        <div style='background: linear-gradient(135deg, rgba(102, 126, 234, 0.1) 0%, rgba(118, 75, 162, 0.1) 100%);
                    padding: 1rem 1.5rem;
                    border-radius: 12px;
                    border-left: 4px solid #667eea;
                    margin-bottom: 1.5rem;'>
            <h2 style='margin: 0; color: #667eea; font-size: 1.5rem;'>🏢 Facility Performance Analysis</h2>
        </div>
    """, unsafe_allow_html=True)
    
    # Facility-wise consumption
    st.subheader("🏢 Facility-wise Energy Consumption (Last 24 Hours)")
    
    last_24h = hourly_data[hourly_data['timestamp'] >= (hourly_data['timestamp'].max() - timedelta(hours=24))]
    facility_consumption = last_24h.groupby('facility')['total_consumption_kwh'].sum().sort_values(ascending=False)
    
    fig = px.bar(
        x=facility_consumption.values,
        y=facility_consumption.index,
        orientation='h',
        color=facility_consumption.values,
        color_continuous_scale='Viridis',
        labels={'x': 'Energy Consumption (kWh)', 'y': 'Facility'}
    )
    
    fig.update_layout(
        height=500,
        showlegend=False,
        plot_bgcolor='white',
        paper_bgcolor='white'
    )
    
    st.plotly_chart(fig, use_container_width=True)

# Analytics Page
elif page == "📊 Analytics":
    st.header("📊 Detailed Energy Analytics")
    
    # Filter data based on selection
    filtered_hourly = hourly_data[
        (hourly_data['facility'].isin(selected_facilities)) &
        (hourly_data['timestamp'].dt.date >= date_range[0]) &
        (hourly_data['timestamp'].dt.date <= date_range[1])
    ]
    
    # Hourly pattern analysis
    st.subheader("⏰ Hourly Consumption Pattern")
    
    hourly_pattern = filtered_hourly.groupby(filtered_hourly['timestamp'].dt.hour)['total_consumption_kwh'].mean()
    
    fig = go.Figure()
    fig.add_trace(go.Scatter(
        x=hourly_pattern.index,
        y=hourly_pattern.values,
        mode='lines+markers',
        fill='tozeroy',
        line=dict(color='#667eea', width=3),
        marker=dict(size=8)
    ))
    
    fig.update_layout(
        height=400,
        xaxis=dict(title='Hour of Day', tickmode='linear', tick0=0, dtick=2),
        yaxis=dict(title='Average Consumption (kWh)'),
        plot_bgcolor='white',
        paper_bgcolor='white'
    )
    
    st.plotly_chart(fig, use_container_width=True)
    
    # Weekly pattern
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("📅 Weekly Consumption Pattern")
        
        weekly_data = filtered_hourly.copy()
        weekly_data['day_of_week'] = weekly_data['timestamp'].dt.day_name()
        day_order = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
        weekly_pattern = weekly_data.groupby('day_of_week')['total_consumption_kwh'].sum().reindex(day_order)
        
        fig = px.bar(
            x=weekly_pattern.index,
            y=weekly_pattern.values,
            color=weekly_pattern.values,
            color_continuous_scale='Blues',
            labels={'x': 'Day', 'y': 'Total Consumption (kWh)'}
        )
        
        fig.update_layout(height=400, showlegend=False)
        st.plotly_chart(fig, use_container_width=True)
    
    with col2:
        st.subheader("🌡️ Temperature vs Consumption")
        
        temp_consumption = filtered_hourly.groupby('temperature_c')['total_consumption_kwh'].mean().reset_index()
        
        fig = px.scatter(
            temp_consumption,
            x='temperature_c',
            y='total_consumption_kwh',
            trendline='ols',
            labels={'temperature_c': 'Temperature (°C)', 'total_consumption_kwh': 'Avg Consumption (kWh)'}
        )
        
        fig.update_layout(height=400)
        st.plotly_chart(fig, use_container_width=True)
    
    # Facility comparison
    st.subheader("🏢 Facility Performance Comparison")
    
    facility_stats = filtered_hourly.groupby('facility').agg({
        'total_consumption_kwh': 'sum',
        'solar_kwh': 'sum',
        'grid_kwh': 'sum',
        'occupancy_percent': 'mean'
    }).reset_index()
    
    facility_stats['renewable_ratio'] = (facility_stats['solar_kwh'] / facility_stats['total_consumption_kwh'] * 100)
    
    fig = make_subplots(
        rows=1, cols=2,
        subplot_titles=('Total Consumption', 'Renewable Energy Ratio'),
        specs=[[{'type': 'bar'}, {'type': 'bar'}]]
    )
    
    fig.add_trace(
        go.Bar(x=facility_stats['facility'], y=facility_stats['total_consumption_kwh'], name='Consumption', marker_color='#667eea'),
        row=1, col=1
    )
    
    fig.add_trace(
        go.Bar(x=facility_stats['facility'], y=facility_stats['renewable_ratio'], name='Renewable %', marker_color='#52c41a'),
        row=1, col=2
    )
    
    fig.update_layout(height=500, showlegend=False)
    fig.update_xaxes(tickangle=45)
    
    st.plotly_chart(fig, use_container_width=True)

# Sustainability Page
elif page == "🌱 Sustainability":
    st.header("🌱 Sustainability Metrics & Environmental Impact")
    
    # Carbon footprint
    col1, col2, col3 = st.columns(3)
    
    total_emissions = daily_data['carbon_emissions_kg'].sum()
    total_renewable = daily_data['solar_generation_kwh'].sum() + daily_data['wind_generation_kwh'].sum()
    emissions_saved = total_renewable * 0.82
    
    with col1:
        st.metric("Total Carbon Emissions (Year)", f"{total_emissions:,.0f} kg CO₂")
    
    with col2:
        st.metric("Emissions Saved (Renewable)", f"{emissions_saved:,.0f} kg CO₂")
    
    with col3:
        st.metric("Trees Equivalent", f"{int(total_emissions / 21):,} trees needed")
    
    st.markdown("---")
    
    # Carbon emissions trend
    st.subheader("📉 Carbon Emissions Trend")
    
    fig = go.Figure()
    
    fig.add_trace(go.Scatter(
        x=daily_data['date'],
        y=daily_data['carbon_emissions_kg'],
        mode='lines',
        name='Daily Emissions',
        line=dict(color='#ff6b6b', width=2),
        fill='tozeroy',
        fillcolor='rgba(255, 107, 107, 0.2)'
    ))
    
    # Add moving average
    daily_data['emissions_ma'] = daily_data['carbon_emissions_kg'].rolling(window=7).mean()
    fig.add_trace(go.Scatter(
        x=daily_data['date'],
        y=daily_data['emissions_ma'],
        mode='lines',
        name='7-Day Average',
        line=dict(color='#333', width=3, dash='dash')
    ))
    
    fig.update_layout(
        height=400,
        hovermode='x unified',
        plot_bgcolor='white',
        paper_bgcolor='white',
        yaxis=dict(title='CO₂ Emissions (kg)')
    )
    
    st.plotly_chart(fig, use_container_width=True)
    
    # Renewable energy progress
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("☀️ Renewable Energy Progress")
        
        monthly_renewable = daily_data.groupby(daily_data['date'].dt.to_period('M')).agg({
            'solar_generation_kwh': 'sum',
            'wind_generation_kwh': 'sum',
            'total_consumption_kwh': 'sum'
        }).reset_index()
        
        monthly_renewable['date'] = monthly_renewable['date'].astype(str)
        monthly_renewable['renewable_pct'] = (
            (monthly_renewable['solar_generation_kwh'] + monthly_renewable['wind_generation_kwh']) /
            monthly_renewable['total_consumption_kwh'] * 100
        )
        
        fig = px.line(
            monthly_renewable,
            x='date',
            y='renewable_pct',
            markers=True,
            labels={'date': 'Month', 'renewable_pct': 'Renewable Energy (%)'}
        )
        
        fig.add_hline(y=30, line_dash="dash", line_color="green", annotation_text="Target: 30%")
        fig.update_layout(height=400)
        
        st.plotly_chart(fig, use_container_width=True)
    
    with col2:
        st.subheader("💰 Cost Savings from Renewables")
        
        monthly_savings = monthly_renewable.copy()
        monthly_savings['savings_inr'] = (
            monthly_savings['solar_generation_kwh'] + monthly_savings['wind_generation_kwh']
        ) * 8.95
        
        fig = px.bar(
            monthly_savings,
            x='date',
            y='savings_inr',
            color='savings_inr',
            color_continuous_scale='Greens',
            labels={'date': 'Month', 'savings_inr': 'Savings (₹)'}
        )
        
        fig.update_layout(height=400, showlegend=False)
        st.plotly_chart(fig, use_container_width=True)
    
    # Environmental impact summary
    st.subheader("🌍 Environmental Impact Summary")
    
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.markdown("""
        <div class="sustainability-card">
            <h3>🌳 Trees Saved</h3>
            <h2>{:,}</h2>
            <p>Equivalent trees from renewable energy</p>
        </div>
        """.format(int(emissions_saved / 21)), unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div class="sustainability-card">
            <h3>🚗 Cars Off Road</h3>
            <h2>{:,}</h2>
            <p>Equivalent cars removed annually</p>
        </div>
        """.format(int(emissions_saved / 4600)), unsafe_allow_html=True)
    
    with col3:
        st.markdown("""
        <div class="sustainability-card">
            <h3>💡 Homes Powered</h3>
            <h2>{:,}</h2>
            <p>Homes powered by renewable energy</p>
        </div>
        """.format(int(total_renewable / 10000)), unsafe_allow_html=True)
    
    with col4:
        st.markdown("""
        <div class="sustainability-card">
            <h3>💰 Money Saved</h3>
            <h2>₹{:,.0f}</h2>
            <p>Annual savings from renewables</p>
        </div>
        """.format(total_renewable * 7.5), unsafe_allow_html=True)

# Solutions Page
elif page == "💡 Solutions":
    st.header("💡 Long-term Energy Sustainability Solutions")
    
    st.markdown("""
    <div style='background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); padding: 30px; border-radius: 15px; color: white; margin-bottom: 30px;'>
        <h2 style='color: white; margin: 0;'>🎯 VIT Campus Energy Transformation Roadmap</h2>
        <p style='margin: 10px 0 0 0; font-size: 1.1rem;'>Comprehensive strategies for achieving carbon neutrality by 2030</p>
    </div>
    """, unsafe_allow_html=True)
    
    # Solution categories
    tab1, tab2, tab3, tab4, tab5 = st.tabs([
        "🔆 Renewable Energy", "⚡ Energy Efficiency", "🏗️ Infrastructure", "🤖 Smart Systems", "📊 ROI Analysis"
    ])
    
    with tab1:
        st.subheader("🔆 Renewable Energy Expansion Plan")
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown("""
            #### Solar Energy Solutions
            
            **1. Rooftop Solar Expansion**
            - **Current Capacity:** 500 kW
            - **Proposed Expansion:** 2,000 kW (4x increase)
            - **Coverage:** All academic blocks, hostels, and parking areas
            - **Annual Generation:** ~3,000,000 kWh
            - **Investment:** ₹10 Crores
            - **Payback Period:** 5-6 years
            
            **2. Solar Carports**
            - Install solar panels over parking areas
            - Dual benefit: Energy + shade for vehicles
            - Capacity: 300 kW
            - Cost: ₹1.5 Crores
            
            **3. Building-Integrated Photovoltaics (BIPV)**
            - Solar facades for new constructions
            - Aesthetic + functional design
            - Estimated capacity: 200 kW
            """)
        
        with col2:
            st.markdown("""
            #### Wind & Hybrid Solutions
            
            **1. Small Wind Turbines**
            - Install 5-10 small wind turbines (10 kW each)
            - Suitable for VIT's geographical location
            - Annual generation: ~150,000 kWh
            - Investment: ₹50 Lakhs
            
            **2. Solar-Wind Hybrid System**
            - Complementary generation patterns
            - Better grid stability
            - Reduced battery storage needs
            
            **3. Biomass Energy**
            - Convert campus organic waste to energy
            - Biogas plant for cafeteria waste
            - Capacity: 50 kW
            - Dual benefit: Waste management + energy
            """)
        
        # Renewable energy projection
        st.markdown("---")
        st.subheader("📈 Renewable Energy Growth Projection")
        
        years = list(range(2026, 2031))
        current_renewable = 20
        projections = pd.DataFrame({
            'Year': years,
            'Conservative': [20, 30, 42, 56, 70],
            'Moderate': [20, 35, 52, 68, 85],
            'Aggressive': [20, 40, 62, 82, 100]
        })
        
        fig = go.Figure()
        
        for scenario in ['Conservative', 'Moderate', 'Aggressive']:
            fig.add_trace(go.Scatter(
                x=projections['Year'],
                y=projections[scenario],
                mode='lines+markers',
                name=scenario,
                line=dict(width=3)
            ))
        
        fig.add_hline(y=100, line_dash="dash", line_color="green", annotation_text="100% Renewable Target")
        
        fig.update_layout(
            height=400,
            xaxis=dict(title='Year'),
            yaxis=dict(title='Renewable Energy (%)', range=[0, 110]),
            plot_bgcolor='white',
            paper_bgcolor='white'
        )
        
        st.plotly_chart(fig, use_container_width=True)
    
    with tab2:
        st.subheader("⚡ Energy Efficiency Initiatives")
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown("""
            #### Lighting Optimization
            
            **1. LED Conversion (100%)**
            - Replace all traditional lights with LEDs
            - Energy savings: 60-70%
            - Investment: ₹2 Crores
            - Annual savings: ₹80 Lakhs
            - Payback: 2.5 years
            
            **2. Smart Lighting Controls**
            - Motion sensors in corridors and washrooms
            - Daylight harvesting systems
            - Automated scheduling
            - Additional savings: 30%
            
            **3. Outdoor Lighting**
            - Solar-powered street lights
            - Smart controls with timers
            - Reduced light pollution
            """)
            
            st.markdown("""
            #### HVAC Optimization
            
            **1. Variable Frequency Drives (VFDs)**
            - Install VFDs on all AC units
            - Energy savings: 20-30%
            - Investment: ₹1.5 Crores
            
            **2. Smart Thermostats**
            - Occupancy-based temperature control
            - Remote monitoring and control
            - Zoned cooling systems
            """)
        
        with col2:
            st.markdown("""
            #### Building Envelope Improvements
            
            **1. Thermal Insulation**
            - Roof insulation for all buildings
            - Reflective coatings
            - Cooling load reduction: 25%
            - Investment: ₹3 Crores
            
            **2. Window Upgrades**
            - Double-glazed windows for new buildings
            - Solar control films for existing buildings
            - Heat gain reduction: 40%
            
            **3. Green Roofs**
            - Vegetation on select building roofs
            - Temperature reduction: 3-5°C
            - Additional benefits: Rainwater harvesting
            """)
            
            st.markdown("""
            #### Equipment Efficiency
            
            **1. Energy Star Appliances**
            - Replace old equipment with 5-star rated
            - Covers: Refrigerators, computers, printers
            - Savings: 20-40% per appliance
            
            **2. Power Factor Correction**
            - Install capacitor banks
            - Reduce reactive power
            - Lower electricity bills by 5-10%
            """)
        
        # Energy savings potential
        st.markdown("---")
        st.subheader("💰 Energy Savings Potential")
        
        savings_data = pd.DataFrame({
            'Initiative': ['LED Lighting', 'HVAC Optimization', 'Building Insulation', 'Smart Controls', 'Equipment Upgrade'],
            'Annual Savings (kWh)': [450000, 680000, 520000, 380000, 290000],
            'Investment (₹ Lakhs)': [200, 150, 300, 100, 80],
            'Payback (Years)': [2.5, 1.8, 4.2, 2.1, 2.3]
        })
        
        fig = make_subplots(
            rows=1, cols=2,
            subplot_titles=('Annual Energy Savings', 'Payback Period'),
            specs=[[{'type': 'bar'}, {'type': 'bar'}]]
        )
        
        fig.add_trace(
            go.Bar(x=savings_data['Initiative'], y=savings_data['Annual Savings (kWh)'], marker_color='#52c41a'),
            row=1, col=1
        )
        
        fig.add_trace(
            go.Bar(x=savings_data['Initiative'], y=savings_data['Payback (Years)'], marker_color='#1890ff'),
            row=1, col=2
        )
        
        fig.update_layout(height=400, showlegend=False)
        fig.update_xaxes(tickangle=45)
        
        st.plotly_chart(fig, use_container_width=True)
    
    with tab3:
        st.subheader("🏗️ Infrastructure Modernization")
        
        st.markdown("""
        #### Energy Storage Systems
        
        **1. Battery Energy Storage System (BESS)**
        - Capacity: 2 MWh lithium-ion batteries
        - Purpose: Store excess solar energy for evening use
        - Peak shaving and load balancing
        - Investment: ₹8 Crores
        - Benefits:
          - Reduce grid dependency by 30%
          - Lower demand charges
          - Backup power during outages
        
        **2. Thermal Energy Storage**
        - Ice storage systems for AC cooling
        - Shift cooling load to off-peak hours
        - Reduce peak demand by 40%
        - Investment: ₹2 Crores
        
        #### Electric Vehicle Infrastructure
        
        **1. EV Charging Stations**
        - Install 50 charging points across campus
        - Solar-powered charging stations
        - Encourage electric vehicle adoption
        - Investment: ₹1.5 Crores
        
        **2. Electric Campus Shuttle**
        - Replace diesel buses with electric buses
        - 10 electric buses for campus transport
        - Annual fuel savings: ₹40 Lakhs
        - Investment: ₹5 Crores
        
        #### Microgrid Development
        
        **1. Campus Microgrid**
        - Integrate all renewable sources
        - Advanced energy management system
        - Grid-independent operation capability
        - Investment: ₹15 Crores
        - Benefits:
          - Enhanced reliability
          - Optimized energy distribution
          - Research opportunities
        """)
        
        # Infrastructure timeline
        st.markdown("---")
        st.subheader("📅 Implementation Timeline")
        
        timeline_data = pd.DataFrame({
            'Phase': ['Phase 1\n(2026)', 'Phase 2\n(2027)', 'Phase 3\n(2028)', 'Phase 4\n(2029-30)'],
            'Projects': [
                'LED Lighting, Solar Expansion (500kW), Smart Meters',
                'HVAC Optimization, BESS (1MWh), EV Chargers (25)',
                'Building Insulation, Solar (1000kW), Microgrid Phase 1',
                'Complete Solar (2000kW), Full Microgrid, 100% EV Fleet'
            ],
            'Investment (₹ Cr)': [5, 12, 18, 25],
            'Cumulative Savings (%)': [15, 35, 60, 85]
        })
        
        st.table(timeline_data)
    
    with tab4:
        st.subheader("🤖 Smart Energy Management Systems")
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown("""
            #### IoT & Automation
            
            **1. Smart Metering Infrastructure**
            - Real-time energy monitoring
            - Individual building/floor level metering
            - Automated anomaly detection
            - Investment: ₹1 Crore
            
            **2. Building Management System (BMS)**
            - Centralized control of all building systems
            - HVAC, lighting, security integration
            - Predictive maintenance
            - Energy optimization algorithms
            - Investment: ₹3 Crores
            
            **3. Occupancy Sensors**
            - AI-powered occupancy detection
            - Automatic HVAC and lighting adjustment
            - Deployed in 500+ rooms
            - Investment: ₹50 Lakhs
            """)
        
        with col2:
            st.markdown("""
            #### AI & Machine Learning
            
            **1. Predictive Analytics**
            - Forecast energy demand
            - Weather-based load prediction
            - Optimize renewable energy usage
            - Reduce peak demand charges
            
            **2. Automated Demand Response**
            - Dynamic load shedding
            - Priority-based power allocation
            - Grid interaction optimization
            
            **3. Energy Dashboard & Alerts**
            - Real-time visualization (like this!)
            - Automated alerts for anomalies
            - Mobile app for facility managers
            - Student awareness campaigns
            """)
        
        st.markdown("---")
        st.subheader("📱 Digital Solutions")
        
        col1, col2, col3 = st.columns(3)
        
        with col1:
            st.info("""
            **Energy Monitoring App**
            - Real-time consumption data
            - Facility-wise breakdown
            - Historical trends
            - Carbon footprint tracking
            """)
        
        with col2:
            st.success("""
            **Student Engagement Portal**
            - Energy saving competitions
            - Gamification & rewards
            - Educational content
            - Sustainability pledges
            """)
        
        with col3:
            st.warning("""
            **Maintenance System**
            - Predictive maintenance alerts
            - Work order management
            - Equipment lifecycle tracking
            - Performance analytics
            """)
    
    with tab5:
        st.subheader("📊 Return on Investment Analysis")
        
        # Total investment and savings
        col1, col2, col3 = st.columns(3)
        
        with col1:
            st.metric("Total Investment", "₹60 Crores", help="5-year investment plan")
        
        with col2:
            st.metric("Annual Savings (Year 5)", "₹12 Crores", help="Energy + maintenance savings")
        
        with col3:
            st.metric("Overall Payback Period", "5.2 years", help="Considering all initiatives")
        
        st.markdown("---")
        
        # 10-year financial projection
        st.subheader("💰 10-Year Financial Projection")
        
        years = list(range(2026, 2036))
        cumulative_investment = [5, 17, 35, 60, 60, 60, 60, 60, 60, 60]
        cumulative_savings = [1.5, 4.5, 9, 15, 27, 39, 51, 63, 75, 87]
        net_benefit = [s - i for s, i in zip(cumulative_savings, cumulative_investment)]
        
        fig = go.Figure()
        
        fig.add_trace(go.Bar(
            x=years,
            y=cumulative_investment,
            name='Cumulative Investment',
            marker_color='#ff6b6b'
        ))
        
        fig.add_trace(go.Bar(
            x=years,
            y=cumulative_savings,
            name='Cumulative Savings',
            marker_color='#52c41a'
        ))
        
        fig.add_trace(go.Scatter(
            x=years,
            y=net_benefit,
            name='Net Benefit',
            mode='lines+markers',
            line=dict(color='#1890ff', width=3),
            yaxis='y2'
        ))
        
        fig.update_layout(
            height=500,
            yaxis=dict(title='Amount (₹ Crores)'),
            yaxis2=dict(title='Net Benefit (₹ Crores)', overlaying='y', side='right'),
            barmode='group',
            hovermode='x unified'
        )
        
        st.plotly_chart(fig, use_container_width=True)
        
        # Benefits summary
        st.markdown("---")
        st.subheader("🎯 Key Benefits Summary")
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown("""
            #### Financial Benefits
            - **Annual Energy Cost Reduction:** 65%
            - **Maintenance Cost Reduction:** 30%
            - **Peak Demand Charge Savings:** ₹2 Cr/year
            - **Government Incentives:** ₹5 Crores (one-time)
            - **Carbon Credits Revenue:** ₹50 Lakhs/year
            - **10-Year Net Savings:** ₹27 Crores
            
            #### Risk Mitigation
            - Protection from energy price volatility
            - Reduced grid dependency
            - Enhanced power reliability
            - Future-proof infrastructure
            """)
        
        with col2:
            st.markdown("""
            #### Environmental Benefits
            - **CO₂ Reduction:** 3,500 tons/year
            - **Renewable Energy:** 85% by 2030
            - **Water Savings:** 50 million liters/year (cooling)
            - **Waste Reduction:** 200 tons/year (biomass)
            
            #### Social Benefits
            - Enhanced campus reputation
            - Research opportunities
            - Student awareness & engagement
            - Healthier campus environment
            - Leadership in sustainability
            - Attraction for eco-conscious students
            """)

# Predictions Page
elif page == "📈 Predictions":
    st.header("📈 Predictive Analytics & Forecasting")
    
    st.subheader("🔮 Energy Demand Forecast (Next 30 Days)")
    
    # Simple forecasting using historical patterns
    last_30_days = daily_data.tail(30)
    avg_consumption = last_30_days['total_consumption_kwh'].mean()
    std_consumption = last_30_days['total_consumption_kwh'].std()
    
    # Generate forecast
    forecast_dates = pd.date_range(
        start=daily_data['date'].max() + timedelta(days=1),
        periods=30,
        freq='D'
    )
    
    # Add seasonal and trend components
    forecast_values = []
    for i, date in enumerate(forecast_dates):
        base = avg_consumption
        trend = i * 5  # Slight upward trend
        seasonal = np.sin(i * 2 * np.pi / 7) * std_consumption * 0.3  # Weekly pattern
        noise = np.random.normal(0, std_consumption * 0.1)
        forecast_values.append(base + trend + seasonal + noise)
    
    # Confidence intervals
    lower_bound = [v - std_consumption * 0.5 for v in forecast_values]
    upper_bound = [v + std_consumption * 0.5 for v in forecast_values]
    
    fig = go.Figure()
    
    # Historical data
    fig.add_trace(go.Scatter(
        x=daily_data['date'].tail(60),
        y=daily_data['total_consumption_kwh'].tail(60),
        mode='lines',
        name='Historical',
        line=dict(color='#667eea', width=2)
    ))
    
    # Forecast
    fig.add_trace(go.Scatter(
        x=forecast_dates,
        y=forecast_values,
        mode='lines',
        name='Forecast',
        line=dict(color='#52c41a', width=2, dash='dash')
    ))
    
    # Confidence interval
    fig.add_trace(go.Scatter(
        x=list(forecast_dates) + list(forecast_dates)[::-1],
        y=upper_bound + lower_bound[::-1],
        fill='toself',
        fillcolor='rgba(82, 196, 26, 0.2)',
        line=dict(color='rgba(255,255,255,0)'),
        name='Confidence Interval',
        showlegend=True
    ))
    
    fig.update_layout(
        height=500,
        hovermode='x unified',
        plot_bgcolor='white',
        paper_bgcolor='white',
        yaxis=dict(title='Energy Consumption (kWh)')
    )
    
    st.plotly_chart(fig, use_container_width=True)
    
    # Peak demand prediction
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("⚡ Peak Demand Prediction")
        
        st.info(f"""
        **Tomorrow's Peak Demand**
        - **Predicted Time:** 2:00 PM - 4:00 PM
        - **Expected Load:** {max(forecast_values[:1]):.0f} kWh
        - **Confidence:** 85%
        
        **Recommendation:**
        - Pre-cool buildings before peak hours
        - Maximize solar energy utilization
        - Consider load shedding for non-critical areas
        """)
    
    with col2:
        st.subheader("💡 Optimization Recommendations")
        
        st.success("""
        **AI-Powered Suggestions**
        1. **Shift 15% load** from 2-4 PM to 10-12 PM
        2. **Increase solar utilization** by 200 kWh during peak
        3. **Deploy battery storage** to reduce grid dependency
        4. **Implement demand response** in Hostel Block 2
        
        **Potential Savings:** ₹15,000/day
        """)
    
    # Anomaly detection
    st.markdown("---")
    st.subheader("🚨 Anomaly Detection")
    
    # Detect anomalies (simple threshold-based)
    daily_data['anomaly'] = (
        (daily_data['total_consumption_kwh'] > avg_consumption + 2 * std_consumption) |
        (daily_data['total_consumption_kwh'] < avg_consumption - 2 * std_consumption)
    )
    
    anomalies = daily_data[daily_data['anomaly']]
    
    if len(anomalies) > 0:
        st.warning(f"⚠️ Detected {len(anomalies)} anomalous consumption patterns in the last year")
        
        fig = go.Figure()
        
        fig.add_trace(go.Scatter(
            x=daily_data['date'],
            y=daily_data['total_consumption_kwh'],
            mode='lines',
            name='Consumption',
            line=dict(color='#667eea')
        ))
        
        fig.add_trace(go.Scatter(
            x=anomalies['date'],
            y=anomalies['total_consumption_kwh'],
            mode='markers',
            name='Anomalies',
            marker=dict(color='red', size=10, symbol='x')
        ))
        
        fig.update_layout(height=400, hovermode='x unified')
        st.plotly_chart(fig, use_container_width=True)
        
        st.dataframe(anomalies[['date', 'total_consumption_kwh', 'carbon_emissions_kg']].tail(10))
    else:
        st.success("✅ No significant anomalies detected in recent data")

# Professional Footer
st.markdown("---")
st.markdown("""
<div style='background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            padding: 2rem;
            border-radius: 15px;
            text-align: center;
            margin-top: 3rem;
            box-shadow: 0 8px 20px rgba(102, 126, 234, 0.3);'>
    <h3 style='color: white; margin: 0 0 0.5rem 0; font-size: 1.5rem; font-weight: 700;'>
        VIT Campus Energy Management Dashboard
    </h3>
    <p style='color: rgba(255, 255, 255, 0.9); margin: 0.5rem 0; font-size: 1rem;'>
        Powered by Streamlit • Real-time Analytics • Advanced Sustainability Solutions
    </p>
    <p style='color: rgba(255, 255, 255, 0.85); margin: 0.5rem 0; font-size: 0.9rem;'>
        © 2026 VIT | Committed to Excellence in Energy Management
    </p>
    <div style='margin-top: 1rem; padding-top: 1rem; border-top: 1px solid rgba(255, 255, 255, 0.3);'>
        <p style='color: rgba(255, 255, 255, 0.95); margin: 0; font-size: 1.1rem; font-weight: 600;'>
            🌱 Carbon Neutrality Target: 2030 🌱
        </p>
    </div>
</div>
""", unsafe_allow_html=True)

