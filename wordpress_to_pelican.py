#!/usr/bin/env python3
"""
WordPress to Pelican Converter

This script extracts blog posts from a WordPress SQL backup file and converts them
to Pelican-compatible markdown files with proper frontmatter.

Usage: python wordpress_to_pelican.py
"""

import re
import os
import html
from datetime import datetime
from pathlib import Path


def unescape_sql_string(text):
    """Unescape SQL-escaped strings (handle escaped quotes and other characters)"""
    if not text:
        return ""
    
    # Handle SQL escape sequences
    text = text.replace("\\'", "'")
    text = text.replace('\\"', '"')
    text = text.replace("\\\\", "\\")
    text = text.replace("\\n", "\n")
    text = text.replace("\\r", "\r")
    text = text.replace("\\t", "\t")
    
    # Unescape HTML entities
    text = html.unescape(text)
    
    return text


def clean_wordpress_content(content):
    """Clean WordPress content and convert to markdown"""
    if not content:
        return ""
    
    # Remove WordPress block comments
    content = re.sub(r'<!-- wp:[^>]*? -->', '', content)
    content = re.sub(r'<!-- /wp:[^>]*? -->', '', content)
    
    # Convert basic HTML to markdown
    # Headers
    content = re.sub(r'<h1[^>]*>(.*?)</h1>', r'# \1', content, flags=re.DOTALL)
    content = re.sub(r'<h2[^>]*>(.*?)</h2>', r'## \1', content, flags=re.DOTALL)
    content = re.sub(r'<h3[^>]*>(.*?)</h3>', r'### \1', content, flags=re.DOTALL)
    content = re.sub(r'<h4[^>]*>(.*?)</h4>', r'#### \1', content, flags=re.DOTALL)
    content = re.sub(r'<h5[^>]*>(.*?)</h5>', r'##### \1', content, flags=re.DOTALL)
    content = re.sub(r'<h6[^>]*>(.*?)</h6>', r'###### \1', content, flags=re.DOTALL)
    
    # Horizontal rules
    content = re.sub(r'<hr[^>]*/?>', '\n---\n', content)
    
    # Paragraphs
    content = re.sub(r'<p[^>]*>(.*?)</p>', r'\1\n\n', content, flags=re.DOTALL)
    
    # Bold and italic
    content = re.sub(r'<strong[^>]*>(.*?)</strong>', r'**\1**', content, flags=re.DOTALL)
    content = re.sub(r'<b[^>]*>(.*?)</b>', r'**\1**', content, flags=re.DOTALL)
    content = re.sub(r'<em[^>]*>(.*?)</em>', r'*\1*', content, flags=re.DOTALL)
    content = re.sub(r'<i[^>]*>(.*?)</i>', r'*\1*', content, flags=re.DOTALL)
    
    # Links - handle cases where href has content but link text is empty
    content = re.sub(r'<a[^>]*href="([^"]*)"[^>]*>(.*?)</a>', lambda m: f'[{m.group(2) if m.group(2).strip() else m.group(1)}]({m.group(1)})', content, flags=re.DOTALL)
    
    # Blockquotes
    content = re.sub(r'<blockquote[^>]*>(.*?)</blockquote>', lambda m: '\n> ' + m.group(1).strip().replace('\n', '\n> ') + '\n', content, flags=re.DOTALL)
    
    # Images (convert to simple markdown images)
    content = re.sub(r'<img[^>]*src="([^"]*)"[^>]*alt="([^"]*)"[^>]*/?>', r'![\2](\1)', content, flags=re.DOTALL)
    content = re.sub(r'<img[^>]*src="([^"]*)"[^>]*/?>', r'![](\1)', content, flags=re.DOTALL)
    
    # Remove figure tags but keep content
    content = re.sub(r'<figure[^>]*>(.*?)</figure>', r'\1', content, flags=re.DOTALL)
    content = re.sub(r'<figcaption[^>]*>(.*?)</figcaption>', r'\n*\1*\n', content, flags=re.DOTALL)
    
    # Lists
    content = re.sub(r'<ul[^>]*>', '', content)
    content = re.sub(r'</ul>', '\n', content)
    content = re.sub(r'<ol[^>]*>', '', content)
    content = re.sub(r'</ol>', '\n', content)
    content = re.sub(r'<li[^>]*>(.*?)</li>', r'- \1', content, flags=re.DOTALL)
    
    # Line breaks
    content = re.sub(r'<br\s*/?>', '\n', content)
    
    # Remove WordPress shortcodes (they won't work in static site)
    content = re.sub(r'\[/?[^\]]*\]', '', content)
    
    # Remove complex WordPress blocks that don't convert well
    content = re.sub(r'<div class="wp-block-[^"]*"[^>]*>.*?</div>', '', content, flags=re.DOTALL)
    
    # Clean up extra whitespace
    content = re.sub(r'\n\s*\n\s*\n', '\n\n', content)
    content = content.strip()
    
    return content


def sanitize_filename(filename):
    """Sanitize filename for filesystem"""
    # Remove or replace problematic characters
    filename = re.sub(r'[^\w\-_\.]', '-', filename)
    filename = re.sub(r'-+', '-', filename)
    filename = filename.strip('-')
    return filename


def parse_wordpress_sql(sql_file_path):
    """Parse WordPress SQL file and extract blog posts"""
    posts = []
    
    with open(sql_file_path, 'r', encoding='utf-8', errors='ignore') as f:
        content = f.read()
    
    # Find all INSERT statements for wp_posts
    # Note: Using lazy matching (.+?) instead of [^;]+ because post content may contain semicolons
    insert_pattern = r"INSERT INTO `wp_posts` \([^)]+\) VALUES \((.+?)\);$"
    matches = re.findall(insert_pattern, content, re.DOTALL | re.MULTILINE)
    
    for match in matches:
        # Split the values, being careful about commas inside quoted strings
        values = []
        current_value = ""
        in_quotes = False
        quote_char = None
        i = 0
        
        while i < len(match):
            char = match[i]
            
            if not in_quotes:
                if char in ["'", '"']:
                    in_quotes = True
                    quote_char = char
                    current_value += char
                elif char == ',':
                    values.append(current_value.strip())
                    current_value = ""
                else:
                    current_value += char
            else:
                if char == quote_char:
                    # Check if it's escaped
                    if i > 0 and match[i-1] == '\\':
                        current_value += char
                    else:
                        in_quotes = False
                        quote_char = None
                        current_value += char
                else:
                    current_value += char
            
            i += 1
        
        # Add the last value
        if current_value.strip():
            values.append(current_value.strip())
        
        # Skip if we don't have enough values
        if len(values) < 23:
            continue
            
        # Extract the fields we need (based on the CREATE TABLE statement)
        try:
            post_id = values[0]
            post_date = values[2].strip("'")
            post_content = values[4].strip("'")
            post_title = values[5].strip("'")
            post_excerpt = values[6].strip("'")
            post_status = values[7].strip("'")
            post_name = values[11].strip("'")  # slug
            post_type = values[20].strip("'")
            
            # Only process published blog posts
            if post_type == 'post' and post_status == 'publish':
                # Unescape the content
                post_content = unescape_sql_string(post_content)
                post_title = unescape_sql_string(post_title)
                post_excerpt = unescape_sql_string(post_excerpt)
                post_name = unescape_sql_string(post_name)
                
                # Skip if no title or content
                if not post_title.strip() or not post_content.strip():
                    continue
                
                posts.append({
                    'id': post_id,
                    'title': post_title,
                    'content': post_content,
                    'excerpt': post_excerpt,
                    'date': post_date,
                    'slug': post_name,
                })
        except (IndexError, ValueError) as e:
            print(f"Error parsing post: {e}")
            continue
    
    return posts


def create_pelican_post(post, output_dir):
    """Create a Pelican markdown file from a WordPress post"""
    # Parse the date
    try:
        date_obj = datetime.strptime(post['date'], '%Y-%m-%d %H:%M:%S')
        date_str = date_obj.strftime('%Y-%m-%d %H:%M')
    except ValueError:
        print(f"Invalid date format for post '{post['title']}': {post['date']}")
        date_str = post['date']
    
    # Clean the content
    content = clean_wordpress_content(post['content'])
    
    # Create filename
    if post['slug']:
        filename = f"{post['slug']}.md"
    else:
        filename = f"{sanitize_filename(post['title'].lower().replace(' ', '-'))}.md"
    
    # Create Pelican frontmatter
    frontmatter = f"""Title: {post['title']}
Date: {date_str}
Slug: {post['slug'] if post['slug'] else sanitize_filename(post['title'].lower().replace(' ', '-'))}"""
    
    if post['excerpt'].strip():
        frontmatter += f"\nSummary: {post['excerpt'].strip()}"
    
    # Combine frontmatter and content
    full_content = f"{frontmatter}\n\n{content}"
    
    # Write the file
    output_path = output_dir / filename
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(full_content)
    
    return output_path


def main():
    """Main function"""
    # Configuration
    sql_file = "/Users/rbucks/Downloads/jetpack-backup-rbucks-com-2025-06-12-20-11-32/sql/wp_posts.sql"
    output_dir = Path("content")
    
    # Create output directory
    output_dir.mkdir(exist_ok=True)
    
    print(f"Parsing WordPress SQL file: {sql_file}")
    
    # Check if SQL file exists
    if not os.path.exists(sql_file):
        print(f"Error: SQL file not found at {sql_file}")
        return
    
    # Parse the SQL file
    posts = parse_wordpress_sql(sql_file)
    
    print(f"Found {len(posts)} published blog posts")
    
    if not posts:
        print("No posts found. Check the SQL file path and format.")
        return
    
    # Convert each post
    created_files = []
    for post in posts:
        try:
            output_path = create_pelican_post(post, output_dir)
            created_files.append(output_path)
            print(f"Created: {output_path}")
        except Exception as e:
            print(f"Error creating post '{post['title']}': {e}")
    
    print(f"\nConversion complete! Created {len(created_files)} markdown files in '{output_dir}' directory.")
    
    # Show summary of created files
    if created_files:
        print("\nCreated files:")
        for file_path in created_files:
            print(f"  - {file_path}")


if __name__ == "__main__":
    main()