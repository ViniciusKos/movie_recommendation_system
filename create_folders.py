import os
from pathlib import Path

def create_project_dir(directory):
    """ Helper function to create a directory if it does not exist. """
    if not os.path.exists(directory):
        os.makedirs(directory)
        print(f"Directory {directory} created")
    else:
        print(f"Directory {directory} already exists")

def setup_project_structure():
    """ Sets up the folder structure for a machine learning project in the current working directory. """
    # Get the current working directory
    root_path = Path(os.getcwd())
    
    # Define the directory structure
    folders = [
        "data/raw",
        "data/processed",
        "data/external",
        "notebooks",
        "src/data",
        "src/features",
        "src/models",
        "src/visualization",
        "models",
        "reports/figures",
    ]

    # Create directories
    for folder in folders:
        create_project_dir(root_path / folder)

    # Create files
    files = [
        "src/__init__.py",
        "src/data/make_dataset.py",
        "src/features/build_features.py",
        "src/models/train_model.py",
        "src/models/predict_model.py",
        "src/visualization/visualize.py",
        "requirements.txt",
        "setup.py",
        "Dockerfile",
        ".gitignore",
        "README.md"
    ]
    
    for file in files:
        file_path = root_path / file
        if not file_path.exists():
            file_path.touch()
            print(f"File {file} created")
        else:
            print(f"File {file} already exists")

if __name__ == "__main__":
    setup_project_structure()
