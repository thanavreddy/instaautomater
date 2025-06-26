# Instagram Automater

A Python automation script that uses Selenium WebDriver to log into Instagram, search for a specific profile, follow the account, and extract basic profile statistics.

## Features

- Automated Instagram login
- Profile search functionality  
- Automatic following of target profiles
- Profile statistics extraction (posts, followers, following count)
- Data export to text file
- Error handling with screenshot capture

## Prerequisites

Before running this script, ensure you have the following installed:

- Python 3.7 or higher
- Google Chrome browser
- ChromeDriver (compatible with your Chrome version)

## Installation

1. Clone this repository:
```bash
git clone https://github.com/thanavreddy/instaautomater.git
cd instaautomater
```

2. Install required Python packages:
```bash
pip install selenium
```

3. Download ChromeDriver:
   - Visit [ChromeDriver Downloads](https://chromedriver.chromium.org/)
   - Download the version matching your Chrome browser
   - Add ChromeDriver to your system PATH or place it in the project directory

## Configuration

1. Open the script file and update the login credentials:
```python
USERNAME = "your_instagram_username"
PASSWORD = "your_instagram_password"
```

2. Modify the target profile to search for (currently set to "cbitosc"):
```python
search_input.send_keys("target_username")
```

## Usage

Run the script using Python:
```bash
python main.py
```

## What the Script Does

1. **Login Process**: Automatically logs into Instagram using provided credentials
2. **Popup Handling**: Dismisses common Instagram popups like "Save Info" and notification prompts
3. **Profile Search**: Searches for the specified Instagram profile
4. **Follow Action**: Attempts to follow the target profile (skips if already following)
5. **Data Extraction**: Retrieves profile statistics including post count, followers, and following count
6. **File Export**: Saves extracted data to `cbitosc_profile.txt`

## Output

The script generates a text file named `cbitosc_profile.txt` containing:
- Profile name
- Number of posts
- Follower count
- Following count

Example output:
```
CBIT OSC Instagram Profile
Posts: 150
Followers: 2,543
Following: 312
```

## Error Handling

- The script includes comprehensive error handling
- If an error occurs, a screenshot is automatically saved as `error.png`
- Console output provides status updates and error messages

## Important Notes

### Legal and Ethical Considerations
- This script is for educational purposes only
- Ensure you comply with Instagram's Terms of Service
- Respect rate limits and avoid excessive automation
- Only use this script on accounts you own or have explicit permission to access

### Security Warnings
- **Never commit your actual Instagram credentials to version control**
- Consider using environment variables for sensitive information
- Be cautious when sharing this code with hardcoded credentials

### Limitations
- Instagram frequently updates their UI, which may break element selectors
- The script may require updates to XPath selectors over time
- Rate limiting by Instagram may affect script performance

## Troubleshooting

### Common Issues

**ChromeDriver not found**
- Ensure ChromeDriver is installed and in your PATH
- Verify ChromeDriver version matches your Chrome browser version

**Element not found errors**
- Instagram may have changed their UI structure
- Try increasing wait times in the script
- Check the error screenshot for visual debugging

**Login failures**
- Verify your Instagram credentials are correct
- Check if your account requires two-factor authentication
- Ensure your account is not temporarily restricted

### Debug Mode
To enable more detailed debugging:
1. Check the generated `error.png` screenshot
2. Add additional `time.sleep()` statements to slow down execution
3. Use browser developer tools to inspect current page elements

## Dependencies

- `selenium`: Web automation framework
- `webdriver`: Chrome WebDriver for browser control
- `time`: Built-in Python module for delays
