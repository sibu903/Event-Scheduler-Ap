import schedule
import time

events = []

def add_event():
    title = input("Enter event title: ")
    description = input("Enter event description: ")
    date = input("Enter event date in YYYY-MM-DD format: ")
    time_str = input("Enter event time in HH:MM format: ")

    event = {
        'title': title,
        'description': description,
        'date': date,
        'time': time_str
    }

    events.append(event)
    print(f"Event '{title}' added on {date} at {time_str}")
    schedule.every().day.at(time_str).do(trigger_event, title)

def view_events():
    print("Scheduled Events:")
    for event in events:
        print(f"Title: {event['title']}, Description: {event['description']}, "
              f"Date: {event['date']}, Time: {event['time']}")

def edit_event():
    title = input("Enter event title to edit: ")
    event = next((e for e in events if e['title'] == title), None)

    if event:
        event['description'] = input("Enter new event description: ")
        event['date'] = input("Enter new event date in YYYY-MM-DD format: ")
        event['time'] = input("Enter new event time in HH:MM format: ")
        print(f"Event '{title}' edited. New details: {event}")
    else:
        print(f"Event '{title}' not found.")

def delete_event():
    title = input("Enter event title to delete: ")
    event = next((e for e in events if e['title'] == title), None)

    if event:
        events.remove(event)
        print(f"Event '{title}' deleted.")
    else:
        print(f"Event '{title}' not found.")

def search_events_by_date():
    search_date = input("Enter date to search events (YYYY-MM-DD): ")
    matching_events = [event for event in events if event['date'] == search_date]

    if matching_events:
        print(f"Events on {search_date}:")
        for event in matching_events:
            print(f"Title: {event['title']}, Description: {event['description']}, "
                  f"Date: {event['date']}, Time: {event['time']}")
    else:
        print(f"No events found on {search_date}.")

def trigger_event(title):
    print(f"Event '{title}' triggered at:", time.strftime("%Y-%m-%d %H:%M:%S"))

while True:
    print("\nEvent Scheduler Menu:")
    print("1. Add Event")
    print("2. View Events")
    print("3. Edit Event")
    print("4. Delete Event")
    print("5. Search Events by Date")
    print("6. Exit")

    choice = input("Enter your choice (1-6): ")

    if choice == '1':
        add_event()
    elif choice == '2':
        view_events()
    elif choice == '3':
        edit_event()
    elif choice == '4':
        delete_event()
    elif choice == '5':
        search_events_by_date()
    elif choice == '6':
        print("Exiting Event Scheduler. Goodbye!")
        break
    else:
        print("Invalid choice. Please enter a number between 1 and 6.")

    schedule.run_pending()
    time.sleep(1)
