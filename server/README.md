# BlockPay Server Side

## Overview

BlockPay Server Side is a Python application that serves as the backend for processing payments using blockchain technology. This server-side application is built with Python 3.11.5 and utilizes a virtual environment (.venv) to manage dependencies.

## Prerequisites

Before running the BlockPay Server Side application, ensure that you have the following prerequisites installed:

- Python 3.11.5: [Download Python](https://www.python.org/downloads/release)

## Setup

1. Clone the BlockPay Server Side repository:

   ```bash
   git clone https://github.com/PRANJALRANA11/BlockPay
   cd BlockPay/server
   ```

2. Create a virtual environment and activate it:

   ```bash
   python -m venv .venv
   source .venv/bin/activate   # For Linux/Mac
   .venv\Scripts\activate      # For Windows
   ```

3. Install dependencies using the provided requirements.txt file:

   ```bash
   pip install -r requirements.txt
   ```



## Running the Server

Start the BlockPay Server by running the following command:

```bash
uvicorn main:app --reload #for development 
```

The server will start running at `http://localhost:8000`.



