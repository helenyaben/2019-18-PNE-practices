'''

IMPORTING LIBRARIES


There are many python libraries available for you to use. You only have to install them. This installation depends on the type of python interpreter you have installed

(1)Go to the Settings/project-2018-19-PNE-practises/project interpreter
(2)On the top right, click on the gear icon to add a python interpreter
(3)Click on virtualenv environment if that is not your current python interpreter. Click on OK
(4)A new venv folder will appear in your project (make sure this folder is excluded from your project)

Now we can install and use other libraries. Let's install termcolor: a library for printing with color on the console.


'''


import termcolor

termcolor.cprint("Hey! this is printed in green!", 'green')