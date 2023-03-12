#!/usr/bin/env python

def request_check_sum() -> str:
    check_sum = input("Enter the sha256 check sum, or press enter to skip:\n")
    if check_sum == None:
        check_sum = ''
        """if user input is empty, sets check_sum to empty string"""
    return check_sum

def resource_request() -> str:
    resource_requested = input("Enter a url or file path to scan. Press enter to pick file:\n")
    if resource_requested == None:
        resource_requested = ''
        """if user input is empty, sets resource_requested to empty string"""
    return resource_requested

def final_results(found, not_found) -> list:
    if len(not_found) > 0:
        see_raw = input("No threats detected!\n Press any key to exit or enter 'raw' to see raw results.\n")
        if see_raw.lower() == "raw":
            return not_found
        exit()
    elif len(found) > 0:
        print("--------> WARNING! <--------\n !!!!!THREAT DETECTED!!!!!\n\nPlease submit a ticket for review with the below included.\n")
        return found

