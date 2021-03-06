'''
  usage: download the file to a notebook via 
  
  !curl https://raw.githubusercontent.com/luca-arts/seeingtheimperceptible/main/notebooks/database_mod.py -o /content/database_mod.py --silent
  from database_mod import *
'''


def link_nextcloud(Nextcloud_URL="https://cloud.bxlab.net/remote.php/dav/files/colab/colabfiles/"):
    '''
    link_nextcloud is a function which mounts a nextcloud database ´Nextcloud_URL´ to /content/database
    returns the link to the database
    '''
    from subprocess import run, Popen, PIPE, STDOUT
    import os
    run(['apt', 'install', '-y', 'davfs2'])
    run(['pip', 'install', 'getpass'])
    import getpass
    nextcloud = "/content/database"
    os.makedirs(nextcloud, exist_ok=True)

    if os.path.isfile("/etc/fstab"):
        os.remove("/etc/fstab")
    with open("/etc/fstab", "a") as f:
        f.write(Nextcloud_URL + " " + nextcloud + " davfs user,rw,auto 0 0")
    un = input("what's the username for nextcloud? ")
    pw = getpass.getpass("what's the password for user {}? ".format(un))
    p = run(['mount', nextcloud], stdout=PIPE,
            input='{}\n{}\n'.format(un, pw), encoding='ascii')
    print(p.returncode)
    assert(p.returncode == 0)
    print(p.stdout)
    txt = "/etc/fstab"
    viewTxt = open(txt, "r")
    txtContent = viewTxt.read()
    # print("content of /etc/fstab: {}".format(txtContent))

    return nextcloud


def download_zip(zip_filename='output.zip', output_folder='/content/output_folder'):
    '''
    a function to automatically download the results stored in <output_folder> to your local computer in zip format
    '''
    import os
    from google.colab import files
    if os.path.exists(zip_filename):
        os.remove(zip_filename)
    os.system(f"zip -r -j {zip_filename} {output_folder}/*")
    files.download(zip_filename)


def create_io(database='/content/database/', topic=None, library=None, input_redirect=None):
    '''
    create_io is a function which creates an input link to the dataset, more specifically to a directory called `topic`
    An output folder for experiments gets created via `topic/library` 
    '''
    import shutil
    import os
    if(input_redirect is None):
        input_folder = os.path.join(database, topic, 'input')
    else:
        input_folder = input_redirect
    output_folder = os.path.join(database, topic, library)
    if os.path.exists(output_folder):
        shutil.rmtree(output_folder)
    os.makedirs(output_folder)
    return input_folder, output_folder
