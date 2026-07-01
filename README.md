# Autonomous Self-Healing Infrastructure & Security Patching Engine

An AI-powered incident response workflow that automatically detects application failures, performs AI-driven root cause analysis, generates remediation suggestions, validates security, and routes incidents for human approval before deployment.

---

## Features

- Automated production incident detection
- AI-powered root cause analysis
- Severity classification (Low, Medium, High, Critical)
- AI-generated code repair suggestions
- Security validation using guardrails
- Human-in-the-loop approval workflow
- Automated email notifications
- Incident logging and reporting

---

## Tech Stack

- Python
- FastAPI
- n8n
- Groq LLM
- Gmail Integration
- JavaScript (n8n Code Nodes)
- REST APIs
- Webhooks

---

## Workflow

```
FastAPI Crash
      │
      ▼
Webhook Trigger
      │
      ▼
AI Investigation Agent
      │
      ▼
Severity Classification
      │
      ▼
High / Critical?
      │
      ├── No → End Workflow
      │
      └── Yes
             │
             ▼
      AI Code Repair Agent
             │
             ▼
      Security Guardrail
             │
             ▼
      Human Approval Email
```

---

## Incident Scenarios Tested

### High Severity Incident

Simulated a production application crash using:

```
ZeroDivisionError (division by zero)
```

Workflow executed:

- FastAPI generated the incident
- Error logged
- Webhook triggered
- AI Investigation Agent analyzed the root cause
- Severity classified as **High**
- AI generated a repair suggestion
- Security guardrail validated the response
- Professional approval email sent to the engineer

---

### Low Severity Incident

Simulated an input validation error:

```
Invalid age supplied
```

Workflow executed:

- Validation error generated
- AI Investigation Agent analyzed the issue
- Severity classified as **Low**
- Workflow stopped after severity classification
- No repair generation
- No approval email sent

This demonstrates intelligent workflow routing based on incident severity.

---

## Project Highlights

- Built an autonomous AI incident response workflow using n8n.
- Implemented multi-agent architecture for investigation and remediation.
- Added security guardrails before human review.
- Demonstrated conditional workflow execution based on AI severity classification.
- Integrated FastAPI with n8n using Webhooks for real-time incident processing.
- Automated professional incident reporting through Gmail.

---

## Future Improvements

- GitHub Pull Request generation
- Automatic deployment after approval
- Docker sandbox for code execution
- Vector database for historical incident retrieval
- Slack / Microsoft Teams notifications
- Kubernetes deployment automation
- Jira incident creation
