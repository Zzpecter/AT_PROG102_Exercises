"""
1 _root should contain folders: applications, configurations, module_name
2 module_name contains python files
3 applications should contain a valid JSON file
4 python files should compile
5 config.json must be in root and contain the property "platform_version"
6 One error and the validation fails
"""

import argparse
import os

from pythonValidator import PythonValidator 
from jsonValidator import JsonValidator 
from folderValidator import FolderValidator 


if __name__ == '__main__':
    parser = argparse.ArgumentParser(prog='pyPackValidator.py')
    parser.add_argument('--module', type=str, default='abc',  help='input directory name to test from the packages folder')
    opt = parser.parse_args()
    rootDir = f'packages/{opt.module}'

    fVal = FolderValidator(rootDir)
    pyVal = PythonValidator(rootDir)
    jVal = JsonValidator(rootDir)

    #STEP 1: root should contain folders: applications, configurations, module_name
    passesTest = fVal.validate()

    if passesTest:
        passesTest = False
        #STEP 2: module_name contains python files AND
        #STEP 4: python files should compile
        passesTest = pyVal.validate()

        if passesTest:
            passesTest = False
            #STEP 3: applications should contain a valid JSON file
            #STEP 5: config.json must be in root and contain the property "platform_version"
            jVal.get_files_in_folder(rootDir + '/applications/')
            passesTest = jVal.validate()

            if passesTest:
                print('Python Package is Valid!')
            else:
                print('Invalid Python Package!\nError Log:')
                for log in jVal.errorLogs:
                    print(log)
        else:
            print('Invalid Python Package!\nError Log:')
            for log in pyVal.errorLogs:
                print(log)
    else:
        print('Invalid Python Package!\nError Log:')
        for log in fVal.errorLogs:
            print(log)

        