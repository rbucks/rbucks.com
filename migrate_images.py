#!/usr/bin/env python3
"""
WordPress to Pelican Image Migration Script

This script migrates WordPress images from a backup to a Pelican site by:
1. Finding all image references in markdown files that contain "wp-content/uploads"
2. Extracting the image URLs and determining which actual image files need to be copied
3. Copying the referenced images to the Pelican content/images/ directory
4. Updating the markdown files to replace WordPress image URLs with local relative paths
5. Handling different image URL formats (full URLs, relative URLs, various extensions)
6. Only copying images that are actually referenced in the blog posts

Author: Created for rbucks.com migration
Date: 2025-06-29
"""

import os
import re
import shutil
from pathlib import Path
from urllib.parse import urlparse
import logging
from typing import Set, Dict, List, Tuple
import hashlib

# Setup logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('migrate_images.log'),
        logging.StreamHandler()
    ]
)
logger = logging.getLogger(__name__)

class ImageMigrator:
    def __init__(self):
        # Configuration
        self.content_dir = Path("/Users/rbucks/Documents/Code/rbucks/rbucks.com/content")
        self.backup_images_dir = Path("/Users/rbucks/Downloads/jetpack-backup-rbucks-com-2025-06-12-20-11-32/wp-content/uploads")
        self.target_images_dir = Path("/Users/rbucks/Documents/Code/rbucks/rbucks.com/content/images")
        
        # Image patterns to match
        self.image_patterns = [
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
        
        # Supported image extensions
        self.image_extensions = {'.jpg', '.jpeg', '.png', '.gif', '.webp', '.svg', '.bmp'}
        
        # Track found images and processed files
        self.found_images: Set[str] = set()
        self.processed_files: Dict[str, List[str]] = {}
        self.copied_images: Dict[str, str] = {}  # original_path -> new_path
        self.missing_images: Set[str] = set()
        
    def ensure_directories(self):
        """Create necessary directories if they don't exist."""
        self.target_images_dir.mkdir(parents=True, exist_ok=True)
        logger.info(f"Ensured target directory exists: {self.target_images_dir}")
        
    def find_image_references(self) -> Dict[str, Set[str]]:
        """
        Find all image references in markdown files.
        Returns a dict mapping file paths to sets of image paths.
        """
        file_to_images = {}
        
        # Find all markdown files
        md_files = list(self.content_dir.glob("*.md"))
        logger.info(f"Found {len(md_files)} markdown files to process")
        
        for md_file in md_files:
            try:
                with open(md_file, 'r', encoding='utf-8') as f:
                    content = f.read()
                
                images_in_file = set()
                
                # Apply all patterns
                for pattern in self.image_patterns:
                    matches = re.findall(pattern, content, re.IGNORECASE)
                    for match in matches:
                        # Clean up the match - remove any query parameters
                        clean_match = match.split('?')[0]
                        images_in_file.add(clean_match)
                        self.found_images.add(clean_match)
                
                if images_in_file:
                    file_to_images[str(md_file)] = images_in_file
                    logger.info(f"Found {len(images_in_file)} images in {md_file.name}")
                    
            except Exception as e:
                logger.error(f"Error processing {md_file}: {e}")
                
        logger.info(f"Total unique images found: {len(self.found_images)}")
        return file_to_images
    
    def find_source_image_path(self, image_path: str) -> Path:
        """
        Find the actual source image file in the backup directory.
        Handles various path formats and tries to locate the file.
        """
        # Clean the path - remove leading slashes and wp-content/uploads prefix
        clean_path = image_path.lstrip('/')
        if clean_path.startswith('wp-content/uploads/'):
            clean_path = clean_path[len('wp-content/uploads/'):]
        
        # Construct the full path
        source_path = self.backup_images_dir / clean_path
        
        # Check if file exists
        if source_path.exists():
            return source_path
            
        # If not found, try to find it with case-insensitive search
        # This handles cases where filenames might have different cases
        parent_dir = source_path.parent
        filename = source_path.name
        
        if parent_dir.exists():
            for file in parent_dir.iterdir():
                if file.name.lower() == filename.lower():
                    return file
        
        # If still not found, try to find the original file without WordPress size suffixes
        # WordPress adds suffixes like -1024x768, -683x1024, etc.
        # Try removing these suffixes and look for the original file
        if parent_dir.exists():
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
                                logger.info(f"Found original file: {filename} -> {file.name}")
                                return file
                    break
                    
        return None
    
    def generate_target_path(self, image_path: str) -> Path:
        """
        Generate the target path for an image, organizing by year when possible.
        """
        # Extract year from path if available
        year_match = re.search(r'/(\d{4})/', image_path)
        if year_match:
            year = year_match.group(1)
            # Get the filename
            filename = Path(image_path).name
            return self.target_images_dir / year / filename
        else:
            # No year found, put in general directory
            filename = Path(image_path).name
            return self.target_images_dir / filename
    
    def copy_images(self):
        """Copy all found images from backup to target directory."""
        logger.info("Starting image copy process...")
        
        copied_count = 0
        missing_count = 0
        
        for image_path in self.found_images:
            source_path = self.find_source_image_path(image_path)
            
            if source_path is None:
                logger.warning(f"Could not find source image: {image_path}")
                self.missing_images.add(image_path)
                missing_count += 1
                continue
                
            target_path = self.generate_target_path(image_path)
            
            # Create target directory if it doesn't exist
            target_path.parent.mkdir(parents=True, exist_ok=True)
            
            # Check if target already exists and is the same file
            if target_path.exists():
                if self.files_are_identical(source_path, target_path):
                    logger.info(f"Image already exists and is identical: {target_path.name}")
                    self.copied_images[image_path] = str(target_path)
                    continue
                else:
                    # File exists but is different - generate unique name
                    target_path = self.generate_unique_filename(target_path)
            
            try:
                shutil.copy2(source_path, target_path)
                self.copied_images[image_path] = str(target_path)
                copied_count += 1
                logger.info(f"Copied: {source_path.name} -> {target_path}")
                
            except Exception as e:
                logger.error(f"Error copying {source_path} to {target_path}: {e}")
                missing_count += 1
                
        logger.info(f"Image copy complete. Copied: {copied_count}, Missing: {missing_count}")
        
    def files_are_identical(self, file1: Path, file2: Path) -> bool:
        """Check if two files are identical using MD5 hash."""
        try:
            with open(file1, 'rb') as f1, open(file2, 'rb') as f2:
                hash1 = hashlib.md5(f1.read()).hexdigest()
                hash2 = hashlib.md5(f2.read()).hexdigest()
                return hash1 == hash2
        except Exception:
            return False
    
    def generate_unique_filename(self, path: Path) -> Path:
        """Generate a unique filename if the target already exists."""
        counter = 1
        stem = path.stem
        suffix = path.suffix
        parent = path.parent
        
        while True:
            new_name = f"{stem}_{counter}{suffix}"
            new_path = parent / new_name
            if not new_path.exists():
                return new_path
            counter += 1
    
    def update_markdown_files(self, file_to_images: Dict[str, Set[str]]):
        """Update markdown files to use local image references."""
        logger.info("Starting markdown file updates...")
        
        updated_files = 0
        
        for file_path, images in file_to_images.items():
            try:
                with open(file_path, 'r', encoding='utf-8') as f:
                    content = f.read()
                
                original_content = content
                
                # Replace each image reference
                for image_path in images:
                    if image_path in self.copied_images:
                        # Calculate relative path from content directory to image
                        target_path = Path(self.copied_images[image_path])
                        relative_path = os.path.relpath(target_path, self.content_dir)
                        
                        # Use Pelican's {static} syntax for static files
                        pelican_path = f"{{static}}/images/{target_path.name}"
                        if target_path.parent.name != "images":
                            # Include subdirectory (like year) in path
                            pelican_path = f"{{static}}/images/{target_path.parent.name}/{target_path.name}"
                        
                        # Replace all variations of this image reference
                        patterns_to_replace = [
                            f'https://rbucks.com/wp-content/uploads/{image_path}',
                            f'http://rbucks.com/wp-content/uploads/{image_path}',
                            f'/wp-content/uploads/{image_path}',
                            f'wp-content/uploads/{image_path}',
                        ]
                        
                        for old_pattern in patterns_to_replace:
                            content = content.replace(old_pattern, pelican_path)
                            
                        logger.info(f"Replaced image reference: {image_path} -> {pelican_path}")
                    else:
                        logger.warning(f"Image not copied, skipping replacement: {image_path}")
                
                # Write back to file if content changed
                if content != original_content:
                    with open(file_path, 'w', encoding='utf-8') as f:
                        f.write(content)
                    updated_files += 1
                    logger.info(f"Updated file: {Path(file_path).name}")
                    
            except Exception as e:
                logger.error(f"Error updating {file_path}: {e}")
                
        logger.info(f"Markdown update complete. Updated {updated_files} files.")
    
    def generate_report(self):
        """Generate a summary report of the migration."""
        logger.info("\n" + "="*60)
        logger.info("MIGRATION REPORT")
        logger.info("="*60)
        logger.info(f"Total images found in markdown files: {len(self.found_images)}")
        logger.info(f"Images successfully copied: {len(self.copied_images)}")
        logger.info(f"Images not found in backup: {len(self.missing_images)}")
        
        if self.missing_images:
            logger.info("\nMissing images:")
            for img in sorted(self.missing_images):
                logger.info(f"  - {img}")
                
        logger.info(f"\nImages copied to: {self.target_images_dir}")
        logger.info("Migration complete!")
        
        # Write detailed report to file
        report_path = Path("migration_report.txt")
        with open(report_path, 'w') as f:
            f.write("WordPress to Pelican Image Migration Report\n")
            f.write("=" * 50 + "\n\n")
            f.write(f"Total images found: {len(self.found_images)}\n")
            f.write(f"Images copied: {len(self.copied_images)}\n")
            f.write(f"Images missing: {len(self.missing_images)}\n\n")
            
            if self.copied_images:
                f.write("Copied Images:\n")
                f.write("-" * 20 + "\n")
                for orig, new in sorted(self.copied_images.items()):
                    f.write(f"{orig} -> {new}\n")
                f.write("\n")
                
            if self.missing_images:
                f.write("Missing Images:\n")
                f.write("-" * 20 + "\n")
                for img in sorted(self.missing_images):
                    f.write(f"{img}\n")
                    
        logger.info(f"Detailed report written to: {report_path}")
    
    def run(self):
        """Run the complete migration process."""
        logger.info("Starting WordPress to Pelican image migration...")
        
        # Verify directories exist
        if not self.content_dir.exists():
            logger.error(f"Content directory not found: {self.content_dir}")
            return False
            
        if not self.backup_images_dir.exists():
            logger.error(f"Backup images directory not found: {self.backup_images_dir}")
            return False
        
        # Create target directory
        self.ensure_directories()
        
        # Step 1: Find all image references
        file_to_images = self.find_image_references()
        
        if not self.found_images:
            logger.info("No images found to migrate!")
            return True
            
        # Step 2: Copy images
        self.copy_images()
        
        # Step 3: Update markdown files
        self.update_markdown_files(file_to_images)
        
        # Step 4: Generate report
        self.generate_report()
        
        return True

def main():
    """Main function to run the migration."""
    migrator = ImageMigrator()
    
    try:
        success = migrator.run()
        if success:
            print("\n✅ Migration completed successfully!")
            print("Check the log file 'migrate_images.log' for detailed information.")
            print("Check 'migration_report.txt' for a summary of what was migrated.")
        else:
            print("\n❌ Migration failed. Check the log for details.")
            return 1
            
    except KeyboardInterrupt:
        print("\n⚠️  Migration interrupted by user.")
        return 1
    except Exception as e:
        logger.error(f"Unexpected error during migration: {e}")
        print(f"\n❌ Migration failed with error: {e}")
        return 1
        
    return 0

if __name__ == "__main__":
    exit(main())