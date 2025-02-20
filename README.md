Based on the information available from the repository, here is an installation guide for the Fintech AI Chatbot project:

# Fintech AI Chatbot Installation Guide

This guide provides step-by-step instructions to set up and run the Fintech AI Chatbot on your local machine.

## Prerequisites

Before you begin, ensure you have the following installed:

- **Python 3.13**: The project is built using Python 3.13. You can download it from the official Python website.

- **Virtual Environment**: It's recommended to use a virtual environment to manage dependencies.

## Installation Steps

1. **Clone the Repository**:

   ```bash
   git clone https://github.com/GitArunjangid/Chatbot.git
   ```


   Navigate into the project directory:

   ```bash
   cd Chatbot
   ```


2. **Set Up a Virtual Environment**:

   Create a virtual environment:

   ```bash
   python3.13 -m venv venv
   ```


   Activate the virtual environment:

   - On Windows:

     ```bash
     venv\Scripts\activate
     ```

   - On macOS and Linux:

     ```bash
     source venv/bin/activate
     ```

3. **Install Dependencies**:

   Ensure you have `pip` installed. Then, install the required packages:

   ```bash
   pip install -r requirements.txt
   ```


   If you encounter a permissions error, you might see a message like:

   ```
   Defaulting to user installation because normal site-packages is not writeable
   ```


   To resolve this, ensure your virtual environment is activated. If the issue persists, you can force installation within the user directory:

   ```bash
   pip install --user -r requirements.txt
   ```


4. **Set Up Environment Variables**:

   The project includes a `.env` file. Ensure this file contains all necessary environment variables. If it's missing, create one based on the project's requirements.

5. **Run the Chatbot**:

   Start the chatbot application:

   ```bash
   python ollama.py
   ```



