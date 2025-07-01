#!/usr/bin/env python3
"""
Script to fix image references that include size suffixes like -1024x768
when the actual files don't have these suffixes.
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

def find_sized_image_references():
    """Find markdown files with size-suffixed image references."""
    images = find_all_images()
    content_dir = Path("content")
    fixes = []
    
    # Find all markdown files
    for md_file in content_dir.glob("*.md"):
        with open(md_file, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Find image references with size suffixes like -1024x768
        size_pattern = r'\{static\}/images/([^)]+?)-(\d+x\d+)(\.[a-zA-Z]+)'
        matches = re.findall(size_pattern, content)
        
        for match in matches:
            base_name = match[0]
            size_suffix = match[1]  # like "1024x768"
            extension = match[2]    # like ".jpg"
            
            # The referenced filename with size suffix
            referenced_filename = f"{base_name}-{size_suffix}{extension}"
            # What we should look for (without size suffix)
            actual_filename = f"{base_name}{extension}"
            
            # Check if the actual file (without size suffix) exists
            if actual_filename in images:
                correct_path = images[actual_filename]
                referenced_path = referenced_filename
                
                fixes.append({
                    'file': str(md_file),
                    'old_ref': f"{{static}}/images/{referenced_path}",
                    'new_ref': f"{{static}}/images/{correct_path}",
                    'description': f"Remove size suffix from {referenced_filename}"
                })
    
    return fixes

def apply_fixes(fixes, dry_run=True):
    """Apply the fixes to the markdown files."""
    for fix in fixes:
        file_path = fix['file']
        old_ref = fix['old_ref']
        new_ref = fix['new_ref']
        
        if dry_run:
            print(f"Would fix in {file_path}:")
            print(f"  {old_ref} -> {new_ref}")
        else:
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
            
            if old_ref in content:
                content = content.replace(old_ref, new_ref)
                
                with open(file_path, 'w', encoding='utf-8') as f:
                    f.write(content)
                
                print(f"Fixed in {file_path}: {fix['description']}")
            else:
                print(f"Reference not found in {file_path}: {old_ref}")

if __name__ == "__main__":
    print("Finding sized image references...")
    fixes = find_sized_image_references()
    
    if fixes:
        print(f"\nFound {len(fixes)} sized image references to fix:")
        print("\nDry run - showing what would be changed:")
        apply_fixes(fixes, dry_run=True)
        
        print(f"\nApplying these {len(fixes)} fixes...")
        apply_fixes(fixes, dry_run=False)
        print("\nFixes applied!")
    else:
        print("No sized image references found!")