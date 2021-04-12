"""
1 _root should contain folders: applications, configurations, module_name
2 module_name contains python files
3 applications should contain a valid JSON file
4 python files should compile
5 config.json must be in root and contain the property "platform_version"
6 One error and the validation fails
"""

import py_compile
import argparse
import os
import json

def compilePython(file):
    success = True
    try:
        py_compile.compile(file, doraise=True)
    except py_compile.PyCompileError:
        success = False
    return success

def tryJson(filename):
    
    try:
        with open(filename) as f:
            json.load(f)
            return True
    except ValueError as e:
        return False

def tryJsonForProperty(jsonFile, propName):
    with open(jsonFile) as f:
        data = json.load(f)
    if propName not in data:
        return False
    else:
        return True

if __name__ == '__main__':
    parser = argparse.ArgumentParser(prog='pyPackValidator.py')
    parser.add_argument('--module', type=str, default='abc',  help='input directory name to test from the packages folder')
    opt = parser.parse_args()
    rootDir = f'packages/{opt.module}'

    #STEP 1: root should contain folders: applications, configurations, module_name
    rootFiles = os.listdir(rootDir)
    appFolderExists, confFolderExists, moduleFolderExists = False, False, False
    for f in rootFiles:
        if f == 'applications':
            appFolderExists = True
        elif f == 'configurations':
            confFolderExists = True
        elif f == str(opt.module):
            moduleFolderExists = True
    allConditions = []
    allConditions.append(appFolderExists)
    allConditions.append(confFolderExists)
    allConditions.append(moduleFolderExists)

    #error logs
    errorLogs=[]
    if not appFolderExists:
        errorLogs.append('No applications folder found.')
    if not confFolderExists:
        errorLogs.append('No configurations folder found.')
    if not moduleFolderExists:
        errorLogs.append(f'No {opt.module} folder found.')

    #STEP 2: module_name contains python files
    moduleDir = rootDir + f'/{opt.module}'
    pythonFilesFound = False
    
    try:
        moduleFiles = os.listdir(moduleDir)
        for f in moduleFiles:
            if f.endswith('.py'):
                pythonFilesFound = True
    except:
        pass
    
    allConditions.append(pythonFilesFound)

    #error logs
    if not pythonFilesFound:
        errorLogs.append('No python files found.')

    #STEP 3: applications should contain a valid JSON file
    appDir = rootDir + f'/applications/'
    appJsonValid = False

    try:
        appFiles = os.listdir(appDir)

        for f in appFiles:
            appJsonDir = appDir
            if f.endswith('.json'):
                appJsonDir += f 
                if tryJson(appJsonDir):
                    appJsonValid = True
                    break
    except:
        pass
    allConditions.append(appJsonValid)

    #error logs
    if not appJsonValid:
        errorLogs.append('No valid JSON files found in applications folder.')

    #STEP 4: python files should compile
    pyFiles = []
    pyCompiles = True
    for root, dirs, files in os.walk(rootDir):
        for name in files:
            if name.endswith((".py")):
                # whatever
                pyFiles.append(str(root + "/" + name))

    for pyFile in pyFiles:
        if not compilePython(pyFile):
            pyCompiles = False
            break
    allConditions.append(pyCompiles)

    #error logs
    if not pyCompiles:
        errorLogs.append('There are some invalid python files in the package.')


    #STEP 5: config.json must be in root and contain the property "platform_version"
    cfgJsonValid = False
    propName = 'platform_version'

    if 'config.json' in rootFiles and tryJson(rootDir + '/config.json'):
        cfgJsonValid = tryJsonForProperty(rootDir + '/config.json', propName)
    allConditions.append(cfgJsonValid)

    #error logs
    if not cfgJsonValid:
        errorLogs.append('config.json in root directory is invalid! Check for platform_version property.')

    #STEP 6: One error and the validation fails
    if False in allConditions:
        print('Invalid Python Package!\nError Log:')
        for log in errorLogs:
            print(log)

    else:
        print('Python Package is Valid!')

        