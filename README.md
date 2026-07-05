# 📡 Dynamic 5G-NTN Traffic Offloading Simulator

![Python](https://img.shields.io/badge/Python-3.8%2B-blue)
![Matplotlib](https://img.shields.io/badge/Matplotlib-Data_Visualization-orange)
![Status](https://img.shields.io/badge/Status-Completed-success)

## 📌 Project Overview
This repository contains a time-step simulation environment and predictive routing algorithm designed to mitigate severe data packet loss in 5G terrestrial networks during extreme, localized traffic surges (e.g., major public events). 

Traditional 5G Non-Terrestrial Network (NTN) offloading policies utilize a static, reactive threshold that often results in bottleneck failures before Low Earth Orbit (LEO) satellite backhauls can absorb overflow. This project introduces a **Dynamic Predictive Routing Algorithm** that uses spatial user density modeling and temporal rate-of-change analysis to proactively allocate satellite bandwidth *before* absolute tower saturation occurs.

📄 **Read the full IEEE-formatted research paper:** [Dynamic_5G_NTN_Offloading_Algorithm.pdf]([./Dynamic_5G_NTN_Offloading_Algorithm.pdf](https://github.com/Blueflame777/5G-NTN-Offloading-Simulator/blob/main/Dynamic_5G_NTN_Offloading_Algorithm.pdf))

---

## 🚀 Key Features
* **Spatial Density Grid Generation:** Simulates realistic 5G User Equipment (UE) clusters using a randomized 10x10 geographical grid.
* **Stochastic Traffic Modeling:** Implements baseline user bandwidth requirements (2.0 Mbps) with randomized network jitter/fluctuation factors.
* **Rate-of-Change Predictive Logic:** Continuously monitors the growth rate ($G$) of data demand. If $G > 10\%$, the system proactively unlocks expanded satellite backhaul limits and reserves a 20% terrestrial emergency buffer.
* **Automated Comparative Visualization:** Generates side-by-side graphical analysis comparing industry-standard static routing against the proposed dynamic algorithm.

---

## 📊 Simulation Results

The simulation was executed over a 60-minute interval with an 80% localized traffic surge injected at $t=20$. 

* **Static Routing (Baseline):** Reached instantaneous hardware saturation, resulting in severe and sustained data packet loss.
* **Dynamic Routing (Proposed):** Successfully anticipated the demand trajectory, neutralizing the bottleneck and maintaining a near-zero packet loss environment.

* ![Simulation Results]([./surge_graph.png](https://github.com/Blueflame777/5G-NTN-Offloading-Simulator/blob/main/Figure_1.2.png))

---

## 💻 Installation & Usage

**1. Clone the repository:**
```bash
git clone [[https://github.com/B/5G-NTN-Offloading.git](https://github.com/Blueflame777/5G-NTN-Offloading-Simulator)]
cd 5G-NTN-Offloading
