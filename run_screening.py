import clr
import os

# Load DWSIM Automation DLL
clr.AddReference(
    r"C:\Users\sofiya chavarekar\AppData\Local\DWSIM\DWSIM.Automation.dll"
)

from DWSIM.Automation import Automation

print("✅ DWSIM Automation loaded")

# Create automation object
sim = Automation()

# Full path to flowsheet
flowsheet_path = os.path.abspath("test.dwxmz")

# Load flowsheet
sim.LoadFlowsheet(flowsheet_path)
print("✅ Flowsheet loaded")

# Get flowsheet object (THIS IS THE KEY)
fs = sim.Flowsheet

# --- LIST MATERIAL STREAMS ---
print("\n📌 Available Material Streams:")
for name in fs.MaterialStreams.Keys:
    print(" -", name)

# --- ACCESS FEED STREAM ---
feed = fs.MaterialStreams["Feed"]

# Change Feed Temperature (Kelvin)
feed.Phases[0].Properties.temperature = 350.0
print("\n🔥 Feed temperature set to 350 K")

# Run simulation
fs.Run()
print("▶ Simulation executed")

# Access outlet stream (change name if different)
product = fs.MaterialStreams["Product"]

print(
    f"🌡 Outlet Temperature: "
    f"{product.Phases[0].Properties.temperature:.2f} K"
)
