# COS730 Assignment 2 — Task 1: Baseline Implementation

## Overview
This folder contains the baseline implementation (Correctness Phase) of the **Intelligent Submission and Review System**.  
The code was implemented exactly as specified in the provided sequence diagram. No optimisations were introduced at this stage; placeholders were deliberately used to preserve the raw flow.

---

## Folder Structure
```
Original/
├── src/        # Python source code for baseline implementation
├── diagrams/   # Baseline UML diagrams (sequence/class)
│   ├── Task6_Original-MethodCall&ExecutionTimes/   # Execution runtime screenshots
│       ├── Orig_Run1-2.png  
│       ├── Orig_Run3-4.png
│       ├── Orig_Run5-6.png
│       ├── Orig_Run7-8.png
│       └──  Orig_Run9-10.png 
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
- **ReviewerManager** → filters conflicts, checks workload, provides reviewer lists  
- **Reviewer** → receives assignment and submits scores  
- **EvaluationManager** → calculates averages, checks consensus, applies rules  
- **NotificationService** → communicates acceptance, rejection, or revision outcomes    

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
Execution time: 0.41–1.45 ms (across repeated runs)
Total method calls: 12
```

This confirms the system executes end‑to‑end with all lifeline interactions visible.  
The global counter consistently reports **12 method calls**, which is one more than the 11 interactions in the baseline diagram. The discrepancy arises because an additional helper/constructor method is being instrumented with `call_counter()`. This is documented in **Task 6** as part of the empirical evaluation.


