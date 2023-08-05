import os
import requests
import json

KEY_RESULT_VALUE = "result"

def sendUpdateRequest(c):
    try:
        job = os.environ['AI_MAKER_JOB_ID']
        pod_name = os.environ['HOSTNAME']
        token = os.environ['AI_MAKER_TOKEN']
        url = os.environ['AI_MAKER_HOST']
    except KeyError as e:
        print ("[KeyError] Please assign {} value".format(str(e)))
        return -1
    HEADERS = {"content-type" : "application/json",
               "Authorization" : "bearer "+token}
    body = json.dumps({ KEY_RESULT_VALUE : c })
    url = url+"/api/v1/ai-maker/callback/results/jobs/"+job+"/pod/"+pod_name
    return requests.post(url, data = body, headers = HEADERS)

def saveValidationResult(result):
    try:
        cronjob = os.environ['AI_MAKER_CRONJOB_ID']
        token = os.environ['AI_MAKER_TOKEN']
        url = os.environ['AI_MAKER_HOST']
    except KeyError as e:
        print ("[KeyError] Please assign {} value".format(str(e)))
        return -1
    HEADERS = {"content-type" : "application/json",
               "Authorization" : "bearer "+token}
    body = json.dumps({ KEY_RESULT_VALUE : result })
    print(cronjob)
    url = url+"/api/v1/ai-maker/callback/results/validations/"+cronjob
    print(url)
    return requests.post(url, data = body, headers = HEADERS)
