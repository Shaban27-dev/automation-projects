from weather import weather_workflow
from stock import stock_workflow
from utils import log_error


def main():
    try:
        options = {
            "1": weather_workflow,
            "2": stock_workflow
        }

        print("1. Weather Alert")
        print("2. Stock Alert")

        choice = input("Choose (1/2): ").strip()

        action = options.get(choice)

        if not action:
            raise ValueError("Invalid choice")

        action()

    except Exception as e:
        log_error(e)
        print(f"❌ Error: {e}")


if __name__ == "__main__":
    main()