import os 
import platform

def setup_environment():
    if platform.system() == 'Windows':
        print('Really bro? you\'re gonna develop on Windows? You better have some \
            rad games on your system otherwise I have no respect for you.')
        print('setting up your environment')
        os.system('py -3 -m pip install requests')
        print('All done! Have fun with Atlas')
    elif platform.system() == 'Linux':
        print('MY MAN! Love that you\'re using Linux my dude. GG')
        print('Setting up the environment for you my dude.')
        os.system('pip3 install requests')
        print('All done! Have fun with Atlas')
    elif platform.system() == 'Darwin':
        print('I see that you\'re using a MAC OS\n fuck you and your stupid mac.\
            but I\'m a generous god and will set up the env for you as well, you fucking \
                mac os using fuckity fuck fuck')
        os.system('pip3 install requests')
        print('All done! Have fun with Atlas')

setup_environment()
