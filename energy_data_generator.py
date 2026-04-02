"""
Mock Data Generator for VIT Campus Energy Utility Dashboard
Generates realistic energy consumption data for various campus facilities
"""

import pandas as pd
import numpy as np
from datetime import datetime, timedelta
import random

class VITEnergyDataGenerator:
    """Generate mock energy data for VIT campus facilities"""
    
    def __init__(self, seed=42):
        np.random.seed(seed)
        random.seed(seed)
        
        # Campus facilities
        self.facilities = [
            'Academic Block A', 'Academic Block B', 'Academic Block C',
            'Library', 'Hostel Block 1', 'Hostel Block 2', 'Hostel Block 3',
            'Cafeteria', 'Sports Complex', 'Research Labs', 'Administration',
            'Auditorium', 'Medical Center'
        ]
        
        # Energy sources
        self.energy_sources = ['Grid', 'Solar', 'Wind', 'Diesel Generator']
        
    def generate_hourly_data(self, days=30):
        """Generate hourly energy consumption data"""
        data = []
        start_date = datetime.now() - timedelta(days=days)
        
        for facility in self.facilities:
            base_consumption = self._get_base_consumption(facility)
            
            for day in range(days):
                current_date = start_date + timedelta(days=day)
                
                for hour in range(24):
                    timestamp = current_date + timedelta(hours=hour)
                    
                    # Add time-based variations
                    hour_factor = self._get_hour_factor(hour, facility)
                    day_factor = self._get_day_factor(current_date.weekday())
                    
                    # Calculate consumption with noise
                    consumption = base_consumption * hour_factor * day_factor
                    consumption *= np.random.uniform(0.85, 1.15)  # Add randomness
                    
                    # Energy source distribution
                    solar_available = 1 if 6 <= hour <= 18 else 0
                    
                    data.append({
                        'timestamp': timestamp,
                        'facility': facility,
                        'total_consumption_kwh': round(consumption, 2),
                        'grid_kwh': round(consumption * 0.6 * (1 - solar_available * 0.3), 2),
                        'solar_kwh': round(consumption * 0.3 * solar_available, 2),
                        'wind_kwh': round(consumption * 0.08, 2),
                        'diesel_kwh': round(consumption * 0.02, 2),
                        'temperature_c': round(np.random.uniform(22, 38), 1),
                        'occupancy_percent': self._get_occupancy(facility, hour, current_date.weekday())
                    })
        
        return pd.DataFrame(data)
    
    def generate_daily_summary(self, days=365):
        """Generate daily summary data for trend analysis"""
        data = []
        start_date = datetime.now() - timedelta(days=days)
        
        # Simulate an ongoing sustainability initiative
        initial_solar = 500
        solar_growth_rate = 4.5  # Daily increase in solar capacity over the year
        
        for day in range(days):
            current_date = start_date + timedelta(days=day)
            month = current_date.month
            
            # Base daily consumption with weekly seasonality
            base_consumption = 9500 + np.sin(day / 3.14) * 500
            
            # 1. Weather and Academic Calendar Effects
            if month in [4, 5, 8, 9]: # Summer & Post-Summer Peak
                base_consumption *= 1.4  # Heavy AC usage
            elif month in [12, 1]:  # Winter
                base_consumption *= 0.85
                
            # Vacations (Lower consumption)
            if month in [6, 7]: # Summer Vacation
                base_consumption *= 0.6
                
            # Events / Tech Fests (GraVITas in Sept, Riviera in Feb)
            if month == 2 and 10 <= current_date.day <= 15:
                base_consumption *= 1.5
            if month == 9 and 20 <= current_date.day <= 25:
                base_consumption *= 1.45
            
            # Weekend reduction
            if current_date.weekday() >= 5:
                base_consumption *= 0.75
                
            # Add some daily realistic noise
            daily_consumption = base_consumption * np.random.uniform(0.95, 1.05)
            
            # 2. Sustainability Trends (Growing Solar Capacity)
            # Solar capacity grows over the year to show "progress"
            current_solar_capacity = initial_solar + (solar_growth_rate * day)
            
            # Solar generation depends on weather (lower in winter/monsoon, higher in summer)
            solar_efficiency = np.random.uniform(0.8, 1.0)
            if month in [7, 8, 11, 12]:  # Monson/Winter
                solar_efficiency *= 0.7
                
            solar_generation = current_solar_capacity * solar_efficiency
            wind_generation = np.random.uniform(400, 800) + np.sin(day / 10) * 100
            
            # Cap renewables if they exceed consumption (unlikely but safe)
            if solar_generation + wind_generation > daily_consumption:
                solar_generation = daily_consumption * 0.7
                wind_generation = daily_consumption * 0.3
                
            grid_consumption = daily_consumption - solar_generation - wind_generation
            
            data.append({
                'date': current_date.date(),
                'total_consumption_kwh': round(daily_consumption, 2),
                'solar_generation_kwh': round(solar_generation, 2),
                'wind_generation_kwh': round(wind_generation, 2),
                'grid_consumption_kwh': round(grid_consumption, 2),
                'carbon_emissions_kg': round(grid_consumption * 0.82, 2),
                # TANGEDCO Commercial Tariff Approximation
                # Base Rate ~₹8.5/kWh. Adjusted for Time-of-Day (Peak +20%, Off-peak -5%)
                # Blended average grid rate roughly ₹8.95 / kWh + fixed demand charges
                'cost_inr': round(grid_consumption * 8.95 + (solar_generation + wind_generation) * 1.2, 2),
                'renewable_percentage': round((solar_generation + wind_generation) / daily_consumption * 100, 2)
            })
        
        return pd.DataFrame(data)
    
    def generate_facility_metadata(self):
        """Generate metadata for each facility"""
        data = []
        
        for facility in self.facilities:
            data.append({
                'facility': facility,
                'area_sqm': np.random.randint(2000, 15000),
                'max_capacity': np.random.randint(200, 2000),
                'ac_units': np.random.randint(20, 150),
                'lighting_points': np.random.randint(100, 800),
                'solar_panels': np.random.randint(0, 200),
                'energy_rating': random.choice(['A', 'B', 'C', 'D']),
                'last_audit_date': (datetime.now() - timedelta(days=np.random.randint(30, 365))).date()
            })
        
        return pd.DataFrame(data)
    
    def _get_base_consumption(self, facility):
        """Get base consumption for facility type"""
        consumption_map = {
            'Academic Block A': 180, 'Academic Block B': 170, 'Academic Block C': 175,
            'Library': 120, 'Hostel Block 1': 200, 'Hostel Block 2': 195, 'Hostel Block 3': 190,
            'Cafeteria': 250, 'Sports Complex': 150, 'Research Labs': 220,
            'Administration': 100, 'Auditorium': 160, 'Medical Center': 130
        }
        return consumption_map.get(facility, 150)
    
    def _get_hour_factor(self, hour, facility):
        """Get consumption multiplier based on hour using smooth distributions"""
        base = 0.3 
        
        if 'Hostel' in facility:
            morning_peak = 0.6 * np.exp(-0.5 * ((hour - 8.0) / 1.5)**2)
            evening_peak = 0.8 * np.exp(-0.5 * ((hour - 21.0) / 2.5)**2)
            return base + morning_peak + evening_peak
        elif 'Cafeteria' in facility:
            lunch_peak = 1.0 * np.exp(-0.5 * ((hour - 13.0) / 1.5)**2)
            dinner_peak = 0.8 * np.exp(-0.5 * ((hour - 19.5) / 1.5)**2)
            return base + lunch_peak + dinner_peak
        elif 'Library' in facility:
            day_usage = 0.8 * np.exp(-0.5 * ((hour - 14.0) / 4.0)**2)
            return base + day_usage
        else:
            working_hours = 0.9 * np.exp(-0.5 * ((hour - 14.0) / 3.0)**2)
            return base + working_hours
    
    def _get_day_factor(self, weekday):
        """Get consumption multiplier based on day of week"""
        if weekday >= 5:  # Weekend
            return 0.6
        return 1.0
    
    def _get_occupancy(self, facility, hour, weekday):
        """Get occupancy percentage smoothly"""
        if weekday >= 5:
            base = 20
        else:
            base = 70
            
        peak_factor = np.exp(-0.5 * ((hour - 14.0) / 4.0)**2)
        occupancy = base * peak_factor + np.random.uniform(5, 15)
        
        if 'Hostel' in facility:
            # Reverse occupancy for hostels (students leave during day)
            occupancy = 100 - occupancy
            
        return min(100, max(0, occupancy))


def generate_all_data():
    """Generate all mock data files"""
    generator = VITEnergyDataGenerator()
    
    print("Generating hourly data...")
    hourly_data = generator.generate_hourly_data(days=30)
    hourly_data.to_csv('data/hourly_energy_data.csv', index=False)
    print(f"✓ Generated {len(hourly_data)} hourly records")
    
    print("Generating daily summary...")
    daily_data = generator.generate_daily_summary(days=365)
    daily_data.to_csv('data/daily_energy_summary.csv', index=False)
    print(f"✓ Generated {len(daily_data)} daily records")
    
    print("Generating facility metadata...")
    facility_data = generator.generate_facility_metadata()
    facility_data.to_csv('data/facility_metadata.csv', index=False)
    print(f"✓ Generated metadata for {len(facility_data)} facilities")
    
    print("\n✅ All data generated successfully!")


if __name__ == "__main__":
    import os
    os.makedirs('data', exist_ok=True)
    generate_all_data()
