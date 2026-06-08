# GitHub Release Guide for v1.1.0

## Step-by-Step Instructions

### 1. Commit and Push Changes

```bash
git add .
git commit -m "Release v1.1.0: Interactive folder selection, folder renaming, and bug fixes"
git push origin main
```

### 2. Create GitHub Release

1. Go to your repository: https://github.com/Ansh-Singh-2000/smartrename
2. Click on "Releases" (right sidebar)
3. Click "Draft a new release"

### 3. Fill in Release Details

**Tag version:** `v1.1.0`  
- Click "Choose a tag"
- Type: `v1.1.0`
- Select "Create new tag: v1.1.0 on publish"

**Target:** `main` (default)

**Release title:** `Smart Rename v1.1.0 - Interactive Folder Selection & Folder Renaming`

**Description:** Copy and paste from `RELEASE_NOTES_v1.1.0.md` (or use the content below)

### 4. Upload Executable

Click "Attach binaries by dropping them here or selecting them"

Upload: `executables/SmartRename_v1.1.0.exe`

### 5. Publish Release

- ✅ Make sure "Set as the latest release" is checked
- Click "Publish release"

---

## Release Description Template

```markdown
# Smart Rename v1.1.0

## 🎉 What's New

### Interactive Folder Selection
- At startup, press Enter for current directory or type any folder path
- No more running in the wrong directory!
- Command-line support: `SmartRename_v1.1.0.exe "D:\Your\Folder"`

### Folder Renaming Support  
- Rename subfolders in addition to files
- Smart detection: only asks if folders exist
- Same AI intelligence for both files and folders

### Better Iteration Support
- File list automatically refreshes after each rename
- Make multiple changes without restarting
- Conversation history clears for fresh context

### Case-Only Renames (Windows)
- Properly handles: `example.txt` → `Example.txt`
- Uses temporary files for Windows compatibility
- No more collision errors for case changes

## 🐛 Bug Fixes

- Fixed "File not found" errors with rename chains
- Fixed collision detection for case-insensitive filesystems
- Fixed iteration errors when renaming same files multiple times
- Added UTF-8 encoding for proper Unicode display

## 📥 Download

**Windows Executable (Recommended):**
- [SmartRename_v1.1.0.exe](https://github.com/Ansh-Singh-2000/smartrename/releases/download/v1.1.0/SmartRename_v1.1.0.exe) (10.3 MB)
- No Python required
- Portable - run from anywhere

**Or run from source:**
```bash
git clone https://github.com/Ansh-Singh-2000/smartrename.git
cd smartrename
pip install -r requirements.txt
python smart_rename.py
```

## 🚀 Quick Start

1. Download the executable above
2. Double-click to run
3. Press Enter for current directory or type folder path
4. Enter your [free Groq API key](https://console.groq.com) (first run only)
5. Start renaming with natural language!

## 💡 Usage Examples

**Example 1: Work in Different Folder**
```
Press Enter to use current directory, or enter folder path:
> D:\Documents\Photos

You: add "vacation_" prefix to all files
✓ Successfully renamed 50/50 file(s)
```

**Example 2: Rename Folders**
```
Include folders for renaming? (y/n): y

You: replace spaces with underscores
✓ Successfully renamed 15/15 item(s)
```

**Example 3: Capitalize Filenames**
```
You: capitalize first letter of all files
✓ Successfully renamed 20/20 file(s)
```

## 🔄 Upgrading from v1.0.0

Simply download the new executable - your API key is preserved!

No breaking changes. All v1.0.0 features work the same way.

## 📋 Full Changelog

See [CHANGELOG.md](CHANGELOG.md) for complete details.

---

**Created by Ansh Singh**  
🌐 [anshverse.in](https://anshverse.in)  
📱 [@a.n.s.h_chauhan_](https://instagram.com/a.n.s.h_chauhan_)

**Previous Release:** [v1.0.0](https://github.com/Ansh-Singh-2000/smartrename/releases/tag/v1.0.0)
```

---

## After Publishing

1. Update any external links pointing to the download
2. Test the download link works
3. Announce on social media if desired
4. Consider creating a GitHub discussion post

## Verification Checklist

- [ ] Tag is `v1.1.0`
- [ ] Executable uploaded: `SmartRename_v1.1.0.exe`
- [ ] Marked as latest release
- [ ] Release notes are clear and complete
- [ ] Download link tested
