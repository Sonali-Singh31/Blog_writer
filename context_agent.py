import os
from typing import Dict, List, Any

from tools import fetch_news, fetch_quotes, fetch_related_words, retry_api_call


class ContextAgent:
    
    def __init__(self, gemini_model):
       
        self.gemini_model = gemini_model
        
    def research_topic(self, topic: str) -> Dict[str, Any]:
        
        research_data = {
            "keywords": [],
            "news": [],
            "quotes": [],
            "facts": [],
            "related_topics": []
        }
        
        research_data["keywords"] = self._generate_keywords(topic)
        research_data["news"] = fetch_news(topic)
        research_data["quotes"] = fetch_quotes(topic)
        research_data["facts"] = self._generate_facts(topic)
        research_data["related_topics"] = self._generate_related_topics(topic)
        
        return research_data
    
    def _generate_keywords(self, topic: str) -> List[str]:
        keywords = []
        
        topic_words = [word.strip().lower() for word in topic.split() if len(word.strip()) > 3]
        keywords.extend(topic_words)
        
        related_words = fetch_related_words(topic, max_results=10)
        keywords.extend(related_words)
        
        for word in topic_words:
            word_related = fetch_related_words(word, max_results=5)
            keywords.extend(word_related)
        
        unique_keywords = list(set(keywords))
        unique_keywords.sort(key=len)
        
        return unique_keywords[:20]
    
    def _generate_facts(self, topic: str) -> List[str]:
        facts_prompt = f"""
         "{topic}".
        """
        
        try:
            response = self.gemini_model.generate_content(facts_prompt)
            facts_text = response.text.strip()
            raw_facts = [
                line.strip()[2:].strip() if line.strip().startswith("- ") else line.strip()
                for line in facts_text.split("\n")
                if line.strip() and not line.strip().startswith("#")
            ]
            facts = [fact for fact in raw_facts if len(fact) > 10]
            return facts
        except Exception as e:
            print(f"Failed to generate facts: {e}")
            return []
    
    def _generate_related_topics(self, topic: str) -> List[str]:
        topics_prompt = f""""{topic}".
        """
        
        try:
            response = self.gemini_model.generate_content(topics_prompt)
            topics_text = response.text.strip()
            raw_topics = [
                line.strip()[2:].strip() if line.strip().startswith("- ") else line.strip()
                for line in topics_text.split("\n")
                if line.strip() and not line.strip().startswith("#")
            ]
            topics = [topic for topic in raw_topics if len(topic) > 5]
            return topics
        except Exception as e:
            print(f"Failed to generate related topics: {e}")
            return []
    
    def enrich_outline(self, topic: str, outline: List[str]) -> Dict[str, Any]:
        enrichment_data = {}
        
        for section in outline:
            section_data = {
                "keywords": [],
                "facts": [],
                "quotes": []
            }
            
            section_keywords = fetch_related_words(section, max_results=5)
            section_data["keywords"] = section_keywords
            
            section_quotes = fetch_quotes(section, limit=1)
            if not section_quotes:
                section_quotes = fetch_quotes(topic, limit=1)
            section_data["quotes"] = section_quotes
            
            try:
                fact_prompt = f""" "{section}" 
                """
                response = self.gemini_model.generate_content(fact_prompt)
                section_data["facts"] = [response.text.strip()]
            except Exception:
                section_data["facts"] = []
            
            enrichment_data[section] = section_data
        
        return enrichment_data
