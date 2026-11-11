![Android Automation CI](https://github.com/alifdev/quizmaster-mobile-automation/actions/workflows/android-automation.yml/badge.svg)

# QuizMaster Android Mobile Automation

An Android mobile test automation project for **QuizMaster**, a Flutter-based quiz application. This project uses Python, Appium, and Pytest to validate key application flows through an automated test suite.

## Project Overview

The framework follows the **Page Object Model (POM)** design pattern to separate test logic from page interactions and improve maintainability.

**Application Under Test:** [QuizMaster](https://github.com/Kevinnnhub/quizmaster)

## Tech Stack

- Python 3.14
- Pytest 9.2
- Appium-Python-Client 6.0
- Appium Server 3.1.2
- UiAutomator2 Driver 6.7.1
- Selenium WebDriver
- Android Emulator

## Automated Test Coverage

The current test suite contains 15 automated tests covering:

| Area | Test Scenarios |
|---|---|
| App Launch | Verify that the application opens and the home screen is displayed |
| Category Selection | Select the History quiz category |
| Quiz Initialization | Start a quiz and verify the initial question |
| Answer Selection | Select an answer and validate the feedback |
| Question Progression | Verify progression to the next question |
| Answer Validation | Validate answers using the application's question data |
| Timer | Verify countdown behavior and timer expiration |
| Quiz Completion | Complete a quiz and verify the results screen |
| Score Calculation | Verify the final score calculation |
| Quiz State | Verify quiz state reset when starting a new session |
| Replay | Start a new quiz using the Play Again action |
| Leaderboard | Save a quiz score and verify the leaderboard entry |

## Project Structure

```text
QuizMaster-Mobile-Automation/
├── config/
│   └── settings.py
├── pages/
│   ├── base_page.py
│   ├── home_page.py
│   ├── quiz_page.py
│   └── results_page.py
├── reports/
├── test_data/
│   └── questions.json
├── tests/
│   ├── test_answer_key.py
│   ├── test_answer_selection.py
│   ├── test_app_launch.py
│   ├── test_category_selection.py
│   ├── test_play_again.py
│   ├── test_question_progression.py
│   ├── test_quiz_answer_key.py
│   ├── test_quiz_completion.py
│   ├── test_quiz_full_answer_key.py
│   ├── test_quiz_score_calculation.py
│   ├── test_quiz_state_reset.py
│   ├── test_quiz_timer.py
│   ├── test_quiz_timer_expiration.py
│   ├── test_save_quiz_score.py
│   └── test_start_quiz.py
├── utils/
│   └── answer_key.py
├── conftest.py
├── pytest.ini
├── requirements.txt
└── .gitignore
```

## Prerequisites

Make sure the following tools are installed and configured:

- Python 3.14 or compatible version
- Node.js and npm
- Java JDK 17
- Android SDK and Android Emulator
- Appium Server
- Appium UiAutomator2 driver

The project was developed and tested on Windows using an Android emulator.

## Setup and Installation

### 1. Clone the repository

```bash
git clone <YOUR_GITHUB_REPOSITORY_URL>
cd QuizMaster-Mobile-Automation
```

### 2. Create and activate a virtual environment

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

### 3. Install Python dependencies

```bash
pip install -r requirements.txt
```

### 4. Install Appium

If Appium is not already installed:

```bash
npm install -g appium
```

Install the UiAutomator2 driver:

```bash
appium driver install uiautomator2
```

### 5. Prepare the Android emulator

Start an Android emulator and verify that it is detected:

```bash
adb devices
```

Make sure the QuizMaster application is installed on the emulator.

The current configuration uses:

- Device UDID: `emulator-5554`
- Application package: `com.example.quizmaster`
- Application activity: `.MainActivity`

Update `config/settings.py` if your emulator or application configuration is different.

### 6. Start the Appium server

Open a separate terminal and run:

```bash
appium --address 127.0.0.1 --port 4723
```

### 7. Run the automated tests

From the project root directory:

```bash
pytest -v
```

For a shorter failure report:

```bash
pytest -v --tb=short
```

## Test Execution Result

Latest full regression execution:

| Metric | Result |
|---|---:|
| Total Tests | 15 |
| Passed | 15 |
| Failed | 0 |
| Execution Time | 6 minutes 29 seconds |

**Status: All 15 automated tests passed.**

## Test Data

The question dataset is maintained by the original QuizMaster application repository and is not redistributed in this automation repository.

Download the dataset from the original source:

[QuizMaster questions.json](https://raw.githubusercontent.com/Kevinnnhub/quizmaster/main/assets/questions.json)

Place the downloaded file at:

`test_data/questions.json`

On Windows PowerShell, you can download it using:

```powershell
Invoke-WebRequest `
  -Uri "https://raw.githubusercontent.com/Kevinnnhub/quizmaster/main/assets/questions.json" `
  -OutFile "test_data/questions.json"
```

The `AnswerKey` utility reads this local dataset to validate the expected correct answers during automated tests.

## Design Approach

- **Page Object Model:** Separates page locators and interactions from test scenarios.
- **Reusable Base Page:** Centralizes common actions and explicit wait behavior.
- **Data-Driven Validation:** Uses question data to validate correct answers.
- **Explicit Waits:** Waits for relevant UI elements and application state changes.
- **Independent Test Scenarios:** Covers key user flows through separate test cases.

## Disclaimer

This repository contains the mobile automation test framework. The QuizMaster application is a separate application used as the system under test. All product names and application source code belong to their respective owners.