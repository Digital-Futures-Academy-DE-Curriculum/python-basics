import os

cwd = os.getcwd()
demo_file_path = os.path.join(cwd, '..', 'trainer_demo_files', 'demo_files', 'data.txt')

try:
    file = open(demo_file_path)
    # lunch = False
    # question = "Is it lunch yet?"
    # response = lunch + question
except FileNotFoundError:
    print("FileNotFoundError: That file does not exist")
    
except OSError as e:
    print(f'OSError: {e}')
except TypeError as e:
    print(f'TypeError: {e}')
except Exception as e:
    print(f'An error occurred: {e}')
finally:
    print("happens regardless of the outcome")

print("hello world")
