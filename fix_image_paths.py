#!/usr/bin/env python3
"""
Script to find and fix missing image references in Pelican markdown files.
This script identifies images that exist in year/month subdirectories but are
referenced without the subdirectory path in the markdown files.
"""

import os
import re
import glob
from pathlib import Path

def find_all_images():
    """Find all images in the content/images directory."""
    images = {}
    images_dir = Path("content/images")
    
    # Find all image files recursively
    for img_path in images_dir.rglob("*"):
        if img_path.is_file() and img_path.suffix.lower() in ['.jpg', '.jpeg', '.png', '.gif', '.webp']:
            filename = img_path.name
            # Store the relative path from content/images/
            relative_path = str(img_path.relative_to(images_dir))
            images[filename] = relative_path
    
    return images

def find_missing_references():
    """Find markdown files with missing image references."""
    images = find_all_images()
    content_dir = Path("content")
    fixes = []
    
    # Find all markdown files
    for md_file in content_dir.glob("*.md"):
        with open(md_file, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Find image references in the format {static}/images/filename
        image_pattern = r'\{static\}/images/([^)]+)'
        matches = re.findall(image_pattern, content)
        
        for match in matches:
            # Extract just the filename from the path
            filename = os.path.basename(match)
            
            # Check if this filename exists in our images dict
            if filename in images:
                correct_path = images[filename]
                # If the referenced path doesn't match the correct path
                if match != correct_path:
                    fixes.append({
                        'file': str(md_file),
                        'old_path': match,
                        'new_path': correct_path,
                        'filename': filename
                    })
    
    return fixes

def apply_fixes(fixes, dry_run=True):
    """Apply the fixes to the markdown files."""
    for fix in fixes:
        file_path = fix['file']
        old_ref = f"{{static}}/images/{fix['old_path']}"
        new_ref = f"{{static}}/images/{fix['new_path']}"
        
        if dry_run:
            print(f"Would fix in {file_path}:")
            print(f"  {old_ref} -> {new_ref}")
        else:
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
            
            content = content.replace(old_ref, new_ref)
            
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(content)
            
            print(f"Fixed in {file_path}: {fix['filename']}")

if __name__ == "__main__":
    print("Finding missing image references...")
    fixes = find_missing_references()
    
    if fixes:
        print(f"\nFound {len(fixes)} image references to fix:")
        print("\nDry run - showing what would be changed:")
        apply_fixes(fixes, dry_run=True)
        
        # Auto-apply fixes
        apply_fixes(fixes, dry_run=False)
        print("\nFixes applied!")
    else:
        print("No missing image references found!")