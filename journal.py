import argparse
import json
import os


class JournalApp:
    """
    A journaling app that supports multiple users, creating entries, listing entries,
    deleting individual entries, and deleting entire journals.

    Attributes:
        data_file (str): Path to the JSON file used to persist journal data.
    """

    def __init__(self, data_file="journals.json"):
        """
        Initialize the JournalApp with the specified data file.

        Args:
            data_file (str): Path to the JSON file for storing journal data.
        """
        self.data_file = data_file
        if not os.path.exists(self.data_file):
            self._initialize_file()

    def _initialize_file(self):
        """Create an empty JSON file to store journal data."""
        with open(self.data_file, "w") as file:
            json.dump({}, file)

    def load_journals(self):
        """
        Load all journal data from the JSON file.

        Returns:
            dict: A dictionary where keys are usernames and values are lists of journal entries.
        """
        with open(self.data_file, "r") as file:
            return json.load(file)

    def save_journals(self, journals):
        """
        Save all journal data to the JSON file.

        Args:
            journals (dict): A dictionary containing all journal data.
        """
        with open(self.data_file, "w") as file:
            json.dump(journals, file, indent=4)

    def create_entry(self, user, title, content):
        """
        Create a new journal entry for a user.

        Args:
            user (str): Username to associate with the entry.
            title (str): Title of the journal entry.
            content (str): Content of the journal entry.
        """
        journals = self.load_journals()
        if user not in journals:
            journals[user] = []
        journals[user].append({"title": title, "content": content})
        self.save_journals(journals)
        print(f"Journal entry '{title}' added for user '{user}'.")

    def list_entries(self, user):
        """
        List all journal entries for a user.

        Args:
            user (str): Username whose entries are to be listed.

        Expected Output:
            Prints the list of all journal entry titles for the user.
            If no entries exist, prints a message indicating no entries were found.
        """
        journals = self.load_journals()
        if user not in journals or not journals[user]:
            print(f"No journal entries found for user '{user}'.")
            return
        print(f"Journal Entries for '{user}':")
        for i, entry in enumerate(journals[user], 1):
            print(f"{i}. {entry['title']}")

    def delete_entry(self, user, title):
        """
        Delete a specific journal entry for a user by its title.

        Args:
            user (str): Username whose entry is to be deleted.
            title (str): Title of the journal entry to delete.
        """
        journals = self.load_journals()
        if user not in journals:
            print(f"No entries found for user '{user}'.")
            return
        journals[user] = [entry for entry in journals[user] if entry["title"] != title]
        self.save_journals(journals)
        print(f"Deleted entry '{title}' for user '{user}'.")

    def delete_journal(self, user):
        """
        Delete all journal entries for a user.

        Args:
            user (str): Username whose journal is to be deleted.
        """
        journals = self.load_journals()
        if user in journals:
            del journals[user]
            self.save_journals(journals)
            print(f"Deleted entire journal for user '{user}'.")
        else:
            print(f"No journal found for user '{user}'.")


def main():
    """
    Main function to parse arguments and execute commands.

    Args:
        None. Arguments are parsed from the command line.
    
    Returns:
        Executes the specified command based on the provided arguments.
    """
    parser = argparse.ArgumentParser(description="Multi-User Journaling App")
    subparsers = parser.add_subparsers(dest="command")

    # Create entry command
    create_parser = subparsers.add_parser("create", help="Create a new journal entry")
    create_parser.add_argument("--user", required=True, help="Username")
    create_parser.add_argument("--title", required=True, help="Title of the journal entry")
    create_parser.add_argument("--content", required=True, help="Content of the journal entry")

    # List entries command
    list_parser = subparsers.add_parser("list", help="List all journal entries")
    list_parser.add_argument("--user", required=True, help="Username")

    # Delete entry command
    delete_entry_parser = subparsers.add_parser("delete_entry", help="Delete a journal entry")
    delete_entry_parser.add_argument("--user", required=True, help="Username")
    delete_entry_parser.add_argument("--title", required=True, help="Title of the journal entry to delete")

    # Delete journal command
    delete_journal_parser = subparsers.add_parser("delete_journal", help="Delete an entire journal")
    delete_journal_parser.add_argument("--user", required=True, help="Username")

    args = parser.parse_args()

    app = JournalApp()

    if args.command == "create":
        app.create_entry(args.user, args.title, args.content)
    elif args.command == "list":
        app.list_entries(args.user)
    elif args.command == "delete_entry":
        app.delete_entry(args.user, args.title)
    elif args.command == "delete_journal":
        app.delete_journal(args.user)
    else:
        parser.print_help()


if __name__ == "__main__":
    main()
