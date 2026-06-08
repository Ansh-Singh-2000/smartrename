# Smart Rename v1.1.0 Release Notes

## 🎉 What's New

### Interactive Folder Selection
- **No more running in wrong directory!** At startup, you can now:
  - Press Enter to use current directory
  - Type any folder path to work in that directory
- Command-line support still works: `SmartRename.exe "D:\Your\Folder"`

### Folder Renaming Support
- **Rename subfolders too!** The tool now asks if you want to include folders for renaming
- Only asks when folders exist in the directory (smart detection)
- Same AI intelligence and safety features for both files and folders

### Better Iteration Support
- **Make multiple changes easily!** File list automatically refreshes after each rename
- Conversation history clears for fresh context each time
- No more errors when renaming the same files multiple times

### Case-Only Renames (Windows)
- **Capitalize with confidence!** Now properly handles case-only renames like:
  - `example.txt` → `Example.txt`
  - `myFolder` → `MyFolder`
- Uses temporary intermediate files to ensure Windows compatibility

## 🐛 Bug Fixes

- Fixed "File not found" errors when renaming creates name chains
- Fixed collision detection for case-insensitive Windows filesystem
- Fixed iteration errors when working with same files multiple times
- Added UTF-8 encoding support for proper Unicode display in Windows console

## 🔧 Technical Improvements

- Smart rename chain handling with automatic ordering
- Deadlock resolution using temporary names
- Case-insensitive collision detection on Windows
- Enhanced file list refresh logic
- Better error messages and user feedback

## 📋 Full Changelog

See [CHANGELOG.md](CHANGELOG.md) for complete details.

## 🚀 Upgrading from v1.0.0

Simply download the new executable - your API key and settings are preserved in `~/.smartrename/config.json`

No breaking changes! All v1.0.0 features work exactly the same way.

## 💡 Usage Examples

### Example 1: Work in Different Folder
```
Press Enter to use current directory, or enter folder path:
> D:\Documents\Photos

Include folders for renaming? (y/n): n
Found 50 file(s)

You: add prefix "vacation_"
✓ Successfully renamed 50/50 file(s)
```

### Example 2: Rename Folders
```
Press Enter to use current directory, or enter folder path:
> [Press Enter]

Include folders for renaming? (y/n): y
Found 10 item(s)

You: replace spaces with underscores in folder names
✓ Successfully renamed 3/3 item(s)
```

### Example 3: Multiple Iterations
```
You: lowercase all files
✓ Successfully renamed 20/20 file(s)
File list refreshed

You: add date prefix "2026-06-08_"
✓ Successfully renamed 20/20 file(s)
File list refreshed

You: capitalize first letter
✓ Successfully renamed 20/20 file(s)
```

## 🙏 Thank You

Thanks to all users who reported issues and suggested improvements!

---

**Created by Ansh Singh**  
🌐 [anshverse.in](https://anshverse.in)  
📱 [@a.n.s.h_chauhan_](https://instagram.com/a.n.s.h_chauhan_)
