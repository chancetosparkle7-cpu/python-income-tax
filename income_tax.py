income = 3500
tax = 0

if income >= 5000:
    tax = income * 0.5
    level = "고소득자"
elif income >= 3000:
    tax = income * 0.25
    level = "중산층"
else:
    tax = income * 0.1
    level = "저소득자"

print(f"소득: {income}원")
print(f"소득 수준: {level}")
print(f"세금: {tax}원")
print(f"GitHub 계정: {github_account}")
