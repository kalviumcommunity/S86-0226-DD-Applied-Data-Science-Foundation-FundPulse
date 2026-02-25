# S86-0226-DD-Applied-Data-Science-Foundation-FundPulse..

🧪 Data Science Environment Verification

This milestone verifies that my local system is properly configured and ready for Data Science development. I confirmed that Python is installed and callable from the terminal by running python --version, which returned the installed Python version successfully. I also verified that Conda is installed and functioning by running conda --version. After confirming this, I created a dedicated Conda environment using conda create -n ds_env python=3.x -y and activated it using conda activate ds_env. I validated that the environment was active by checking conda info --envs, where the active environment was clearly indicated.

Next, I launched Jupyter Notebook using jupyter notebook (or jupyter lab) and confirmed that it opened successfully in the browser. Inside Jupyter, I executed a Python test cell using import sys and print(sys.version) to verify that Python runs correctly within the notebook. I also checked print(sys.executable) to ensure that Jupyter is using the same Conda environment, confirming environment consistency.

All verification steps were successfully completed, confirming that Python, Conda, and Jupyter are properly configured. The system is stable, consistent, and ready for Data Science sprint development.