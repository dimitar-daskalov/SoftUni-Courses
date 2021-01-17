number_of_guest_invited = int(input())

regular_guests_invited = set()
vip_guests_invited = set()

regular_guests_attended = set()
vip_guests_attended = set()

for _ in range(number_of_guest_invited):
    guest = input()
    if guest[0].isdigit():
        vip_guests_invited.add(guest)
    else:
        regular_guests_invited.add(guest)

command = input()
while not command == "END":
    guest_attended = command
    if guest_attended[0].isdigit():
        vip_guests_attended.add(guest_attended)
    else:
        regular_guests_attended.add(guest_attended)
    command = input()

vip_not_coming = vip_guests_invited.difference(vip_guests_attended)
regular_not_coming = regular_guests_invited.difference(regular_guests_attended)

print(len(vip_not_coming) + len(regular_not_coming))
not_coming = sorted(vip_not_coming) + sorted(regular_not_coming)

for guest in not_coming:
    print(guest)