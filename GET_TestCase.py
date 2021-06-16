# -*- coding: utf-8 -*-
"""
Created on Mon Jun 14 08:34:21 2021

@author: KIT
"""

import shutil
import os
import sys
import os
from py_jama_rest_client.client import JamaClient




def GET_TestCase():
    print(os.getcwd())
    #Insert code of GET Test Case here
    # Setup your Jama instance url, username, and password.
    # You may use environment variables, or enter your information directly.
    # Reminder: Follow your companies security policies for storing passwords.
    #jama_url = os.environ['https://93137.jamacloud.com']
    #jama_api_username = os.environ['kittidej_art@tdem.toyota-asia.com']
    #jama_api_password = os.environ['123456789']
    
    # Create the JamaClient
    #jama_client = JamaClient(host_domain=jama_url, credentials=(jama_api_username, jama_api_password))
    jama_client = JamaClient('https://93137.jamacloud.com', credentials=('kittidej_art@tdem.toyota-asia.com', '123456789'))
    
    # Get the list of projects from Jama
    # The client will return to us a JSON array of Projects, where each project is a JSON object.
    project_list = jama_client.get_projects()
    
    project_items = jama_client.get_items(46)
    action = []
    for item in project_items:
       # print(item)
        test_case_id = item['globalId']
        if(test_case_id=='GID-55799'):
            test_case_info = item['fields']
            test_case_step = test_case_info['testCaseSteps']
            for step in test_case_step:
                action.append(step)

            
            #print(action)
    
            
    if os.path.exists("testcase.txt"):
        os.remove("testcase.txt")
        f = open("testcase.txt", "w")
        f.close()
    else:
        f = open("testcase.txt", "w")
        f.close()
      
      
    with open(os.path.join('testcase.txt'), 'a') as the_file:
        for item in action:
            expected = item['expectedResult']
            the_file.write(expected+'\n')

            
    print("GET TestCase Completed")
    
    #
    
    # Print the data out for each project.
    # for project in project_list:
    #     project_name = project['fields']['name']
    #     print('\n---------------' + project_name + '---------------')
    
    #     # Print each field
    #     for field_name, field_data in project.items():
    
    #         # If one of the fields(i.e. "fields") is a dictionary then print it's sub fields indented.
    #         if isinstance(field_data, dict):
    #             print(field_name + ':')
    #             # Print each sub field
    #             for sub_field_name in field_data:
    #                 sub_field_data = field_data[sub_field_name]
    #                 print('\t' + sub_field_name + ': ' + str(sub_field_data))
    
    #         # If this field is not a dictionary just print its field.
    #         else:
    #             print(field_name + ': ' + str(field_data))
    
    
    
if __name__ == "__main__":
    #Call function here
    GET_TestCase()