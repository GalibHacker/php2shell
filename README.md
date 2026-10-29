Execution Steps:
1. Run python3 shell_generator.py to create the PHP file.
2. Edit reverseshell.php to change TARGETIP to your machine's IP address.
3. Run python3 netcat_listener.py to start the listener.
4. Upload reverse_shell.php to the target server using the bash script or manually.
5. Trigger the file by accessing http://target.com/reverse_shell.php in a browser.
6. Receive the interactive shell in your Python listener.
