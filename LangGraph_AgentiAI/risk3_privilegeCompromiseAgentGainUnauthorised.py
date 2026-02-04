class FileAgent:
    def __init__(self, user_role):
        self.user_role = user_role  # e.g., "admin" or "guest"

    def delete_file(self, filename):
        if self.user_role == "admin":
            print(f"[ADMIN] Deleted {filename}")
        else:
            print(f"[GUEST] Permission denied to delete {filename}")

# Example of privilege compromise:
agent = FileAgent(user_role="admin")  # Agent inherits elevated privileges
agent.delete_file("important_data.txt")  # ⚠️ Risk: agent can delete critical files