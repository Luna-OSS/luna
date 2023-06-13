"""LUNA Tests."""

import time
import multiprocessing
import requests

class Tester:
    """Tests if the program is working as expected."""

    def __init__(self):
        """Runs the tests."""
        # pylint: disable=import-outside-toplevel
        import main

        self.server = multiprocessing.Process(target=main.run, args=(5000,))
        self.server.start()

        time.sleep(1)
        print('Server started!')

        resp = requests.get('http://localhost:5000/', timeout=5)
        assert 'The current time is:' in resp.text

    def stop(self):
        """Runs after the tests are done, whether they have been successful or not."""
        self.server.terminate()
