class Notebook:
    """A class to store and display notes."""

    def __init__(self):
        """Initialize an empty list of notes."""
        self.notes = []

    def add_note(self, note):
        """Add a new note to the notebook."""
        self.notes.append(note)

    def show_notes(self):
        """Display all stored notes with numbering."""
        for index, note in enumerate(self.notes, start=1):
            print(f"{index}. {note}")


# Create a Notebook object
my_notebook = Notebook()

# Add three notes
my_notebook.add_note("Buy groceries")
my_notebook.add_note("Read a book")
my_notebook.add_note("Call the doctor")

# Display all notes
my_notebook.show_notes()