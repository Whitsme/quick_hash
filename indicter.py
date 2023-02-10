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
        writer(box, "sandbox")

def analysis(resource, resource_sum, results):
    for k,v in results.items():
        box.clear()
        box.append(resource)
        box.append(resource_sum)
        for kk, vv in v.items():
            if vv is not str:
                vv == ''
            box.append(vv)
        writer(box, "sandbox")
