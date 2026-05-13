# COS730 Assignment 2 — Task 5: Optimised Implementation

## Overview
This folder contains the **optimised implementation** of the submission workflow, refactored to align with the improved sequence diagram.  
The design achieves cleaner separation of concerns, centralised decision logic, and functional equivalence with the baseline system.

---

## 📂 Folder Structure
```
Optimised/
 ├── src/                  # Refactored Python source code
 │   ├── main.py           # Test driver script
 │   ├── UI.py             # User interface entry point
 │   ├── SubmissionController.py
 │   ├── Validator.py
 │   ├── Database.py
 │   ├── ReviewerManager.py
 │   ├── EvaluationManager.py
 │   └── NotificationService.py
 ├── diagrams/            
 │   ├── optimised_sequence.puml
 │   └── optimised_sequence.png   # Optimised sequence diagram
 │   └── Task6_Optimised-MethodCall&ExecutionTimes/   # Execution runtime screenshots
 │       ├── Opt_Run1-2.png
 │       ├── Opt_Run3-4.png
 │       ├── Opt_Run5-6.png
 │       ├── Opt_Run7-8.png
 │       └── Opt_Run9-10.png
 └── README.md         
```

---

## Refactoring Highlights
- **SubmissionController**: Delegates orchestration only, removing embedded logic.  
- **Validator**: Owns validation and rejection handling.  
- **ReviewerManager**: Encapsulates reviewer filtering and assignment.  
- **EvaluationManager**: Implements Task 3 decision table rules (R1–R5).  
- **NotificationService**: Decoupled from evaluation, responsible only for communicating outcomes.  

---

## Class Changes from Baseline
- **SubmissionController**: Previously contained validation, database, reviewer, and evaluation logic inline. Now delegates to specialised classes.  
- **Validator**: Previously only validated input. Now also owns rejection logic.  
- **ReviewerManager**: Previously scattered reviewer logic. Now consolidated into one class.  
- **EvaluationManager**: Previously averaged scores without rules. Now centralises decision table logic.  
- **NotificationService**: Previously coupled with evaluation. Now decoupled, triggered solely by outcomes.  

---

## Test Cases
Execution evidence demonstrates functional equivalence with the baseline system:

| Test Case              | Input                        | Outcome                          |
|------------------------|------------------------------|----------------------------------|
| Invalid submission     | Missing title                | Rejected: Invalid format         |
| No reviewers           | force_no_reviewers flag      | Rejected: No reviewers available |
| Low scores             | [1,2,2]                      | Rejected                         |
| Moderate scores        | [3,3,4]                      | Revision                         |
| High scores            | [5,5,4]                      | Accepted                         |

---

## Mapping to Decision Table
- **R1**: High average with consensus → Accepted  
- **R2**: Moderate average with consensus → Revision  
- **R3**: Low average with consensus → Rejected  
- **R4**: No consensus → Revision  
- **R5**: No reviewers → Rejected  

---

## Traceability
Each lifeline in the optimised sequence diagram is mapped to a corresponding class in the `Optimised/src` folder.  
This ensures strict traceability between design artefacts, implementation, and test evidence.

---

## Execution Evidence
Running `main.py` in the optimised design produces fewer method calls compared to the baseline:

- **Invalid submissions**: 3 calls (vs. 12 baseline)  
- **Valid submissions**: 7 calls (vs. 12 baseline)  
- **Execution times**: 0.01–0.06 ms across repeated runs  

This confirms that the optimised design achieves functional equivalence while reducing redundant interactions and improving efficiency.

