from netoprmgr.main_cli import MainCli

if __name__ == "__main__":
    answer=input(
    'Type "template" to create template on data folder\n\n'
    'Press Number for MENU :\n'
    'Type "web" for accessing web version\n'
    '0. Device Identification (Still Development)\n'
    '1. Device Availability Check\n'
    '2. Capture\n'
    '3. Create Report\n'
    '4. Show Environment Report\n'
    '5. Show Log Report\n'
    '6. New Create Report\n'
    'Type "quit" to quit program\n'
    )
    if answer == '0':
        MainCli.deviceIdentification()
    elif answer == '1':
        MainCli.deviceAvailability()
    elif answer == '2':
        MainCli.captureDevice()
    elif answer == '3':
        MainCli.createReport()
    elif answer == '4':
        MainCli.showEnvironment()
    elif answer == '5':
        MainCli.showLog()
    elif answer == '6':
        MainCli.createNewReport()
    elif answer == 'web':
        MainCli.webAccess()