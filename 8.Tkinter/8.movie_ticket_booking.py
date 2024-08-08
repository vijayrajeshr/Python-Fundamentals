import tkinter as tk
from tkinter import messagebox

def update_showtimes_and_theaters(*args):
    movie = movie_var.get()
    if movie:
        showtimes = movies[movie]["showtimes"]
        theaters = movies[movie]["theaters"]
        
        # Update showtime and theater dropdowns
        showtime_var.set(showtimes[0])
        theater_var.set(theaters[0])

        showtime_menu['menu'].delete(0, 'end')
        for showtime in showtimes:
            showtime_menu['menu'].add_command(label=showtime, command=tk._setit(showtime_var, showtime))
        
        theater_menu['menu'].delete(0, 'end')
        for theater in theaters:
            theater_menu['menu'].add_command(label=theater, command=tk._setit(theater_var, theater))

def book_tickets():
    movie = movie_var.get()
    showtime = showtime_var.get()
    theater = theater_var.get()
    num_tickets = num_tickets_entry.get()
    
    try:
        num_tickets = int(num_tickets)
        if num_tickets <= 0:
            raise ValueError("Number of tickets must be positive.")
    except ValueError as e:
        messagebox.showerror("Invalid Input", str(e))
        return

    print(f"Booking {num_tickets} tickets for {movie} at {showtime} in {theater}")

    # Replace this with actual booking logic (database, payment, etc.)

# Movie information
movies = {
    "Leo": {"language": "Tamil", "showtimes": ["10:00 AM", "2:00 PM", "6:00 PM"], "theaters": ["PVR", "INOX", "Cinepolis"]},
    "Indian 2": {"language": "Tamil", "showtimes": ["11:00 AM", "3:00 PM", "7:00 PM"], "theaters": ["PVR", "INOX"]},
    "John Wick Chapter 5": {"language": "English", "showtimes": ["12:00 PM", "4:00 PM", "8:00 PM"], "theaters": ["Cinepolis"]}
}

# Create GUI elements
root = tk.Tk()
root.title("Vijay's Ticket Booking Site")

movie_var = tk.StringVar(root)
showtime_var = tk.StringVar(root)
theater_var = tk.StringVar(root)

movie_label = tk.Label(root, text="Select Movie:")
movie_menu = tk.OptionMenu(root, movie_var, *movies.keys())

showtime_label = tk.Label(root, text="Select Showtime:")
showtime_var.set(list(movies.values())[0]["showtimes"][0])
showtime_menu = tk.OptionMenu(root, showtime_var, *movies[list(movies.keys())[0]]["showtimes"])

theater_label = tk.Label(root, text="Select Theater:")
theater_var.set(list(movies.values())[0]["theaters"][0])
theater_menu = tk.OptionMenu(root, theater_var, *movies[list(movies.keys())[0]]["theaters"])

num_tickets_label = tk.Label(root, text="Number of Tickets:")
num_tickets_entry = tk.Entry(root)

book_button = tk.Button(root, text="Book Now", command=book_tickets)

# Layout
movie_label.grid(row=0, column=0, padx=10, pady=10)
movie_menu.grid(row=0, column=1, padx=10, pady=10)
showtime_label.grid(row=1, column=0, padx=10, pady=10)
showtime_menu.grid(row=1, column=1, padx=10, pady=10)
theater_label.grid(row=2, column=0, padx=10, pady=10)
theater_menu.grid(row=2, column=1, padx=10, pady=10)
num_tickets_label.grid(row=3, column=0, padx=10, pady=10)
num_tickets_entry.grid(row=3, column=1, padx=10, pady=10)
book_button.grid(row=4, column=0, columnspan=2, pady=10)

movie_var.trace("w", update_showtimes_and_theaters)

root.mainloop()
