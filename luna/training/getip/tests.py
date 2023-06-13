"""LUNA Tests."""

import os
import requests
import subprocess

class Tester:
    """Tests if the program is working as expected."""

    def __init__(self):
        """Runs the tests."""

        # check the print output of cli.app.main()
        os.chdir(os.path.dirname(__file__))
        output = subprocess.check_output(['python', 'cli.py']).decode('utf8')

        ip_addr = requests.get('https://checkip.amazonaws.com', timeout=5).text.strip()
        assert ip_addr in output

    def stop(self):
        """Runs after the tests are done, whether they have been successful or not."""
        # no need to stop anything
