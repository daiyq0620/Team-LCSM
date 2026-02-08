# Team-LCSM: Access to Care

## Overview

This project analyzes the **National Health Interview Survey (NHIS) – Adult Summary Health Statistics** dataset to identify population subgroups most vulnerable to barriers in healthcare access.

We apply **two complementary modeling approaches**—a vulnerability-metric–based model and a full-variable clustering model—to capture both **upstream structural vulnerability** and **current, lived vulnerability**. The goal is to understand *who is most at risk of falling through the cracks* and *why*.

---

## Dataset

### Source
- NHIS Adult Summary Health Statistics (CDC)

### Data Files

- **Access_to_Care_Dataset.csv**  
  Primary dataset containing all cleaned NHIS records used for modeling.

- **base_trends_clean.csv**  
  Pre-processed baseline trends used for time-series and trend comparisons.

- **filtered_data.csv**  
  Subset of the dataset filtered by analysis-specific criteria (e.g., excluding totals).

- **subgroup_summary.csv**  
  Aggregated subgroup-level statistics used for vulnerability scoring and ranking.
---

## Visualization
`Access to Care Dashboard.twb`

---

## Notebooks

### `ModelFullVariable.ipynb`
**Full-Variable Categorization & Clustering**

- Categorizes all available variables into 5 categories
- Applies unsupervised clustering to identify groups with compound risk profiles
- Captures vulnerability emerging from all interacting factors

---

### `ModelVulnerable.ipynb`
**Vulnerability-Metric Modeling**

- Focuses on theory-driven vulnerability dimensions:
  - Barrier: whether individuals are unable to obtain timely or adequate care.
  - Persistence: ongoing or unstable health and care challenges.
  - Spillover: consequences beyond healthcare.
- Designed to identify systematically underserved populations

> The two notebooks differ primarily in **feature engineering strategy**, not modeling technique.

---

## Key Methodology

### 1. Data Preparation
- Removed aggregate “Total” rows and "Age groups with 75 years and older" as they conflict with other subgroups definition

### 2. Feature Engineering
- ModelFullVariable: Categorizes all available variables into 5 categories
- ModelVulnerable: Focuses on 3 vulnerability dimensions

### 3. Scaling
- Standardized all features using `StandardScaler` to ensure comparability across metrics

### 4. Clustering
- Applied **KMeans clustering**
- Selected **k = 5** using the elbow method

### 5. Identifying the Most Vulnerable Cluster
- Ranked clusters for each vulnerability dimension (higher = worse)
- Summed ranks across dimensions
- Identified the cluster with the **lowest total rank score** as the most vulnerable

### 6. Subgroup Risk Scoring
- Computed a composite **risk score** for each subgroup as the mean of vulnerability metrics
- Within the most vulnerable cluster:
  - Ranked each `GROUP × SUBGROUP` pair by risk score
  - Identified the highest-risk subgroup per category


---

## Team

Team LCSM  
Datathon / Applied Health Analytics Project
