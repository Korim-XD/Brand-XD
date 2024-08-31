import os,time,platform
os.system('pip uninstall requests chardet urllib3 idna certifi -y;pip install chardet urllib3 idna certifi requests')
bit = platform.architecture()[0]
if bit=='64bit':
    import fire
elif bit=='32bit':
    import fire
