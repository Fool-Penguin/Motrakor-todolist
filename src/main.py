"""Main entry point for the To-Do List CLI application.

This module implements the CLI interface with a REPL-style interaction.
"""

import json
import os
from models import TodoItem, Priority, Status

def display_pre_login_menu():
    """Display the pre-login menu options."""
    print("\n" + "=" * 40)
    print("  Welcome to To-Do List Manager")
    print("=" * 40)
    print("\n[1] Login")
    print("[2] Sign Up")
    print("[3] Exit")
    print()


def get_user_choice():
    """Get and validate user's menu choice.

    Returns:
        The user's choice as a string.
    """
    choice = input("Please select an option (1-3): ").strip()
    return choice

# ================= Load & Save users from/to JSON =============== 
def load_users(filename="login.json"):
    """Load users from JSON file."""
    if os.path.exists(filename):
        with open(filename, 'r') as f:
            return json.load(f)
    return []

def save_users(users, filename="login.json"):
    """Save users to JSON file."""
    with open(filename, 'w') as f:
        json.dump(users, f, indent=4)

# ================= Load & Save todos from/to JSON ===============
def load_todos(filename="todos.json"):
    """Load todos from JSON file."""
    if os.path.exists(filename):
        with open(filename, 'r') as f:
            todos_data = json.load(f)
            return [TodoItem.from_dict(todo) for todo in todos_data]
    return []

def save_todos(todos, filename="todos.json"):
    """Save todos to JSON file."""
    todos_data = [todo.to_dict() for todo in todos]
    with open(filename, 'w') as f:
        json.dump(todos_data, f, indent=4)

# =================== User Login here =================== 
def handle_login(users):
    """Handle the login process.
    
    Args:
        users: List of user dictionaries
        
    Returns:
        Username if login successful, None otherwise
    """
    print("\n--- Login ---")
    username = input("Username: ").strip()
    password = input("Password: ").strip()
    # TODO: Implement login logic
    for user in users:
        if user.get("username") == username and str(user.get("password")) == password:
            print(f"Login successful! Welcome back, {username}!")
            return username
    print("Invalid username or password.")
    return None

# =================== User Signup here ===================
def handle_signup():
    """Handle the signup process.
    
    Returns:
        Username if signup successful, None otherwise
    """
    print("\n--- Sign Up ---")
    username = input("Username: ").strip()
    password = input("Password: ").strip()
    
    users = load_users()
    # TODO: Implement login logic
    # Check if username already exists
    for user in users:
        if user.get("username") == username:
            print("Username already exists. Please choose another.")
            return None

    users.append({"username": username, "password": password})
    save_users(users)
    print(f"Account created successfully! Welcome, {username}!")
    return username

# =================== Create Todo Item =================== 
def handle_create_todo(username):
    """Handle creating a new todo item.
    
    Args:
        username: The username of the person creating the todo
    """
    print("\n--- Create New Todo ---")
    
    title = input("Title: ").strip()
    if not title:
        print("Title cannot be empty.")
        return
    
    details = input("Details: ").strip()
    
    print("\nPriority levels: HIGH, MID, LOW")
    priority_input = input("Priority (default: MID): ").strip().upper()
    if not priority_input:
        priority = Priority.MID
    else:
        try:
            priority = Priority[priority_input]
        except KeyError:
            print(f"Invalid priority. Using default (MID).")
            priority = Priority.MID
    
    # Create the todo item
    todo = TodoItem(
        title=title,
        details=details,
        priority=priority,
        owner=username
    )
    
    # Load existing todos and add the new one
    todos = load_todos()
    todos.append(todo)
    save_todos(todos)
    
    print(f"Todo created successfully! ID: {todo.id}")

def display_post_login_menu():
    """Display the post-login menu options."""
    print("\n" + "=" * 40)
    print("  Todo List Manager")
    print("=" * 40)
    print("\n[1] Create Todo")
    print("[2] View All Todos")
    print("[3] View Todo Details")
    print("[4] Mark Todo as Completed")
    print("[5] Logout")
    print()

def handle_post_login(username):
    """Handle the post-login menu and operations.
    
    Args:
        username: The logged-in username
    """
    while True:
        display_post_login_menu()
        choice = input("Please select an option (1-5): ").strip()
        
        if choice == "1":
            handle_create_todo(username)
        elif choice == "2":
            # Placeholder for viewing all todos
            print("\n--- All Todos ---")
            todos = load_todos()
            user_todos = [t for t in todos if t.owner == username]
            if not user_todos:
                print("You have no todos yet.")
            else:
                for todo in user_todos:
                    status_symbol = "✓" if todo.status == Status.COMPLETED else "○"
                    print(f"{status_symbol} [{todo.priority.value}] {todo.title}")
        elif choice == "3":
            # Placeholder for viewing todo details
            print("\n--- Todo Details ---")
            print("Feature coming soon...")
        elif choice == "4":
            # Placeholder for marking as completed
            print("\n--- Mark Todo as Completed ---")
            print("Feature coming soon...")
        elif choice == "5":
            print("Logged out successfully!")
            break
        else:
            print("\nInvalid option. Please select 1-5.")

def main():
    """Main application loop.

    Implements a REPL (Read-Eval-Print Loop) for the CLI application.
    """
    
    print("Starting To-Do List Application...")

    while True:
        display_pre_login_menu()
        choice = get_user_choice()

        if choice == "1":
            users = load_users()
            username = handle_login(users)
            if username:
                handle_post_login(username)
        elif choice == "2":
            username = handle_signup()
            if username:
                handle_post_login(username)
        elif choice == "3":
            print("\nThank you for using To-Do List Manager. Goodbye!")
            break
        else:
            print("\nInvalid option. Please select 1, 2, or 3.")


if __name__ == "__main__":
    main()
