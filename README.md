# Laundry Availability Checker

This is a simple Python script that allows you to check the availability of specific washers and dryers in a Circuit Laundry location using the FlashCashOnline API.

## Prerequisites

Before using this script, make sure you have the following:

1. Python installed on your system (Python 3.x recommended).
2. The `requests` library, which can be installed using `pip`:
   ```
   pip install requests
   ```

## Getting Started

1. Open the script in a text editor or integrated development environment (IDE).
2. You'll need to set your authentication token in the `AUTH` variable. Replace the empty string `""` with your actual authorization token.
3. Configure the `BASE_API` variable to match the API endpoint you want to access. The example provided is set to the FlashCashOnline API for retrieving machine information.
4. Update the `MACHINES` dictionary with the machine types and their corresponding IDs. You can add or remove machines as needed.

## Usage

1. Run the script by executing it. You can do this by opening your command prompt or terminal and navigating to the script's directory. Then, run:
   ```
   python Laundry.py
   ```
   
   The script will make API requests to check the availability of washers and dryers.

2. The script will display the availability of each machine in a user-friendly format. It will show whether a machine is available or when it is expected to become available.

## Functions

- `make_get_request(url, authorization)`: This function sends a GET request to the specified URL with an optional authorization token.

- `get_machine_availability(machine_type)`: This function checks the availability of machines of the given type and returns a list of availability statuses.

- `main()`: The main function that prints the availability of all washers and dryers.

## Disclaimer

This script is for educational purposes and assumes you have proper authorization to access the specified API. Make sure to comply with the terms of use and any legal restrictions when using this code.
