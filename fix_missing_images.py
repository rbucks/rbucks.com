#!/usr/bin/env python3
import os
import re
import glob

def find_and_fix_missing_images():
    """
    Find missing image references and try to replace them with existing files
    by removing size suffixes like -1024x768, -300x225, etc.
    """
    
    # Get all markdown files
    md_files = glob.glob('content/*.md')
    print(f'Found {len(md_files)} markdown files')
    
    fixed_files = 0
    total_fixes = 0
    
    for md_file in md_files:
        try:
            with open(md_file, 'r', encoding='utf-8') as f:
                content = f.read()
            
            original_content = content
            
            # Find all image references
            image_pattern = r'{static}/images/([^}]+\.(jpg|jpeg|png|gif|webp))'
            matches = re.findall(image_pattern, content, re.IGNORECASE)
            
            for match in matches:
                image_path = match[0]  # Full path without {static}/images/
                full_path = f'content/images/{image_path}'
                
                # Check if the file exists
                if not os.path.exists(full_path):
                    # Try to find the file without size suffix
                    # Remove patterns like -1024x768, -300x225, etc.
                    base_path = re.sub(r'-\d+x\d+(?=\.[^.]+$)', '', image_path)
                    base_full_path = f'content/images/{base_path}'
                    
                    if os.path.exists(base_full_path):
                        # Replace the reference with the base version
                        old_ref = f'{{static}}/images/{image_path}'
                        new_ref = f'{{static}}/images/{base_path}'
                        content = content.replace(old_ref, new_ref)
                        print(f'  Fixed: {image_path} -> {base_path}')
                        total_fixes += 1
                    else:
                        # Try other common variations
                        # Remove _1_105_c suffix
                        alt_path = re.sub(r'_1_105_c(?=\.[^.]+$)', '', image_path)
                        alt_full_path = f'content/images/{alt_path}'
                        
                        if os.path.exists(alt_full_path):
                            old_ref = f'{{static}}/images/{image_path}'
                            new_ref = f'{{static}}/images/{alt_path}'
                            content = content.replace(old_ref, new_ref)
                            print(f'  Fixed: {image_path} -> {alt_path}')
                            total_fixes += 1
                        else:
                            # Try without _1_102_o suffix
                            alt_path2 = re.sub(r'_1_102_o(?=\.[^.]+$)', '', image_path)
                            alt_full_path2 = f'content/images/{alt_path2}'
                            
                            if os.path.exists(alt_full_path2):
                                old_ref = f'{{static}}/images/{image_path}'
                                new_ref = f'{{static}}/images/{alt_path2}'
                                content = content.replace(old_ref, new_ref)
                                print(f'  Fixed: {image_path} -> {alt_path2}')
                                total_fixes += 1
                            else:
                                print(f'  Missing: {image_path} (no alternative found)')
            
            # Save the file if changes were made
            if content != original_content:
                with open(md_file, 'w', encoding='utf-8') as f:
                    f.write(content)
                fixed_files += 1
                print(f'Updated {os.path.basename(md_file)}')
        
        except Exception as e:
            print(f'Error processing {md_file}: {e}')
    
    print(f'\nSummary: Fixed {total_fixes} image references in {fixed_files} files')

if __name__ == '__main__':
    find_and_fix_missing_images()