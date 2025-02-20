import os
import sys

# Add the src and tests directories to the Python path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), 'src')))
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), 'tests')))

# Import and run the test module
import test_count_even_numbers
