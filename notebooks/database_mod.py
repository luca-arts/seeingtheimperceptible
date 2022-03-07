# usage: download the file via !curl https://raw.githubusercontent.com/luca-arts/seeingtheimperceptible/main/notebooks/database_mod.py -o /content/database_mod.py
def link_nextcloud(Nextcloud_URL="https://cloud.bxlab.net/remote.php/dav/files/colab/colabfiles/"):
  '''
  link_nextcloud is a function which mounts a nextcloud database ´Nextcloud_URL´ to /content/database
  returns the link to the database
  '''
  import os
  !apt install -y davfs2  > /dev/null

  nextcloud = "/content/database"
  os.makedirs(nextcloud, exist_ok=True)

  if os.path.isfile("/etc/fstab"):
    os.remove("/etc/fstab")
  with open("/etc/fstab" , "a") as f:
    f.write(Nextcloud_URL + " " + nextcloud + " davfs user,rw,auto 0 0")
  !mount {nextcloud}

  # open existing text file
  txt = "/etc/fstab"
  viewTxt = open(txt, "r")
  txtContent = viewTxt.read()
  print("txtContent: {}".format(txtContent))
  
  return nextcloud
  
def create_io(database='/content/database/', topic=None, library=None):
  '''
  create_io is a function which creates an input link to the dataset, more specifically to a directory called `topic`
  An output folder for experiments gets created via `topic/library` 
  '''
  import shutil, os
  # clean and rebuild the image folders
  input_folder = database+topic

  output_folder = database+topic+'/'+library
  if os.path.exists(output_folder):
    shutil.rmtree(output_folder)
  os.makedirs(output_folder)
  return input_folder, output_folder
