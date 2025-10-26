import re
from datetime import datetime

class InternalAuditor:
    def __init__(self):
        self.audit_log = []

    def scan_submission(self, policy_data):
        errors = []
        # 1. Data Integrity (no blanks/errors)
        if not policy_data.get('customer_id'):
            errors.append("Missing customer ID")
        # 2. Compliance Check (regex for formats)
        if not re.match(r'^[A-Z]{2}\d{6}$', policy_data.get('policy_number', '')):
            errors.append("Invalid policy number format")
        # 3. Fraud Detection (simple ML sim — flag anomalies)
        if policy_data.get('premium') < 0 or policy_data.get('risk_score') > 1.0:
            errors.append("Anomaly detected — human review")
        # 4. Tax/Regulatory Flags
        if policy_data.get('country') == 'ZA' and not policy_data.get('sars_id'):
            errors.append("SARS ID required for SA")
        
        timestamp = datetime.now().isoformat()
        audit_entry = {"timestamp": timestamp, "errors": errors, "approved": len(errors) == 0}
        self.audit_log.append(audit_entry)
        
        if errors:
            print(f"Audit Failed: {len(errors)} errors. Human veto needed.")
            return False
        print("Audit Passed — Policy Approved.")
        return True

# Demo
auditor = InternalAuditor()
policy = {"customer_id": "J123", "policy_number": "FI001234", "premium": 500, "risk_score": 0.3, "country": "ZA", "sars_id": "123456"}
auditor.scan_submission(policy)
