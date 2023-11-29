from datetime import date

class Hotel:
    def __init__(self):
        self.rooms = {}
        self.available_room = {'std': [101, 102, 103], 'delux': [201, 202, 203], 'execu': [301, 302, 303], 'suite': [401, 402, 403]}
        self.roomprice = {'std': 2000, 'delux': 4000, 'execu': 6000, 'suite': 8000}

    def check_in(self, name, address, phone):
        roomtype = int(input('Room type:\n1. Standard\n2. Delux\n3. Executive\n4. Suite\nSelect a room type: '))
        if roomtype == 1:
            room_type_name = 'std'
        elif roomtype == 2:
            room_type_name = 'delux'
        elif roomtype == 3:
            room_type_name = 'execu'
        elif roomtype == 4:
            room_type_name = 'suite'
        else:
            print("Choose a valid room type")
            return
        if self.available_room[room_type_name]:
            room_no = self.available_room[room_type_name].pop(0)
        else:
            print(f"Sorry, {room_type_name.capitalize()} room not available")
            return

        d, m, y = map(int, input("Enter the check-in-date in date, month, year: ").split())
        check_in = date(y, m, d)
        self.rooms[room_no] = {
            'name': name,
            'address': address,
            'phone': phone,
            'check_in_date': check_in,
            'room_type': roomtype,
            'roomservice': 0
        }
        print(f"Checked in {name}, {address} to room: {room_no} on {check_in}")

    def room_service(self, room_no):
        if room_no in self.rooms:
            print("****Mridha Restaurant Menu****")
            print("1. Tea/Coffee: tk.20  2. Dessert: tk.80 3. Breakfast: tk.100 4. Lunch: tk.150 5. Dinner: tk.120 6. Exit")
            while True:
                c = int(input("Select your Choice: "))
                if c == 1:
                    q = int(input("Enter the quantity: "))
                    self.rooms[room_no]['roomservice'] += 20 * q
                elif c == 2:
                    q = int(input("Enter the quantity: "))
                    self.rooms[room_no]['roomservice'] += 80 * q
                elif c == 3:
                    q = int(input("Enter the quantity: "))
                    self.rooms[room_no]['roomservice'] += 100 * q
                elif c == 4:
                    q = int(input("Enter the quantity: "))
                    self.rooms[room_no]['roomservice'] += 150 * q
                elif c == 5:
                    q = int(input("Enter the quantity: "))
                    self.rooms[room_no]['roomservice'] += 120 * q
                elif c == 6:
                    break
                else:
                    print("Invalid Option")
            print("Room service tk:", self.rooms[room_no]['roomservice'], "\n")
        else:
            print("Invalid room Number")

    def display_occupied(self):
        if not self.rooms:
            print("No rooms are occupied at this moment")
        else:
            print("Occupied Rooms:")
            print("-------------------")
            print('Room no. Name Phone')
            print("--------------------")
            for room_number, details in self.rooms.items():
                print(room_number, '\t', details['name'], '\t', details['phone'])

    def check_out(self, room_number):
        if room_number in self.rooms:
            check_out_date = date.today()
            check_in_date = self.rooms[room_number]['check_in_date']
            duration = (check_out_date - check_in_date).days
            roomtype = self.rooms[room_number]['room_type']
            if roomtype == 1:
                room_type_name = 'std'
            elif roomtype == 2:
                room_type_name = 'delux'
            elif roomtype == 3:
                room_type_name = 'execu'
            elif roomtype == 4:
                room_type_name = 'suite'
            else:
                print("Invalid room type")
                return

            self.available_room[room_type_name].append(room_number)
            print("----------------------------------")
            print('Mridha Hotel Receipt')
            print(f"Name: {self.rooms[room_number]['name']} \nAddress: {self.rooms[room_number]['address']}")
            print(f"Phone: {self.rooms[room_number]['phone']}")
            print(f'Room Number: {room_number}')
            print(f"Check-in date: {check_in_date.strftime('%d %B %Y')}")
            print(f'Check-out date: {check_out_date.strftime("%d %B %Y")}')
            print(f'No. of Days: {duration}\tPrice per day: tk.{self.roomprice[room_type_name]}')
            roombill = self.roomprice[room_type_name] * duration
            roomservice = self.rooms[room_number]['roomservice']
            print('Room bill: tk.', roombill)
            print('Room service: tk.', roomservice)
            print('Total Bill: tk', roombill + roomservice)
            del self.rooms[room_number]
        else:
            print(f"Room {room_number} is not occupied.")

    def display_room_availability(self):
        print("Room Availability Status:")
        for room_type, room_numbers in self.available_room.items():
            print(f"{room_type} rooms available: {room_numbers}")
        print("---------------------------------------------------")

    def modify_room_type_price(self):
        room_type = input("Enter the new room type (e.g., 'suite'): ")
        if room_type in self.available_room:
            new_price = int(input(f"Enter the new price for {room_type}: "))
            self.roomprice[room_type] = new_price
            print(f"{room_type} room price has been updated to tk.{new_price}")
        else:
            print(f"{room_type} is not a valid room type.")

    def review_final_bill(self, room_number):
        if room_number in self.rooms:
            check_out_date = date.today()
            check_in_date = self.rooms[room_number]['check_in_date']
            duration = (check_out_date - check_in_date).days
            roomtype = self.rooms[room_number]['room_type']
            if roomtype == 1:
                room_type_name = 'std'
            elif roomtype == 2:
                room_type_name = 'delux'
            elif roomtype == 3:
                room_type_name = 'execu'
            elif roomtype == 4:
                room_type_name = 'suite'
            else:
                print("Invalid room type")
                return

            print("----------------------------------")
            print('Mridha Hotel Receipt')
            print(f"Name: {self.rooms[room_number]['name']} \nAddress: {self.rooms[room_number]['address']}")
            print(f"Phone: {self.rooms[room_number]['phone']}")
            print(f'Room Number: {room_number}')
            print(f"Check-in date: {check_in_date.strftime('%d %B %Y')}")
            print(f'Check-out date: {check_out_date.strftime("%d %B %Y")}')
            print(f'No. of Days: {duration}\tPrice per day: tk.{self.roomprice[room_type_name]}')
            roombill = self.roomprice[room_type_name] * duration
            roomservice = self.rooms[room_number]['roomservice']
            print('Room bill: tk.', roombill)
            print('Room service: tk.', roomservice)
            print('Total Bill: tk', roombill + roomservice)
        else:
            print(f"Room {room_number} is not occupied.")
    def display_room_types_and_prices(self):
        print("Room Types and Prices:")
        for room_type, price in self.roomprice.items():
            print(f"{room_type.capitalize()}: tk.{price}")
        print("---------------------------------------------------")

    def extend_check_out_date(self, room_number, new_check_out_date):
        if room_number in self.rooms:
            self.rooms[room_number]['check_in_date'] = new_check_out_date
            print(f"The check-out date for room {room_number} has been extended to {new_check_out_date}")
        else:
            print(f"Room {room_number} is not occupied.")
    def start_app(self):
        while True:
            print("____________________________________")
            print("Welcome to Mridha hotel")
            print("1. Check-in")
            print("2. Room service")
            print("3. Display occupied Rooms")
            print("4. Check-out")
            print("5. Display Room Availability")
            print("6. Modify Room Type and Price")
            print("7. Extend Check-out Date")
            print("8. Review Final Bill")
            print("9. Display Room Types and Prices")
            print("10. Exit")
            choice = input("Enter your choice (1-10): ")
            if choice == '1':
                name = input("Enter Client name: ")
                address = input("Enter address: ")
                phone = input("Enter phone number: ")
                self.check_in(name, address, phone)
            elif choice == '2':
                room_no = int(input("Enter room number: "))
                self.room_service(room_no)
            elif choice == '3':
                self.display_occupied()
            elif choice == '4':
                room_number = int(input("Enter room number: "))
                self.check_out(room_number)
            elif choice == '5':
                self.display_room_availability()
            elif choice == '6':
                self.modify_room_type_price()
            elif choice == '7':
                room_number = int(input("Enter room number: "))
                new_check_out_date = self.get_date_input("Enter the new check-out date (dd mm yyyy): ")
                self.extend_check_out_date(room_number, new_check_out_date)
            elif choice == '8':
                room_number = int(input("Enter room number: "))
                self.review_final_bill(room_number)
            elif choice == '9':
                self.display_room_types_and_prices()
            elif choice == '10':
                break
            else:
                print("Invalid choice, please try again")

    def get_date_input(self, message):
        d, m, y = map(int, input(message).split())
        return date(y, m, d)

    def get_room_type_name(self, room_type):
        if room_type == 1:
            return 'std'
        elif room_type == 2:
            return 'delux'
        elif room_type == 3:
            return 'execu'
        elif room_type == 4:
            return 'suite'
        else:
            return 'unknown'

h = Hotel()
h.start_app()
