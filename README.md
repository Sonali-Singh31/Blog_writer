# Agentic Python Blog Writer

## Overview
The **Agentic Python Blog Writer** is an AI-driven script that autonomously generates long-form SEO blogs based on a given topic. It mimics the role of a junior blog writer by performing the following tasks:
- Analyzing the input topic and breaking it down into relevant subtopics.
- Researching using external APIs to gather useful information.
- Generating content with an SEO-optimized structure.
- Exporting blog posts and structured metadata.

This project aims to automate the blog writing process for anyone needing SEO-optimized content for their website or blog.

## How to Run the Script

### Requirements
Ensure you have Python 3.7+ installed on your system.

### Steps to Run the Script:
1. **Clone the repository**:
    ```bash
    git clone https://github.com/Sonali-Singh31/Blog_writer.git
    cd Blog_writer
    ```

2. **Install dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

3. **Set up your environment variables**:
    Create a `.env` file in the root directory of the project and add your API keys:
    ```env
    GEMINI_API_KEY=your-gemini-api-key
    NEWSDATA_API_KEY=your-newsdata-api-key

    # Gemini Model Configuration
    GEMINI_MODEL_NAME=gemini-1.5-pro
    GEMINI_TEMPERATURE=0.7
    GEMINI_TOP_P=0.95
    GEMINI_TOP_K=40
    GEMINI_MAX_OUTPUT_TOKENS=8192

    # Blog Generation Settings
    DEFAULT_BLOG_SECTIONS=5
    WORDS_PER_SECTION=250
    OUTPUT_DIRECTORY=output

    # API Retry Settings
    MAX_RETRIES=3
    BASE_DELAY=1.0

    # Content Enrichment Settings
    MAX_NEWS_ARTICLES=3
    MAX_QUOTES=2
    MAX_RELATED_KEYWORDS=10

    # CLI Display Settings
    SHOW_PROGRESS=True
    VERBOSE_OUTPUT=False
    ```

4. **Run the script**:
    After completing the setup, you can run the script with the following command:
    ```bash
    python main.py "How Python is used in AI" --tone educational
    ```

   - `"How Python is used in AI"`: Replace this with the topic you want to generate a blog about.
   - `--tone`: Optionally, specify the tone of the blog (e.g., `educational`, `formal`, `creative`).

## Setup Instructions

### Step 1: API Keys
- **Google Gemini API**: To use the Google Gemini API for content generation, you need to obtain an API key from the [Google Cloud Platform](https://cloud.google.com/).
- **NewsData.io API**: To fetch related news articles, sign up for NewsData.io and get your API key.
- **Additional APIs**:
    - Datamuse API (for keyword suggestions).
    - Quotable.io API (for including quotes).

### Example Blog Output
```Output


Example Blog Output
Here’s an example of the blog generated for the topic "How Python is used in AI":

Generated Blog
markdown
Copy
Edit
# How Python Is Used In AI

Artificial intelligence (AI) is revolutionizing many industries, and Python has become one of the most popular programming languages for AI development. This blog post will explore why Python is the preferred language for AI, the tools it offers for AI development, and how you can leverage these tools to build intelligent systems.

## Why Python is Popular in AI

Python's simplicity, readability, and rich ecosystem make it the ideal language for AI projects. It allows developers to focus on solving AI problems rather than worrying about low-level programming. Its vast libraries and frameworks provide ready-to-use solutions for a wide range of AI tasks.

### Key Libraries in Python for AI

1. **NumPy**: Essential for numerical computations and data manipulation.
2. **Pandas**: Used for data analysis and manipulation.
3. **Scikit-learn**: A powerful library for machine learning algorithms.
4. **TensorFlow & PyTorch**: Leading frameworks for deep learning.
5. **Keras**: An easy-to-use API for building deep learning models.

These libraries provide pre-built functions that help simplify the process of developing AI models.

## Machine Learning with Python

Python’s machine learning libraries make it easy to implement machine learning algorithms. Some common machine learning tasks you can perform with Python include:
- **Supervised Learning**: Algorithms like linear regression and support vector machines.
- **Unsupervised Learning**: Clustering algorithms such as K-means.
- **Reinforcement Learning**: Python libraries like TensorFlow provide frameworks to build reinforcement learning agents.

## Deep Learning with Python

Deep learning is a subfield of machine learning that is used for tasks like image recognition, speech recognition, and natural language processing. Python’s deep learning frameworks, such as TensorFlow and PyTorch, are widely used for training neural networks.

For example, you can use **Keras** (built on top of TensorFlow) to create a Convolutional Neural Network (CNN) for image classification. The process is simple and streamlined with Python.

## Conclusion

Python has become a dominant language for AI due to its ease of use, extensive libraries, and vibrant community. Whether you're developing machine learning models, deep learning systems, or working with natural language processing, Python provides the tools and resources you need to succeed.

By leveraging Python's libraries and frameworks, you can build state-of-the-art AI applications and contribute to the growing field of artificial intelligence.
