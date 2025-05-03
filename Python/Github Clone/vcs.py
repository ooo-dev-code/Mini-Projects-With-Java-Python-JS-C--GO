import os
import hashlib
import pickle

def init_vcs():
    os.makedirs('.vcs_storage', exist_ok=True)
    print("Version control system initialized.")
    
def snapshot(directory):
    snapshot_hash = hashlib.sha256()
    snapshot_data = {"files": {}}
    
    for root, dirs, files in os.walk(directory):
        for file in files:
            if ".vcs_storage" in os.path.join(root, file):
                continue
            file_path = os.path.join(root, file)
            with open(file_path, 'rb') as f:
                content = f.read()
                snapshot_hash.update(content)
                snapshot_data["files"][file_path] = content.decode('utf-8', errors='ignore')
                
    hash_digest = snapshot_hash.hexdigest()
    snapshot_data["file_list"] = list(snapshot_data["files"].keys())
    
    with open(f'.vcs_storage/snapshot_{hash_digest}.pkl', 'wb') as f:
        pickle.dump(snapshot_data, f)
        
    print(f"Snapshot created with hash: {hash_digest}")
    
def revert_to_snapshot(hash_digest):
    snapshot_path = f'.vcs_storage/snapshot_{hash_digest}.pkl'
    
    if not os.path.exists(snapshot_path):
        print("Snapshot not found.")
        return
    
    with open(snapshot_path, 'rb') as f:
        snapshot_data = pickle.load(f)
        
    for file_path, content in snapshot_data["files"].items():
        os.makedirs(os.path.dirname(file_path), exist_ok=True)
        with open(file_path, 'wb') as f:
            f.write(content)
            
    current_files = set()
    for root, dirs, files in os.walk('.', topdown=True):
        if ".vcs_storage" in root:
            continue
        for file in files:
            current_files.add(os.path.join(root, file))
            
    snapshot_files = set(snapshot_data["file_list"])
    files_to_delete = current_files - snapshot_files
    
    # Prompt before deleting files
    for file in files_to_delete:
        if os.path.exists(file):
            confirm = input(f"Do you want to delete {file}? (y/n): ").strip().lower()
            if confirm == 'y':
                os.remove(file)
                print(f"Deleted: {file}")
            else:
                print(f"Skipped: {file}")
                
    print(f"Reverted to snapshot: {hash_digest}")
    
if __name__ == "__main__":
    import sys
    
    if len(sys.argv) < 2:
        print("Usage: python vcs.py <command> [<args>]")
        sys.exit(1)
    
    command = sys.argv[1]
    
    if command == "init":
        init_vcs()
    elif command == "snapshot":
        directory = sys.argv[2] if len(sys.argv) > 2 else "."
        snapshot(directory)
    elif command == "revert":
        hash_digest = sys.argv[2]
        revert_to_snapshot(hash_digest)
    else:
        print("Unknown command.")
