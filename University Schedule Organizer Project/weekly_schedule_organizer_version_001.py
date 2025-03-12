import pandas as pd
from datetime import datetime, timedelta

def generate_schedule_with_breaks(start_time, end_time, lesson_duration_minutes, break_after_minutes, lunch_break_start, lunch_break_duration):
    time_slots = []
    current_time = start_time
    total_class_time = 0
    
    while current_time + timedelta(minutes=lesson_duration_minutes) <= end_time:
        time_slots.append(current_time.strftime('%H:%M'))
        
        current_time += timedelta(minutes=lesson_duration_minutes)
        
        total_class_time += lesson_duration_minutes
        
        if current_time == lunch_break_start:
            current_time += timedelta(minutes=lunch_break_duration)
            total_class_time = 0
            
        elif total_class_time >= break_after_minutes:
            current_time += timedelta(minutes=10)
            total_class_time = 0
    
    time_slots = sorted(list(set(time_slots)), key=lambda x: datetime.strptime(x, '%H:%M'))
    
    return time_slots

def add_multiple_lessons(schedule_df, subject, num_lessons, available_slots, days_of_week):
    lessons_added = 0
    
    while lessons_added < num_lessons:
        target_weekday = input("Enter the target weekday (e.g., Monday, Tuesday, etc.): ").lower()

        if target_weekday not in [day.lower() for day in days_of_week]:
            print("Invalid weekday. Please try again.")
            continue

        for day in days_of_week:
            if day.lower() != target_weekday:
                continue

            for slot in available_slots[:]:
                if pd.isna(schedule_df.at[slot, day]):
                    user_input = input(f"Would you like to schedule {subject} at {slot} on {day}? (yes/no): ")
                    if user_input.lower() != "yes":
                        continue 
                    
                    schedule_df.at[slot, day] = subject
                    lessons_added += 1
                    available_slots.remove(slot)
                    print(f"{subject} scheduled at {slot} on {day}.")
                    
                    if lessons_added >= num_lessons:
                        break

            if lessons_added < num_lessons:
                print(f"No lessons were scheduled on {day}. Please try another day.")
                break
    
    return schedule_df

start_time = datetime.strptime('09:00', '%H:%M')
end_time = datetime.strptime('18:00', '%H:%M')
lesson_duration_minutes = 40
break_after_minutes = 80
lunch_break_start = datetime.strptime('13:20', '%H:%M')
lunch_break_duration = 20

days_of_week = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']
available_slots = generate_schedule_with_breaks(start_time, end_time, lesson_duration_minutes, break_after_minutes, lunch_break_start, lunch_break_duration)
schedule_df = pd.DataFrame(index=available_slots, columns=days_of_week)

pre_existing_classes = {
    "Monday": {
        "13:40": "Koreya dili",
        "14:20": "Koreya dili",
        "15:10": "Mülki Müdafiə Y-Zeynalov",
        "15:50": "Mülki Müdafiə Y-Zeynalov"
    },
    "Tuesday": {
        "13:40": "Koreya dili",
        "14:20": "Koreya dili",
        "15:10": "Kompüter qrafikası",
        "15:50": "Kompüter qrafikası",
        "16:40": "Kompüter qrafikası"
    },
    "Thursday": {
        "13:40": "Koreya dili",
        "14:20": "Koreya dili",
        "15:10": "Obyek yönümlü proqramlaşdırma",
        "15:50": "Obyek yönümlü proqramlaşdırma",
        "16:40": "Obyek yönümlü proqramlaşdırma"
    },
    "Friday": {
        "13:40": "Koreya dili",
        "14:20": "Koreya dili",
        "15:10": "Engineer riyaziyyatı D.Orucov",
        "15:50": "Engineer riyaziyyatı D.Orucov",
        "16:40": "Engineer riyaziyyatı D.Orucov"
    },
    "Saturday": {
        "10:30": "Elektron Dövrələr-N. İsgandarov",
        "11:10": "Elektron Dövrələr-N. İsgandarov",
        "12:00": "Elektron Dövrələr-N.İsgandarov"
    }
}

for day, classes in pre_existing_classes.items():
    for time, subject in classes.items():
        schedule_df.at[time, day] = subject

while True:
    subject = input("Enter the subject (or type 'exit' to finish): ")
    if subject.lower() == 'exit':
        break
    
    num_lessons = int(input("Enter the number of lessons (each 40 minutes): "))

    schedule_df = add_multiple_lessons(schedule_df, subject, num_lessons, available_slots, days_of_week)

    another_class = input("Do you want to add another class? (yes/no): ").lower()
    if another_class != 'yes':
        break
        
schedule_df.fillna("", inplace=True)

current_date = datetime.now().strftime('%Y-%m-%d')
excel_file_name = f"class_schedule_{current_date}.xlsx"
schedule_df.to_excel(excel_file_name, index=True)

print(f"\nClass Schedule saved to {excel_file_name}.")
print("\nFinal Class Schedule in Pandas Table:")
print(schedule_df)
