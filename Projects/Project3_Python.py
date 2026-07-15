from __future__ import annotations

import argparse
import random
from dataclasses import dataclass
from datetime import datetime, timedelta
from pathlib import Path
from typing import Optional

import pandas as pd


DEFAULT_DATA_FILE = Path(__file__).with_name("shipment_data.csv")


@dataclass(frozen=True)
class Shipment:
	order_id: str
	status: str
	origin: str
	destination: str
	weight_kg: float
	shipment_date: datetime
	delivery_date: datetime
	delay_days: int
	delivery_days: int

	@property
	def route(self) -> str:
		return f"{self.origin} -> {self.destination}"


class ShipmentTracker:
	def __init__(self, csv_path: Path | str) -> None:
		self.csv_path = Path(csv_path)
		self.df = self._load_data()

	def _load_data(self) -> pd.DataFrame:
		if not self.csv_path.exists():
			raise FileNotFoundError(
				f"Shipment data file not found: {self.csv_path}. Generate it first or use the generate-sample-data command."
			)

		data = pd.read_csv(self.csv_path)
		required_columns = {"order_id", "status", "origin", "destination", "weight_kg"}
		missing_columns = required_columns - set(data.columns)
		if missing_columns:
			missing_list = ", ".join(sorted(missing_columns))
			raise ValueError(f"Missing required columns: {missing_list}")

		for column in ("shipment_date", "delivery_date"):
			if column in data.columns:
				data[column] = pd.to_datetime(data[column], errors="coerce")

		if "delivery_days" not in data.columns:
			if {"shipment_date", "delivery_date"}.issubset(data.columns):
				data["delivery_days"] = (data["delivery_date"] - data["shipment_date"]).dt.days
			else:
				data["delivery_days"] = pd.NA

		if "delay_days" not in data.columns:
			data["delay_days"] = 0

		data["delay_days"] = pd.to_numeric(data["delay_days"], errors="coerce").fillna(0).astype(int)
		data["delivery_days"] = pd.to_numeric(data["delivery_days"], errors="coerce")

		return data

	def get_by_id(self, order_id: str) -> Optional[Shipment]:
		matches = self.df.loc[self.df["order_id"].astype(str) == str(order_id)]
		if matches.empty:
			return None

		row = matches.iloc[0]
		return self._row_to_shipment(row)

	def get_delayed(self, threshold: int) -> pd.DataFrame:
		delayed = self.df.loc[self.df["delay_days"] > threshold].copy()
		return delayed.sort_values(by=["delay_days", "order_id"], ascending=[False, True])

	def flag_delayed_beyond(self, days: int) -> pd.DataFrame:
		return self.get_delayed(days)

	def average_delay_by_route(self) -> pd.DataFrame:
		route_frame = self.df.copy()
		route_frame["route"] = route_frame["origin"].astype(str) + " -> " + route_frame["destination"].astype(str)

		summary = (
			route_frame.groupby("route", as_index=False)
			.agg(
				shipments=("order_id", "count"),
				average_delivery_days=("delivery_days", "mean"),
				average_delay_days=("delay_days", "mean"),
			)
			.sort_values(by=["average_delivery_days", "shipments"], ascending=[False, False])
		)
		summary["average_delivery_days"] = summary["average_delivery_days"].round(2)
		summary["average_delay_days"] = summary["average_delay_days"].round(2)
		return summary

	def _row_to_shipment(self, row: pd.Series) -> Shipment:
		shipment_date = row.get("shipment_date")
		delivery_date = row.get("delivery_date")

		if pd.isna(shipment_date):
			shipment_date = datetime.min
		if pd.isna(delivery_date):
			delivery_date = datetime.min

		delivery_days = row.get("delivery_days")
		if pd.isna(delivery_days):
			delivery_days = 0

		return Shipment(
			order_id=str(row["order_id"]),
			status=str(row["status"]),
			origin=str(row["origin"]),
			destination=str(row["destination"]),
			weight_kg=float(row["weight_kg"]),
			shipment_date=pd.to_datetime(shipment_date).to_pydatetime(),
			delivery_date=pd.to_datetime(delivery_date).to_pydatetime(),
			delay_days=int(row["delay_days"]),
			delivery_days=int(delivery_days),
		)


def generate_sample_data(output_path: Path, rows: int = 75, seed: int = 42) -> Path:
	random.seed(seed)

	origins = ["Delhi", "Mumbai", "Bengaluru", "Chennai", "Hyderabad", "Pune", "Kolkata", "Ahmedabad"]
	destinations = ["Jaipur", "Lucknow", "Surat", "Indore", "Nagpur", "Bhopal", "Patna", "Kochi"]
	statuses = ["Delivered", "Delayed", "In Transit", "Out for Delivery", "Returned"]
	status_weights = [0.55, 0.2, 0.12, 0.08, 0.05]

	base_date = datetime(2026, 1, 1)
	records = []

	for index in range(rows):
		origin = random.choice(origins)
		destination = random.choice([place for place in destinations if place != origin])
		shipment_date = base_date + timedelta(days=random.randint(0, 120))
		delivery_days = random.randint(1, 12)
		delay_days = max(0, int(random.gauss(2, 2))) if random.random() < 0.4 else random.randint(0, 1)
		status = random.choices(statuses, weights=status_weights, k=1)[0]
		if status == "Delivered" and delay_days == 0 and random.random() < 0.25:
			delay_days = random.randint(1, 4)

		records.append(
			{
				"order_id": f"ORD{1000 + index:04d}",
				"status": status,
				"origin": origin,
				"destination": destination,
				"weight_kg": round(random.uniform(0.5, 28.0), 2),
				"shipment_date": shipment_date.date().isoformat(),
				"delivery_date": (shipment_date + timedelta(days=delivery_days + delay_days)).date().isoformat(),
				"delay_days": delay_days,
				"delivery_days": delivery_days + delay_days,
			}
		)

	sample_frame = pd.DataFrame.from_records(records)
	output_path.parent.mkdir(parents=True, exist_ok=True)
	sample_frame.to_csv(output_path, index=False)
	return output_path


def format_shipment(shipment: Shipment) -> str:
	return "\n".join(
		[
			f"Order ID: {shipment.order_id}",
			f"Status: {shipment.status}",
			f"Route: {shipment.route}",
			f"Weight (kg): {shipment.weight_kg:.2f}",
			f"Shipment Date: {shipment.shipment_date.date().isoformat()}",
			f"Delivery Date: {shipment.delivery_date.date().isoformat()}",
			f"Delay Days: {shipment.delay_days}",
			f"Delivery Days: {shipment.delivery_days}",
		]
	)


def print_dataframe(frame: pd.DataFrame, empty_message: str) -> None:
	if frame.empty:
		print(empty_message)
		return

	print(frame.to_string(index=False))


def build_parser() -> argparse.ArgumentParser:
	parser = argparse.ArgumentParser(
		description="Shipment Tracking & Analytics CLI built with pandas and Python fundamentals."
	)
	parser.add_argument(
		"--data",
		default=str(DEFAULT_DATA_FILE),
		help=f"Path to the shipment CSV file. Default: {DEFAULT_DATA_FILE.name}",
	)

	subparsers = parser.add_subparsers(dest="command", required=True)

	status_parser = subparsers.add_parser("status", help="Check the shipment status by order ID")
	status_parser.add_argument("order_id", help="Order ID to look up")

	delayed_parser = subparsers.add_parser("delayed", help="Show shipments delayed beyond a threshold")
	delayed_parser.add_argument("--threshold", type=int, default=3, help="Delay threshold in days")

	subparsers.add_parser("route-average", help="Show average delivery time by route")

	flag_parser = subparsers.add_parser("flag", help="Flag shipments delayed beyond X days")
	flag_parser.add_argument("--days", type=int, default=5, help="Delay threshold in days")

	sample_parser = subparsers.add_parser("generate-sample-data", help="Generate a realistic sample shipment CSV")
	sample_parser.add_argument("--rows", type=int, default=75, help="Number of rows to generate")
	sample_parser.add_argument("--seed", type=int, default=42, help="Random seed for repeatable data")
	sample_parser.add_argument(
		"--output",
		default=str(DEFAULT_DATA_FILE),
		help=f"Output CSV path. Default: {DEFAULT_DATA_FILE.name}",
	)

	return parser


def run_command(args: argparse.Namespace) -> None:
	if args.command == "generate-sample-data":
		output_path = generate_sample_data(Path(args.output), rows=args.rows, seed=args.seed)
		print(f"Sample data written to {output_path}")
		return

	data_path = Path(args.data)
	if not data_path.exists():
		print(f"No data file found at {data_path}. Generating sample data first.")
		generate_sample_data(data_path)

	tracker = ShipmentTracker(data_path)

	if args.command == "status":
		shipment = tracker.get_by_id(args.order_id)
		if shipment is None:
			print(f"Order ID {args.order_id} was not found.")
			return
		print(format_shipment(shipment))
		return

	if args.command == "delayed":
		delayed_shipments = tracker.get_delayed(args.threshold)
		print_dataframe(delayed_shipments, f"No shipments were delayed beyond {args.threshold} days.")
		return

	if args.command == "route-average":
		averages = tracker.average_delay_by_route()
		print_dataframe(averages, "No route data available.")
		return

	if args.command == "flag":
		flagged = tracker.flag_delayed_beyond(args.days)
		print_dataframe(flagged, f"No shipments were delayed beyond {args.days} days.")
		return

	raise ValueError(f"Unsupported command: {args.command}")


def main() -> None:
	parser = build_parser()
	args = parser.parse_args()
	run_command(args)


if __name__ == "__main__":
	main()
