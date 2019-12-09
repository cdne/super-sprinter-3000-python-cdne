import csv
import os

DATA_FILE_PATH = os.getenv('DATA_FILE_PATH') if 'DATA_FILE_PATH' in os.environ else 'data.csv'
DATA_HEADER = ['id', 'title', 'user_story', 'acceptance_criteria', 'business_value', 'estimation', 'status']
STATUSES = ['planning', 'todo', 'in progress', 'review', 'done']


def get_all_user_story():
    return []


# Read content from desired file and returns a dictionary
def read_csv(file_name):
    story_list = []
    with open(file_name, 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            story_list.append(row)
    return story_list

# Write content to file
def write_csv(file_name, data):
    with open(file_name, 'w+', newline='') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=DATA_HEADER)
        writer.writeheader()
        for story in data:
            writer.writerow(story)
