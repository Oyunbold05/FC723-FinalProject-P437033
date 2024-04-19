# List to store booked seats
booked_seat = []

# Defining seat rows and columns
num_rows = 7
num_columns = 80

# List to store the floor plan
floor_plan = []

# Generating the floor plan
for row in range(num_rows):
    rows = []
    for column in range(num_columns):
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
                if (column == 76 and row in [4, 5, 6,]) or (column == 77 and row in [4, 5, 6]):
                    seat = "S   "
                rows.append(seat)
    floor_plan.append(rows)


# Function to display the floor plan table
def display_floor_plan():
    print("Floor Plan:")
    for each_row in floor_plan:
        print("\t".join(each_row))


# Function to check the availability of a seat
def check_availability(seat_number):
    if seat_number in booked_seat:
        print(f"Seat {seat_number} is already booked.")
    else:
        print(f"Seat {seat_number} is available.")


# Function to book a seat if it is available
def book_seat(seat_number):
    if seat_number in booked_seat:
        print(f"Seat {seat_number} is already booked.")
    else:
        column_index = seat_number[:-1]
        row_index = seat_number[-1]
        # Split the seat number by its row and column index.
        row_mapping = {'A': 0, 'B': 1, 'C': 2, 'D': 4, 'E': 5, 'F': 6}

        if row_index in row_mapping:
            row_index = row_mapping[row_index]
        else:
            print("Invalid seat number.")

        # Book the seat by updating the floor plan and adding to booked_seat list
        floor_plan[int(row_index)][(int(column_index)-1)] = f"{seat_number}-R"
        print(f"Seat {seat_number} has been booked successfully.")
        booked_seat.append(seat_number)
        display_floor_plan()


# Function to free a booked seat.
def free_seat(seat_number):
    if seat_number in booked_seat:
        # Remove the seat from booked_seat list
        booked_seat.remove(seat_number)
        # Split the seat number by its row and column index.
        column_index = seat_number[:-1]
        row_index = seat_number[-1]
        # Mapping for turning row letter into row index. (Index 3 is aisle)
        row_mapping = {'A': 0, 'B': 1, 'C': 2, 'D': 4, 'E': 5, 'F': 6}

        if row_index in row_mapping:
            row_index = row_mapping[row_index]
        else:
            print("Invalid seat number.")

        # Free the seat by updating the floor plan
        floor_plan[int(row_index)][(int(column_index) - 1)] = f"{seat_number}-F"
        print(f"Seat {seat_number} has been freed successfully.")
        display_floor_plan()

    else:
        print(f"Seat {seat_number} has not been booked yet.")


# Function to show booking state
def show_booking_state():
    if booked_seat:
        for seats in booked_seat:
            print(seats)
    else:
        print("No booking has made currently.")



