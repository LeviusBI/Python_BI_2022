# Python_BI_2022
Тут я буду ~~говнокодить~~ **решать ДЗ**
Instructions for pain.py
###1) OC version:

distributor ID:	Ubuntu
Description:	**Ubuntu 22.04.1 LTS**
Release:	22.04
Codename:	jammy

If you youse Ubuntu Linux, you can find version of your ubuntu by Ctrl+Alt+T and running __lsb_release__ -a command

Check Google how to update it

###2) Python version - 3.9.13

You can check your version in Ubuntu Linux Terminal by running __python --version__ command

Check Google how to update it

###3) Creating virtual environment

I was creating this project in Visual Studio Code. All commands were run in terminal in VSC. Furthemore, you need to run commands from dir of your project.
For example, if pain.py is in folder ~/I/Hate/myself/ you need to: Ctrl+Alt+T, then run "cd ~/I/Hate/myself/". Only after ##this## you can use commands below.

I have preinstalled Anaconda, so I was using conda commands to creat venv. Checl Google how to install Anaconda. About creation of venv you can read below:

1) We need python 3.10 to run pain.py because of matches, so run this: conda create -n venv python=3.10
2) Then: conda activate venv
3)Then you need to Ctrl+Shift+P, then you need to start typing Select Interpretator and in the list you need to choode correspond interpretator. You wiil understand it, because there will be a path with a name of your venv
4) Just click it, bruh

###4) Importing

When all the programs are run, it is time to real pain)))

just run this comands in the same terminal as before (check venv before your current path)

pip install --upgrade google-api-python-client
pip install scanpy
pip install opencv-python
pip install aiohttp
python -m pip install "kivy[base]"
pip install biopython
pip install beautifulsoup4

Then run the script

Congratulations! You died.

Run pip freeze > requirements.txt to save all 

###5) Then you can deactivate venv and change interpretator
conda deactivate - in terminal of VSC
Ctrl+Sift+P and choose 'base' interpretator - in VSC generally

###6) You can also delete venv. Just Google.
Bye-bye!

