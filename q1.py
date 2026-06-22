# q1.py
# CS253 Assignment
# Question 1
# Name: Rajasa Lingamsetti
# Roll Number: 240596


def format_line(text):
    text = str(text)

    # Truncate if longer than 46 characters
    if len(text) > 46:
        text = text[:43] + "..."

    return "*" + text.center(46) + "*"


def generate_invites(guest_list, event_details):
    invites = {}

    border = "*" * 50

    for guest in guest_list:
        card = []

        card.append(border)
        card.append(format_line("Saraswati Puja Invitation"))
        card.append(format_line("Utkal Parishad, IIT Kanpur"))
        card.append(format_line(""))

        card.append(format_line(f"Dear {guest['Name']},"))
        card.append(format_line(guest["Affiliation"]))
        card.append(format_line(""))

        card.append(format_line(f"Date: {event_details['Date']}"))
        card.append(format_line(f"Venue: {event_details['Venue']}"))
        card.append(format_line(f"Schedule: {event_details['Schedule']}"))

        card.append(border)

        invites[guest["Email"]] = "\n".join(card)

    return invites


# Example usage
guests = [
    {
        "Name": "Aman",
        "Affiliation": "CSE Dept",
        "Email": "aman@iitk.ac.in"
    },
    {
        "Name": "Dr. Very Long Name That Definitely Exceeds The Character Limit",
        "Affiliation": "Physics Department With A Very Long Name Too",
        "Email": "dr.long@iitk.ac.in"
    }
]

details = {
    "Date": "Feb 14, 2026",
    "Venue": "Community Hall",
    "Schedule": "10:00 AM"
}

result = generate_invites(guests, details)

for email, invite in result.items():
    print("Email:", email)
    print(invite)
    print()