from db import writer

box = []
in_box = []

def sandbox(resource, resource_sum, results):
    for k,v in results.items():
        box.clear()
        box.append(resource)
        box.append(resource_sum)
        for kk, vv in v.items():
            if vv is not str:
                vv == ''
            box.append(vv)
        writer(box, "file_sandbox")

def analysis(resource, resource_sum, results):
    try:
        results = results.items()
    except:
        results = results[0].items()
    for k,v in results:
        box.clear()
        box.append(resource)
        box.append(resource_sum)
        for kk, vv in v.items():
            try:
                vv = str(vv)
            except:
                vv == ''
            box.append(vv)
        if len(box) > 7:
            writer(box, "file_analysis")
        else:
            writer(box, "url_analysis")
