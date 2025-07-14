#!/usr/bin/env python3
import os
import re
import glob

def remove_missing_image_references():
    """
    Remove or comment out references to images that don't exist
    """
    
    # Get all markdown files
    md_files = glob.glob('content/*.md')
    print(f'Found {len(md_files)} markdown files')
    
    fixed_files = 0
    total_removals = 0
    
    for md_file in md_files:
        try:
            with open(md_file, 'r', encoding='utf-8') as f:
                content = f.read()
            
            original_content = content
            lines = content.split('\n')
            new_lines = []
            
            for line in lines:
                # Look for image references in this line
                image_match = re.search(r'!\[[^\]]*\]\({static}/images/([^}]+\.(jpg|jpeg|png|gif|webp))\)', line, re.IGNORECASE)
                
                if image_match:
                    image_path = image_match.group(1)
                    full_path = f'content/images/{image_path}'
                    
                    # Check if the file exists
                    if not os.path.exists(full_path):
                        # Comment out this line
                        new_lines.append(f'<!-- Missing image: {image_path} -->')
                        print(f'  Removed: {image_path}')
                        total_removals += 1
                    else:
                        new_lines.append(line)
                else:
                    new_lines.append(line)
            
            # Rejoin content
            new_content = '\n'.join(new_lines)
            
            # Save the file if changes were made
            if new_content != original_content:
                with open(md_file, 'w', encoding='utf-8') as f:
                    f.write(new_content)
                fixed_files += 1
                print(f'Updated {os.path.basename(md_file)}')
        
        except Exception as e:
            print(f'Error processing {md_file}: {e}')
    
    print(f'\nSummary: Removed {total_removals} missing image references from {fixed_files} files')

if __name__ == '__main__':
    remove_missing_image_references()