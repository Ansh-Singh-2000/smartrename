# Changelog

## [1.1.0] - 2026-06-08

### Added
- **Interactive Folder Selection**: At startup, user can press Enter for current directory or type a folder path
  - Command-line support: `python smart_rename.py "C:\path\to\folder"`
  - Interactive prompt: Just enter path when asked or press Enter for current directory
  - Executable support: `SmartRename.exe "C:\path\to\folder"`
  
- **Folder Renaming**: Optional ability to rename subfolders
  - Interactive prompt: "Include folders for renaming? (y/n)"
  - Only asks if folders exist in the directory
  - Works alongside file renaming
  - Same AI intelligence and safety features apply

### Changed
- Updated version to 1.1.0
- Enhanced system prompts to handle both files and folders
- Improved item scanning logic
- Smart folder detection: only prompts for folder renaming if folders exist

### Fixed
- Added UTF-8 encoding support for Windows console to handle Unicode characters properly
- Fixed rename chain handling to prevent "File not found" errors when renaming creates temporary conflicts
- Improved rename execution with proper ordering and temporary name resolution for deadlocks

## [1.0.0] - 2026-05-01

### Features
- Natural language file renaming
- AI-powered with Groq LLM
- Safe operations with preview mode
- Collision detection
- Backup logging
- Interactive AI conversations
- Comprehensive error handling
