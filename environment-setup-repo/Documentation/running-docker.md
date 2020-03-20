# Running Docker for Training

_This assumes that you are running within VM that has been setup for Docker & NVIDIA execution ([instructions here](vm-setup.md)) and are connected to that VM ([instructions here](vm-connection.md))._

1. Navigate to the source control directory (`cd jds-arx-poc`)
1. Run `bash sync.sh` to pull the latest changes from source control (may need to run `sudo bash sync.sh`)
1. Run `bash ./docker/build.sh` (OR `bash ./docker/build-cpu.sh`) to build the Docker image 
    * You will only have to do this on changes to the dockerfile.
1. Run `bash ./docker/start.sh` (OR `bash ./docker/start-cpu.sh`) to start the Docker image with bash.

Once the Docker Container is running, you'll need to:

1. Navigate to the source control directory (`cd jds-arx-poc`)
1. Run `bash ./docker/conda-setup.sh` to setup the conda environment
1. Run your python scripts as necessary!