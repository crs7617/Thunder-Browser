# Thunderbolt Browser README

## Overview
The Thunderbolt Browser is a simple web browser application built using Python and the PyQt5 library. This README provides an overview of the code and its functionality.

## Installation
Make sure you have Python and PyQt5 installed. If not, you can install PyQt5 using the following command:
```
pip install PyQt5
```

You'll also need to have a MySQL database set up with the required schema for the login functionality in the code.

## Usage
1. Run the code by executing the Python script.
2. The Thunderbolt Browser window will open with Google as the default homepage.
3. You can navigate to different web pages using the address bar, forward and backward buttons, and the reload button.
4. The login functionality allows you to log in with a username and password. The login details are stored in a MySQL database.
5. The application menu offers options for File, Edit, View, History, Bookmarks, Window, and Help. The 'History' menu shows some example history entries.

## Files and Components
- `Thunderbolt Browser` is the main application window that integrates the web browser and the GUI.
- The `navigate_to_home` and `navigate_to_url` methods are responsible for navigating to the home page and a user-specified URL, respectively.
- The login functionality is included in the code using a MySQL database.
- The GUI components are created using PyQt5, including buttons, labels, and text fields.
- The application menu is defined with various menu items.

## Dependencies
- PyQt5: Used for the graphical user interface.
- PyQt5.QtWebEngineWidgets: Used for the web browser component.
- PyQt5.QtGui: Used for icon handling.
- PyQt5.QtCore: Provides core functionality.
- PyQt5.QtWidgets: Used for various GUI widgets.
- MySQL Connector: Used for database connectivity.

## License
This code is provided under an open-source license. You are free to use, modify, and distribute it as needed.

## Credits
The Thunderbolt Browser code is developed by the author, and it utilizes various open-source libraries.

## Contact Information
For any questions or issues, you can contact the author at [your-email@example.com].

Enjoy browsing with Thunderbolt Browser!



sample on how the web browser looks once it runs along with account details of the users stored and accessed in mysql through the mysql.connector:

![Screenshot (843)](https://github.com/crs7617/Python-project/assets/115174268/7e03177b-d407-47be-9bdd-acd8a2c6d80a)

![Screenshot (848)](https://github.com/crs7617/Python-project/assets/115174268/85e13517-1541-4211-b369-19da83909367)

![Screenshot (852)](https://github.com/crs7617/Python-project/assets/115174268/1a514066-2ca7-4eef-a345-44b3efb8c365)

**
