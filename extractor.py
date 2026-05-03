import os
from datetime import datetime

def extract_files(path):
    file_data = []

    for root, dirs, files in os.walk(path):
        for file in files:
            full_path = os.path.join(root, file)
            stats = os.stat(full_path)

            file_data.append({
                "name": file,
                "path": full_path,
                "size": stats.st_size,
                "created": datetime.fromtimestamp(stats.st_ctime),
                "modified": datetime.fromtimestamp(stats.st_mtime)
            })

    return file_data