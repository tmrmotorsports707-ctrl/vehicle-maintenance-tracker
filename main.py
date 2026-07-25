import json
from pathlib import Path

DATA_FILE = Path("vehicles.json")


def load_vehicles() -> list[dict]:
    """Load vehicle records from the JSON data file."""
    if not DATA_FILE.exists():
        return []

    try:
        with DATA_FILE.open("r", encoding="utf-8") as file:
            return json.load(file)
    except (json.JSONDecodeError, OSError):
        print("Warning: Vehicle data could not be loaded.")
        return []


def save_vehicles(vehicles: list[dict]) -> None:
    """Save vehicle records to the JSON data file."""
    with DATA_FILE.open("w", encoding="utf-8") as file:
        json.dump(vehicles, file, indent=4)


def get_nonempty_input(prompt: str) -> str:
    """Request input until the user enters a nonempty value."""
    while True:
        value = input(prompt).strip()

        if value:
            return value

        print("This field cannot be empty.")


def get_integer_input(prompt: str) -> int:
    """Request a nonnegative integer from the user."""
    while True:
        value = input(prompt).strip()

        try:
            number = int(value)

            if number < 0:
                raise ValueError

            return number
        except ValueError:
            print("Please enter a valid nonnegative whole number.")


def add_vehicle(vehicles: list[dict]) -> None:
    """Create and store a new vehicle record."""
    vehicle = {
        "year": get_integer_input("Vehicle year: "),
        "make": get_nonempty_input("Make: "),
        "model": get_nonempty_input("Model: "),
        "mileage": get_integer_input("Current mileage: "),
        "service_history": [],
    }

    vehicles.append(vehicle)
    save_vehicles(vehicles)

    print(
        f"\nAdded {vehicle['year']} "
        f"{vehicle['make']} {vehicle['model']}."
    )


def view_vehicles(vehicles: list[dict]) -> None:
    """Display all saved vehicles."""
    if not vehicles:
        print("\nNo vehicles have been added.")
        return

    print("\nSaved Vehicles")
    print("-" * 50)

    for index, vehicle in enumerate(vehicles, start=1):
        print(
            f"{index}. {vehicle['year']} "
            f"{vehicle['make']} {vehicle['model']} "
            f"- {vehicle['mileage']:,} miles"
        )


def display_menu() -> None:
    """Display the main application menu."""
    print("\nVehicle Maintenance Tracker")
    print("1. Add vehicle")
    print("2. View vehicles")
    print("3. Exit")


def main() -> None:
    """Run the vehicle maintenance tracker."""
    vehicles = load_vehicles()

    while True:
        display_menu()
        choice = input("Choose an option: ").strip()

        if choice == "1":
            add_vehicle(vehicles)
        elif choice == "2":
            view_vehicles(vehicles)
        elif choice == "3":
            print("Vehicle data saved. Goodbye.")
            break
        else:
            print("Please select option 1, 2, or 3.")


if __name__ == "__main__":
    main()