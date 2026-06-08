# Smart Rename 🚀

An AI-powered file renaming tool that understands natural language. Stop wasting time on repetitive file renames!

## Download 📥

**Want to skip the setup?** Download the standalone executable:

👉 [SmartRename_v1.1.0.exe (10.3 MB)](https://github.com/Ansh-Singh-2000/smartrename/releases/download/v1.1.0/SmartRename_v1.1.0.exe)

- ✅ No Python installation required
- ✅ No dependencies to install
- ✅ Just download and run
- ✅ Works on any Windows PC

On first run, you'll be prompted for a free Groq API key (takes 1 minute to get).

**Previous Versions:** [v1.0.0](https://github.com/Ansh-Singh-2000/smartrename/releases/tag/v1.0.0)

## Features ✨

- **Natural Language Interface** - Just describe what you want: "capitalize first letter of all files ending with 5"
- **Smart AI** - Powered by Groq's fast LLM (llama-3.3-70b-versatile)
- **Flexible Directory** - Run from any folder or specify target folder path
- **Folder Renaming** - Works with files AND folders (optional)
- **Safe Operations** - Preview changes, collision detection, automatic backup logs
- **Interactive** - AI asks for clarification when needed
- **Production Ready** - Comprehensive error handling and edge case coverage

## Quick Start 🏃

### Option 1: Use the Executable (Easiest)

1. Download [SmartRename_v1.1.0.exe](https://github.com/Ansh-Singh-2000/smartrename/releases/download/v1.1.0/SmartRename_v1.1.0.exe)
2. Place it anywhere on your computer
3. Double-click to run
4. Enter folder path or press Enter for current directory
5. Enter your Groq API key when prompted (first run only)
6. Start renaming!

### Option 2: Run from Source

### 1. Install Dependencies

```bash
pip install -r requirements.txt
```

### 2. Run the Tool

```bash
# Run in current directory
python smart_rename.py

# Or specify a target folder
python smart_rename.py "C:\path\to\folder"
```

On first run, you'll be prompted to enter your Groq API key:
- Visit [Groq Console](https://console.groq.com)
- Sign up for free
- Create an API key
- Paste it when prompted

Your API key will be securely saved in `~/.smartrename/config.json` and reused automatically.

**New in v1.1.0:**
- The tool will ask if you want to include folders for renaming
- Choose 'y' to rename both files and folders
- Choose 'n' for files only (default behavior)

## Usage Examples 💡

### Basic Workflow
```
# Step 1: Run the tool
python smart_rename.py

# Step 2: Choose directory
Press Enter to use current directory, or enter folder path:
> D:\Documents\Photos    (or just press Enter for current dir)

# Step 3: Choose if folders should be included
Include folders for renaming? (y/n): n

Found 15 file(s)

# Step 4: Make your request
You: capitalize first letter of all files
AI: [Shows preview of changes]
Proceed with rename? (y/n): y
✓ Successfully renamed 15/15 file(s)
```

### File Renaming Examples
```
You: replace spaces with underscores in all txt files
AI: [Shows preview]

You: add prefix "backup_" to files ending with .log
AI: [Shows preview]

You: rename all images to img_001, img_002, etc
AI: [Shows preview]
```

### Folder Renaming
```
Include folders for renaming? (y/n): y

You: add "project_" prefix to all folders
AI: [Shows preview of folder renames]

You: replace spaces with dashes in folder names
AI: [Shows preview]
```

### Using Command-Line Argument
```bash
# You can also specify folder directly via command line
python smart_rename.py "D:\Documents\Photos"

# Or with executable
SmartRename_v1.1.0.exe "C:\Users\Name\Downloads"
```

## Safety Features 🛡️

- **Backup Logs** - Every rename operation creates a timestamped log file
- **Collision Detection** - Prevents overwriting existing files
- **Preview Mode** - Always shows changes before applying
- **File Validation** - Checks for invalid characters and system files
- **Limits** - Warns on 100+ files, blocks 500+ files

## Building Executable 📦

Convert to standalone .exe (no Python required):

```bash
# Run the build script
build.bat

# Or manually:
pip install pyinstaller
pyinstaller --onefile --name SmartRename smart_rename.py

# Find executable in dist/ folder
```

Note: You'll still need to enter your API key on first run of the .exe

## Project Structure 📁

```
Smart Rename/
├── smart_rename.py      # Main application
├── requirements.txt     # Python dependencies
├── build.bat           # Executable builder
└── README.md           # This file

User config stored at:
~/.smartrename/config.json  # API key storage
```

## Technical Details 🔧

- **Language**: Python 3.7+
- **AI Model**: llama-3.3-70b-versatile (via Groq) - configurable
- **Dependencies**: groq (official SDK)
- **File Limits**: 500 files max, 100 warning threshold
- **Config Storage**: ~/.smartrename/config.json

### Model Configuration

If the default model becomes unavailable, the tool will:
1. Detect the error automatically
2. Prompt you to visit https://console.groq.com/docs/models
3. Ask you to enter a new model name
4. Validate and save the new model
5. Continue working seamlessly

## Error Handling

The tool handles:
- Missing API keys
- Network failures
- Invalid file names
- Permission errors
- Name collisions
- Large directories
- Malformed AI responses

## Contributing 🤝

Found a bug? Have a feature request? Feel free to open an issue!

## License 📄

MIT License - Feel free to use and modify!

## Author 👨‍💻

Created by Ansh Singh

🌐 Website: [anshverse.in](https://anshverse.in)

📱 Instagram: [@a.n.s.h_chauhan_](https://instagram.com/a.n.s.h_chauhan_)

Need help? Feel free to reach out!

---

**Pro Tip**: At startup, just press Enter to work in current directory, or type any folder path to work there. Enable folder renaming to rename subfolders too!
