#!/usr/bin/env python

import os
import subprocess
import sqlite3
import tui
from inputs import resource_request, request_check_sum, final_results
from hash_slinging_slasher import hash_check, hash_it
from file_check import verify_file
from url_check import verify_url
from virus_total import file_history, url_history
from indicter import sandbox, analysis
from db import builder, reader
from vt import url_id
from crxcavator import crx_report, crx_meta


crx_ignore = ['dangerousfunctions', 'entrypoints', 'extcalls', 'manifest', 'related']
tables = ["file_sandbox", "file_analysis", "url_analysis", "crx_report"]
not_found = []
found = []
boxed = []

conn = sqlite3.connect('scan_results.db')
c = conn.cursor()
"""connects to database and creates cursor"""

def main():

    resource = resource_request()
    """requests file path or url from user"""
    if resource == '':
        subprocess.Popen('explorer /select, {}'.format(os.path)) #currently not working as intended 
        """if user input is empty, opens file explorer to select file"""
        
    elif verify_file(resource) == True:
        """checks input to see if it is a valid file path"""
        check_sum = request_check_sum()
        """requests check sum from user, if available"""
        # if check_sum == '' or hash_check(check_sum) == True:
        #"""if user input check sum, this checks to see if it is a valid sha256 hash """
        resource_sum = hash_it(resource, check_sum)
        """generates hash sum of file"""
        if builder() == True:
            """verifies database exists, if not, creates it"""
            hist_results = file_history(resource_sum, resource)
            """passes resource hash sum to VirusTotal API to check for existing scans"""
            if len(hist_results) > 1:
                sandbox(resource, resource_sum, hist_results[0])
                """processes sandbox results from VirusTotal API for writing to the database"""
                analysis(resource, resource_sum, hist_results[1])
                """processes analysis results from VirusTotal API for writing to the database"""
            else:
                analysis(resource, resource_sum, hist_results[0])
                """processes analysis results from VirusTotal API for writing to the database"""

    elif verify_url(resource) == True:
        if builder() == True:
            """checks input to see if it is a valid url"""
            results = url_history(resource)
            """passes url to VirusTotal API to check for existing scans"""
            resource_id = url_id(resource)
            analysis(resource, resource_id, results)
            """processes analysis results from VirusTotal API for writing to the database"""

    elif crx_meta(resource) == True:
        if builder() == True:
            crx_report(resource)

    else:
        print("The url did not return the correct status, or the file was not found at the path you specified. Please try again.")
        main() 

    for table in tables:
        if reader(table) == True:
            db_info = c.execute("SELECT * FROM {}".format(table))
            if table == "file_sandbox":
                tui.to_this = "Sandbox Results"
                box = db_info.fetchall()
                if len(box) > 0:
                    for i in box:
                        boxed.append("\n{},{},{}".format(box[0], box[1], box[2]))
                        # print("Sandbox Results\n\n{}\n{}\n{}\n".format(box[0], box[1], box[2]))
                    tui.results = boxed
            elif table == "crx_report":
                tui.to_this = "CRXcavator Results"
                box = db_info.fetchall()
                if len(box) > 0:
                    boxed.append("\n{},{},{},{},{},{},{},{},{}".format(box[0][1], box[0][2], box[0][3], box[0][5], box[0][9], box[0][4], box[0][8], box[0][7], box[0][6]))
                    # print("CRXxavator Results:\n\n[CSP Score: {}] + [Permission Score: {}] = Total Score: {}\nName: {} | Version: {} | Last Update: {} | Users: {} | Size: {}\nPermission Warnings: {}\n".format(box[0][1], box[0][2], box[0][3], box[0][5], box[0][9], box[0][4], box[0][8], box[0][7], box[0][6]))
                    tui.results = boxed
            elif table == "file_analysis" or table == "url_analysis":
                tui.to_this = "analysis"
                sys = db_info.fetchall()
                if len(sys) > 0:
                    # print("\nAnalysis Results\n")
                    for i in sys:
                        # if i[2] == "undetected" or i[2] == "type-unsupported":
                        #     not_found.append("Category: {} | Result: {} | Method: {} | Engine Name: {}".format(i[2], i[3], i[4], i[5]))
                        # else:
                        #     found.append("Category: {} | Result: {} | Method: {} | Engine Name: {}".format(i[2], i[3], i[4], i[5]))
                        #     """prints results to the console"""
                        boxed.append("\n{},{},{},{}".format(i[2], i[3], i[4], i[5]))
                    # fnf_list = final_results(found, not_found) 
                    # for i in fnf_list:
                        # print(i)
                    tui.results = boxed
            app = tui.quick_hash()
            app.run()

    # for table in tables:
    #     if reader(table) == True:
    #         db_info = c.execute("SELECT * FROM {}".format(table))
    #         if table == "file_sandbox":
    #             box = db_info.fetchall()
    #             if len(box) > 0:
    #                 for i in box:
    #                     print("Sandbox Results\n\n{}\n{}\n{}\n".format(box[0], box[1], box[2]))
    #         elif table == "crx_report":
    #             box = db_info.fetchall()
    #             if len(box) > 0:
    #                 print("CRXxavator Results:\n\n[CSP Score: {}] + [Permission Score: {}] = Total Score: {}\nName: {} | Version: {} | Last Update: {} | Users: {} | Size: {}\nPermission Warnings: {}\n".format(box[0][1], box[0][2], box[0][3], box[0][5], box[0][9], box[0][4], box[0][8], box[0][7], box[0][6]))
    #         elif table == "file_analysis" or table == "url_analysis":
    #             sys = db_info.fetchall()
    #             if len(sys) > 0:
    #                 print("\nAnalysis Results\n")
    #                 for i in sys:
    #                     if i[2] == "undetected" or i[2] == "type-unsupported":
    #                         not_found.append("Category: {} | Result: {} | Method: {} | Engine Name: {}".format(i[2], i[3], i[4], i[5]))
    #                     else:
    #                         found.append("Category: {} | Result: {} | Method: {} | Engine Name: {}".format(i[2], i[3], i[4], i[5]))
    #                         """prints results to the console"""
    #                 fnf_list = final_results(found, not_found) 
    #                 for i in fnf_list:
    #                     print(i)
    
if __name__ == "__main__":
    main()
