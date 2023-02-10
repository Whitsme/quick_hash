
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