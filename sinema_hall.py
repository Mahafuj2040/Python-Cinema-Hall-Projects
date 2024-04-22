class StarCinema:
    _hall_list = []
    @staticmethod
    def add_hall(hall):
        StarCinema._hall_list.append(hall)
    
class Hall:
    def __init__(self, rows, cols, hall_no):
        self.rows = rows
        self.cols = cols
        self.hall_no = hall_no
        self.seats = {}
        self.show_list = []
        StarCinema.add_hall(self)
    
    
    def entry_show(self, id, movie_name, time):
        show_info = (id, movie_name, time)
        self.show_list.append(show_info)
        
        self.seats[id] = []
        
        for i in range(self.rows):
            row = []
            for j in range(self.cols):
                row.append(0)
            self.seats[id].append(row)
    
    
    
    def book_seats(self, id, row, col):
        if self.seats.get(id):
            if 0 <= row <self.rows and 0 <= col <self.cols:
                if self.seats[id][row][col] == 0:
                    self.seats[id][row][col] =1
                    print("**--------------------------------**\n")
                    print(f'Seat booked successfully at row -> {row + 1} and colum-> {col +1}.')
                    print("**---------------------------------**\n")
                
                else:
                    print('-- !!! --- This seat is already booked so You select another seat.')
            
        else:
            print("Invalid show ID.")
                
                
    def view_show_list(self):
        if len(self.show_list) > 0: 
            print("List of Shows: ")
            for show_info in self.show_list:
                print("**----------------------------------**")
                print(f" Movie Name: {show_info[1]}\n Movie Time: {show_info[2]}\n Movie or ID: {show_info[0]}")
                print("**----------------------------------**")
        else:
            print("No shows available.")
    
    
    def view_available_seats(self,id):
        if self.seats.get(id):
            print('Available seats for show ID {id}')
            for row in self.seats[id]:
                print(row)
        else:
                print('Invalid show ID.')

            


Rajshahi_Hall = Hall(5, 6, 1)

Rajshahi_Hall.entry_show("1", "Avengers: Endgame", "1:00pm")
Rajshahi_Hall.entry_show("2", "Avatar: The Way of Wate", "4:00pm")
Rajshahi_Hall.entry_show("3", "Titanic", "8:00pm")



run = True
while run:
    print("\n\n\n----------Welcome to the RAJSHAHI HALL program-----------\n\n")
    print('Option 1: View all shows today')
    print('Option 2: View available seats')
    print("Option 3: Book Ticket")
    print("Option 4: Exit")
    print("Option 5: To access admin for add (Show & Movie) details")

    op = int(input('\n\tEnter Your Option: '))

    if op == 4:
        print('\n\n\t\t You Successfully Exit')
        run = False
        break

    elif op == 1:
        Rajshahi_Hall.view_show_list()

    elif op == 2:
        show_id = input('Enter Show ID: ')
        Rajshahi_Hall.view_available_seats(show_id)

    elif op == 3:
        show_id = input("Enter your Show ID: ")
        row = int(input("Enter your seat row number: ")) - 1  
        col = int(input("Enter your seat column number: ")) - 1  
        Rajshahi_Hall.book_seats(show_id, row, col)
        
    elif op == 5:
        n = input("Admin enter Your Password: ")
        print("\n\t\t Succesfully your entered ----> :) ")
        
        if(n == '111'):
            name = input("\nEnter Your Movie Name: ")
            id_ = input("Enter your movie id: ")
            time = input("Enter your movie start time: ")
            Rajshahi_Hall.entry_show(id_, name, time)
            print("Add Movie Succesfully :)")
