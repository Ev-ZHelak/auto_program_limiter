# Simple Time Limit for Programs

This script allows you to set time limits for the execution of specific programs.

## Dependencies
- psutil
- pyttsx3

## Usage
1. Install the necessary dependencies if they haven't been installed yet.
2. Create a file named `Killist.txt` with information about time limits and the programs to be launched.
3. Run the script.

## Format of Killist.txt
Each line in the `Killist.txt` file should contain the following information:

```
program_name time_limit_in_minutes days_of_week
```

For example:

```
chrome.exe 30 1 2 3 4 5
notepad.exe 15 6 7
```

This means that the `chrome` program can run for up to 30 minutes on Monday, Tuesday, Wednesday, Thursday, and Friday. The `notepad` program can run for up to 15 minutes on Saturday and Sunday.

## Notes
- Running programs are monitored in an infinite loop.
- If a program exceeds the set time limit, it will be automatically closed.
- Information about launches and closures is recorded in the `programs.json` file.

**Attention: Use this script responsibly and ensure it complies with local laws and policies of your organization.**
