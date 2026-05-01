#!/usr/bin/env python3
"""
Smart Rename - AI-powered file renaming tool
Author: Ansh Singh
Website: anshverse.in
"""

import os
import json
import sys
from datetime import datetime
from pathlib import Path
from typing import List, Dict, Optional, Tuple
from groq import Groq

# Constants
VERSION = "1.0.0"
AUTHOR = "Ansh Singh"
WEBSITE = "anshverse.in"
MAX_FILES_WARNING = 100
MAX_FILES_HARD_LIMIT = 500
MODEL = "llama-3.3-70b-versatile"
EXCLUDED_PATTERNS = ['.git', '__pycache__', 'node_modules', '.env', 'rename_log_']
CONFIG_DIR = Path.home() / ".smartrename"
CONFIG_FILE = CONFIG_DIR / "config.json"

class SmartRename:
    def __init__(self):
        self.api_key = self.load_api_key()
        if not self.api_key:
            self.api_key = self.prompt_and_save_api_key()
        
        self.model = self.load_model()
        self.client = Groq(api_key=self.api_key)
        self.current_dir = Path.cwd()
        self.files = []
        self.conversation_history = []
    
    def load_api_key(self) -> Optional[str]:
        """Load API key from config file in user's home directory."""
        try:
            if CONFIG_FILE.exists():
                with open(CONFIG_FILE, 'r') as f:
                    config = json.load(f)
                    return config.get('groq_api_key')
        except Exception:
            pass
        return None
    
    def load_model(self) -> str:
        """Load model name from config file, return default if not found."""
        try:
            if CONFIG_FILE.exists():
                with open(CONFIG_FILE, 'r') as f:
                    config = json.load(f)
                    return config.get('model', MODEL)
        except Exception:
            pass
        return MODEL
    
    def save_config(self, api_key: str, model: str = None) -> bool:
        """Save API key and model to config file in user's home directory."""
        try:
            CONFIG_DIR.mkdir(parents=True, exist_ok=True)
            
            # Load existing config to preserve other settings
            config = {}
            if CONFIG_FILE.exists():
                try:
                    with open(CONFIG_FILE, 'r') as f:
                        config = json.load(f)
                except Exception:
                    pass
            
            # Update config
            config['groq_api_key'] = api_key
            if model:
                config['model'] = model
            elif 'model' not in config:
                config['model'] = MODEL
            
            with open(CONFIG_FILE, 'w') as f:
                json.dump(config, f, indent=2)
            
            # Set file permissions (read/write for owner only)
            if os.name != 'nt':  # Unix-like systems
                os.chmod(CONFIG_FILE, 0o600)
            
            return True
        except Exception as e:
            print(f"Warning: Could not save config: {e}")
            return False
    
    def prompt_and_save_api_key(self) -> str:
        """Prompt user for API key on first run and save it."""
        print("\n" + "=" * 60)
        print("  FIRST TIME SETUP")
        print("=" * 60)
        print("\nWelcome to Smart Rename!\n")
        print("To use this tool, you need a free Groq API key.")
        print("\nSteps to get your API key:")
        print("  1. Visit: https://console.groq.com")
        print("  2. Sign up for free (takes 1 minute)")
        print("  3. Create an API key")
        print("  4. Copy and paste it below\n")
        print("Your API key will be securely stored at:")
        print(f"  {CONFIG_FILE}\n")
        
        while True:
            api_key = input("Enter your Groq API key: ").strip()
            
            if not api_key:
                print("❌ API key cannot be empty. Please try again.\n")
                continue
            
            # Basic validation
            if len(api_key) < 20:
                print("❌ API key seems too short. Please check and try again.\n")
                continue
            
            # Test the API key
            print("\nValidating API key...", end="", flush=True)
            try:
                test_client = Groq(api_key=api_key)
                # Make a minimal test request
                test_client.chat.completions.create(
                    model=MODEL,
                    messages=[{"role": "user", "content": "test"}],
                    max_tokens=5
                )
                print(" ✓")
                
                # Save the key
                if self.save_config(api_key):
                    print(f"✓ API key saved successfully!\n")
                else:
                    print("⚠️  API key validated but could not be saved.")
                    print("You may need to enter it again next time.\n")
                
                return api_key
            
            except Exception as e:
                print(" ✗")
                print(f"\n❌ Error: {e}\n")
                print("This could be due to:")
                print("  - Invalid API key")
                print("  - Network connection issue")
                print("  - Model no longer available\n")
                print("To fix model issues:")
                print("  1. Visit: https://console.groq.com/docs/models")
                print("  2. Find an available model")
                print("  3. Enter it below\n")
                
                choice = input("Enter 'r' to retry, 'm' to change model, or 'q' to quit: ").strip().lower()
                
                if choice == 'q':
                    print("\nSetup cancelled. Run the tool again when ready.")
                    print(f"Need help? Visit: {WEBSITE}")
                    sys.exit(0)
                elif choice == 'm':
                    custom_model = input("\nEnter model name: ").strip()
                    if custom_model:
                        try:
                            test_client.chat.completions.create(
                                model=custom_model,
                                messages=[{"role": "user", "content": "test"}],
                                max_tokens=5
                            )
                            print("\n✓ Model validated successfully!")
                            if self.save_config(api_key, custom_model):
                                print(f"✓ Configuration saved!\n")
                            return api_key
                        except Exception as model_error:
                            print(f"\n❌ Model validation failed: {model_error}")
                            print(f"Need help? Visit: {WEBSITE}\n")
                print()
        
    def scan_files(self) -> List[str]:
        """Scan current directory for files, excluding system and hidden files."""
        try:
            all_items = os.listdir(self.current_dir)
            files = []
            
            for item in all_items:
                path = self.current_dir / item
                # Skip directories, hidden files, and excluded patterns
                if path.is_file() and not item.startswith('.'):
                    if not any(pattern in item for pattern in EXCLUDED_PATTERNS):
                        files.append(item)
            
            return sorted(files)
        except Exception as e:
            raise RuntimeError(f"Failed to scan directory: {e}")
    
    def build_system_prompt(self, files: List[str]) -> str:
        """Build the system prompt with instructions and file list."""
        return f"""You are a smart file renaming assistant. Your job is to help users rename files based on their natural language requests.

CURRENT DIRECTORY: {self.current_dir}
FILES IN DIRECTORY ({len(files)} files):
{chr(10).join(f"  - {f}" for f in files)}

INSTRUCTIONS:
1. Understand the user's renaming request
2. If the request is clear, respond with ONLY a JSON object in this exact format:
   {{"renames": [{{"old": "filename.ext", "new": "newname.ext"}}]}}
3. If you need clarification, ask the user questions in plain text
4. Only include files that need to be renamed in the JSON
5. Preserve file extensions unless explicitly asked to change them
6. Ensure new filenames are valid (no special characters like: \\ / : * ? " < > |)
7. Check for potential name collisions

SAFETY RULES:
- Never rename system files or hidden files
- Warn if multiple files would have the same new name
- Be conservative - when in doubt, ask for clarification

When ready to rename, output ONLY the JSON object, nothing else."""

    def validate_json_response(self, response: str) -> Optional[Dict]:
        """Validate and parse JSON response from AI."""
        try:
            # Try to extract JSON if wrapped in markdown
            if "```json" in response:
                start = response.find("```json") + 7
                end = response.find("```", start)
                response = response[start:end].strip()
            elif "```" in response:
                start = response.find("```") + 3
                end = response.find("```", start)
                response = response[start:end].strip()
            
            data = json.loads(response)
            
            # Validate structure
            if "renames" not in data or not isinstance(data["renames"], list):
                return None
            
            for item in data["renames"]:
                if "old" not in item or "new" not in item:
                    return None
                if not isinstance(item["old"], str) or not isinstance(item["new"], str):
                    return None
            
            return data
        except (json.JSONDecodeError, KeyError, TypeError):
            return None
    
    def check_collisions(self, renames: List[Dict]) -> Tuple[bool, List[str]]:
        """Check for filename collisions."""
        new_names = [r["new"] for r in renames]
        existing_files = set(self.files)
        issues = []
        
        # Check for duplicate new names
        seen = set()
        for name in new_names:
            if name in seen:
                issues.append(f"Duplicate target name: {name}")
            seen.add(name)
        
        # Check if new name already exists (and isn't being renamed)
        old_names = set(r["old"] for r in renames)
        for rename in renames:
            if rename["new"] in existing_files and rename["new"] not in old_names:
                issues.append(f"File already exists: {rename['new']}")
        
        # Check for invalid characters
        invalid_chars = r'\/:*?"<>|'
        for rename in renames:
            if any(char in rename["new"] for char in invalid_chars):
                issues.append(f"Invalid characters in: {rename['new']}")
        
        return len(issues) == 0, issues
    
    def create_backup_log(self, renames: List[Dict]) -> str:
        """Create a backup log file before renaming."""
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        log_filename = f"rename_log_{timestamp}.txt"
        log_path = self.current_dir / log_filename
        
        try:
            with open(log_path, 'w', encoding='utf-8') as f:
                f.write(f"Smart Rename - Backup Log\n")
                f.write(f"Timestamp: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
                f.write(f"Directory: {self.current_dir}\n")
                f.write(f"Total files renamed: {len(renames)}\n")
                f.write("=" * 60 + "\n\n")
                
                for rename in renames:
                    f.write(f"{rename['old']} --> {rename['new']}\n")
            
            return log_filename
        except Exception as e:
            raise RuntimeError(f"Failed to create backup log: {e}")
    
    def execute_renames(self, renames: List[Dict]) -> Tuple[int, List[str]]:
        """Execute the file renames."""
        success_count = 0
        errors = []
        
        for rename in renames:
            old_path = self.current_dir / rename["old"]
            new_path = self.current_dir / rename["new"]
            
            try:
                if not old_path.exists():
                    errors.append(f"File not found: {rename['old']}")
                    continue
                
                old_path.rename(new_path)
                success_count += 1
            except Exception as e:
                errors.append(f"Failed to rename {rename['old']}: {str(e)}")
        
        return success_count, errors
    
    def chat_with_ai(self, user_message: str) -> str:
        """Send message to AI and get response."""
        try:
            self.conversation_history.append({
                "role": "user",
                "content": user_message
            })
            
            response = self.client.chat.completions.create(
                model=self.model,
                messages=[
                    {"role": "system", "content": self.build_system_prompt(self.files)},
                    *self.conversation_history
                ],
                temperature=0.3,
                max_tokens=2000
            )
            
            ai_response = response.choices[0].message.content
            self.conversation_history.append({
                "role": "assistant",
                "content": ai_response
            })
            
            return ai_response
        except Exception as e:
            print(f"\n❌ Error communicating with AI: {e}\n")
            print("This could be due to:")
            print("  - Network connection issue")
            print("  - Model no longer available")
            print("  - API rate limit\n")
            print("To fix model issues:")
            print("  1. Visit: https://console.groq.com/docs/models")
            print("  2. Find an available model")
            print("  3. Enter it below\n")
            
            choice = input("Enter 'm' to change model, 'r' to retry, or 'q' to quit: ").strip().lower()
            
            if choice == 'q':
                print(f"\nNeed help? Visit: {WEBSITE}")
                raise RuntimeError("User cancelled operation")
            elif choice == 'm':
                new_model = input("\nEnter model name: ").strip()
                if new_model:
                    try:
                        test_response = self.client.chat.completions.create(
                            model=new_model,
                            messages=[{"role": "user", "content": "test"}],
                            max_tokens=5
                        )
                        print("\n✓ Model validated successfully!")
                        self.model = new_model
                        self.save_config(self.api_key, new_model)
                        print("✓ Configuration updated!\n")
                        
                        # Retry the original request
                        return self.chat_with_ai(user_message)
                    except Exception as model_error:
                        print(f"\n❌ Model validation failed: {model_error}")
                        print(f"Need help? Visit: {WEBSITE}")
                        raise RuntimeError(f"Model validation failed: {model_error}")
            elif choice == 'r':
                # Retry with same settings
                return self.chat_with_ai(user_message)
            
            raise RuntimeError(f"AI request failed: {e}")
    
    def display_preview(self, renames: List[Dict]):
        """Display preview of changes."""
        print("\n" + "=" * 60)
        print("PREVIEW OF CHANGES:")
        print("=" * 60)
        for i, rename in enumerate(renames, 1):
            print(f"{i}. {rename['old']}")
            print(f"   → {rename['new']}")
        print("=" * 60)
    
    def run(self):
        """Main application loop."""
        # Header
        print("\n" + "=" * 60)
        print("  SMART RENAME - AI-Powered File Renaming Tool")
        print(f"  Version {VERSION}")
        print("=" * 60)
        print(f"Working directory: {self.current_dir}\n")
        
        # Scan files
        try:
            self.files = self.scan_files()
        except Exception as e:
            print(f"❌ Error: {e}")
            return
        
        if not self.files:
            print("No files found in current directory.")
            return
        
        print(f"Found {len(self.files)} file(s)")
        
        # Check file count limits
        if len(self.files) > MAX_FILES_HARD_LIMIT:
            print(f"❌ Too many files ({len(self.files)}). Maximum is {MAX_FILES_HARD_LIMIT}.")
            print("Please run this tool in a directory with fewer files.")
            return
        
        if len(self.files) > MAX_FILES_WARNING:
            print(f"⚠️  Warning: {len(self.files)} files detected. This may take longer.")
            response = input("Continue? (y/n): ").strip().lower()
            if response != 'y':
                print("Cancelled.")
                return
        
        print("\nType your renaming request (or 'quit' to exit)")
        print("Example: 'capitalize first letter of all files'")
        print("Example: 'replace spaces with underscores'\n")
        
        # Main chat loop
        while True:
            try:
                user_input = input("You: ").strip()
                
                if not user_input:
                    continue
                
                if user_input.lower() in ['quit', 'exit', 'q']:
                    print("Goodbye!")
                    print(f"\n💡 Check out more tools at: {WEBSITE}")
                    break
                
                # Easter egg for branding
                if 'who created' in user_input.lower() or 'who made' in user_input.lower() or 'developer' in user_input.lower():
                    print(f"\nAI: This tool was created by {AUTHOR}.")
                    print(f"Visit: {WEBSITE}")
                    print("How can I help you rename files today?\n")
                    continue
                
                print("\nAI: ", end="", flush=True)
                ai_response = self.chat_with_ai(user_input)
                
                # Check if response is JSON
                rename_data = self.validate_json_response(ai_response)
                
                if rename_data:
                    renames = rename_data["renames"]
                    
                    if not renames:
                        print("No files to rename based on your request.\n")
                        continue
                    
                    # Display preview
                    self.display_preview(renames)
                    
                    # Check for collisions
                    is_safe, issues = self.check_collisions(renames)
                    if not is_safe:
                        print("\n⚠️  ISSUES DETECTED:")
                        for issue in issues:
                            print(f"  - {issue}")
                        print("\nPlease refine your request.\n")
                        continue
                    
                    # Confirm
                    confirm = input("\nProceed with rename? (y/n): ").strip().lower()
                    if confirm != 'y':
                        print("Cancelled.\n")
                        continue
                    
                    # Create backup log
                    try:
                        log_file = self.create_backup_log(renames)
                        print(f"✓ Backup log created: {log_file}")
                    except Exception as e:
                        print(f"❌ {e}")
                        continue
                    
                    # Execute renames
                    success_count, errors = self.execute_renames(renames)
                    
                    print(f"\n✓ Successfully renamed {success_count}/{len(renames)} file(s)")
                    
                    if errors:
                        print("\n⚠️  Errors:")
                        for error in errors:
                            print(f"  - {error}")
                    else:
                        print(f"\n💡 Like this tool? Check out more at: {WEBSITE}")
                    
                    # Refresh file list
                    self.files = self.scan_files()
                    print()
                else:
                    # Plain text response
                    print(ai_response + "\n")
            
            except KeyboardInterrupt:
                print("\n\nInterrupted. Goodbye!")
                print(f"\n💡 Check out more tools at: {WEBSITE}")
                break
            except Exception as e:
                print(f"\n❌ Error: {e}\n")

def main():
    try:
        app = SmartRename()
        app.run()
    except KeyboardInterrupt:
        print("\n\nSetup cancelled.")
        print(f"Need help? Visit: {WEBSITE}")
        sys.exit(0)
    except Exception as e:
        print(f"\n❌ Fatal Error: {e}")
        print(f"Need help? Visit: {WEBSITE}")
        sys.exit(1)

if __name__ == "__main__":
    main()
