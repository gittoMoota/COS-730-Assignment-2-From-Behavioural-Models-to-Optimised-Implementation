## Overview
This folder contains the baseline implementation (Correctness Phase) of the **Intelligent Submission and Review System**.  
The code was implemented exactly as specified in the provided sequence diagram. No optimisations were introduced at this stage; placeholders were deliberately used to preserve the raw flow.

---

## 📂 Folder Structure
```
Original/
├── src/        # Python source codes for baseline implementation
├── diagrams/   # Baseline UML diagrams (sequence/class)
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
SubmissionController: Assigning reviewer...
EvaluationManager: Starting evaluation...
EvaluationManager: Calculating average...
EvaluationManager: Checking consensus...
EvaluationManager: Applying rules...
NotificationService: Acceptance notification sent.
NotificationService: Submission accepted
```
This confirms the system executes end‑to‑end with all lifeline interactions visible.

---

## 📖 Notes
- This baseline implementation intentionally preserves inefficiencies for later analysis in **Task 2**.  
- Optimised diagrams and refactored code will be placed in the `Optimised/` folder.  
```

