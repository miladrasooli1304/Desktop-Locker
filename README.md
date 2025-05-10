# Desktop Locker

## Overview
This is a Python script that locks your desktop with a password-protected screen, preventing unauthorized access while keeping your laptop running. I created this because sometimes I need to step away from my laptop but don’t want to shut it down, and I also don’t want anyone messing with my system. This tool helps me secure my desktop easily.

The script uses a fullscreen window with adjustable opacity, a password input field, and a timer for automatic unlocking after a specified period. It’s built with `tkinter` for the GUI and `pywin32` for Windows-specific functionality.

## Features
- Locks the desktop with a password-protected fullscreen window.
- Configurable timer to automatically unlock after a set time (default: 2000 seconds).
- Adjustable screen opacity (default: 10% black).
- Prevents common key combinations (e.g., Alt+Tab, Ctrl+Alt+Delete) from bypassing the lock.
- Simple and lightweight.

## Requirements
- Python 3.6 or higher
- Windows operating system (due to `pywin32` dependency)
- Required Python libraries:
  - `tkinter` (included with Python)
  - `pywin32`

## Installation
1. **Clone the repository**:
   ```bash
   git clone https://github.com/your-username/desktop-locker.git
   cd desktop-locker
   ```

2. **Install dependencies**:
   Ensure Python is installed, then install `pywin32`:
   ```bash
   pip install pywin32
   ```

## Usage
1. **Run the script**:
   Execute the Python script directly:
   ```bash
   python desktop_locker.py
   ```

2. **How it works**:
   - The desktop will be locked with a fullscreen black window (10% opacity by default).
   - Enter the password (default: `92327311304m`) to unlock.
   - If the password is incorrect, an error message will appear.
   - The screen will automatically unlock after the timer expires (default: 2000 seconds).
   - The timer countdown is displayed on the screen.

3. **Customize settings**:
   Modify the following variables at the top of `desktop_locker.py`:
   - `PASSWORD`: Set your desired password.
   - `TIMEOUT_SECONDS`: Change the auto-unlock timer (in seconds).
   - `OPACITY_LEVEL`: Adjust the screen opacity (0.0 to 1.0, where 1.0 is fully black).

## Converting to Executable (.exe)
To create a standalone `.exe` file for easier use:
1. Install `auto-py-to-exe`:
   ```bash
   pip install auto-py-to-exe
   ```
2. Run `auto-py-to-exe`:
   ```bash
   auto-py-to-exe
   ```
3. In the GUI:
   - Select `desktop_locker.py`.
   - Choose **One File** or **One Directory**.
   - (Optional) Add a custom icon (`.ico` file).
   - Click **Convert .py to .exe**.
4. Find the `.exe` in the `output` folder and run it.

## Notes
- **Antivirus**: Some antivirus programs may flag the `.exe` as suspicious. You can temporarily disable your antivirus or digitally sign the `.exe`.
- **Testing**: Test the `.exe` on a system without Python to ensure all dependencies are included.
- **Limitations**: This script is designed for Windows due to `pywin32`. It may not work on macOS or Linux.
- **Security**: While this script prevents casual access, it’s not a substitute for professional security software for sensitive systems.

## Contributing
Feel free to fork this repository, make improvements, and submit pull requests. If you encounter issues or have suggestions, please open an issue on GitHub.

## License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.