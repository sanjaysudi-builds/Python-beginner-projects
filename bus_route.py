user_time = input("Enter the time: ").lower().replace(" ", " ")

# Bus list (times must be in ascending order)
buses = [
    ["8:00am",  "Ilkal → Bagalkot", "KA-42-F-312"],
    ["10:00am", "Ilkal → Bagalkot", "KA-42-F-200"],
    ["3:00pm",  "Ilkal → Mudhol",   "KA-29-F-789"],
    ["10:00pm", "Ilkal → Bagalkot", "KA-42-F-400"],
]

# Clean all bus times (remove spaces & make lowercase)
clean_buses = []
for b in buses:
    clean_buses.append([b[0].lower().replace(" ", ""), b[1], b[2]])

found = False
next_bus = None

for bus in clean_buses:
    bustime = bus[0]

    # 1. CHECK FOR EXACT OR "10 pm" format MATCH
    if (user_time == bustime) or (user_time.replace(":00","") == bustime.replace(":00","")):
        print("\n Bus FOUND!")
        print("Route:", bus[1])
        print("Bus Number:", bus[2])
        found = True
        break

    # 2. FIND NEXT BUS (user_time < bustime)
    # Compare only numbers like "10pm" → "10pm"
    if not found:
        if user_time < bustime:
            if next_bus is None:        # First next bus found
                next_bus = bus

if not found:
    if next_bus:
        print("\n Next available bus:")
        print("Time:", next_bus[0])
        print("Route:", next_bus[1])
        print("Bus Number:", next_bus[2])
    else:
        print("\n No next bus available today.")
