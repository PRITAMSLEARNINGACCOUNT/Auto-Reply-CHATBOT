# AUTO-REPLY CHATBOT

- Created Using GEMINI AI,pyperclip & pyautogui
<!-- - uv is used to make this project -->

# Pre-Requisitory
- Must Have Python Installed Latest Version
- Must Need To Have An API Key From GEMINI API By Google
- `https://ai.google.dev/` grab an API key from this URL simply just by log into your google account

# Installation

1. Fork/Clone/Download this repo

   `git clone https://github.com/PRITAMSLEARNINGACCOUNT/Auto-Reply-CHATBOT`

2. Install uv

   `pip install uv`

3. Create a virtual environment for this project

   `uv venv`

4. Load the virtual environment

   - On Windows Terminal: `.venv\Scripts\activate`
   - On Linux and Git Bash: `source .venv/bin/activate`

5. Run `uv pip install -r requirements.txt`

6. Add Your GEMINI API Key To The System Environmental Varriables

   ### Steps To Add The API Key Grabed From GEMINI API To Your System Environmental Varriable

   - # How to Add a Key to System Environment Variables

     ## Windows

     1. **Open the Start Menu**:

        - Click on the Windows icon in the bottom-left corner of the screen or press the `Windows` key on your keyboard.

     2. **Search for "Environment Variables"**:

        - Type "environment variables" into the search bar and select "Edit the system environment variables" from the results.

     3. **Open Environment Variables Window**:

        - In the System Properties window, click on the "Environment Variables..." button.

     4. **Add a New System Variable**:

        - In the Environment Variables window, you will see two sections: User variables and System variables.
        - Click the "New..." button in the System variables section.

     5. **Enter Variable Name and Value**:

        - In the New System Variable dialog, enter the variable name (e.g., `GEMINI_API_KEY`) in the "Variable name" field.
        - Enter the variable value (e.g., `YOURAPIKEY`) in the "Variable value" field.
        - Click "OK" to save the new variable.

     6. **Apply Changes**:

        - Click "OK" in the Environment Variables window.
        - Click "OK" in the System Properties window to apply the changes.


     ## macOS and Linux

     1. **Open Terminal**:

        - You can open Terminal from the Applications folder or by pressing `Ctrl` + `Alt` + `T` (Linux) or `Cmd` + `Space` and typing `Terminal` (macOS).

     2. **Edit the Profile File**:

        - Depending on the shell you are using (e.g., `bash`, `zsh`), you will need to edit the corresponding profile file:
        - For `bash`, use `.bashrc` or `.bash_profile`.
        - For `zsh`, use `.zshrc`.
        - Open the profile file in a text editor:

        ```sh
        nano ~/.bashrc  # For bash
        nano ~/.zshrc   # For zsh
        ```

     3. **Add the Environment Variable**:

        - Add the following line to the end of the file:

        ```sh
        export GEMINI_API_KEY="YOURAPIKEY"
        ```

     4. **Apply the Changes**:

        - Save the file and exit the editor (`Ctrl` + `X`, then `Y`, then `Enter` for nano).
        - Source the profile file to apply the changes:

        ```sh
        source ~/.bashrc  # For bash
        source ~/.zshrc   # For zsh
        ```

     5. **Verify the Addition**:
        - Type `echo $MY_KEY` to verify that the new environment variable has been added correctly.

7. Run `CHATBOT.py`
