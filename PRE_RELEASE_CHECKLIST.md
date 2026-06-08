# Pre-Release Checklist for v1.1.0

## ✅ Code & Build
- [x] Version updated to 1.1.0 in smart_rename.py
- [x] All features implemented and tested
- [x] Executable built successfully (10.3 MB)
- [x] Executable tested and working
- [x] Icon embedded in executable

## ✅ Documentation
- [x] README.md updated with new features
- [x] CHANGELOG.md updated with v1.1.0 changes
- [x] RELEASE_NOTES_v1.1.0.md created
- [x] Download links point to v1.1.0
- [x] Usage examples updated

## ✅ Files Organization
- [x] executables/ folder created
- [x] SmartRename_v1.0.0.exe moved to executables/
- [x] SmartRename_v1.1.0.exe in executables/
- [x] executables/README.md created
- [x] build/ and dist/ folders cleaned up
- [x] .gitignore updated

## ✅ Git & GitHub
- [ ] All changes committed
- [ ] Pushed to main branch
- [ ] GitHub release created with tag v1.1.0
- [ ] Executable uploaded to release
- [ ] Release notes published
- [ ] Download link tested

## 🧪 Testing Before Release

Test the executable on a clean Windows machine:
1. [ ] Download SmartRename_v1.1.0.exe
2. [ ] Run without Python installed
3. [ ] Enter API key on first run
4. [ ] Test folder path selection (interactive)
5. [ ] Test folder path selection (command-line)
6. [ ] Test folder renaming feature
7. [ ] Test file renaming (basic)
8. [ ] Test iteration (multiple renames)
9. [ ] Test case-only renames
10. [ ] Verify log files created
11. [ ] Check Unicode characters display correctly

## 📝 Git Commands to Execute

```bash
# Stage all changes
git add .

# Commit with descriptive message
git commit -m "Release v1.1.0: Interactive folder selection, folder renaming, and bug fixes

New Features:
- Interactive folder path selection at startup
- Folder/subfolder renaming support with smart detection
- Automatic file list refresh for multiple iterations
- Case-only rename support for Windows

Bug Fixes:
- Fixed rename chain handling
- Fixed case-insensitive collision detection
- Fixed iteration errors
- Added UTF-8 encoding support"

# Push to GitHub
git push origin main

# Create and push tag
git tag -a v1.1.0 -m "Smart Rename v1.1.0"
git push origin v1.1.0
```

## 📦 Files to Upload to GitHub Release

1. **Primary:**
   - `executables/SmartRename_v1.1.0.exe` (10,852,541 bytes)

2. **Optional (source code auto-attached by GitHub):**
   - Source code (zip)
   - Source code (tar.gz)

## 🎯 Post-Release Tasks

- [ ] Verify release appears on GitHub
- [ ] Test download link from release page
- [ ] Update any external documentation
- [ ] Post announcement (optional)
- [ ] Monitor for issues/feedback

## 📊 Release Metrics to Track

- Download count
- Issues reported
- Feature requests
- User feedback

## 🔗 Important Links

- Repository: https://github.com/Ansh-Singh-2000/smartrename
- Releases: https://github.com/Ansh-Singh-2000/smartrename/releases
- Issues: https://github.com/Ansh-Singh-2000/smartrename/issues

---

**Ready to Release?** Follow the [GITHUB_RELEASE_GUIDE.md](GITHUB_RELEASE_GUIDE.md)
