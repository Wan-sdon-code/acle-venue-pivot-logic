# ⚽ Project: ACLE 2026 - Jeddah Model
# Logic: 2 Stadiums + 1-Leg Blitz = 61% Stress Increase

def calculate_bdi_reality():
    stadiums = 2
    games = 11
    days = 13
    
    # BDI = Games per Stadium per Day
    bdi_score = (games / stadiums) / days
    
    # Comparison to Bangkok (0.2593)
    increase = ((bdi_score - 0.2593) / 0.2593) * 100
    
    print("--- JEDDAH PLAN (REALITY) ---")
    print(f"Stadiums: {stadiums}")
    print(f"Games: {games}")
    print(f"Busy Score (BDI): {bdi_score:.4f}")
    print(f"System Stress: {increase:.1f}% HIGHER than Bangkok.")
    print("Result: Grass will be ruined. System Overload.")

if __name__ == "__main__":
    calculate_bdi_reality()
