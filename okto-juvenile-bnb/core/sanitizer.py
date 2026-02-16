import re

class LogSanitizer:
    """
    Silent Fortress: Removes sensitive data from logs before printing.
    """
    PATTERNS = [
        (r'(0x[a-fA-F0-9]{4})[a-fA-F0-9]{32,}(?=[a-fA-F0-9]{4})', r'\1...[REDACTED]'), # EVM Keys/Address (partial)
        (r'AIza[0-9A-Za-z-_]{35}', r'AIza...[REDACTED]'), # Google API Keys
        (r'(sk_live_|sk_test_)[0-9a-zA-Z]{24}', r'\1...[REDACTED]'), # Stripe/API Keys
        (r'Bearer [a-zA-Z0-9\-\._~\+\/]+=*', r'Bearer [REDACTED]'), # Bearer Tokens
    ]

    @staticmethod
    def clean(text):
        if not isinstance(text, str):
            return text
        
        for pattern, replacement in LogSanitizer.PATTERNS:
            text = re.sub(pattern, replacement, text)
        return text

# Teste rápido
if __name__ == "__main__":
    sensitive = "Key: 0x1234567890abcdef1234567890abcdef12345678 is leaked!"
    print(f"Original: {sensitive}")
    print(f"Sanitized: {LogSanitizer.clean(sensitive)}")