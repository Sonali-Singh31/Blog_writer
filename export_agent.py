
import json
import os
from datetime import datetime
from typing import Dict, Any


class ExportAgent:
    
    def __init__(self, output_dir: str = "output"):
        
        self.output_dir = output_dir
        os.makedirs(output_dir, exist_ok=True)
        
    def export_blog(self, content: str, metadata: Dict[str, Any]) -> Dict[str, str]:
        
        # Create timestamp for unique filenames
        timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
        
        # Create slug from metadata or use timestamp
        slug = metadata.get("slug", f"blog-{timestamp}")
        
        # Ensure slug is valid for filenames
        slug = slug.replace(" ", "-").lower()
        
        # Define file paths
        md_path = os.path.join(self.output_dir, f"{slug}.md")
        json_path = os.path.join(self.output_dir, f"{slug}.json")
        
        # Add front matter to markdown if needed
        content_with_frontmatter = self._add_front_matter(content, metadata)
        
        # Write files
        with open(md_path, "w", encoding="utf-8") as md_file:
            md_file.write(content_with_frontmatter)
            
        with open(json_path, "w", encoding="utf-8") as json_file:
            json.dump(metadata, json_file, indent=2)
            
        # Return file paths
        return {
            "markdown": md_path,
            "metadata": json_path
        }
    
    def _add_front_matter(self, content: str, metadata: Dict[str, Any]) -> str:
       
        front_matter = [
            "---",
            f"title: {metadata.get('title', 'Untitled Blog')}",
            f"description: {metadata.get('meta_description', '')}",
            f"date: {datetime.now().strftime('%Y-%m-%d')}",
            f"reading_time: {metadata.get('reading_time', 0)} min",
            f"slug: {metadata.get('slug', '')}",
            "keywords:",
        ]
        
        # Add keywords as a YAML list
        for keyword in metadata.get("keywords", []):
            front_matter.append(f"  - {keyword}")
            
        front_matter.append("---\n")
        
        # Combine front matter with content
        return "\n".join(front_matter) + content
    
    def generate_summary(self, metadata: Dict[str, Any], file_paths: Dict[str, str]) -> str:
        
        summary = [
            "\n" + "=" * 50,
            "✅ BLOG GENERATION COMPLETE",
            "=" * 50,
            f"📝 Title: {metadata.get('title', 'Untitled')}",
            f"📊 Word Count: {metadata.get('word_count', 0)}",
            f"⏱️ Reading Time: {metadata.get('reading_time', 0)} min",
            f"🔗 Slug: {metadata.get('slug', '')}",
            "\n Keywords:",
        ]
        
        for keyword in metadata.get("keywords", []):
            summary.append(f"  - {keyword}")
            
        summary.extend([
            "\n📂 Exported Files:",
            f"  - Markdown: {file_paths['markdown']}",
            f"  - Metadata: {file_paths['metadata']}",
            "\n" + "=" * 50
        ])
        
        return "\n".join(summary)