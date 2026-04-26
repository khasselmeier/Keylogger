# Keylogger

[View the Presentation Slides](https://docs.google.com/presentation/d/1FQDtQlvo8MWzE7AneAfe0fXCZojN-DxeJzJn0ir-sKE/edit?usp=sharing)

## Project Summary 
This project is a Python-based keylogger that captures keyboard input, collects system information, stores data locally, and removes logs after execution.
It demonstrates system-level input monitoring while highlighting cybersecurity and privacy risks.

## Tools Used / Setup
### Libraries
- 'socket' - Retrieves hostname and network information
- 'platform' - Collects system, processor, and machine details
- 'time' - Controls execution timing and delays
- 'os' - Handles file creation and deletion
- 'pynput' - Captures keyboard events in real time

### Environment
- Python 3.14
- Window OS
- Local file storage for logs

### Project Architecture
1. System information collection
2. Keyboard listener
3. Keystroke processing
4. Log file storage
5. Timing and loop control
6. File deletion and cleanup

## Future Project Directions
- Encrypt stored log files
- Improve keystroke filtering and classification
- Add screenshot capture functionality
- Implement secure network transmission of logs
