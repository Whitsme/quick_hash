import os
import subprocess
import sqlite3
from inputs import resource_request, request_check_sum
from hash_slinging_slasher import hash_check, hash_it
from file_check import verify_file
from url_check import verify_url
from virus_total import file_history, url_history
from indicter import sandbox, analysis
from db import builder

conn = sqlite3.connect('scan_results.db')
c = conn.cursor()
"""connects to database and creates cursor"""

def main():

    resource = resource_request()
    """requests file path or url from user"""
    if resource == '':
        subprocess.Popen('explorer /select, {}'.format(os.path))
        """if user input is empty, opens file explorer to select file"""
        
    elif verify_file(resource) == True:
        """checks input to see if it is a valid file path"""
        check_sum = request_check_sum()
        """requests check sum from user, if available"""
        if check_sum == '' or hash_check(check_sum) == True:
            """if user input check sum, this checks to see if it is a valid sha256 hash """
            resource_sum = hash_it(resource, check_sum)
            """generates hash sum of file"""
            if builder() == True:
                """verifies database exists, if not, creates it"""
                hist_results = file_history(resource_sum)
                """passes resource hash sum to VirusTotal API to check for existing scans"""
                sandbox(resource, resource_sum, hist_results[0])
                """processes sandbox results from VirusTotal API for writing to the database"""
                analysis(resource, resource_sum, hist_results[1])
                """processes analysis results from VirusTotal API for writing to the database"""

    elif verify_url(resource) == True:
        """checks input to see if it is a valid url"""
        results = url_history(resource)
        """passes url to VirusTotal API to check for existing scans"""
        analysis(resource, resource_sum, results)
        """processes analysis results from VirusTotal API for writing to the database"""

    else:
        print("The url did not return the correct status, or the file was not found at the path you specified. Please try again.")
        main() 

    sandbox_db = c.execute("SELECT * FROM sandbox")
    box = sandbox_db.fetchall()
    analysis_db = c.execute("SELECT * FROM analysis")
    sys = analysis_db.fetchall()
    """collects results from database for printing to the console"""

    print("Sandbox Results\n\n{}\n{}\n{}\n\nAnalysis Results\n\n{}\n".format(box[0], box[1], box[2], sys))
    """prints results to the console"""

if __name__ == "__main__":
    main()
