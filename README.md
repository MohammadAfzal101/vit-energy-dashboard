# VIT Campus Energy Utility Dashboard

A comprehensive Streamlit dashboard for monitoring and optimizing energy consumption at VIT campus with long-term sustainability solutions.

## 🌟 Features

### 📊 Real-time Monitoring
- Live energy consumption tracking across all campus facilities
- Multi-source energy monitoring (Solar, Wind, Grid, Diesel)
- Facility-wise consumption breakdown
- Temperature and occupancy correlation analysis

### 📈 Advanced Analytics
- Hourly and daily consumption patterns
- Weekly trends and seasonal variations
- Facility performance comparison
- Temperature vs consumption analysis
- Renewable energy ratio tracking

### 🌱 Sustainability Metrics
- Carbon footprint tracking and trends
- Renewable energy progress monitoring
- Environmental impact calculations
- Cost savings from renewable sources
- Emissions reduction equivalents (trees, cars, homes)

### 💡 Long-term Solutions
Comprehensive sustainability roadmap including:
- **Renewable Energy Expansion**: Solar, wind, and hybrid systems
- **Energy Efficiency**: LED lighting, HVAC optimization, building insulation
- **Infrastructure Modernization**: Battery storage, EV charging, microgrid
- **Smart Systems**: IoT sensors, AI-powered optimization, BMS
- **ROI Analysis**: 10-year financial projections and payback analysis

### 📈 Predictive Analytics
- 30-day energy demand forecasting
- Peak demand prediction
- Anomaly detection
- AI-powered optimization recommendations

## 🚀 Quick Start

### Prerequisites
- Python 3.8 or higher
- pip package manager

### Installation

1. Clone or download this repository

2. Install required dependencies:
```bash
pip install -r requirements.txt
```

3. Generate mock data:
```bash
python energy_data_generator.py
```

4. Run the dashboard:
```bash
streamlit run app.py
```

5. Open your browser and navigate to `http://localhost:8501`

## 📁 Project Structure

```
VIT-Energy-Dashboard/
├── app.py                      # Main Streamlit dashboard
├── energy_data_generator.py    # Mock data generator
├── requirements.txt            # Python dependencies
├── README.md                   # This file
└── data/                       # Generated data files
    ├── hourly_energy_data.csv
    ├── daily_energy_summary.csv
    └── facility_metadata.csv
```

## 📊 Dashboard Pages

### 🏠 Overview
- Key performance metrics
- 30-day consumption trends
- Energy source distribution
- Facility-wise consumption (last 24 hours)

### 📊 Analytics
- Hourly consumption patterns
- Weekly trends
- Temperature correlation
- Facility performance comparison

### 🌱 Sustainability
- Carbon emissions tracking
- Renewable energy progress
- Environmental impact summary
- Cost savings analysis

### 💡 Solutions
- Renewable energy expansion plans
- Energy efficiency initiatives
- Infrastructure modernization roadmap
- Smart systems implementation
- Complete ROI analysis

### 📈 Predictions
- 30-day demand forecasting
- Peak demand prediction
- Anomaly detection
- Optimization recommendations

## 🎯 Sustainability Goals

- **2026**: 30% renewable energy
- **2027**: 50% renewable energy
- **2028**: 70% renewable energy
- **2030**: 100% renewable energy (Carbon Neutral)

## 💰 Investment & Returns

- **Total Investment**: ₹60 Crores (5-year plan)
- **Annual Savings (Year 5)**: ₹12 Crores
- **Payback Period**: 5.2 years
- **10-Year Net Savings**: ₹27 Crores

## 🌍 Environmental Impact

- **CO₂ Reduction**: 3,500 tons/year (by 2030)
- **Trees Equivalent**: 166,000+ trees saved
- **Cars Off Road**: 760+ cars equivalent
- **Renewable Energy**: 85% by 2030

## 🛠️ Customization

### Modify Mock Data
Edit `energy_data_generator.py` to:
- Add/remove facilities
- Adjust consumption patterns
- Change data generation parameters
- Modify time ranges

### Customize Dashboard
Edit `app.py` to:
- Add new visualizations
- Modify color schemes
- Add custom metrics
- Integrate real data sources

## 📝 Data Schema

### Hourly Energy Data
- timestamp, facility, total_consumption_kwh
- grid_kwh, solar_kwh, wind_kwh, diesel_kwh
- temperature_c, occupancy_percent

### Daily Summary
- date, total_consumption_kwh
- solar_generation_kwh, wind_generation_kwh
- grid_consumption_kwh, carbon_emissions_kg
- cost_inr, renewable_percentage

### Facility Metadata
- facility, area_sqm, max_capacity
- ac_units, lighting_points, solar_panels
- energy_rating, last_audit_date

## 🔧 Technologies Used

- **Streamlit**: Interactive web dashboard
- **Plotly**: Interactive visualizations
- **Pandas**: Data manipulation
- **NumPy**: Numerical computations
- **Scikit-learn**: Predictive analytics

## 📞 Support

For questions or issues, please contact the VIT Energy Management Team.

## 📄 License

This project is created for VIT Campus energy management purposes.

---

**🌱 Committed to a Sustainable Future 🌱**
