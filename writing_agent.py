import re
from typing import Dict, List, Any, Optional
from tools import setup_gemini_model
from datamuse_utils import get_related_keywords
from tools import clean_text, validate_markdown

class WritingAgent:
    
    def __init__(self, gemini_model):
        self.gemini_model = gemini_model
        
    def generate_blog(self, topic: str, tone: str = "educational", 
                      sections: int = 5, research_data: Optional[Dict[str, Any]] = None) -> str:
        if research_data is None:
            research_data = {
                "keywords": [],
                "news": [],
                "quotes": [],
                "facts": [],
                "related_topics": []
            }

        outline = self._generate_outline(topic, tone, sections, research_data)
        introduction = self._generate_introduction(topic, tone, outline, research_data)

        content_sections = []
        for section_title in outline:
            section_content = self._generate_section(topic, section_title, tone, research_data)
            content_sections.append(f"## {section_title}\n\n{section_content}")

        conclusion = self._generate_conclusion(topic, tone, outline, research_data)

        blog_content = [
            f"# {self._generate_title(topic, tone)}\n",
            introduction,
            *content_sections,
            f"## Conclusion\n\n{conclusion}"
        ]

        full_content = "\n\n".join(blog_content)
        cleaned_content = validate_markdown(clean_text(full_content))
        return cleaned_content

    def _generate_title(self, topic: str, tone: str) -> str:
        title_keywords = get_related_keywords(topic)

        title_prompt = f""" {tone}
        """

        try:
            response = self.gemini_model.generate_content(title_prompt)
            title = response.text.strip()
            return title.replace('"', '').replace("'", "")
        except Exception as e:
            print(f"Failed to generate title: {e}")
            return topic.title()

    def _generate_outline(self, topic: str, tone: str, sections: int, 
                          research_data: Dict[str, Any]) -> List[str]:
        if research_data.get("related_topics") and len(research_data["related_topics"]) >= sections:
            return research_data["related_topics"][:sections]

        keywords_str = ", ".join(get_related_keywords(topic)[:10])

        outline_prompt = f""" {tone} "{topic}". {sections}  :{keywords_str}
        """

        try:
            response = self.gemini_model.generate_content(outline_prompt)
            outline_text = response.text.strip()
            headings = []
            for line in outline_text.split("\n"):
                clean_line = re.sub(r"^\d+\.\s*", "", line).strip()
                if clean_line:
                    headings.append(clean_line)
            return headings
        except Exception as e:
            print(f"Failed to generate outline: {e}")
            return [f"Section {i+1}" for i in range(sections)]

    def _generate_introduction(self, topic: str, tone: str, outline: List[str], research_data: Dict[str, Any]) -> str:
        prompt = f"""{tone} "{topic}".
        """
        try:
            response = self.gemini_model.generate_content(prompt)
            return response.text.strip()
        except Exception as e:
            print(f"Failed to generate introduction: {e}")
            return f"This blog post explores the topic: {topic}."

    def _generate_section(self, topic: str, section_title: str, tone: str, research_data: Dict[str, Any]) -> str:
        prompt = f"""
        Write a {tone} section for the blog post titled "{topic}".
        The section heading is: "{section_title}".
        """
        try:
            response = self.gemini_model.generate_content(prompt)
            return response.text.strip()
        except Exception as e:
            print(f"Failed to generate section '{section_title}': {e}")
            return f"Content about {section_title}."

    def _generate_conclusion(self, topic: str, tone: str, outline: List[str], research_data: Dict[str, Any]) -> str:
        prompt = f"""{tone}  "{topic}".
        """
        try:
            response = self.gemini_model.generate_content(prompt)
            return response.text.strip()
        except Exception as e:
            print(f"Failed to generate conclusion: {e}")
            return f"That's all on the topic of {topic}. Thanks for reading!"
