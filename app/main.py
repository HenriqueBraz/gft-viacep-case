from pathlib import Path
from app.extract.extractor import extract_ceps
from app.transform.transformer import transform_ceps
from app.load.database import init_db, insert_addresses
from app.load.json_writer import write_json
from app.load.xml_writer import write_xml
from app.load.error_writer import write_errors
from app.scripts.generate_ceps import generate_ceps_csv


DATA_PATH = "data/ceps.csv"
DB_PATH = "data/addresses.db"
OUTPUT_JSON = "data/addresses.json"
OUTPUT_XML = "data/addresses.xml"
ERRORS_CSV = "data/errors.csv"


def main() -> None:

    print("Starting app...")
    Path("data").mkdir(parents=True, exist_ok=True)
    csv_path = Path("data/ceps.csv")
    if not csv_path.exists():
        print("Postal code file not found. Generating automatically...")
        generate_ceps_csv(csv_path)

    # Extract
    valid_ceps, invalid_ceps = extract_ceps(DATA_PATH)

    # Transform
    addresses, transform_errors = transform_ceps(valid_ceps)
    all_errors = invalid_ceps + transform_errors

    # Load
    init_db(DB_PATH)
    insert_addresses(DB_PATH, addresses)
    write_json(OUTPUT_JSON, addresses)
    write_xml(OUTPUT_XML, addresses)
    write_errors(ERRORS_CSV, all_errors)
    print("Finished app.")


if __name__ == "__main__":
    main()
