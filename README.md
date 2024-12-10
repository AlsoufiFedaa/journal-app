
A simple command-line application that allows users to create, view, and manage their journal entries. The app supports multiple users and persists journal entries in a JSON file.

# Features
Create New Journal Entries: Users can add a new journal entry with a title and content.
List All Journal Entries: Users can view the titles of all their journal entries.
Support for Multiple Users: Each user has their own set of journal entries.
Delete Journal Entries: Users can delete a specific journal entry or an entire journal.
Data Persistence: Journal entries are saved in a JSON file, so they persist between sessions.
Requirements
Python 3.x

# Installation
Clone this repository to your local machine:

git clone https://github.com/your-username/journal-app.git
Navigate into the project directory:


cd journal-app
Run the app using Python:

python journal.py

# Usage
Create a New Journal Entry
To create a new journal entry, use the following command:


python journal.py --create "Contents of a new journal entry" --title "Title of entry"
List All Journal Entries
To list all journal entries, use:

python journal.py --list
Delete a Specific Journal Entry
To delete a journal entry, use:

python journal.py --delete "Title of entry"
Delete All Journal Entries
To delete all journal entries (clear the entire journal), use:

python journal.py --delete-all
Example
Here’s an example of how you might use the journaling app:

# Create a new journal entry
python journal.py --create "Today I learned Python!" --title "Learning Python"

# List all journal entries
python journal.py --list

# Delete a journal entry
python journal.py --delete "Learning Python"
File Structure
journal.py: The main file for running the journaling app.
journals.json: The JSON file that stores the journal entries.
Data Persistence
Journal entries are saved in the journals.json file. Each entry consists of a title, content, and timestamp. The file is updated whenever a new entry is created or deleted.

# Example of a journal entry in the JSON file:

json
Copy code
{
  "entries": [
    {
      "title": "Learning Python",
      "content": "Today I learned Python!",
      "timestamp": "2024-12-08T14:30:00"
    }
  ]
}
