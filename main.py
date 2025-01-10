from db import initialize_connection, close_connection
from query import add_ingredients_to_user, get_user_ingredients, view_recipe_catalog, get_recipes_user_can_make

def main():
    user_id = int(input("Enter your user ID: "))
    
    while True:
        print("\n1. Add an ingredient to my inventory")
        print("2. Get recipes I can make")
        print("3. View recipe catalog")
        print("4. View my ingredients")
        print("5. Exit")
        choice = input("Choose an option: ")

        if choice == '1':
            # Taking input for one or more ingredients
            ingredient_names = input("Enter comma-separated ingredient names: ").split(',')
            ingredient_names = [name.strip() for name in ingredient_names if name.strip()]  # Ensure no empty strings
            add_ingredients_to_user(user_id, ingredient_names)
        elif choice == '2':
            get_recipes_user_can_make(user_id)
        elif choice == '3':
            view_recipe_catalog()
        elif choice == '4':
            get_user_ingredients(user_id)
        elif choice == '5':
            break
        else:
            print("Invalid choice. Please try again.")

    close_connection()  # Close the database connection at the end

if __name__ == "__main__":
    main()
