## Overview
This folder contains the **optimised implementation** of the submission workflow, refactored to align with the improved sequence diagram.  
The design achieves cleaner separation of concerns, centralised decision logic, and functional equivalence with the baseline system.

## Folder Structure
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
 ├── diagrams/             # Optimised sequence diagram
 │   ├── optimised_sequence.puml
 │   └── optimised_sequence.png
 └── README.md             # Documentation
```

## Refactoring Highlights
- **SubmissionController**: Delegates orchestration only, removing embedded logic.  
- **Validator**: Owns validation and rejection handling.  
- **ReviewerManager**: Encapsulates reviewer filtering and assignment.  
- **EvaluationManager**: Implements Task 3 decision table rules (R1–R5).  
- **NotificationService**: Decoupled from evaluation, responsible only for communicating outcomes.  

## Class Changes from Baseline
- **SubmissionController**: Previously contained validation, database, reviewer, and evaluation logic inline. Now delegates to specialised classes.  
- **Validator**: Previously only validated input. Now also owns rejection logic.  
- **ReviewerManager**: Previously scattered reviewer logic. Now consolidated into one class.  
- **EvaluationManager**: Previously averaged scores without rules. Now centralises decision table logic.  
- **NotificationService**: Previously coupled with evaluation. Now decoupled, triggered solely by outcomes.  

## Test Cases
Execution evidence demonstrates functional equivalence with the baseline system:

| Test Case              | Input                        | Outcome                          |
|------------------------|------------------------------|----------------------------------|
| Invalid submission     | Missing title                | Rejected: Invalid format         |
| No reviewers           | force_no_reviewers flag      | Rejected: No reviewers available |
| Low scores             | [1,2,2]                      | Rejected                         |
| Moderate scores        | [3,3,4]                      | Revision                         |
| High scores            | [5,5,4]                      | Accepted                         |

## Mapping to Decision Table
- R1: High average with consensus → Accepted  
- R2: Moderate average with consensus → Revision  
- R3: Low average with consensus → Rejected  
- R4: No consensus → Revision  
- R5: No reviewers → Rejected  

## Traceability
Each lifeline in the optimised sequence diagram is mapped to a corresponding class in the `Optimised/src` folder.  
This ensures strict traceability between design artefacts, implementation, and test evidence.

## Conclusion
The optimised implementation:
- Aligns with the improved sequence diagram.  
- Encapsulates responsibilities in dedicated classes.  
- Produces outcomes consistent with the decision table rules (R1–R5).  
- Demonstrates functional equivalence with the original system.
```

