# vuln_app.py
import sqlite3
import subprocess
import os

# === Hard-coded credentials (bad) ===
DB_USER = "admin"
DB_PASSWORD = "SuperSecret123"   # Bandit will flag hard-coded credentials

def insecure_sql_lookup(username):
    """
    SQL injection: building SQL with string formatting is unsafe.
    Example of what NOT to do.
    """
    conn = sqlite3.connect("users.db")
    cur = conn.cursor()
    # vulnerable: user input interpolated directly into SQL
    query = "SELECT * FROM users WHERE username = '%s';" % username
    cur.execute(query)
    rows = cur.fetchall()
    conn.close()
    return rows

def insecure_shell_command(arg):
    """
    Command injection: passing user input to shell command directly.
    Example of what NOT to do.
    """
    # vulnerable: shell=True and string concatenation
    cmd = "ls " + arg
    subprocess.call(cmd, shell=True)

def main():
    # these are just example calls (don't actually run with untrusted input)
    insecure_sql_lookup("alice")
    insecure_shell_command("-la")
    print("Done")
