booked_seat = []
num_rows = 7
num_columns = 80
floor_plan = []



for row in range(num_rows):
    rows = []
    for column in range(num_columns):
        if row == 3:
            rows.append("X      ")  # Aisle or storage area
        else:
            if row < 3:
                rows.append(f"{column + 1}{chr(65 + row)}-F")
            else:
                seat = f"{column + 1}{chr(64 + row)}-F"
                if (column == 77 and row in [4, 5, 6,]) or (column == 78 and row in [4, 5, 6]):
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


def book_seat(seat_number):
    if seat_number in booked_seat:
        print(f"Seat {seat_number} is already booked.")
    else:
        column = seat_number[:-1]
        row = seat_number[-1]
        row_mapping = {'A': 0, 'B': 1, 'C': 2, 'D': 3, 'E': 4, 'F': 5}

        if row in row_mapping:
            row = row_mapping[row]
        else:
            print("Invalid seat number.")

        floor_plan[int(row)][(int(column)-1)] = f"{seat_number}-R"
        print(f"Seat {seat_number} has been booked successfully.")
        booked_seat.append(seat_number)
        display_floor_plan()



print(display_floor_plan())
print(book_seat('1A'))
