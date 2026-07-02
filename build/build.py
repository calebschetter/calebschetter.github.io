from pathlib import Path
import subprocess
from utils import validate_directory

BUILD_DIR = Path(__file__).resolve().parent
PROJECT_ROOT = BUILD_DIR.parent
DATA_DIR = PROJECT_ROOT / "data"

INGREDIENTS_DIR = DATA_DIR / "ingredients"
DRINKS_DIR = DATA_DIR / "drinks"

INGREDIENT_SCHEMA = DATA_DIR / "schemas" / "ingredient.schema.json"
DRINK_SCHEMA = DATA_DIR / "schemas" / "drink.schema.json"

def validate() -> bool:
    valid = True

    print("Validating Ingredients...")
    status, errors = validate_directory(
        directory_path = INGREDIENTS_DIR,
        schema_path = INGREDIENT_SCHEMA,
    )
    if not status:
        valid = False
        print(errors)

    print("Validating Drinks...")
    status, errors = validate_directory(
        directory_path = DRINKS_DIR,
        schema_path = DRINK_SCHEMA,
    )
    if not status:
        valid = False
        print(errors)

    return valid

def main():
    valid = validate()
    if valid:
        print("Success")
    else:
        print("Fatal Error")
    

if __name__=="__main__":
    main()