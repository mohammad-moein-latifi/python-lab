from collections import defaultdict
from datetime import datetime


def collect_logins():
    users = defaultdict(list)

    print("Enter login records.")
    print("Format: username, YYYY-MM-DD HH:MM:SS")
    print("Press Enter to finish.\n")

    while True:
        record = input("Login: ").strip()

        if not record:
            break

        try:
            username, login_time = record.split(",", 1)

            username = username.strip()
            login_time = datetime.fromisoformat(login_time.strip())

            if not username:
                print("Error: Username cannot be empty.")
                continue

            users[username].append(login_time)

        except ValueError:
            print("Invalid input. Please try again.")

    return users


def analyze_logins(users):
    print("\n========== Login Report ==========")

    total_users = len(users)
    total_logins = sum(len(logins) for logins in users.values())

    print(f"Total unique users: {total_users}")
    print(f"Total login records: {total_logins}")

    print("\n--- Login Count Per User ---")

    for username, logins in users.items():
        print(f"{username}: {len(logins)} login(s)")

    print("\n--- Users With Only One Login ---")

    single_login_users = [
        username for username, logins in users.items() if len(logins) == 1
    ]

    if single_login_users:
        for username in single_login_users:
            print(username)
    else:
        print("No users found.")

    print("\n--- Users With More Than 3 Logins ---")

    frequent_users = {
        username: sorted(logins)
        for username, logins in users.items()
        if len(logins) > 3
    }

    if not frequent_users:
        print("No users found.")
        return

    for username, logins in frequent_users.items():
        print(f"\nUser: {username}")
        print(f"Total logins: {len(logins)}")
        print("Time intervals between logins:")

        for index in range(1, len(logins)):
            interval = logins[index] - logins[index - 1]

            print(f"  {logins[index - 1]} -> {logins[index]}")
            print(f"  Interval: {interval}")


def main():
    users = collect_logins()

    if not users:
        print("\nNo login records were entered.")
        return

    analyze_logins(users)


if __name__ == "__main__":
    main()
