import csv
from typing import List, Optional

class Theater:
    def __init__(
        self,
        rows: int = 5,
        seats_per_row: int = 10,
        base_price: float = 200.0,
        front_row_extra: float = 100.0,
        student_discount_pct: float = 20.0,
        bookings_file: str = "booking.csv",
    ):
        self.rows = rows
        self.seats_per_row = seats_per_row
        self.seats: List[List[Optional[str]]] = [
            [f"{r+1}-{s+1}" for s in range(seats_per_row)] for r in range(rows)
        ]
        self.base_price = base_price
        self.front_row_extra = front_row_extra
        self.student_discount_pct = student_discount_pct
        self.bookings_file = bookings_file

        # create CSV file with header if it doesn't exist
        try:
            with open(self.bookings_file, "r", newline="") as f:
                pass
        except FileNotFoundError:
            with open(self.bookings_file, "w", newline="") as f:
                writer = csv.writer(f)
                writer.writerow(["name", "row", "seat", "price", "student"])

    def show_seats(self) -> None:
        print("Seat map (Row-Seat). 'X' = booked")
        for r in range(self.rows):                       # FIX: self.rows (not self.row)
            row_display = []
            for s in range(self.seats_per_row):
                val = self.seats[r][s]
                row_display.append(val if val == "X" else f"{r+1}-{s+1}")
            # use proper formatting and join with spaces
            print("Row", r+1, ":", " ".join(f"{x:5}" for x in row_display))
        print()

    def seat_is_available(self, row: int, seat: int) -> bool:
        if not (1 <= row <= self.rows and 1 <= seat <= self.seats_per_row):
            return False
        return self.seats[row - 1][seat - 1] != "X"

    def calculate_price(self, row: int, is_student: bool) -> float:
        price = self.base_price
        if row == 1:
            price += self.front_row_extra
        if is_student:
            price = price * (1 - self.student_discount_pct / 100.0)
        return round(price, 2)

    def book_seat(self, name: str, row: int, seat: int, is_student: bool = False) -> Optional[dict]:
        if not (1 <= row <= self.rows and 1 <= seat <= self.seats_per_row):
            print("Error: row or seat number out of range.")
            return None
        if not self.seat_is_available(row, seat):
            print(f"Seat {row}-{seat} is already booked.")
            return None

        price = self.calculate_price(row, is_student)
        self.seats[row - 1][seat - 1] = "X"

        booking = {
            "name": name,
            "row": row,
            "seat": seat,
            "price": price,
            "student": "Yes" if is_student else "No",
        }

        with open(self.bookings_file, "a", newline="") as f:
            writer = csv.writer(f)
            writer.writerow([booking["name"], booking["row"], booking["seat"], booking["price"], booking["student"]])

        self.print_ticket(booking)
        return booking

    def print_ticket(self, booking: dict) -> None:
        print("\n" + "=" * 30)
        print("      MOVIE TICKET")
        print("=" * 30)
        print(f"Name      : {booking['name']}")
        print(f"Seat      : Row {booking['row']}, Seat {booking['seat']}")
        print(f"Student   : {booking['student']}")
        print(f"Price     : Rs {booking['price']}")
        print("=" * 30 + "\n")


# <-- demo must be at module level (not inside the class) -->
def demo():
    t = Theater()
    print("Initial Seats:")
    t.show_seats()

    # book some seats
    t.book_seat(name="Neha", row=3, seat=5, is_student=False)
    t.book_seat(name="Chandan", row=1, seat=1, is_student=False)
    t.book_seat(name="Ajay", row=1, seat=1, is_student=True)  # will fail (already booked)

    t.show_seats()
    print(f"Bookings saved to {t.bookings_file}")


if __name__ == "__main__":
    demo()
