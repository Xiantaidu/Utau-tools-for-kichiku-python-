import easygui 
import os,shutil
#!/usr/bin/python
data = easygui.enterbox(msg='Enter database.', title=' ', default='', strip=True, image=None, root=None) 
mfolder = easygui.enterbox(msg='Enter move target folder.', title=' ', default='', strip=True, image=None, root=None) 
n=0
move=[]
for root , dirs, files in os.walk(data):
    for name in files:
        if name.endswith(".wav"):
            move.append(os.path.join(root, name))
while n<len(move):
    if os.path.getsize(move[n])<18200:
        shutil.move(move[n], mfolder)
        n+=1
    else:n+=1
easygui.msgbox(msg='done', title=' ', ok_button='OK', image=None, root=None)