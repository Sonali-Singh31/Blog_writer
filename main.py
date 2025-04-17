
import sys
from tools import setup_gemini_model
from writing_agent import WritingAgent

def main():
    if len(sys.argv) < 2:
        print("Usage: python main.py <topic> [--tone <tone>]")
        sys.exit(1)

    topic = sys.argv[1]
    tone = "educational"

    if "--tone" in sys.argv:
        tone_index = sys.argv.index("--tone") + 1
        if tone_index < len(sys.argv):
            tone = sys.argv[tone_index]

    # Setup Gemini model
    gemini_model = setup_gemini_model()

    # Initialize Writing Agent with the model
    writing_agent = WritingAgent(gemini_model)

    # Generate blog content
    blog_content = writing_agent.generate_blog(topic, tone)
    print("\n===== Generated Blog =====\n")
    print(blog_content)

if __name__ == "__main__":
    main()
