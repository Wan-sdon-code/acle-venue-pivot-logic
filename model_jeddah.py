from datetime import datetime

def run_acle_logistics_audit():
    # ---------------------------------------------------------
    # 1. THE TRIP CONSTANT
    # ---------------------------------------------------------
    # Your planned trip to Bangkok
    trip_start = datetime(2026, 4, 26)
    trip_end = datetime(2026, 5, 1)

    # ---------------------------------------------------------
    # 2. SCENARIO A: THE "INITIAL RESEARCH" (Bangkok Hub)
    # ---------------------------------------------------------
    # Assumption: Spread out format, 7 matches, 9 days, 3 stadiums
    bkk_matches = 7
    bkk_days = 9
    bkk_stadiums = 3
    
    # Formula: Matches / (Days * Stadiums)
    bkk_bdi = bkk_matches / (bkk_days * bkk_stadiums)

    # ---------------------------------------------------------
    # 3. SCENARIO B: THE "OFFICIAL REALITY" (Jeddah Hub)
    # ---------------------------------------------------------
    # Reality: Single-leg blitz, 11 matches, 13 days, 2 stadiums
    jed_matches = 11
    jed_days = 13
    jed_stadiums = 2
    official_final_date = datetime(2026, 4, 25)
    
    jed_bdi = jed_matches / (jed_days * jed_stadiums)

    # ---------------------------------------------------------
    # 4. GENERATING THE "VAR" REPORT
    # ---------------------------------------------------------
    print(f"\n{'⚽ ACLE 2026: LOGISTICS RESEARCH AUDIT':^50}")
    print("=" * 50)
    print(f"TRIP DESTINATION: Bangkok, Thailand")
    print(f"TRIP WINDOW:      {trip_start.strftime('%d %b')} - {trip_end.strftime('%d %b')}")
    print("-" * 50)

    # Date & Location Validation (The "VAR Check")
    print("LOGISTICS VALIDATION:")
    if trip_start > official_final_date:
        days_late = (trip_start - official_final_date).days
        print(f"  [!] Result: ❌ MISSED THE ACTION")
        print(f"  [!] Reason: Final whistle is on {official_final_date.strftime('%d %b')}.")
        print(f"  [!] Status: You arrive {days_late} day(s) after the tournament ends.")
    
    print(f"  [!] Venue:  ❌ Relocated to Jeddah, Saudi Arabia.")

    # Operational Load Comparison
    print("-" * 50)
    print("OPERATIONAL LOAD (Blitz Density Index):")
    print(f"  > Bangkok (Initial Thought): {bkk_bdi:.2f}")
    print(f"  > Jeddah (Official Reality): {jed_bdi:.2f}")
    
    # Calculate the percentage increase in pressure
    load_increase = ((jed_bdi - bkk_bdi) / bkk_bdi) * 100
    
    print(f"\nANALYST INSIGHT:")
    print(f"Moving to a single-leg format in Jeddah increased")
    print(f"stadium operational pressure by {load_increase:.1f}%.")
    print("Status: 🔴 CRITICAL LOAD (High pitch wear/logistics risk).")
    print("=" * 50)

if __name__ == "__main__":
    run_acle_logistics_audit()
