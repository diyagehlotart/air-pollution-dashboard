# 🌿 Airwise — Air Pollution Analytics Dashboard

An interactive air-quality dashboard built with **Python, Streamlit, Pandas, and Plotly** to explore air pollution patterns across Indian cities using a simulated dataset.

<p align="center">
  <a href="https://air-pollution-dashboard-xcaobqnazr2fb3yr3eurs8.streamlit.app/">
    <strong>🚀 View Live Dashboard</strong>
  </a>
  &nbsp; | &nbsp;
  <a href="https://github.com/diyagehlotart/air-pollution-dashboard">
    <strong>💻 View Source Code</strong>
  </a>
</p>

---

## 📌 About the Project

**Airwise** is a data visualization project designed to make air-quality information easier to explore and understand.

The dashboard presents key air-quality indicators, compares average AQI across cities, visualizes AQI category distributions, and allows users to filter readings interactively.

The project demonstrates practical skills in data handling, interactive visualization, dashboard design, and Python application deployment.

## ✨ Features

- **KPI Cards:** View average AQI, peak AQI, total readings, and city coverage.
- **City Comparison:** Compare average AQI across selected cities using an interactive bar chart.
- **AQI Category Analysis:** Explore the distribution of air-quality categories with a pie chart.
- **Monitoring Station Analysis:** View station-type distribution using a donut chart.
- **Interactive Filters:** Filter the dashboard by city, year, and AQI category.
- **Data Preview:** Inspect up to 100 rows of the filtered dataset.
- **CSV Upload:** Load a compatible air-pollution dataset through the dashboard.
- **Responsive Layout:** Explore the dashboard through a clean, visually organized interface.

## 🛠️ Tech Stack

| Technology | Purpose |
|---|---|
| Python | Core programming language |
| Pandas | Data loading and analysis |
| Streamlit | Interactive dashboard interface |
| Plotly Express | Interactive charts and visualizations |
| CSV | Dataset storage |
| Git & GitHub | Version control and project hosting |
| Streamlit Community Cloud | Dashboard deployment |

## 📊 Dataset

The project uses a **simulated dataset containing approximately 50,000 records** for dashboard development and practice.

The dataset includes fields such as:

- Date and year
- City and state
- Monitoring station type
- Temperature, humidity, and wind speed
- PM2.5 and PM10
- NO₂, SO₂, CO, and O₃
- AQI and AQI category

**Important:** The dataset is simulated and is intended for educational and demonstration purposes. It is not official monitoring data, and its AQI values should not be used for health decisions, regulatory reporting, or real-world pollution assessments.

## 🚀 Run Locally

### 1. Clone the repository

```bash
git clone https://github.com/diyagehlotart/air-pollution-dashboard.git
```

### 2. Open the project folder

```bash
cd air-pollution-dashboard
```

### 3. Create a virtual environment (recommended)

```bash
python -m venv .venv
```

Activate it on Windows:

```bash
.venv\Scripts\activate
```

### 4. Install the dependencies

```bash
pip install -r requirements.txt
```

### 5. Run the dashboard

```bash
python -m streamlit run air_pollution_dashboard_app.py
```

Streamlit will provide a local URL in the terminal. Open that URL in your browser to use the dashboard.

### 📁 Project Structure

```text
air-pollution-dashboard/
├── air_pollution_dashboard_app.py
├── air_pollution_dashboard_50000_rows.csv
├── requirements.txt
└── README.md
```

## 🔍 How to Use

1. Open the [live dashboard](https://air-pollution-dashboard-xcaobqnazr2fb3yr3eurs8.streamlit.app/).
2. Explore the KPI cards for a quick overview of the selected readings.
3. Use the city, year, and AQI category filters to narrow the analysis.
4. Compare cities and explore the chart distributions.
5. Expand the data preview to inspect filtered records.
6. Upload a compatible CSV file to explore another dataset.

## 🎯 Project Goals

- Practice exploratory data analysis and data visualization.
- Build a user-friendly dashboard with interactive filters.
- Present key indicators through charts and KPI cards.
- Learn how to deploy a Python application online.
- Demonstrate an end-to-end data dashboard project.

## 🔮 Future Improvements

- Integrate verified air-quality datasets from reliable sources.
- Add time-series analysis of AQI trends.
- Include geographical visualizations and city-level maps.
- Add date-range filtering and downloadable filtered data.
- Improve data validation and provide clearer data-source documentation.

## 👩‍💻 Author

**Diya Gehlot**

Computer Science & Design Student | Web Development Enthusiast

- GitHub: [@diyagehlotart](https://github.com/diyagehlotart)
- Project Repository: [Air Pollution Dashboard](https://github.com/diyagehlotart/air-pollution-dashboard)
- Live Demo: [Airwise Dashboard](https://air-pollution-dashboard-xcaobqnazr2fb3yr3eurs8.streamlit.app/)

---

*Built as an educational project to explore data analytics, visualization, and interactive dashboard development.*
