#!/usr/bin/env python3
"""
Run script for Smart AI Resume Analyzer
"""

import os
import sys
import subprocess

def main():
    """Main function to run the application"""
    print("Starting Smart AI Resume Analyzer...")
    app_script = os.path.join(os.path.dirname(os.path.abspath(__file__)), "app.py")
    
    if os.path.exists(app_script):
        try:
            subprocess.run([sys.executable, "-m", "streamlit", "run", app_script])
        except Exception as e:
            print(f"Error starting application: {str(e)}")
            sys.exit(1)
    else:
        print(f"Application script not found at {app_script}")
        sys.exit(1)

if __name__ == "__main__":
    main() 