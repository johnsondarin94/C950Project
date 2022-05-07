# Darin Johnson #001216025
import datetime
import csvreader
import algorithm


# This is the main function, gets called at the start of the program. This function handles the user interface.
def main():
    htable = csvreader.get_hash_table()

    print("\nWelcome to the WGU Parcel Service.")
    print("Package info will be displayed in the following format:")
    print("Package ID, Address, Deadline, Weight, Additional Notes(if applicable), Status, Scheduled leave time, "
          "Expected/Delivery time, Address ID\n")
    print("1. Display status of all packages and total miles driven at the end of the day.")
    print("2. Display status of all packages at a specific time.")
    print("3. Display status of single package at a specific time.")
    print("4. Close Application.\n")

    result = input("Type a number from the choices above and press enter to continue:")

    while result != '4':

        # Displays all packages after the day has ended as well as total miles traveled between all 3 trucks.
        if result == '1':
            truck_list = (algorithm.truck_load_packages())
            algorithm.truck_deliver_packages(truck_list, htable)
            algorithm.print_packages_tally_truck_miles(truck_list)
            input("Press Any Key to return to main menu")
            main()

        # Displays all packages at a specified time, displays updated status, time the truck is scheduled to leave, as
        # well as expected delivery/delivery of packages.
        elif result == '2':
            truck_list = (algorithm.truck_load_packages())
            time = input("Please write a time to view package data (HH:MM:SS):")
            (h, m, s) = time.split(':')
            convert_time = datetime.timedelta(hours=int(h), minutes=int(m), seconds=int(s))
            algorithm.truck_deliver_packages(truck_list, htable)
            print('Package status as of: ' + time)
            for count in range(1, 41):
                package = htable.search(count)
                time_delivered = package.time_delivered
                time_to_leave = package.time_to_leave

                if convert_time >= time_delivered:
                    package.status = 'delivered'
                if convert_time < time_delivered and convert_time < time_to_leave:
                    package.status = 'at the hub'
                if time_delivered > convert_time >= time_to_leave:
                    package.status = 'en route'
                print(package)
            input("Press Any Key to return to main menu")
            main()

        # Displays status of a single package with provided package id, at a specified time.
        elif result == '3':
            truck_list = (algorithm.truck_load_packages())
            input_package_id = input("Please provide the Package ID to continue.")
            time = input("Please write a time to view package data (HH:MM:SS):")
            (h, m, s) = time.split(':')
            convert_time = datetime.timedelta(hours=int(h), minutes=int(m), seconds=int(s))
            algorithm.truck_deliver_packages(truck_list, htable)
            print('Package status as of: ' + time)
            package = htable.search(int(input_package_id))
            time_delivered = package.time_delivered
            time_to_leave = package.time_to_leave

            if convert_time >= time_delivered:
                package.status = 'delivered'
            if convert_time < time_delivered and convert_time < time_to_leave:
                package.status = 'at the hub'
            if time_delivered > convert_time >= time_to_leave:
                package.status = 'en route'
            print(package)
            input("Press Any Key to return to main menu")
            main()
        # Closes the program.
        elif result == '4':
            quit()


main()
