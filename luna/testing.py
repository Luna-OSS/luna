"""Provides a function to run tests in a module."""

import sys
import traceback

def run_tests(tests_module):
    """Runs the tests in the given module."""

    success = False

    tester = None

    try:
        tester = tests_module.Tester()

    # pylint: disable=broad-except
    except Exception:
        print('-----BEGIN LUNA ERROR-----')
        traceback.print_exc()
        print('-----END LUNA ERROR-----')

    else:
        success = True
        print('-----LUNA SUCCESS-----')

    finally:
        try:
            tester.stop()
        except AttributeError:
            pass

    sys.exit(int(not success))
