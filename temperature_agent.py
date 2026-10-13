
model = {
    "Room1": None,
    "Room2": None
}

heater_on_count = {
    "Room1": 0,
    "Room2": 0
}


def temperature_agent(room, reading):
    model[room] = reading

    if reading == "Cold":
        heater_on_count[room] += 1
        action = "Turn Heater ON"

    elif reading == "Hot":
        action = "Turn Heater OFF"

    elif model["Room1"] == "Normal" and model["Room2"] == "Normal":
        action = "All Rooms Comfortable - Idle"

    else:
        action = "Move to Other Room to Check"

    return action


percept_sequence = [
    ("Room1", "Cold"),
    ("Room1", "Normal"),
    ("Room2", "Hot"),
    ("Room2", "Normal")
]

print("Room\tReading\tAction\t\t\tModel")

for room, reading in percept_sequence:
    action = temperature_agent(room, reading)
    print(f"{room}\t{reading}\t{action}\t{model}")

print("\nHeater ON count:", heater_on_count)
