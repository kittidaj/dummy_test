# -*- coding: utf-8 -*-
"""
Created on Mon Jun 14 08:34:22 2021

@author: KIT
"""

import shutil
import os
import sys
import urllib
import json
import random
import requests
from py_jama_rest_client.client import JamaClient

base_url = "https://93137.jamacloud.com/rest/v1/"
auth = ('kittidej_art@tdem.toyota-asia.com', '123456789')

automation_user_id = 13
runs_type_id = 37


def run_single_test(item_id, step_number, test_result):
    update_results(item_id, int(step_number), test_result)
   
def update_results(item_id, step_number, result):
               
    run_url = base_url + "testruns/{}".format(item_id)
    run_to_update = json.loads(requests.get(run_url, auth=auth).text)['data']
    print ("Running testrun {}.".format(run_to_update['id']))
    fields = run_to_update['fields']
    remove_field(fields, 'testRunStatus')
    remove_field(fields, 'executionDate')
    step = fields['testRunSteps'][step_number - 1]
    if result == 'Pass':
        fields['testRunSteps'][step_number - 1]['status'] = 'PASSED'
        fields['testRunSteps'][step_number - 1]['result'] = 'PASSED'
    else:
        fields['testRunSteps'][step_number - 1]['status'] = 'FAILED'
    requests.put(run_url, auth=auth, json={'fields': fields})
    
    print ("completed")

def remove_field(item, field):
    try:
        del item[field]
    except KeyError:
        pass

def run_test(test_run):
    
    testcase_lists = []
    result_lists = []
    
    with open(os.path.join('testcase.txt'), 'r') as the_file:
        for line in the_file:
            testcase_lists.append(line)
    
    with open(os.path.join('result.txt'), 'r') as the_file:
        for line in the_file:
            result_lists.append(line)
    
    #print (testcase)
    
    judgment_result = []
    step_no = 0
    for step in testcase_lists:
        if(step==result_lists[step_no]):
            judgment_result.append("Pass")
            print("STEP"+str(step_no+1)+": Pass" )
        else:
            judgment_result.append("Fail")
            print("STEP"+str(step_no+1)+": Fail" )
        step_no = step_no + 1
        
        
    test_run_id = test_run['id']
    lock_url = base_url + "testruns/{}/lock".format(test_run_id)
    run_is_locked = json.loads(requests.get(lock_url, auth=auth).text)['data']['locked']
    if not run_is_locked:
        step_successfully_run = False
        run_url = base_url + "testruns/{}".format(test_run_id)
        test_run = json.loads(requests.get(run_url, auth=auth).text)['data']
        steps = test_run['fields']['testRunSteps']
        test_result = random.choice(["Pass", "Fail"])
        
        for step_index in range(0, len(steps)):
            test_step = steps[step_index]
            # if test_step['status'] == 'NOT_RUN':
            #     try:
            #         run_single_test(str(test_run_id), str(step_index + 1), test_result)
            #         step_successfully_run = True
            #     except:
            #         print ("Error: Problem running step {} with note: {}.".format(step_index, test_step['notes']))
            # else:
            #     print ("Not running step with status {}.".format(test_step['status']))
            try:
                run_single_test(str(test_run_id), str(step_index + 1), judgment_result[step_index])
                step_successfully_run = True
            except:
                print ("Error: Problem running step {} with note: {}.".format(step_index, test_step['notes']))

        if not step_successfully_run:
            print ("Unlocking test run {}.".format(test_run_id))
            requests.put(lock_url, json={'locked': False}, auth=auth)
    else:
        print ("Run {} is locked.  Skipping.".format(test_run_id))

def get_all_tests(project_id):
    remaining_results = -1
    start_index = 0
    runs = []
    item_type_segment = "abstractitems?itemType={}".format(runs_type_id)
    project = "&project={}".format(project_id)
    url = ''.join([
        base_url,
        item_type_segment,
        project
    ])
    print ("Requesting resource: {}.".format(url))
    while remaining_results != 0:
        start_at = "&startAt={}".format(start_index)
        current_url = url + start_at
        response = requests.get(current_url, auth=auth)
        json_response = json.loads(response.text)
        page_info = json_response['meta']['pageInfo']
        total_results = page_info['totalResults']
        result_count = page_info['resultCount']
        remaining_results = total_results - (start_index + result_count)
        start_index += 20
        runs.extend(json_response['data'])
    print ("Runs evaluated: {}.".format(len(runs)))
    to_remove = []
    for run in runs:
        if not valid_run(run):
            to_remove.append(run)
    for run in to_remove:
        runs.remove(run)
    return runs

def valid_run(run):
    if run['type'] != 'testruns':
        print ("Item {} is not a test run.  Skipping.".format(run['id']))
        return False
    # if run['fields']['testRunStatus'] != 'NOT_RUN':
    #     print ("Run {} status must be NOT_RUN to evaluate.  Skipping.".format(run['id']))
    #     return False
    return True

if __name__ == "__main__":
    tests_to_evaluate = get_all_tests(46)
    for test in tests_to_evaluate:
        run_test(test)
  
    

