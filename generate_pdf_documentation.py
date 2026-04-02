"""
PDF Documentation Generator for VIT Energy Dashboard
Creates a professional PDF with screenshots and explanations
"""

from reportlab.lib.pagesizes import A4, letter
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Image, PageBreak, Table, TableStyle
from reportlab.lib import colors
from reportlab.lib.enums import TA_CENTER, TA_LEFT, TA_JUSTIFY
from reportlab.pdfgen import canvas
from datetime import datetime
import os

class VITEnergyDashboardPDF:
    def __init__(self, filename="VIT_Energy_Dashboard_Documentation.pdf"):
        self.filename = filename
        self.doc = SimpleDocTemplate(
            filename,
            pagesize=letter,
            rightMargin=0.75*inch,
            leftMargin=0.75*inch,
            topMargin=1*inch,
            bottomMargin=0.75*inch
        )
        self.story = []
        self.styles = getSampleStyleSheet()
        self._create_custom_styles()
    
    def _create_custom_styles(self):
        """Create custom paragraph styles"""
        # Title style
        self.styles.add(ParagraphStyle(
            name='CustomTitle',
            parent=self.styles['Heading1'],
            fontSize=24,
            textColor=colors.HexColor('#667eea'),
            spaceAfter=30,
            alignment=TA_CENTER,
            fontName='Helvetica-Bold'
        ))
        
        # Subtitle style
        self.styles.add(ParagraphStyle(
            name='CustomSubtitle',
            parent=self.styles['Heading2'],
            fontSize=16,
            textColor=colors.HexColor('#764ba2'),
            spaceAfter=12,
            spaceBefore=20,
            fontName='Helvetica-Bold'
        ))
        
        # Section header
        self.styles.add(ParagraphStyle(
            name='SectionHeader',
            parent=self.styles['Heading2'],
            fontSize=14,
            textColor=colors.HexColor('#667eea'),
            spaceAfter=10,
            spaceBefore=15,
            fontName='Helvetica-Bold',
            borderWidth=0,
            borderColor=colors.HexColor('#667eea'),
            borderPadding=5,
            leftIndent=10
        ))
        
        # Body text
        self.styles.add(ParagraphStyle(
            name='CustomBody',
            parent=self.styles['BodyText'],
            fontSize=11,
            alignment=TA_JUSTIFY,
            spaceAfter=10,
            leading=14
        ))
        
        # Caption
        self.styles.add(ParagraphStyle(
            name='Caption',
            parent=self.styles['BodyText'],
            fontSize=9,
            textColor=colors.grey,
            alignment=TA_CENTER,
            spaceAfter=15,
            italic=True
        ))
    
    def add_cover_page(self):
        """Add cover page"""
        # Title
        title = Paragraph(
            "VIT Campus Energy Management Dashboard",
            self.styles['CustomTitle']
        )
        self.story.append(Spacer(1, 1.5*inch))
        self.story.append(title)
        
        # Subtitle
        subtitle = Paragraph(
            "Comprehensive Documentation & Analysis",
            self.styles['CustomSubtitle']
        )
        self.story.append(Spacer(1, 0.3*inch))
        self.story.append(subtitle)
        
        # Description
        description = Paragraph(
            """
            This document provides a complete overview of the VIT Campus Energy Management Dashboard,
            including detailed explanations of all visualizations, analytics, sustainability metrics,
            and long-term energy solutions for achieving carbon neutrality by 2030.
            """,
            self.styles['CustomBody']
        )
        self.story.append(Spacer(1, 0.5*inch))
        self.story.append(description)
        
        # Info table
        info_data = [
            ['Institution:', 'VIT Campus'],
            ['Dashboard Type:', 'Energy Management & Sustainability'],
            ['Technology:', 'Streamlit, Python, Plotly'],
            ['Date:', datetime.now().strftime('%B %d, %Y')],
            ['Version:', '1.0']
        ]
        
        info_table = Table(info_data, colWidths=[2*inch, 3.5*inch])
        info_table.setStyle(TableStyle([
            ('BACKGROUND', (0, 0), (0, -1), colors.HexColor('#f0f0f0')),
            ('TEXTCOLOR', (0, 0), (-1, -1), colors.black),
            ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
            ('FONTNAME', (0, 0), (0, -1), 'Helvetica-Bold'),
            ('FONTNAME', (1, 0), (1, -1), 'Helvetica'),
            ('FONTSIZE', (0, 0), (-1, -1), 10),
            ('BOTTOMPADDING', (0, 0), (-1, -1), 8),
            ('TOPPADDING', (0, 0), (-1, -1), 8),
            ('GRID', (0, 0), (-1, -1), 1, colors.grey)
        ]))
        
        self.story.append(Spacer(1, 0.8*inch))
        self.story.append(info_table)
        
        # Footer
        footer = Paragraph(
            "🌱 Committed to Carbon Neutrality by 2030 🌱",
            self.styles['Caption']
        )
        self.story.append(Spacer(1, 1.5*inch))
        self.story.append(footer)
        
        self.story.append(PageBreak())
    
    def add_section(self, title, content, image_path=None, caption=None):
        """Add a section with title, content, and optional image"""
        # Section title
        section_title = Paragraph(title, self.styles['SectionHeader'])
        self.story.append(section_title)
        
        # Content
        for paragraph in content:
            p = Paragraph(paragraph, self.styles['CustomBody'])
            self.story.append(p)
            self.story.append(Spacer(1, 0.1*inch))
        
        # Image if provided
        if image_path and os.path.exists(image_path):
            self.story.append(Spacer(1, 0.2*inch))
            img = Image(image_path, width=6.5*inch, height=3.5*inch, kind='proportional')
            self.story.append(img)
            
            if caption:
                cap = Paragraph(caption, self.styles['Caption'])
                self.story.append(cap)
        
        self.story.append(Spacer(1, 0.3*inch))
    
    def generate(self):
        """Generate the PDF"""
        self.doc.build(self.story)
        print(f"✅ PDF generated successfully: {self.filename}")


def create_dashboard_documentation():
    """Create the complete dashboard documentation PDF"""
    
    pdf = VITEnergyDashboardPDF("VIT_Energy_Dashboard_Documentation.pdf")
    
    # Cover page
    pdf.add_cover_page()
    
    # Table of Contents
    toc_title = Paragraph("Table of Contents", pdf.styles['CustomTitle'])
    pdf.story.append(toc_title)
    pdf.story.append(Spacer(1, 0.3*inch))
    
    toc_items = [
        "1. Dashboard Overview",
        "2. Predictive Analytics & Forecasting",
        "3. Sustainability Metrics & Environmental Impact",
        "4. Long-term Energy Sustainability Solutions",
        "5. Key Features & Benefits",
        "6. Conclusion"
    ]
    
    for item in toc_items:
        p = Paragraph(item, pdf.styles['CustomBody'])
        pdf.story.append(p)
        pdf.story.append(Spacer(1, 0.05*inch))
    
    pdf.story.append(PageBreak())
    
    # Section 1: Dashboard Overview
    pdf.add_section(
        "1. Dashboard Overview",
        [
            """The VIT Campus Energy Management Dashboard is a comprehensive, real-time monitoring system 
            designed to track, analyze, and optimize energy consumption across the entire campus. Built using 
            modern web technologies including Streamlit and Plotly, the dashboard provides actionable insights 
            for achieving carbon neutrality by 2030.""",
            
            """<b>Key Components:</b>""",
            """• <b>Real-time Monitoring:</b> Live tracking of energy consumption across 13 campus facilities""",
            """• <b>Advanced Analytics:</b> Hourly, daily, and seasonal consumption patterns""",
            """• <b>Sustainability Metrics:</b> Carbon footprint tracking and renewable energy progress""",
            """• <b>Predictive Analytics:</b> 30-day demand forecasting with AI-powered recommendations""",
            """• <b>Long-term Solutions:</b> Comprehensive roadmap with ₹60 Crore investment plan"""
        ],
        image_path="screenshot_footer.png",
        caption="Figure 1: Dashboard footer showing commitment to carbon neutrality"
    )
    
    # Section 2: Predictive Analytics
    pdf.add_section(
        "2. Predictive Analytics & Forecasting",
        [
            """The Predictive Analytics section leverages machine learning algorithms to forecast energy 
            demand and provide optimization recommendations.""",
            
            """<b>Energy Demand Forecast (Next 30 Days):</b>""",
            """This graph displays a 30-day forward-looking prediction of energy consumption. The blue line 
            represents historical actual consumption, while the green line with shaded confidence interval 
            shows the predicted values. The confidence band indicates the range within which actual consumption 
            is expected to fall with 85% probability.""",
            
            """<b>Key Insights:</b>""",
            """• Historical patterns show weekly cyclical behavior with weekday peaks""",
            """• Forecast accounts for seasonal variations and temperature correlations""",
            """• Confidence intervals help in capacity planning and resource allocation""",
            
            """<b>Peak Demand Prediction:</b>""",
            """The system predicts tomorrow's peak demand time (2:00 PM - 4:00 PM) with 85% confidence, 
            enabling proactive load management and cost optimization.""",
            
            """<b>Optimization Recommendations:</b>""",
            """• Shift 15% of load from peak hours (2-4 PM) to off-peak (10-12 PM)""",
            """• Increase solar utilization by 200 kWh during peak hours""",
            """• Deploy battery storage to reduce grid dependency""",
            """• Potential daily savings: ₹15,000""",
            
            """<b>Anomaly Detection:</b>""",
            """The bottom chart shows detected anomalies (marked with red X symbols) in consumption patterns. 
            These anomalies indicate unusual energy usage that may require investigation, such as equipment 
            malfunction, unauthorized usage, or system inefficiencies."""
        ],
        image_path="screenshot_predictions.png",
        caption="Figure 2: Predictive Analytics showing 30-day forecast, peak demand prediction, and anomaly detection"
    )
    
    pdf.story.append(PageBreak())
    
    # Section 3: Sustainability Metrics
    pdf.add_section(
        "3. Sustainability Metrics & Environmental Impact",
        [
            """This section provides comprehensive tracking of environmental impact and progress toward 
            sustainability goals.""",
            
            """<b>Carbon Emissions Trend:</b>""",
            """The red area chart displays daily carbon emissions (in kg CO₂) over the past year. The black 
            dashed line represents a 7-day moving average, smoothing out daily fluctuations to reveal the 
            underlying trend. The chart shows seasonal variations with higher emissions during summer months 
            due to increased cooling requirements.""",
            
            """<b>Key Metrics:</b>""",
            """• Total Carbon Emissions (Year): 2,165,336 kg CO₂""",
            """• Emissions Saved (Renewable): 710,771 kg CO₂""",
            """• Trees Needed: 103,111 trees to offset annual emissions""",
            
            """<b>Renewable Energy Progress:</b>""",
            """The blue line chart tracks monthly renewable energy percentage over time. The green dashed 
            line at 30% represents the target threshold. The chart demonstrates steady progress with 
            seasonal peaks during high solar generation months (March-August).""",
            
            """<b>Cost Savings from Renewables:</b>""",
            """The green bar chart shows monthly cost savings (in ₹) achieved through renewable energy 
            generation. Darker green indicates higher savings. Total annual savings exceed ₹6.5 million, 
            demonstrating the strong financial case for renewable investments.""",
            
            """<b>Environmental Impact Summary:</b>""",
            """Four key impact cards display:""",
            """• <b>Trees Saved:</b> 33,846 equivalent trees from renewable energy""",
            """• <b>Cars Off Road:</b> 154 equivalent cars removed annually""",
            """• <b>Homes Powered:</b> 86 homes powered by renewable energy""",
            """• <b>Money Saved:</b> ₹6,500,952 annual savings from renewables"""
        ],
        image_path="screenshot_sustainability.png",
        caption="Figure 3: Sustainability metrics showing carbon emissions, renewable progress, and environmental impact"
    )
    
    pdf.story.append(PageBreak())
    
    # Section 4: Long-term Solutions
    pdf.add_section(
        "4. Long-term Energy Sustainability Solutions",
        [
            """The Solutions section provides a comprehensive roadmap for achieving carbon neutrality by 2030, 
            with detailed plans across five key areas.""",
            
            """<b>Renewable Energy Expansion Plan:</b>""",
            
            """<b>Solar Energy Solutions:</b>""",
            """• Rooftop Solar Expansion: 500 kW → 2,000 kW (4x increase)""",
            """  - Investment: ₹10 Crores""",
            """  - Annual Generation: ~3,000,000 kWh""",
            """  - Payback Period: 5-6 years""",
            """• Solar Carports: 300 kW capacity (₹1.5 Crores)""",
            """• Building-Integrated Photovoltaics: 200 kW estimated capacity""",
            
            """<b>Wind & Hybrid Solutions:</b>""",
            """• Small Wind Turbines: 5-10 units (10 kW each)""",
            """• Solar-Wind Hybrid System for better grid stability""",
            """• Biomass Energy: 50 kW biogas plant for cafeteria waste""",
            
            """<b>Renewable Energy Growth Projection:</b>""",
            """The line chart shows three scenarios (Conservative, Moderate, Aggressive) for renewable energy 
            adoption from 2026 to 2030. The moderate scenario projects 85% renewable energy by 2030, while 
            the aggressive scenario achieves 100% carbon neutrality. The green dashed line marks the 100% 
            renewable target.""",
            
            """<b>Energy Efficiency Initiatives:</b>""",
            """• LED Conversion (100%): 60-70% energy savings, ₹2 Cr investment""",
            """• HVAC Optimization with VFDs: 20-30% savings, ₹1.5 Cr investment""",
            """• Building Insulation: 25% cooling load reduction, ₹3 Cr investment""",
            """• Smart Lighting Controls: Additional 30% savings with motion sensors""",
            
            """<b>Infrastructure Modernization:</b>""",
            """• Battery Energy Storage System (BESS): 2 MWh capacity, ₹8 Crores""",
            """• EV Charging Infrastructure: 50 solar-powered charging points""",
            """• Campus Microgrid: Grid-independent operation, ₹15 Crores""",
            """• Electric Campus Shuttle: 10 electric buses, ₹5 Crores"""
        ],
        image_path="screenshot_solutions.png",
        caption="Figure 4: Long-term sustainability solutions showing renewable energy roadmap and growth projections"
    )
    
    pdf.story.append(PageBreak())
    
    # Section 5: Key Features
    pdf.add_section(
        "5. Key Features & Benefits",
        [
            """<b>Dashboard Features:</b>""",
            """• <b>5 Comprehensive Pages:</b> Overview, Analytics, Sustainability, Solutions, Predictions""",
            """• <b>13 Facilities Monitored:</b> Academic blocks, hostels, cafeteria, sports complex, etc.""",
            """• <b>Real-time Data:</b> 9,360 hourly data points + 365 daily records""",
            """• <b>Interactive Visualizations:</b> 20+ charts with Plotly integration""",
            """• <b>Professional Design:</b> Modern UI with gradient backgrounds and animations""",
            
            """<b>Financial Benefits:</b>""",
            """• Total Investment: ₹60 Crores (5-year plan)""",
            """• Annual Savings (Year 5): ₹12 Crores""",
            """• Payback Period: 5.2 years""",
            """• 10-Year Net Savings: ₹27 Crores""",
            """• Energy Cost Reduction: 65%""",
            
            """<b>Environmental Benefits:</b>""",
            """• CO₂ Reduction: 3,500 tons/year by 2030""",
            """• Renewable Energy: 85% by 2030""",
            """• Water Savings: 50 million liters/year""",
            """• Waste Reduction: 200 tons/year through biomass""",
            
            """<b>Technical Capabilities:</b>""",
            """• AI-powered demand forecasting""",
            """• Automated anomaly detection""",
            """• Peak demand prediction with 85% confidence""",
            """• Multi-scenario planning (Conservative, Moderate, Aggressive)""",
            """• Comprehensive ROI analysis with 10-year projections"""
        ]
    )
    
    # Section 6: Conclusion
    pdf.add_section(
        "6. Conclusion",
        [
            """The VIT Campus Energy Management Dashboard represents a comprehensive solution for monitoring, 
            analyzing, and optimizing energy consumption across the campus. With its combination of real-time 
            monitoring, predictive analytics, and long-term sustainability planning, the dashboard provides 
            all the tools necessary to achieve carbon neutrality by 2030.""",
            
            """<b>Key Achievements:</b>""",
            """• Professional, enterprise-grade dashboard with modern design""",
            """• Comprehensive data coverage across all campus facilities""",
            """• Detailed roadmap with ₹60 Crore investment plan""",
            """• Strong financial justification with 5.2-year payback""",
            """• Clear path to 85-100% renewable energy by 2030""",
            
            """<b>Next Steps:</b>""",
            """1. Integration with real-time smart meter data""",
            """2. Implementation of Phase 1 initiatives (LED, Solar 500kW, Smart Meters)""",
            """3. Deployment of IoT sensors for granular monitoring""",
            """4. Development of mobile application for stakeholder access""",
            """5. Regular reporting and progress tracking against targets""",
            
            """<b>Impact:</b>""",
            """This dashboard not only provides visibility into current energy consumption but also serves 
            as a strategic planning tool for VIT's journey toward sustainability. By combining data-driven 
            insights with actionable recommendations, it empowers decision-makers to make informed choices 
            that balance environmental responsibility with financial prudence.""",
            
            """The commitment to carbon neutrality by 2030 is not just an aspiration—it's a well-planned, 
            financially viable, and technically achievable goal supported by this comprehensive energy 
            management system."""
        ]
    )
    
    # Generate the PDF
    pdf.generate()


if __name__ == "__main__":
    create_dashboard_documentation()
    print("\n✅ PDF documentation created successfully!")
    print("📄 File: VIT_Energy_Dashboard_Documentation.pdf")
