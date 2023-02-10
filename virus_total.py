import vt
from api import api_key

key = api_key()
client = vt.Client(key)
"""collects api key from api.py and connects to VirusTotal API"""

hist_dict = []
"""creates empty list for storing VirusTotal API results"""

def file_history(resource_sum):
    try:
        hist_dict.clear()
        """clears list for storing VirusTotal API results"""
        check_history = client.get_object("/files/{}".format(resource_sum))
        """sends file hash sum to VirusTotal API to check for existing scans"""
        hist = check_history
        """stores VirusTotal API results in variable"""
        if hist != '' or hist != None:
            """checks to see if VirusTotal API returned results"""
            hist_dict.append(hist.sandbox_verdicts)
            hist_dict.append(hist.last_analysis_results)
            return hist_dict
            """appends VirusTotal API results to list and returns list"""
        # file_scan(resource)
        return False
    except:
        return False

def url_history(resource):
    hist_dict.clear()
    """clears list for storing VirusTotal API results"""
    try:
        resource_id = vt.url_id(resource)   
        """generates url id from url for VirusTotal API"""
        scan_results = client.get_object("/urls/{}".format(resource_id))
        """sends url id to VirusTotal API to check for existing scans"""
        hist_dict.append(scan_results.last_analysis_results)
        return hist_dict
        """appends VirusTotal API results to list and returns list"""
    except:
        # url_scan(resource)
        return False
    
"""
def url_scan(resource):
    requested_scan = client.scan_url(resource)
    url_history(requested_scan)

def file_scan(resource):
    with open(resource, "rb") as f:
        analysis = client.scan_file(f)
        while True:
            analysis = client.get_object("/analyses/{}".format(analysis.id))
            print(analysis.status)
            if analysis.status == "completed":
                break
            time.sleep(30)
    file_history(resource_sum)
"""