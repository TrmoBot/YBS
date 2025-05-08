def find_routes(user_input):
    # Dummy parser for "From X to Y"
    if " to " in user_input:
        parts = user_input.lower().replace("from ", "").split(" to ")
        origin, destination = parts[0].strip().title(), parts[1].strip().title()
    else:
        return "Please use format: From [Origin] to [Destination]"

    # Example hardcoded logic
    if origin == "Thamine" and destination == "Myaynigone":
        return (
            "Option (1) - Take YBS (131) from Thamine and get off in Myaynigone Bus Stop\n"
            "Option (2) - Take YBS (41) from Thamine and get off in Hledan and then take (131) and get off at Myaynigone Bus Stop\n"
            "Option (3) - Take YBS (39) from Thamine and get off in Myaynigone Bus Stop\n"
            "Option (4) - Take YBS (61) from Thamine and get off in Myaynigone Bus Stop"
        )
    else:
        return "Sorry, route data not available yet. Please try another query."
