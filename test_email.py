from chains.email_chain import generate_email


response = generate_email(
    recipient="Manager",
    purpose="Request leave",
    details="I need two days leave due to personal reasons.",
    tone="Professional"
)

print(response)