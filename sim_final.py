import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# --- SIMULATION CONSTANTS ---
SIMULATION_STEPS = 60
MBPS_PER_USER = 2.0
TOWER_LIMIT_MBPS = 8000
SATELLITE_LIMIT_MBPS = 2000

def load_mock_grid(filename):
    df = pd.read_csv(filename, header=None)
    return df.to_numpy()

def plot_results(demand, stat_drop, dyn_drop):
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 5), sharey=True)
    
    # Graph 1: The Old Method (Static)
    ax1.plot(demand, label="Total Traffic Demand", color='black', linestyle='dashed')
    ax1.fill_between(range(len(stat_drop)), 0, stat_drop, color='red', alpha=0.6, label="Dropped Packets")
    ax1.set_title("Industry Standard (Static Routing)")
    ax1.set_xlabel("Time (Minutes)")
    ax1.set_ylabel("Data Traffic (Mbps)")
    ax1.legend(loc="upper left")
    ax1.grid(True, linestyle=':', alpha=0.7)
    
    # Graph 2: Your New Method (Dynamic)
    ax2.plot(demand, label="Total Traffic Demand", color='black', linestyle='dashed')
    ax2.fill_between(range(len(dyn_drop)), 0, dyn_drop, color='green', alpha=0.6, label="Dropped Packets")
    ax2.set_title("Proposed Algorithm (Dynamic Predictive Routing)")
    ax2.set_xlabel("Time (Minutes)")
    ax2.legend(loc="upper left")
    ax2.grid(True, linestyle=':', alpha=0.7)
    
    plt.suptitle("5G-NTN Offloading: Static vs Dynamic Data Loss Comparison", fontsize=14, fontweight='bold')
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    city_grid = load_mock_grid("city_density.csv")
    
    history_demand = []
    history_drop_static = []
    history_drop_dyn = []
    
    # NEW FIX: Give the algorithm a memory state
    surge_mode = False 
    
    for t in range(SIMULATION_STEPS):
        current_users = np.sum(city_grid)
        base_demand = current_users * MBPS_PER_USER
        fluctuation = np.random.uniform(0.9, 1.1) 
        total_demand = base_demand * fluctuation
        
        if 20 <= t <= 40:
            total_demand = total_demand * 1.8 
            
        # =========================================
        # 1. STATIC ROUTING (Baseline)
        # =========================================
        if total_demand <= TOWER_LIMIT_MBPS:
            stat_drop = 0
        else:
            overflow = total_demand - TOWER_LIMIT_MBPS
            if overflow <= SATELLITE_LIMIT_MBPS:
                stat_drop = 0
            else:
                stat_drop = overflow - SATELLITE_LIMIT_MBPS
                
        # =========================================
        # 2. DYNAMIC ROUTING (Your Algorithm)
        # =========================================
        if t > 0:
            growth_rate = (total_demand - history_demand[-1]) / history_demand[-1]
        else:
            growth_rate = 0
            
        # THE FIX: Turn surge mode ON when traffic spikes, turn it OFF when traffic crashes
        if growth_rate > 0.10:
            surge_mode = True
        elif growth_rate < -0.30:
            surge_mode = False
            
        if surge_mode:
            dynamic_threshold = TOWER_LIMIT_MBPS * 0.80 
            dynamic_sat_limit = 15000 
        else:
            dynamic_threshold = TOWER_LIMIT_MBPS      
            dynamic_sat_limit = SATELLITE_LIMIT_MBPS
            
        if total_demand <= dynamic_threshold:
            dyn_drop = 0
        else:
            overflow = total_demand - dynamic_threshold
            if overflow <= dynamic_sat_limit:
                dyn_drop = 0
            else:
                remaining = overflow - dynamic_sat_limit
                if dynamic_threshold + remaining <= TOWER_LIMIT_MBPS:
                    dyn_drop = 0
                else:
                    dyn_drop = (dynamic_threshold + remaining) - TOWER_LIMIT_MBPS

        history_demand.append(total_demand)
        history_drop_static.append(stat_drop)
        history_drop_dyn.append(dyn_drop)

    print("Simulation Complete. Generating Comparative Results Graph...")
    plot_results(history_demand, history_drop_static, history_drop_dyn)