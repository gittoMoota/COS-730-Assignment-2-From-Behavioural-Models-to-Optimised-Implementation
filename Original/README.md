# COS730 Assignment 2 — Task 1: Baseline Implementation

## Overview
This folder contains the **baseline implementation (Correctness Phase)** of the Intelligent Submission and Review System.  
The code was implemented exactly as specified in the provided sequence diagram. No optimisations were introduced at this stage.

---

## 📂 Folder Structure
```
Original/
├── src/        # Python source code for baseline implementation
├── diagrams/   # Provided baseline UML diagrams (sequence/class)
└── README.md   # Documentation for Task 1
```

---

## Class Mapping (Traceability)
Each lifeline in the sequence diagram is mapped to a class:

- **Researcher** → initiates submission via the UI  
- **UI** → forwards submission requests to the controller  
- **SubmissionController** → orchestrates the workflow  
- **Validator** → checks submission format  
- **Database** → saves submissions and retrieves reviewers  
- **ReviewerManager** → filters conflicts, checks workload, assigns reviewers  
- **Reviewer** → saves and submits scores  
- **EvaluationManager** → calculates averages, checks consensus, applies rules  
- **NotificationService** → communicates acceptance, rejection, or revision outcomes  

---

## Requirements Satisfied
- All interactions preserved (method calls mirror the diagram)  
- Object responsibilities match the diagram lifelines  
- No optimisations introduced (placeholders used intentionally)  
- Implemented in Python (object‑oriented)  
- Traceability maintained between diagram and code  

---

## Execution Evidence
Running `main.py` produces the following baseline output:

```
Validator: Checking format of submission...
Database: Saving submission...
Database: Fetching reviewers...
ReviewerManager: Filtering conflicts...
ReviewerManager: Checking workload...
EvaluationManager: Calculating average...
EvaluationManager: Checking consensus...
EvaluationManager: Applying rules...
NotificationService: Acceptance notification sent.
NotificationService: Submission accepted
```

This confirms the system executes end‑to‑end with all lifeline interactions visible.



## 📖 Notes
- This baseline implementation intentionally preserves inefficiencies for later analysis in Task 2.  
- Optimised diagrams and refactored code will be placed in the `Optimised` folder.  

