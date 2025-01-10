import json
from db import connection, cursor, initialize_connection

def add_ingredients_to_user(user_id, ingredient_names):
    """Add ingredients to a user's inventory."""
    # Ensure connection is active and cursor is initialized
    initialize_connection()  # Ensure this is called before interacting with the database

    # Check if the cursor is initialized
    if cursor is None:
        print("Error: Cursor is not initialized.")
        return

    # Convert list of ingredients to JSON format
    ingredient_names_json = json.dumps(ingredient_names)
    
    try:
        # Ensure the cursor is available and the procedure exists
        cursor.callproc('add_ingredients_to_user', (user_id, ingredient_names_json))
        connection.commit()
        print("Ingredients added to your inventory.")
    except Exception as e:
        print(f"Error while adding ingredients: {e}")


def get_user_ingredients(user_id):
    """Retrieve the ingredients a user has in their inventory."""
    # Ensure connection is active and cursor is initialized
    initialize_connection()

    # Check if the cursor is initialized
    if cursor is None:
        print("Error: Cursor is not initialized.")
        return

    query = """
        SELECT i.name
        FROM ingredients i
        JOIN user_ingredients ui ON i.ingredient_id = ui.ingredient_id
        WHERE ui.user_id = %s;
    """
    cursor.execute(query, (user_id,))
    ingredients = cursor.fetchall()
    if ingredients:
        print("Your ingredients:")
        for ingredient in ingredients:
            print(f"- {ingredient[0]}")
    else:
        print("No ingredients found.")

def view_recipe_catalog():
    """View all available recipes."""
    # Ensure connection is active and cursor is initialized
    initialize_connection()

    # Check if the cursor is initialized
    if cursor is None:
        print("Error: Cursor is not initialized.")
        return

    cursor.execute("SELECT recipe_id, name FROM recipes")
    recipes = cursor.fetchall()
    print("Recipe Catalog:")
    for recipe in recipes:
        print(f"- {recipe[1]} (ID: {recipe[0]})")

def get_recipes_user_can_make(user_id):
    """Get recipes the user can make based on their ingredients."""
    # Ensure connection is active and cursor is initialized
    initialize_connection()

    # Check if the cursor is initialized
    if cursor is None:
        print("Error: Cursor is not initialized.")
        return

    query = """
        SELECT 
            r.recipe_id,
            r.name AS recipe_name
        FROM recipes r
        WHERE check_if_user_can_make_recipe(%s, r.recipe_id) = 'Yes';
    """
    cursor.execute(query, (user_id,))
    recipes = cursor.fetchall()
    if recipes:
        print("Recipes you can make:")
        for recipe in recipes:
            print(f"- {recipe[1]} (ID: {recipe[0]})")
    else:
        print("No recipes found that match your ingredients.")
