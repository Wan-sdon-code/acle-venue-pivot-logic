# ⚽ Project: ACLE 2026 - Bangkok Model
# Logic: 3 Stadiums + 2-Leg Games = Low Stress

def calculate_bdi():
    stadiums = 3
    games = 7
    days = 9
    
    # BDI = Games per Stadium per Day
    bdi_score = (games / stadiums) / days
    
    print("--- BANGKOK PLAN (INITIAL GUESS) ---")
    print(f"Stadiums: {stadiums}")
    print(f"Games: {games}")
    print(f"Busy Score (BDI): {bdi_score:.4f}")
    print("Result: Grass has time to rest. System is Stable.")

if __name__ == "__main__":
    calculate_bdi()
