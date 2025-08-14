# 🛂 Access Control Scanner Challenge
#
# 1. Create a set of revoked badge numbers.
# 2. Create two empty lists: "approved" and "denied".
# 3. Start a loop to collect visitor info:
#    - Ask for the visitor's name (or type "done" to finish).
#    - If the name is "done", exit the loop.
#    - Otherwise, ask for their badge number.
#    - Check if the badge is revoked:
#        • If revoked: add the name to "denied" and display "ACCESS DENIED".
#        • If not: add the name to "approved" and display "ACCESS GRANTED".
# 4. Print the final "Access Summary" for "✅ Approved Visitors" & "⛔️ Denied Visitors":
#    - Sort both lists alphabetically.
#    - Display the total number of approved and denied visitors.





revoked_badge_numbers = { 1023, 1055, 1101, 1128, 1150,
    1204, 1220, 1255, 1300, 1333,
    1401, 1450, 1502, 1525, 1555}

approved_badge_numbers = []
denied_badge_numbers = []

while True:
    visitors_name = input("Enter visitors name TYPE (Done or D) if you are done:  ").capitalize()

    if visitors_name== "Done" or visitors_name== "D":
        break
    else:
        badge_number = int(input("Enter badge number:  "))

        if badge_number in revoked_badge_numbers:
            denied_badge_numbers.append(visitors_name)
            print("Access Denied")
        else:
            approved_badge_numbers.append(visitors_name)
            print("Access Granted")
print("==== Access Summary ====")

print("---- Approved Visitors ----")

for person in sorted(approved_badge_numbers):
    print(f"Approved - {person}")

print("---- Denied Visitors ----")

for person in sorted(denied_badge_numbers):
 print(f"denied\n -{person} ")

approved_badge_numbers = len(approved_badge_numbers)
denied_badge_numbers = len(denied_badge_numbers)

sum_all_numbers = approved_badge_numbers + denied_badge_numbers
print(f"Total number of Visitors {sum_all_numbers}")