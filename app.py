class ApacheAirline:
    def __init__(self):
        # List to store booked seats
        self.booked_seat = []

        # Defining seat rows and columns
        self.num_rows = 7
        self.num_columns = 80

        # List to store the floor plan
        self.floor_plan = []

    def generate_floor_plan(self):
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
                        if (column == 76 or 77) and row in [4, 5, 6]:
                            seat = "S   "
                        rows.append(seat)
            floor_plan.append(rows)
        return floor_plan

    # Function to display the floor plan table
    def display_floor_plan(self):
        print("Floor Plan:")
        for each_row in self.floor_plan:
            print("\t".join(each_row))
        print("Seat marking:\n F - Available seats"
              "  R - Booked seats"
              "  S - Storage area"
              "  X - Aisle")

    # Function to check the availability of a seat
    def check_availability(self, seat_number):
        if seat_number in self.booked_seat:
            print(f"Seat {seat_number} is already booked.")
        else:
            print(f"Seat {seat_number} is available.")

    # Function to book a seat if it is available
    def book_seat(self, seat_number):
        if seat_number in self.booked_seat:
            print(f"Sorry, seat {seat_number} is already booked.")
        else:
            # Split the seat number by its row letter and column number.
            column_number = int(seat_number[:-1])
            row_letter = seat_number[-1]

            row_mapping = {'A': 0, 'B': 1, 'C': 2, 'D': 4, 'E': 5, 'F': 6}

            # Check if seat exists and not located in aisle or storage area.
            if (row_letter in row_mapping) and (1 <= column_number <= 80) and not (column_number in [76, 77] and row_letter in ['D', 'E', 'F']):
                row_index = row_mapping[row_letter]  # Convert row letter into row index.
                column_index = column_number - 1
                # Book the seat by updating the floor plan and adding to booked_seat list.
                self.floor_plan[row_index][column_index] = f"{seat_number}-R"
                print(f"Seat {seat_number} has been booked successfully.")
                self.booked_seat.append(seat_number)
            else:
                print("Invalid seat number.")

    # Function to free a booked seat.
    def free_seat(self, seat_number):
        if seat_number in self.booked_seat:
            # Remove the seat from booked_seat list
            self.booked_seat.remove(seat_number)

            # Split the seat number by its row letter and column number.
            column_number = int(seat_number[:-1])
            row_letter = seat_number[-1]

            # Mapping for turning row letter into row index. (Index 3 is aisle)
            row_mapping = {'A': 0, 'B': 1, 'C': 2, 'D': 4, 'E': 5, 'F': 6}

            # Convert row letter into row index and column number into column index.
            row_index = row_mapping[row_letter]
            column_index = column_number - 1

            # Free the seat by updating the floor plan
            self.floor_plan[row_index][column_index] = f"{seat_number}-F"
            print(f"Seat {seat_number} has been freed successfully.")
        else:
            print(f"Seat {seat_number} has not been booked yet.")

    # Function to show booking state
    def show_booking_state(self):
        if self.booked_seat:
            print("The booked seats are: ")
            for seats in self.booked_seat:
                print(seats)
        else:
            print("No booking has been made currently.")


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
