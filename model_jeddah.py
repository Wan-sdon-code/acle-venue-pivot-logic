import time

def run_jeddah_model():
    print("⚽ STARTING: Jeddah Football Research (The Real Plan)...")
    time.sleep(1)

    # --- Data from the AFC Reality Check ---
    stadiums = 2
    total_matches = 11
    total_days = 13
    
    # Bangkok baseline for comparison
    bangkok_load_score = 0.259 

    print(f"\n📋 THE REALITY STATS:")
    print(f"- Total Stadiums: {stadiums}")
    print(f"- Total Matches: {total_matches}")
    print(f"- Time Period: {total_days} Days")
    time.sleep(1)

    # --- Calculations ---
    # Matches per stadium
    load_per_stadium = total_matches / stadiums
    
    # Matches per day per stadium (The Busy Score)
    jeddah_load_score = (total_matches / total_days) / stadiums
    
    # Calculating the increase in congestion
    increase = ((jeddah_load_score - bangkok_load_score) / bangkok_load_score) * 100

    # --- The Result ---
    print("\n📊 THE ANALYSIS:")
    print(f"❌ Stadium Load: {load_per_stadium:.2f} matches per stadium.")
    print(f"❌ Busy Score: {jeddah_load_score:.3f} matches per day per stadium.")
    print(f"⚠️ Result: This is a {increase:.0f}% increase in congestion!")

    print("\n💡 CONCLUSION: The pitch is in CRITICAL condition.")
    print("There is almost no time for the grass to recover between games.")
    print("--------------------------------------------------")

if __name__ == "__main__":
    run_jeddah_model()
