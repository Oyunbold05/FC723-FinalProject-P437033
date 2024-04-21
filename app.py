import random
import string
import csv

# Class for the software for ApacheAirline
class ApacheAirline:
    def __init__(self):
        # Dictionary to store booked seats
        self.booked_seat = {}

        # Defining seat rows and columns
        self.num_rows = 7
        self.num_columns = 80

        # Generating floor plan
        self.floor_plan = self.generate_floor_plan()

    # Function to check validity of seat number
    def seat_validity_checker(self, seat_number):
        # Check if seat exist in the aircraft and not located in the storage area or aisle.
        if ((seat_number[-1].isalpha() and ord(seat_number[-1].upper()) - ord('A') < self.num_rows) and
    (seat_number[:-1].isdigit() and 1 <= int(seat_number[:-1]) <= self.num_columns)):
            return True
        else:
            return False

    # Function for splitting seat number into row and column index. For example, 1A => row 'A' column '1' =>
    # row index '0' and column index '0'.
    def seat_index(self, seat_number):
        # Split the seat number by its row letter and column number.
        column_number = int(seat_number[:-1])
        row_letter = seat_number[-1]

        # Mapping for turning row letter into row index. (Index 3 is aisle)
        row_mapping = {'A': 0, 'B': 1, 'C': 2, 'D': 4, 'E': 5, 'F': 6}

        # Convert row letter into row index and column number into column index.
        row_index = row_mapping[row_letter]
        column_index = column_number - 1

        return row_index, column_index

    # Function to generate floor plan
    def generate_floor_plan(self):
        # List for floor plan which later be displayed in shape of table
        floor_plan = []
        # Generating the floor plan
        for row in range(self.num_rows):
            rows = []
            for column in range(self.num_columns):
                if row == 3:
                    # Row index 3 => 4th row is aisle which is marked as 'X'
                    rows.append("X      ")
                else:
                    if row < 3:
                        # Generating seat numbers for rows A, B, C
                        rows.append(f"{column + 1}{chr(65 + row)}-F")
                    else:
                        # Generating seat numbers for rows D, E, F
                        seat = f"{column + 1}{chr(64 + row)}-F"
                        # Row D, E, F and Column index 76, 77 => 77th, 78th columns are storage area which is marked as S.
                        if (column == 76 and row in [4, 5, 6]) or (column == 77 and row in [4, 5, 6]):
                            seat = "S   "
                        rows.append(seat)
            floor_plan.append(rows)
        return floor_plan

    # Function to display the floor plan table
    def display_floor_plan(self):
        print("Floor Plan:")
        # Displaying floor plan as table
        for each_row in self.floor_plan:
            print("\t".join(each_row))
        print("Seat marking:\n F - Available seats"
              "  R - Booked seats"
              "  S - Storage area"
              "  X - Aisle")

    # Function to check the availability of a seat
    def check_availability(self, seat_number):
        # Check validity of the seat number
        if not self.seat_validity_checker(seat_number):
            print("Invalid seat number(DOES NOT EXIST or Storage and Aisle area")
        # Check if seat is booked.
        if seat_number in self.booked_seat:
            print(f"Seat {seat_number} is already booked.")
        else:
            print(f"Seat {seat_number} is available.")

    # Function to book a seat if it is available
    def book_seat(self, seat_number):
        if seat_number in self.booked_seat:
            print(f"Sorry, seat {seat_number} is already booked.")
        else:
            # Check if seat exists and not located in aisle or storage area.
            if self.seat_validity_checker(seat_number):
                # Get booking details from user.
                booking_details = self.get_booking_details()

                # Book the seat by updating the floor plan and adding to booked_seat list.
                self.floor_plan[self.seat_index(seat_number)[0]][self.seat_index(seat_number)[1]] = f"{seat_number}-R"
                print(f"Seat {seat_number} has been booked successfully.")

                # Generate random booking reference for booked seat and store them together in booked_seat dictionary.
                booking_reference = self.generate_booking_reference()
                self.booked_seat[seat_number] = booking_reference

                # Save booking details to CSV file.
                self.save_booking_details_to_csv(booking_reference, seat_number, booking_details)
            else:
                print("Invalid seat number.")

    # Function to free a booked seat.
    def free_seat(self, seat_number):
        # Check if seat is booked.
        if seat_number in self.booked_seat:
            # Remove the seat from booked_seat dictionary
            del self.booked_seat[seat_number]
            # Remove the booking details from csv file.
            self.remove_booking_details_from_csv(seat_number)

            # Free the seat by updating the floor plan.
            self.floor_plan[self.seat_index(seat_number)[0]][self.seat_index(seat_number)[0]] = f"{seat_number}-F"
            print(f"Seat {seat_number} has been freed successfully.")
        else:
            print(f"Seat {seat_number} has not been booked yet.")

    # Function to show booking state
    def show_booking_state(self):
        if self.booked_seat:
            print("The booked seats are: ")
            # Loop through each seat in booked_seat dictionary.
            for seat, reference in self.booked_seat.items():
                # Print booking reference with seat number.
                print(f"Seat {seat}: Booked with booking reference {reference}")
        else:
            print("No booking has been made currently.")

    # Function to generate booking reference
    def generate_booking_reference(self):
        while True:
            # Generate random reference
            reference = ''.join(
                random.choices(string.ascii_uppercase + string.digits, k=8))
            # Check if reference is unique
            if reference not in self.booked_seat.values():
                return reference

    # Function to save booking details as CSV file
    def save_booking_details_to_csv(self, booking_reference, seat_number, booking_details):
        with open('booking_details.csv', mode='a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(
                [f"Booking {booking_reference}", f"Seat Label: {seat_number}"] + list(booking_details.values()))

    # Function to get booking details
    def get_booking_details(self):
        passport_number = input("Enter passport number: ")
        first_name = input("Enter first name: ")
        last_name = input("Enter last name: ")
        return {
            "passport_number": passport_number,
            "first_name": first_name,
            "last_name": last_name,
        }

    # Function to delete the booking details for the freed seat number
    def remove_booking_details_from_csv(self, seat_number):
        # Initialize a list to store rows not to delete
        rows_to_keep = []
        # Open CSV file in read mode
        with open('booking_details.csv', mode='r') as file:
            # Create CSV reader object
            reader = csv.reader(file)
            # Loop through rows in CSV
            for row in reader:
                # Check if it's not the row to remove
                if row[1] != f"Seat Label: {seat_number}":
                    # Add row to list of rows to keep
                    rows_to_keep.append(row)
        # Open CSV file in write mode
        with open('booking_details.csv', mode='w', newline='') as file:
            # Create CSV writer object
            writer = csv.writer(file)
            # Write rows to CSV file
            writer.writerows(rows_to_keep)


# Menu which contains all the functions.
def main():
    burak757 = ApacheAirline()
    while True:
        print("\nMenu:")
        print("1. Display floor plan")
        print("2. Check availability of seat")
        print("3. Book a seat")
        print("4. Free a seat")
        print("5. Show booking state")
        print("6. Exit program")

        option = input("Enter your option: ")

        if option == "1":
            burak757.display_floor_plan()
        elif option == "2":
            seat_number = input("Enter seat number to check availability (e.g., 1A): ").upper()
            burak757.check_availability(seat_number)
        elif option == "3":
            seat_number = input("Enter seat number to book (e.g., 1A): ").upper()
            burak757.book_seat(seat_number)
        elif option == "4":
            seat_number = input("Enter seat number to free (e.g., 1A): ").upper()
            burak757.free_seat(seat_number)
        elif option == "5":
            burak757.show_booking_state()
        elif option == "6":
            print("Exiting program.")
            break
        else:
            print("Invalid option. Please enter a valid option.")


if __name__ == "__main__":
    main()
