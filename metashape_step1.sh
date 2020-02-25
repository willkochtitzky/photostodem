#!/bin/bash
#SBATCH --time=24:00:00
#SBATCH --account=def-copland
#SBATCH --cpus-per-task=8
#SBATCH --mem-per-cpu=4G
#SBATCH --mail-user=<will.kochtitzky@uottawa.ca>
#SBATCH --mail-type=ALL
#SBATCH --job-name="Thores2_S1_init"

# Specify the time after which the license should be deactivated
timeout=23.7h

while [ 0 ]; do     # Starts an infinite loop, 0 means success
 printf "Trying Will's lic (1381)"
 metashape.sh --activate E9JK3-2195O-78YNM-6NAOE-4J1LC -platform offscreen #Will's work license
 if [ $? = 0 ]; then
    # If we get here, a licence was activated
    break;
  fi

 printf "Trying back middle lic(1382)"
 metashape.sh --activate E6AC7-RJTLK-58ZX6-5GF9P-PR8ZK -platform offscreen #1384 back middle computer
 if [ $? = 0 ]; then
    # If we get here, a licence was activated
    break;
 fi

 printf "Trying Will's personal lic"
 metashape.sh --activate EC9GZ-7UBFV-347KM-H6FZG-3EXJC -platform offscreen #Will's personal license
 if [ $? = 0 ]; then
    # If we get here, a licence was activated
    break;
 fi

 printf "Trying Abby's lic (1382)"
 metashape.sh --activate EDKE8-GMYJA-E1LCS-XS4JR-5H75N -platform offscreen # Abby 1382 license
 if [ $? = 0 ]; then
    # If we get here, a licence was activated
    break;
  fi

 printf "Trying Claire's lic(1386)"
 metashape.sh --activate E8H1F-H9HHU-6Z9R2-EMYGZ-1P2U8 -platform offscreen
 if [ $? = 0 ]; then
    # If we get here, a licence was activated
    break;
  fi

 printf "Trying Brittany's lic(1385)"
 metashape.sh --activate EC13M-5HER2-XZHH1-X7XFE-3OG8K -platform offscreen
 if [ $? = 0 ]; then
    # If we get here, a licence was activated
    break;
  fi

 printf "Trying Luke's lic (1388)"
 metashape.sh --activate EDKE8-GMYJA-E1LCS-XS4JR-5H75N -platform offscreen
 if [ $? = 0 ]; then
    # If we get here, a licence was activated
    break;
  fi


#Sleep for 30 seconds before you try to activate again
Sleep 30

done



# Function that deactivates the license
deactivatelicense() {
  echo "deactivating license"

  until metashape.sh --deactivate -platform offscreen ]; do
        echo "Retrying to deactivate"
        sleep 10
  done

  exit $1
}


# Deactivate the license when we receive SIGUSR1
trap "deactivatelicense 1" USR1

# Save our process ID which we use to send the SIGUSR1 to
procid=$$

# Start a subshell in the background with the main job
(
  echo "Starting job"
  # The code for running your job goes here instead of sleep
  #-------------------------------------------------------------------------
metashape.sh -r metashape_intialize_and_load.py -platform offscreen
sbatch metashape_step2.sh
  #-------------------------------------------------------------------------
  exitcode=$?
  echo "Done job"
) &

# Start a subshell in the background to deactivate the licence after $timeout time
(
  sleep $timeout
  echo "Time out reached, deactivating license"
  kill -USR1 $procid
  exit 0
) &

# Wait for the first subshell (main job) to finish
wait %1
exitcode=$?

# If the main job finished first, kill the second subshell that has the timer
kill -9 %2

# There is no timer anymore, so deactivate the license ourselves
deactivatelicense $exitcode


