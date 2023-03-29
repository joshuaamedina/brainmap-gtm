import os
import subprocess
import argparse
import logging


logging.basicConfig(level=logging.INFO,
format='%(asctime)s %(levelname)s %(message)s',
      filename='converter.log',
      filemode='w')

parser = argparse.ArgumentParser(description ='gtm commands')
parser.add_argument('-r','--radius',type=int,required=True,
                    help='Radius to use for gtm')
parser.add_argument('-a','--ale',type=float,required=True,
                    help='Ale Threshold')
parser.add_argument('-f','--filter',type=str,required=True,
                    help='Filter for gtm')
parser.add_argument('-s','--sleuth',type=str,required=True,
                    help='Sleuth file name')
parser.add_argument('-d','--directory',type=str,required=True,
                    help='Directory containing xGTM')

args = parser.parse_args()

radius = args.radius
ale = args.ale
filter = args.filter
sleuth = args.sleuth
direc = args.directory
logging.info(f'directory : {direc}, sleuth {sleuth}')

subprocess.run([f"ls"],shell=True)
subprocess.run([f"""ls {direc} """],shell=True)

subprocess.run([f"""/scratch/tacc/apps/matlab/2022b/bin/matlab -nodesktop -nodisplay -nosplash -r "gtm {direc} {sleuth} {radius} {ale} {filter}" """],shell=True)

sleuthFiles = sleuth.split('.')[0] + '_'

print(sleuthFiles)

files = [f for f in os.listdir(direc) if os.path.isfile(f)]
for f in files:
    if f.startswith(sleuthFiles):
        print(f)

#    if filename.startswith(f'{sleuthFiles}'):
#        print(filename)

subprocess.run([f"""for file in $(ls {direc}/{sleuthFiles}*); do cp "$file" .;done """],shell=True)

subprocess.run([f"""rm -r  {direc} """],shell=True)
