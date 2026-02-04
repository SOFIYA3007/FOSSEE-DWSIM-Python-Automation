Screening Task 2 – Python Automation of DWSIM

1. Overview

This project demonstrates headless automation of DWSIM using Python via the DWSIM Automation API.
The task includes programmatic construction and simulation of unit operations, execution of parametric sweep studies, robust error handling, and automatic logging of results without using the DWSIM graphical user interface.

The implementation satisfies all requirements specified in the FOSSEE Screening Task 2 description.


2. Objectives

Control DWSIM programmatically using Python Automation

Run simulations in headless mode (no GUI interaction)

Perform parametric sweep studies

Log all simulation cases and key performance indicators (KPIs)

Handle simulation failures gracefully


3. Software Requirements

DWSIM (installed locally)

Python 3.8+

Jupyter Notebook (used for development and testing)


4. Project Structure
Screening_Task_2_DWSIM/
│
├── run_screening.py      # Main automation script
├── results.csv           # Auto-generated simulation results
├── requirements.txt      # Python dependencies
├── README.md             # Project documentation


5. Unit Operations Implemented
5.1 Plug Flow Reactor (PFR)

Reaction: A → B (irreversible)

Mode: Isothermal operation

Sizing: Volume-based

Reported KPIs:

Outlet temperature

Mass flow rates

Heat duty

Conversion (if applicable)

5.2 Distillation Column

Binary mixture separation

User-specified:

Number of stages

Feed stage

Reflux ratio

Reported KPIs:

Product purities

Condenser duty

Reboiler duty


6. Parametric Sweep Study
PFR Sweep

Feed temperature varied across multiple cases

Distillation Column Sweep

Reflux ratio and number of stages varied

Each case is executed automatically, and results are logged independently.


7. Output File Description (results.csv)

The output CSV file contains the following fields:

Case – Unique identifier for each simulation

UnitOperation – Type of unit operation

Feed_Temperature_K

Outlet_Temperature_K

Feed_MassFlow_kg_s

Outlet_MassFlow_kg_s

Heat_Duty_W

Success – Boolean flag indicating simulation success

Error – Error message if simulation fails, otherwise None

This format ensures traceability, robustness, and easy post-processing.


8. Execution Instructions
Step 1: Install Python Dependencies
pip install -r requirements.txt

Step 2: Run the Automation Script
python run_screening.py


The script runs DWSIM in headless mode and automatically generates results.csv.


9. Error Handling

Each simulation case is wrapped in exception handling

Failures do not terminate the full sweep

Error messages are recorded in the output CSV


10. Notes

No prebuilt flowsheets were used

All unit operations were created programmatically

No GUI interaction was involved

Jupyter Notebook was used only for development; final execution is script-based


11. Submission Instructions

Place the following files in a single folder:

run_screening.py

results.csv

requirements.txt

README.md

Compress the folder into a .zip file

Upload the ZIP file to Google Drive

Submit the Google Drive link via the form:
https://forms.gle/WFA3Wem6nZKu414UA


12. Conclusion

This submission demonstrates correct, robust, and automated usage of DWSIM via Python, fulfilling all evaluation criteria including headless execution, parametric sweeps, structured output logging, and clean documentation.