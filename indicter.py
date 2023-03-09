from db import writer

crx_filter = ["last_updated", "name", "permission_warnings", "size", "users"]
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

def crx_returned(resource, results):
    box.clear()
    box.append(resource)
    recent_version = len(results) - 1
    for k,v in results[recent_version].items():
        if k == 'data':
            for kk,vv in v.items():
                if kk == 'risk':
                    for k_k,v_v in vv.items():
                        if k_k == 'csp':
                            for kk_k,vv_v in v_v.items():
                                if kk_k == 'total':
                                    box.append(vv_v)
                        elif k_k == 'permissions':
                            for kk_k,vv_v in v_v.items():
                                box.append(vv_v)
                        elif k_k == 'total':
                            box.append(v_v)
                if kk == 'webstore':
                    for k_k, v_v in vv.items():
                        if k_k in crx_filter:
                            if k_k == "permission_warnings":
                                if v_v == []:
                                    v_v = '*'
                                elif v_v is dict:
                                    v_v = v_v.items()
                            box.append(v_v)
        elif k == 'version':
            box.append(v)
    writer(box, "crx_report")
