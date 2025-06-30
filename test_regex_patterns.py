#!/usr/bin/env python3
"""
Test script to compare regex patterns and see why the original script might be missing post 275
"""

import re


def test_regex_patterns():
    """Test different regex patterns to see which ones match post 275"""
    sql_file = "/Users/rbucks/Downloads/jetpack-backup-rbucks-com-2025-06-12-20-11-32/sql/wp_posts.sql"
    
    print("Testing Regex Patterns for Post 275")
    print("=" * 80)
    
    with open(sql_file, 'r', encoding='utf-8', errors='ignore') as f:
        content = f.read()
    
    # Test patterns
    patterns = [
        ("Original Pattern", r"INSERT INTO `wp_posts` \([^)]+\) VALUES \(([^;]+)\);"),
        ("Flexible Pattern", r"INSERT INTO `wp_posts`[^)]+\) VALUES \(([^;]+)\);"),
        ("Dotall Pattern", r"INSERT INTO `wp_posts` \([^)]+\) VALUES \(([^;]+)\);"),
        ("Multiline Pattern", r"INSERT INTO `wp_posts`.*?VALUES \(([^;]+)\);"),
    ]
    
    post_275_found = False
    
    for name, pattern in patterns:
        print(f"\n🔍 Testing: {name}")
        print(f"Pattern: {pattern}")
        
        try:
            # Test without DOTALL
            matches = re.findall(pattern, content)
            print(f"  Matches (no flags): {len(matches)}")
            
            # Check if any match contains post 275
            found_275 = False
            for match in matches:
                if match.strip().startswith('275,'):
                    found_275 = True
                    post_275_found = True
                    break
            
            print(f"  Contains Post 275: {found_275}")
            
            # Test with DOTALL
            matches_dotall = re.findall(pattern, content, re.DOTALL)
            print(f"  Matches (DOTALL): {len(matches_dotall)}")
            
            # Check if any match contains post 275
            found_275_dotall = False
            for match in matches_dotall:
                if match.strip().startswith('275,'):
                    found_275_dotall = True
                    post_275_found = True
                    break
            
            print(f"  Contains Post 275 (DOTALL): {found_275_dotall}")
            
        except Exception as e:
            print(f"  Error: {e}")
    
    print(f"\n📊 SUMMARY:")
    print(f"Post 275 found by at least one pattern: {post_275_found}")
    
    # Let's also check the original wordpress_to_pelican.py logic
    print(f"\n🔍 Testing Original Script Logic:")
    original_pattern = r"INSERT INTO `wp_posts` \([^)]+\) VALUES \(([^;]+)\);"
    matches = re.findall(original_pattern, content, re.DOTALL)
    print(f"Original pattern matches: {len(matches)}")
    
    # Check each match for post 275
    for i, match in enumerate(matches):
        if '275,' in match and 'An ode to the suburbs' in match:
            print(f"✅ Found post 275 in match {i+1}")
            print(f"Match starts with: {match[:100]}...")
            break
    else:
        print("❌ Post 275 not found in any matches")
        
        # Let's check why - look at the structure around post 275
        print("\n🔍 Investigating why post 275 is missed...")
        
        # Find the line with post 275
        lines = content.split('\n')
        for i, line in enumerate(lines):
            if '275,' in line and 'An ode to the suburbs' in line:
                print(f"Found post 275 on line {i+1}")
                print(f"Line starts with: {line[:100]}...")
                
                # Check if this line matches the pattern
                if re.match(original_pattern, line, re.DOTALL):
                    print("✅ Line matches the original pattern")
                else:
                    print("❌ Line does NOT match the original pattern")
                    
                    # Check what part fails
                    if line.startswith('INSERT INTO `wp_posts`'):
                        print("  ✅ Starts with INSERT INTO `wp_posts`")
                    else:
                        print(f"  ❌ Does not start with INSERT INTO `wp_posts`, starts with: {line[:50]}")
                        
                    if 'VALUES (' in line:
                        print("  ✅ Contains VALUES (")
                    else:
                        print("  ❌ Does not contain VALUES (")
                        
                    if line.endswith(');'):
                        print("  ✅ Ends with );")
                    else:
                        print(f"  ❌ Does not end with );, ends with: {line[-10:]}")
                
                break
        else:
            print("❌ Could not find post 275 in any line")


def main():
    test_regex_patterns()


if __name__ == "__main__":
    main()