#!/usr/bin/env python3
import os
import re
import glob

def fix_image_paths():
    # Get all markdown files in content directory
    md_files = glob.glob('content/*.md')
    print(f'Found {len(md_files)} markdown files')
    
    fixed_files = 0
    total_fixes = 0
    
    for md_file in md_files:
        try:
            with open(md_file, 'r', encoding='utf-8') as f:
                content = f.read()
            
            original_content = content
            
            # Fix image paths - look for {static}/YYYY/MM/filename or {filename}/YYYY/MM/filename
            # and change them to {static}/images/YYYY/MM/filename
            
            # Pattern 1: {static}/YYYY/MM/filename -> {static}/images/YYYY/MM/filename
            content = re.sub(r'{static}/(\d{4}/\d{2}/[^}]+)', r'{static}/images/\1', content)
            
            # Pattern 2: {filename}/YYYY/MM/filename -> {static}/images/YYYY/MM/filename  
            content = re.sub(r'{filename}/(\d{4}/\d{2}/[^}]+)', r'{static}/images/\1', content)
            
            # Pattern 3: Simple filename references that should be in images/
            # Look for common image files at root level and add images/ prefix
            image_extensions = ['jpg', 'jpeg', 'png', 'gif', 'webp']
            for ext in image_extensions:
                # Pattern: {static}/filename.ext -> {static}/images/filename.ext (only for standalone files)
                content = re.sub(f'{{static}}/([^/]+\\.{ext})', r'{static}/images/\1', content, flags=re.IGNORECASE)
                content = re.sub(f'{{filename}}/([^/]+\\.{ext})', r'{static}/images/\1', content, flags=re.IGNORECASE)
            
            if content != original_content:
                # Count the number of changes
                fixes = len(re.findall(r'{static}/images/', content)) - len(re.findall(r'{static}/images/', original_content))
                
                with open(md_file, 'w', encoding='utf-8') as f:
                    f.write(content)
                
                fixed_files += 1
                total_fixes += fixes
                print(f'Fixed {os.path.basename(md_file)}: {fixes} image paths updated')
        
        except Exception as e:
            print(f'Error processing {md_file}: {e}')
    
    print(f'\nSummary: Fixed {total_fixes} image paths in {fixed_files} files')

if __name__ == '__main__':
    fix_image_paths()