<div align="center">

<img width="877" height="510" alt="image" src="https://github.com/user-attachments/assets/723ade04-6669-4533-8337-b88fb9811cec" />



# Q2 2026 WiFi Churn & Retention Radar

### End-to-End BI Project — Data Extraction → Cleaning → Power BI · Tableau · Looker Studio

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Databricks](https://img.shields.io/badge/Databricks-FF3621?style=for-the-badge&logo=databricks&logoColor=white)
![PySpark](https://img.shields.io/badge/PySpark-E25A1C?style=for-the-badge&logo=apachespark&logoColor=white)
![Power BI](https://img.shields.io/badge/Power%20BI-F2C811?style=for-the-badge&logo=powerbi&logoColor=black)
![Unity Catalog](https://img.shields.io/badge/Unity_Catalog-Databricks-red?style=for-the-badge)
![Delta Lake](https://img.shields.io/badge/Delta%20Lake-003366?style=for-the-badge&logo=delta&logoColor=white)
![SQL](https://img.shields.io/badge/SQL-4479A1?style=for-the-badge&logo=mysql&logoColor=white)
![DAX](https://img.shields.io/badge/DAX-KPI%20Measures-5E5E5E?style=for-the-badge)
![Data Modeling](https://img.shields.io/badge/Data%20Modeling-Relationships-2F855A?style=for-the-badge)
![Looker Studio](https://img.shields.io/badge/Looker%20Studio-4285F4?style=for-the-badge)
![GitHub](https://img.shields.io/badge/GitHub-181717?style=for-the-badge&logo=github&logoColor=white)



> A complete end-to-end analyst portfolio project built across three industry-standard BI platforms.
> Python (Data Extraction) →Raw data → Cleaning → Modeling → Power BI · Tableau · Looker Studio

</div>

---
## Live Demos

A single-page BI dashboard analyzing public WiFi subscriber behavior, churn risk, and revenue leakage for Q2 2026 — built in Power BI, Tableau, and Looker Studio from the same dataset.



| Platform | Link |
|---|---|
| Power BI | See `/Dashboard` folder (`.pbix` file) |
| Tableau Public | [Q2 2026 WiFi Churn & Retention Radar](https://public.tableau.com/app/profile/ajit.jha/viz/Q22026WiFiChurnRetentionRadar/Dashboard1?publish=yes) |
| Looker Studio | [Live Report](https://datastudio.google.com/s/uJ7jL8B3D8w) |
| GitHub Repo | [Ajitjha3095/Q2-2026-WiFi-Churn-Retention-Radar](https://github.com/Ajitjha3095/Q2-2026-WiFi-Churn-Retention-Radar) |





## 📑 Table of Contents

- [Project Overview](#project-overview)
- [Business Problem](#business-problem)
- [Business Requirements](#business-requirements)
- [Dataset](#dataset)
- [KPIs & Calculations](#kpis--calculations)
   - [DAX (Power BI)](#dax-power-bi)
   - [Tableau (Calculated Fields)](#tableau-calculated-fields)
   - [Looker Studio (Calculated Fields)](#looker-studio-calculated-fields)
- [Dashboard Layout](#dashboard-layout)
- [Key Insights](#key-insights)
- [Tech Stack](#tech-stack)
- [Skills Demonstrated](#skills-demonstrated)
  - [Data Analytics](#data-analytics)
  - [Data Modeling](#data-modeling)
  - [Business Intelligence](#business-intelligence)
  - [Analytical Skills](#analytical-skills)
- [Repository Structure](#repository-structure)
- [How to Run](#how-to-run)
- [Author](#author)
- [License](#license)

---

##  Project Overview
This project demonstrates an end-to-end data analytics and business intelligence workflow using Python and modern visualization tools.The pipeline extracts WiFi service data using Python, performs data cleaning and transformation, prepares an analytics-ready dataset, and delivers interactive dashboards using Google Looker Studio, Tableau, and Power BI.The project showcases practical data analytics concepts including data extraction, data cleansing, data transformation, data modeling, and business intelligence reporting to analyze customer activity, churn, revenue leakage, and service performance.

##  Business Problem
A public WiFi network operator offers tiered subscription plans (Free, Basic, Premium, Family, Business) across multiple physical hotspot locations (cafes, coworking spaces, transit hubs). Leadership needed visibility into:

- How many subscribers are active vs. churning, and where churn is concentrated
- Which authentication methods and device types correlate with higher support-ticket volume
- How much monthly recurring revenue (MRR) is at risk from churned/inactive users
- Which locations and plans are underperforming, to prioritize retention efforts

This dashboard was built to answer those questions in a single view, for both technical stakeholders and non-technical management.

## Business Requirements

|  | Requirement |
|---|---|
| 1 | Single-page dashboard — no scrolling, no secondary pages |
| 2 | Must be understandable by non-technical management in under 30 seconds |
| 3 | Highlight at-risk metrics (churn, negative feedback) visually, not just numerically |
| 4 | Break down churn and revenue by Location, Device Type, Auth Method, and Subscription Plan |
| 5 | Support filtering by Plan, Device Type, and Package without page reload |
| 6 | Reporting period: Q2 2026 |
| 7 | Rebuildable across multiple BI tools (Power BI, Tableau, Looker Studio) for portfolio/cross-platform demonstration |

---
## Dataset

**Source file:** `wifi_user_enhanced_data.csv`

| Column | Description |
|---|---|
| `User_ID` | Unique subscriber identifier |
| `Device_Type` | Smartphone, Laptop, Tablet, Smart TV, IoT Device |
| `Location` | Physical hotspot location |
| `Auth_Method` | WPA2-Enterprise, Captive Portal, Social Login, OTP Verification |
| `Subscription_Plan` | Free, Basic, Premium, Family, Business |
| `Subscription_Price` | Monthly price in USD |
| `Tickets_Raised` | Number of support tickets raised by the user |
| `Previous_Feedback` | Awesome, Good, Average, Poor, Leave to other provider |
| `Active_Status` | Active / Inactive |

Raw and cleaned data live in `/DataSet`. Data preparation scripts live in `/Python File`.

---

## KPIs & Calculations

| KPI | Logic |
|---|---|
| **Active Users** | Count of users where `Active_Status = Active` |
| **Churn Rate %** | Inactive users ÷ Total users |
| **Billing Now (MRR)** | Sum of `Subscription_Price` for active users only |
| **Issue Volume** | Average `Tickets_Raised` across all users |
| **Negative Feedback %** | Users with feedback = "Poor" or "Leave to other provider" ÷ Total users |
| **Revenue Leakage** | Revenue lost from inactive/churned users vs. total potential revenue |

### DAX (Power BI)

```dax
Active Users = 
CALCULATE(COUNTROWS('wifi_user_enhanced_data csv'), 'wifi_user_enhanced_data csv'[Active_Status] = "Active")

Churn % = 
DIVIDE(
    CALCULATE(COUNTROWS('wifi_user_enhanced_data csv'), 'wifi_user_enhanced_data csv'[Active_Status] = "Inactive"),
    COUNTROWS('wifi_user_enhanced_data csv')
)

MRR = SUM ('wifi_user_enhanced_data csv'[Subscription_Price])

Avg Tickets = AVERAGE('wifi_user_enhanced_data csv'[Tickets_Raised])

Negative Feedback % = 
DIVIDE(
    CALCULATE(
        COUNTROWS('wifi_user_enhanced_data csv'),
        'wifi_user_enhanced_data csv'[Previous_Feedback] IN {"Poor", "Leave to other provider"}
    ),
    COUNTROWS('wifi_user_enhanced_data csv')
)
```

### Tableau (Calculated Fields)

```
Active Users        : IF [Active Status] = "Active" THEN 1 ELSE 0 END
Churn %              : SUM(IF [Active Status] = "Inactive" THEN 1 ELSE 0 END) / COUNTD([User ID])
MRR                  : SUM([Subscription Price])
Negative Feedback %  : SUM(IF [Previous Feedback] = "Poor" OR [Previous Feedback] = "Leave to other provider" THEN 1 ELSE 0 END) / COUNTD([User ID])
```

### Looker Studio (Calculated Fields)

```
Active Users        : CASE WHEN Active_Status = "Active" THEN 1 ELSE 0 END
Churn %              : SUM(CASE WHEN Active_Status = "Inactive" THEN 1 ELSE 0 END) / COUNT(User_ID)
MRR                  : SUM(Subscription_Price)
Negative Feedback %  : SUM(CASE WHEN Previous_Feedback IN ("Poor","Leave to other provider") THEN 1 ELSE 0 END) / COUNT(User_ID)
```

---
## Dashboard Layout

- **Header** — Title + Plan / Device Type / Package slicers
- **KPI Row** — 5 cards: Active Users, Churn Rate, Billing Now, Issue Volume, Negative Feedback (risk KPIs highlighted in red)
- **Revenue by Plan** — Donut chart, sequential blue scale
- **Revenue Leakage** — Donut chart, revenue lost highlighted in red/coral
- **Active vs Inactive by Device Type** — Stacked bar chart
- **Total Users by Feedback** — Horizontal bar chart, sorted descending
- **Matrix of Churn** — Location-level breakdown: Active Users, Churn %, Avg Tickets, Total Revenue, Inactive Users, Revenue Lost

---

## Key Insights

- Overall churn rate stands at **29.10%**, with **Innovation Park Gate** and **Metro Station Exit** showing the highest churn among all locations.
- **Revenue leakage is significant** — roughly **18%** of total potential revenue is lost to inactive/churned subscribers.
- **Captive Portal** authentication correlates with the highest average support tickets, suggesting onboarding friction is a churn driver.
- Negative feedback (**28.5%**) closely tracks the churn rate, reinforcing that support experience directly impacts retention.

---
## Tech Stack

- **BI Tools:** Power BI, Tableau Public, Looker Studio
- **Data Prep:** Python (Pandas)
- **Data Format:** CSV
- **Version Control:** GitHub

## Skills Demonstrated

### Data Analytics
- Python
- Data Extraction
- Data Cleaning
- Data Transformation
- Data Validation
- Data Preparation

### Data Modeling
- Data Modeling
- KPI Development
- Business Metrics Design
- Calculated Fields
- Data Relationships

### Business Intelligence
- Power BI
- DAX
- Tableau
- Tableau Calculated Fields
- Google Looker Studio
- Looker Studio Calculated Fields
- Interactive Dashboard Development
- Data Visualization
- Data Storytelling

### Analytical Skills
- Customer Churn Analysis
- Revenue Loss Analysis
- Customer Retention Analysis
- User Behavior Analysis
- Performance Monitoring
- Dashboard Design

## Repository Structure

```

WiFi Churn & Retention Radar Analytics/
│
├── Dataset/                  # Dataset
│   └── wifi_user_enhanced_data.csv      # Wifi dataset
│
├── Python File/                  
│   └── Data_Collections.py        # data extraction, data cleaning, and loading
│
├── dashboards/                 # Business Intelligence Dashboards
│   ├── powerbi/                # Power BI project files
│   └── tableau/                # Tableau workbook files
│
├── images/                     # Dashboard previews and documentation assets
│   ├── powerbi.png             # Power BI dashboard screenshot
│   ├── tableau.png             # Tableau dashboard screenshot
│   └── looker.png              # Looker Studio dashboard screenshot
│
├── LICENSE                     # Project license
└── README.md                   # Project documentation
```

## How to Run

### 1. Clone the Repository

```bash
git clone https://github.com/Ajitjha3095/Q2-2026-WiFi-Churn-Retention-Radar.git
cd your-repository
```

### 2. Open the Dataset

The dataset is located in the `Dataset/` folder.

### 3. Open the Dashboard

Choose your preferred BI tool:

- **Power BI:** Open the `.pbix` file using Power BI Desktop.
- **Tableau:** Open the `.twb` or `.twbx` file using Tableau Desktop/Public.
- **Looker Studio:** Connect the dataset to Google Looker Studio and import the calculated fields if required.

### 4. Explore the Dashboard

Use the available filters and slicers to analyze:

- Customer Activity
- Customer Churn
- Revenue Loss
- Feedback Analysis
- Location Performance
- Device Usage

## Author

**Ajit Jha**  
*Data Analytics & Data Engineering Portfolio Project*

- **GitHub:** [Ajitjha3095](https://github.com/Ajitjha3095)
- **LinkedIn:** [Ajit Jha](https://www.linkedin.com/in/ajitjha01/)

---

## License

This project is licensed under the **MIT License**.  
See the [LICENSE](LICENSE) file for details.
