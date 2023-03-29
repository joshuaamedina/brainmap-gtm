# Allow over-ride
if [ -z "${CONTAINER_IMAGE}" ]
then
    version=$(cat ./_util/VERSION)
    CONTAINER_IMAGE="index.docker.io/library/ubuntu:bionic"
fi
. lib/container_exec.sh

# Write an excution command below that will run a script or binary inside the 
# requested container, assuming that the current working directory is 
# mounted in the container as its WORKDIR. In place of 'docker run' 
# use 'container_exec' which will handle setup of the container on 
# a variety of host environments. 
#
# Here is a template:
#
# container_exec ${CONTAINER_IMAGE} COMMAND OPTS INPUTS
#
# Here is an example of counting words in local file 'poems.txt',
# outputting to a file 'wc_out.txt'
#
# container_exec ${CONTAINER_IMAGE} wc poems.txt > wc_out.txt
#

# set -x

# set +x

BINDPATH=" --bind /opt/intel:/opt/intel "

module unload xalt

singularity pull gtm.sif docker://joshuaamedina2000/joshuaam_gtm:0.0.1

singularity exec gtm.sif cp -r /xGTM_portal .

mv ${input1} xGTM_portal/

singularity exec ${BINDPATH} gtm.sif python3 gtmWrapper.py -d $PWD/xGTM_portal/ -s ${input1} -r ${radius} -a ${ale} -f ${filter}
