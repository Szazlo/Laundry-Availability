import requests
import json

AUTH = ""
BASE_API = "https://phoneadmin.flashcashonline.com/api/user/GetMachineInfo?machineId="
MACHINES = {
    "Washer": ["PNRP23LK", "3M3N9IJ4"],
    "Dryer": ["CLS0289L", "CYC6UDOI"],
}


def make_get_request(url, authorization=AUTH):
    """Makes a GET request to the given URL.

    Args:
        url: The URL to make the request to.
        authorization: The authentication token to use.

    Returns:
        The response text, or an error message if the request fails.
    """

    headers = {"Authorization": f"Bearer {authorization}"}

    try:
        response = requests.get(url, headers=headers)

        if response.status_code == 200:
            return response.text
        else:
            return f"Request failed with status code {response.status_code}"
    except requests.exceptions.RequestException as e:
        return f"Request failed with error: {e}"


def get_machine_availability(machine_type):
    """Gets the availability of all machines of the given type.

    Args:
        machine_type: The type of machine to check availability for.

    Returns:
        A list of strings, where each string is either "Machine Available" or
        "Machine not available. Completion time: <time>".
    """

    availability = []

    for machine in MACHINES[machine_type]:
        info = make_get_request(BASE_API + machine)
        data = json.loads(info)

        if data["Data"]["Available"]:
            availability.append(f"{machine_type} Available")
        else:
            end = data["EstimatedCompletionTime"]
            availability.append(f"{machine_type} unavailable. Completion time: {end}")

    return availability


def main():
    """Prints the availability of all washers and dryers."""

    print("""LAUNDRY AVAILABILITY
===================""")

    washer_availability = get_machine_availability("Washer")
    dryer_availability = get_machine_availability("Dryer")

    for machine in washer_availability:
        print(machine)

    for machine in dryer_availability:
        print(machine)


if __name__ == "__main__":
    main()
