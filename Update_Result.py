# -*- coding: utf-8 -*-
"""
Created on Mon Jun 14 08:34:22 2021

@author: KIT
"""

import shutil
import os
import sys
from py_jama_rest_client.client import JamaClient


def Update_Result():
    #Insert code of Execute Test here
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
            judgment_result.append(1)
            print("STEP"+str(step_no+1)+": Passed" )
        else:
            judgment_result.append(0)
            print("STEP"+str(step_no+1)+": Failed" )
        step_no = step_no + 1
            

    
    # {
    # "op": "REPLACE",
    # "path": "/fields/testRunStatus",
    # "value": "PASSED"
    # }
        
    #     {
    # "op": "replace",
    # "path": "/fields/name",
    # "value": "New Updated Name"
    # }
    
    
    
    jama_client = JamaClient('https://93137.jamacloud.com', credentials=('kittidej_art@tdem.toyota-asia.com', '123456789'))
    
    # Get the list of projects from Jama
    # The client will return to us a JSON array of Projects, where each project is a JSON object.
    project_list = jama_client.get_projects()
    
    # project_items = jama_client.get_items(46)
    # action = []
    # for item in project_items:
    #     # print(item)
    #     test_case_id = item['globalId']
    #     if(test_case_id=='GID-55802'):
    #         item_id = item['id']
    #         test_case_info = item['fields']
    #         test_case_step = test_case_info['testCaseSteps']
    #         for step in test_case_step:
    #             action.append(step)
    
    
    test = jama_client.get_item(8036)
    test = jama_client.get_test
    
    testrun_list = jama_client.get_testruns(8060)
    
    
    
    
    
    
    testcycle_list = jama_client.get_test_cycle(46);

    #testrun_list = jama_client.get_testruns(8057)
    
    data_to_patch = {
      "op": "REPLACE",
      "path": "/fields/testRunStatus",
      "value": "PASSED"
    }

    jama_client.patch_item(8060, data_to_patch)
    print ("completed")
    


if __name__ == "__main__":
    #Call function here
    Update_Result()