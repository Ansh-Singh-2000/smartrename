# Smart Rename 🚀

An AI-powered file renaming tool that understands natural language. Stop wasting time on repetitive file renames!

## Features ✨

- **Natural Language Interface** - Just describe what you want: "capitalize first letter of all files ending with 5"
- **Smart AI** - Powered by Groq's fast LLM (llama-3.3-70b-versatile)
- **Safe Operations** - Preview changes, collision detection, automatic backup logs
- **Interactive** - AI asks for clarification when needed
- **Production Ready** - Comprehensive error handling and edge case coverage

## Quick Start 🏃

### 1. Install Dependencies

```bash
pip install -r requirements.txt
```

### 2. Run the Tool

```bash
python smart_rename.py
```

On first run, you'll be prompted to enter your Groq API key:
- Visit [Groq Console](https://console.groq.com)
- Sign up for free
- Create an API key
- Paste it when prompted

Your API key will be securely saved in `~/.smartrename/config.json` and reused automatically.

## Usage Examples 💡

```
You: capitalize first letter of all files
AI: [Shows preview of changes]
Proceed with rename? (y/n): y
✓ Successfully renamed 15/15 file(s)

You: replace spaces with underscores in all txt files
AI: [Shows preview]

You: add prefix "backup_" to files ending with .log
AI: [Shows preview]

You: rename all images to img_001, img_002, etc
AI: [Shows preview]
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

**Pro Tip**: Run the tool in the directory you want to rename files in. It only affects the current directory (non-recursive).
