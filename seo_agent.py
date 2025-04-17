import json
import re
from typing import Dict, List, Any

import google.generativeai as genai
from datamuse_utils import get_related_keywords


class SEOAgent:
    
    def __init__(self, gemini_model):
        
        self.gemini_model = gemini_model
        
    def optimize_content(self, topic: str, content: str) -> Dict[str, Any]:
       
        # Calculate reading time (average reading speed: 200 words per minute)
        word_count = len(content.split())
        reading_time = max(1, round(word_count / 200))
        
        # Generate SEO metadata using Gemini
        seo_prompt = f"""'{topic}'
        {content[:3000]}...
        """
        
        seo_response = self.gemini_model.generate_content(seo_prompt)
        
        try:
            # Extract JSON from the response
            json_pattern = r'```json(.*?)```'
            json_match = re.search(json_pattern, seo_response.text, re.DOTALL)
            
            if json_match:
                seo_data = json.loads(json_match.group(1).strip())
            else:
                seo_data = json.loads(seo_response.text)
                
        except (json.JSONDecodeError, AttributeError):
            # Fallback if JSON parsing fails
            seo_data = {
                "title": self._generate_title(topic),
                "meta_description": self._generate_meta_description(content),
                "slug": self._generate_slug(topic),
                "keywords": self._generate_keywords(topic, content)
            }
        
        # Ensure we have all the required keys
        if "title" not in seo_data:
            seo_data["title"] = self._generate_title(topic)
        if "meta_description" not in seo_data:
            seo_data["meta_description"] = self._generate_meta_description(content)
        if "slug" not in seo_data:
            seo_data["slug"] = self._generate_slug(topic)
        if "keywords" not in seo_data:
            seo_data["keywords"] = self._generate_keywords(topic, content)
            
        # Add reading time
        seo_data["reading_time"] = reading_time
        seo_data["word_count"] = word_count
        
        # Enhance keywords with Datamuse via utils
        seo_data["keywords"] = self._enhance_keywords(seo_data["keywords"])
        
        return seo_data
    
    def _generate_title(self, topic: str) -> str:
        return f"{topic.title()}: A Comprehensive Guide"
    
    def _generate_meta_description(self, content: str) -> str:
        # Take first 150 characters of content, strip markdown, and add ellipsis
        clean_text = re.sub(r'#+ |[*_`]', '', content[:200])
        return clean_text[:157] + "..."
    
    def _generate_slug(self, topic: str) -> str:
        return topic.lower().replace(' ', '-').replace('?', '').replace('!', '')
    
    def _generate_keywords(self, topic: str, content: str) -> List[str]:
        return [topic.lower()] + topic.lower().split()[:3]
    
    def _enhance_keywords(self, base_keywords: List[str]) -> List[str]:
        return get_related_keywords(base_keywords)
