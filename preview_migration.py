#!/usr/bin/env python3
"""
Preview WordPress to Pelican Image Migration

This script shows what images would be migrated without actually copying them.
Use this to understand the scope before running the full migration.
"""

import os
import re
from pathlib import Path
from urllib.parse import urlparse

def preview_migration():
    """Preview what images would be migrated."""
    content_dir = Path("/Users/rbucks/Documents/Code/rbucks/rbucks.com/content")
    backup_images_dir = Path("/Users/rbucks/Downloads/jetpack-backup-rbucks-com-2025-06-12-20-11-32/wp-content/uploads")
    
    # Image patterns to match
    image_patterns = [
        # WordPress format without alt text: !(URL)
        r'!\(https?://rbucks\.com/wp-content/uploads/([^)]+)\)',
        # Standard markdown format: ![alt](URL)
        r'!\[.*?\]\(https?://rbucks\.com/wp-content/uploads/([^)]+)\)',
        # Relative URLs starting with /
        r'!\[.*?\]\(/wp-content/uploads/([^)]+)\)',
        r'!\(/wp-content/uploads/([^)]+)\)',
        # Direct wp-content/uploads references
        r'!\[.*?\]\(wp-content/uploads/([^)]+)\)',
        r'!\(wp-content/uploads/([^)]+)\)',
        # HTML img tags with full URLs
        r'<img[^>]*src=["\']https?://rbucks\.com/wp-content/uploads/([^"\']+)["\'][^>]*>',
        # HTML img tags with relative URLs
        r'<img[^>]*src=["\']/?wp-content/uploads/([^"\']+)["\'][^>]*>',
    ]
    
    found_images = set()
    file_to_images = {}
    
    # Find all markdown files
    md_files = list(content_dir.glob("*.md"))
    print(f"📄 Found {len(md_files)} markdown files to analyze")
    print()
    
    for md_file in md_files:
        try:
            with open(md_file, 'r', encoding='utf-8') as f:
                content = f.read()
            
            images_in_file = set()
            
            # Apply all patterns
            for pattern in image_patterns:
                matches = re.findall(pattern, content, re.IGNORECASE)
                for match in matches:
                    clean_match = match.split('?')[0]
                    images_in_file.add(clean_match)
                    found_images.add(clean_match)
            
            if images_in_file:
                file_to_images[md_file.name] = images_in_file
                print(f"📝 {md_file.name}: {len(images_in_file)} images")
                for img in sorted(images_in_file):
                    print(f"   → {img}")
                print()
                
        except Exception as e:
            print(f"❌ Error processing {md_file}: {e}")
    
    print(f"📊 SUMMARY")
    print(f"   Total markdown files with images: {len(file_to_images)}")
    print(f"   Total unique images found: {len(found_images)}")
    print()
    
    # Check which images exist in backup
    print("🔍 Checking which images exist in backup...")
    existing_images = set()
    missing_images = set()
    
    for image_path in found_images:
        # Clean the path
        clean_path = image_path.lstrip('/')
        if clean_path.startswith('wp-content/uploads/'):
            clean_path = clean_path[len('wp-content/uploads/'):]
        
        source_path = backup_images_dir / clean_path
        
        if source_path.exists():
            existing_images.add(image_path)
        else:
            # Try case-insensitive search
            parent_dir = source_path.parent
            filename = source_path.name
            found = False
            
            if parent_dir.exists():
                for file in parent_dir.iterdir():
                    if file.name.lower() == filename.lower():
                        existing_images.add(image_path)
                        found = True
                        break
            
            # If still not found, try to find the original file without WordPress size suffixes
            if not found and parent_dir.exists():
                filename_stem = Path(filename).stem
                filename_ext = Path(filename).suffix
                
                # Common WordPress size suffix patterns
                size_patterns = [
                    r'-\d+x\d+$',  # -1024x768
                    r'-\d+x\d+@2x$',  # -1024x768@2x
                    r'_\d+_\d+_c$',  # _1_105_c
                    r'_\d+_\d+_o$',  # _1_102_o
                    r'_\d+_\d+_a$',  # _1_201_a
                    r'-\d+$',  # -1, -2, etc.
                ]
                
                for pattern in size_patterns:
                    if re.search(pattern, filename_stem):
                        # Remove the suffix and try to find the file
                        clean_stem = re.sub(pattern, '', filename_stem)
                        possible_names = [
                            f"{clean_stem}{filename_ext}",
                            f"{clean_stem}{filename_ext.lower()}",
                            f"{clean_stem}{filename_ext.upper()}",
                        ]
                        
                        for possible_name in possible_names:
                            for file in parent_dir.iterdir():
                                if file.name.lower() == possible_name.lower():
                                    print(f"   → Found original: {filename} -> {file.name}")
                                    existing_images.add(image_path)
                                    found = True
                                    break
                            if found:
                                break
                        break
            
            if not found:
                missing_images.add(image_path)
    
    print(f"✅ Images found in backup: {len(existing_images)}")
    print(f"❌ Images missing from backup: {len(missing_images)}")
    
    if missing_images:
        print("\nMissing images:")
        for img in sorted(missing_images):
            print(f"   ❌ {img}")
    
    print(f"\n📈 MIGRATION PREVIEW")
    print(f"   Would copy {len(existing_images)} images")
    print(f"   Would update {len(file_to_images)} markdown files")
    print(f"   {len(missing_images)} images would be skipped (not found)")
    
    if len(existing_images) > 0:
        print(f"\n🚀 Ready to run migration! Execute:")
        print(f"   python3 migrate_images.py")
    else:
        print(f"\n⚠️  No images found to migrate.")

if __name__ == "__main__":
    preview_migration()