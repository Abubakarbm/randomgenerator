import requests
import os
from time import sleep
import re
from tkinter import Tk, filedialog

def discover_files(url, max_attempts=100, patience=20):
    """
    Repeatedly POST to the URL to discover all unique PDF files.
    
    Args:
        url: The file generation URL
        max_attempts: Maximum number of requests to make
        patience: Stop after this many consecutive attempts without finding new files
    
    Returns:
        Dictionary with file names as keys and their content as values
    """
    discovered_files = {}
    attempts_without_new = 0
    
    headers = {
        "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8",
        "accept-language": "en-GB,en;q=0.9,en-US;q=0.8",
        "cache-control": "max-age=0",
        "content-type": "application/x-www-form-urlencoded",
        "referer": url,
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"
    }
    
    print(f"Discovering files from: {url}")
    print(f"This may take a while...\n")
    
    for attempt in range(1, max_attempts + 1):
        try:
            response = requests.post(url, headers=headers, timeout=10)
            
            if response.status_code != 200:
                print(f"[Attempt {attempt}] Error: Status code {response.status_code}")
                continue
            
            
            content_disposition = response.headers.get('Content-Disposition', '')
            
            if 'filename=' in content_disposition:
               
                filename_match = re.search(r'filename[^;=\n]*=(([\'"]).*?\2|[^;\n]*)', content_disposition)
                if filename_match:
                    filename = filename_match.group(1).strip('"\'')
                else:
                    filename = f"file_{attempt}.pdf"
            else:
                filename = f"file_{attempt}.pdf"
            
            if filename not in discovered_files:
                discovered_files[filename] = response.content
                attempts_without_new = 0
                print(f"[Attempt {attempt}] Found NEW file: {filename} (Total: {len(discovered_files)})")
            else:
                attempts_without_new += 1
                print(f"[Attempt {attempt}] Duplicate: {filename} (No new files for {attempts_without_new} attempts)")
            
            if attempts_without_new >= patience:
                print(f"\n✓ No new files found in {patience} attempts. Discovery complete!")
                break
            sleep(0.5) 
        except requests.exceptions.Timeout:
            print(f"[Attempt {attempt}] Timeout - skipping")
        except Exception as e:
            print(f"[Attempt {attempt}] Error: {e}")
    
    return discovered_files

def save_files(files_dict, download_folder):
    successful = 0
    failed = 0
    skipped = 0
    
    for filename, content in files_dict.items():
        try:
            file_path = os.path.join(download_folder, filename)
            
            if os.path.exists(file_path):
                print(f"Skipped (already exists): {filename}")
                skipped += 1
                continue
            
            with open(file_path, 'wb') as f:
                f.write(content)
            
            file_size = len(content) / 1024 
            print(f"Saved: {filename} ({file_size:.2f} KB)")
            successful += 1
            
        except Exception as e:
            print(f"Failed to save {filename}: {e}")
            failed += 1
    
    return successful, failed, skipped

def main():
    print("=" * 60)
    print("Random PDF File Downloader")
    print("=" * 60)
    
    url = input("\nEnter the file generation URL: ").strip()

    if not url:
        print("Error: No URL provided!")
        return
    
    print("\n" + "=" * 60)
    print("DISCOVERING FILES")
    print("=" * 60 + "\n")
    
    max_attempts = input("Maximum attempts to make? (default: 100): ").strip()
    max_attempts = int(max_attempts) if max_attempts.isdigit() else 100
    
    patience = input("Stop after how many attempts without new files? (default: 20): ").strip()
    patience = int(patience) if patience.isdigit() else 20
    
    discovered_files = discover_files(url, max_attempts, patience)
    
    if not discovered_files:
        print("\nNo files discovered. Please check the URL and try again.")
        return
    
    print("\n" + "=" * 60)
    print("DISCOVERY COMPLETE")
    print("=" * 60)
    print(f"\nTotal files found: {len(discovered_files)}")
    
    
    print("\n" + "=" * 60)
    print("SAVE FILES")
    print("=" * 60 + "\n")
    
    save_choice = input(f"Save all {len(discovered_files)} files to disk? (yes/no): ").strip().lower()
    
    if save_choice == 'yes':
        browse_choice = input("Browse for folder using file explorer? (yes/no): ").strip().lower()
        
        if browse_choice == 'yes':
            print("\nOpening file explorer... (check if a window opened)")
            root = Tk()
            root.withdraw()  # Hide the main tkinter window
            root.attributes('-topmost', True)  # Bring dialog to front
            
            download_folder = filedialog.askdirectory(title="Select Download Folder")
            root.destroy()
            
            if not download_folder:
                print("No folder selected. Using current directory.")
                download_folder = os.getcwd()
        else:
            download_folder = input("Enter folder path (leave blank for current directory): ").strip()
            download_folder = download_folder if download_folder else os.getcwd()
        
        # to create folder if it doesn't exist
        os.makedirs(download_folder, exist_ok=True)
        
        print(f"\nSaving files to: {download_folder}\n")
        
        successful, failed, skipped = save_files(discovered_files, download_folder)
        
        print("\n" + "=" * 60)
        print("SAVE COMPLETE")
        print("=" * 60)
        print(f"Successfully saved: {successful}")
        print(f"Skipped (already exist): {skipped}")
        print(f"Failed: {failed}")
        print(f"Location: {download_folder}")
    else:
        print("\nSave cancelled.")

if __name__ == "__main__":
    main()