import datetime

# Define the patient's itinerary
patient_itinerary = {}

# Function to add an activity to the itinerary
def add_activity(time, activity):
    patient_itinerary[time] = activity

# Function to remove an activity from the itinerary
def remove_activity(time):
    if time in patient_itinerary:
        del patient_itinerary[time]

# Function to get the next activity
def get_next_activity():
    now = datetime.datetime.now().time()
    future_activities = {time: activity for time, activity in patient_itinerary.items() if time > now}
    if future_activities:
        next_activity_time = min(future_activities.keys())
        return future_activities[next_activity_time]
    else:
        return None