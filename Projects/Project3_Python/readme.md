Shipment Tracking & Analytics CLI

A command-line tool for tracking shipment status and analyzing delivery performance, built with Python and pandas.

Features


Look up shipments by order ID
Flag delayed shipments beyond a configurable threshold
Analyze average delivery time by route (origin → destination)
Generate realistic sample data for testing, no external dataset required


Tech Stack


Python 3.10+
pandas
argparse (standard library)


Installation

bashgit clone <your-repo-url>
cd <repo-folder>
pip install -r requirements.txt

Usage

If no data file exists yet, the tool will automatically generate one on first run. You can also generate it manually:

bashpython shipment_tracker.py generate-sample-data --rows 75 --seed 42

Check the status of a specific shipment:

bashpython shipment_tracker.py status ORD1000

Order ID: ORD1000
Status: Delivered
Route: Bengaluru -> Lucknow
Weight (kg): 10.94
Shipment Date: 2026-02-02
Delivery Date: 2026-02-05
Delay Days: 1
Delivery Days: 3

View shipments delayed beyond a threshold:

bashpython shipment_tracker.py delayed --threshold 3

View average delivery time by route:

bashpython shipment_tracker.py route-average

Flag shipments delayed beyond X days:

bashpython shipment_tracker.py flag --days 5

Use a custom data file:

bashpython shipment_tracker.py --data path/to/your_data.csv status ORD1000

Data Format

The CLI expects a CSV with these columns (extra columns are ignored):

ColumnTypeRequiredorder_idstringYesstatusstringYesoriginstringYesdestinationstringYesweight_kgfloatYesshipment_datedateOptionaldelivery_datedateOptionaldelay_daysintOptional (defaults to 0)delivery_daysintOptional (derived from dates if missing)

Project Structure

.
├── shipment_tracker.py    # Main CLI application
├── shipment_data.csv      # Sample data (auto-generated, gitignored)
├── requirements.txt
└── README.md

Notes

This project was built to practice core data-handling patterns with pandas — loading and validating CSVs, cleaning/coercing types, groupby aggregations, and building a clean CLI interface with argparse — outside of a notebook environment.