# Contact Book Application

A simple contact book application built using Python and Tkinter. This application allows users to add, edit, delete, view, and reset contact information.

## Features

- Add new contacts
- Edit existing contacts
- Delete contacts
- View contact details
- Reset the form
- List of contacts displayed in a listbox

## Requirements

- Python 3.x
- Tkinter (usually included with Python)

## Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/yourusername/contact-book.git
    ```
2. Navigate to the project directory:
    ```bash
    cd contact-book
    ```

## How to Use

1. **Run the Application**:
    ```bash
    python contact_book.py
    ```

2. **Add a Contact**:
    - Fill in the "Name", "Contact No.", and "Email" fields.
    - Click the "Add" button.

3. **Edit a Contact**:
    - Select a contact from the list.
    - Modify the details in the "Name", "Contact No.", and "Email" fields.
    - Click the "Edit" button.

4. **Delete a Contact**:
    - Select a contact from the list.
    - Click the "Delete" button.

5. **View a Contact**:
    - Select a contact from the list.
    - Click the "View" button to display the details in the form fields.

6. **Reset the Form**:
    - Click the "Reset" button to clear all form fields.

7. **Exit the Application**:
    - Click the "Exit" button to close the application.

## Code Overview

### Main Application Setup

The main application window is set up using Tkinter, with a frame for the listbox and scrollbar.

### Functions

- `add_contact()`: Adds a new contact to the contact list.
- `edit_contact()`: Edits the selected contact.
- `delete_contact()`: Deletes the selected contact.
- `view_contact()`: Displays the details of the selected contact.
- `reset_form()`: Resets the form fields.
- `update_listbox()`: Updates the listbox with the current contacts.
- `exit_app()`: Exits the application.
