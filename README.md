# BibleBeaconAI
BibleBeaconAI is an open-source AI Agent designed to integrate AI into Christian faith-based activities, serving as an assistant during sermons.

This is an open-source FastAPI project that uses an agent to process Bible queries and return relevant verses.

## Installation

1. Clone this repository.
2. Install dependencies:

    ```bash
    pip install -r requirements.txt
    ```

3. Run the FastAPI application:

    ```bash
    uvicorn app.main:app --reload
    ```

--

## Usage

### 1. Query Bible verses by topic:

POST request to `/agent/query` with the body:

```json
{
  "topic": "For God so loved the worled, that he.."
}

#### Agent Response:

================================ Human Message =================================

For God so loved the worled, that he..
================================== Ai Message ==================================
Tool Calls:
  suggest_bible_verses (call_7vcrFAgEguHxmYUKjOHW5IT9)
 Call ID: call_7vcrFAgEguHxmYUKjOHW5IT9
  Args:
    topic: God's love
================================= Tool Message =================================
Name: suggest_bible_verses

[{"translation": "KJV", "book": 43, "chapter": 3, "verses": [16]}]
================================== Ai Message ==================================

The verse you're referring to is John 3:16, which in the King James Version (KJV) is:

"For God so loved the world, that he gave his only begotten Son, that whosoever believeth in him should not perish, but have everlasting life." 

This verse emphasizes God's immense love for humanity and the gift of salvation through Jesus Christ.

--

**1. Project Overview**

- **Goals**: Enhance sermon preparation and delivery through speech-to-text transcription, Bible verse detection, message summarization, and action item generation for the congregation.
- **Scope**: The tool will support speech recognition, Bible verse detections, summarization, and user interaction.
- **Vision**: To provide a comprehensive AI tool that supports preachers in effectively delivering sermons and the congregations for automated material/notes generation.
- **Mission**: To assist preachers by automating repetitive tasks(manual verse opening), allowing them to focus on their message and congregation.

---

**2. Feature Overview**

- **Speech-to-Text Transcription**: Real-time conversion of sermon content into text.
- **Bible Verse Detection**: Identification of relevant Bible verses based on sermon content.
- **Message Summarization**: Generation of concise summaries of sermon messages.
- **Action Item Generation**: Creation of actionable items based on sermon content for the congregation.
- **Integration with Bible APIs/Databases**: Seamless connection to existing resources for accurate verse reference.
- **User Interface**: An interface for preachers to review and interact with generated content.

**Visuals**: Mockups and diagrams will be included to provide a clear understanding of the system's functionality.

---

**3. Contributing Guidelines**

- **Contribution Workflow**: Information on how to report issues, suggest features, and submit code changes.
- **Code Reviews and Testing**: Expectations for maintaining code quality and ensuring functionality.
- **Documentation**: Requirements for contributors to keep documentation up-to-date and relevant.

---

**4. Technical Documentation**

- **System Architecture**: Diagrams and explanations of the system's structure.
- **API Documentation**: Detailed information on any public APIs involved in the project.
- **Technology Stack**: Description of the technologies and tools used in the development of the project.
- **Roadmap**: Future plans and improvements, providing insight into upcoming features and enhancements.

---

**5. Resources**

- **Community Forums**: Links to forums where users can discuss the project and seek support.
- **Documentation Repositories**: Access to comprehensive documentation and guides.
- **Developer Hub**: Resources for developers interested in contributing to the project.

---

**6. Credits and Acknowledgments**

- **Contributors**: Recognition of all individuals who have contributed to the project, including developers, testers, and supporters will be added here in the future.

---

**7. Documentation Hosting and Versioning**

- **GitHub Pages**: The documentation will be hosted on GitHub Pages for a polished presentation.
- **Versioning**: The documentation will be versioned to match project releases, ensuring users have access to the most current information.

---

**8. Community Contributions to Documentation**

- **Process for Submission**: A clear process for submitting documentation improvements, empowering the community to maintain and enhance project resources.

---

**Conclusion**

Preacher's Companion aims to be a valuable tool for preachers, enhancing their ability to deliver impactful sermons. The project seeks to foster a community of contributors and users who can collaborate to improve and expand the tool's capabilities.