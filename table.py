import mysql.connector

# Connect to the MySQL database
connection = mysql.connector.connect(
    host='127.0.0.1',        # Replace with your MySQL host (e.g., '127.0.0.1' or server address)
    user='root',             # Replace with your MySQL username
    password='Salle123!',    # Replace with your MySQL password
    database='recipes'       # Replace with your database name (this will be created if not present)
)

if connection.is_connected():
    print("Connected to MySQL database")

# Create a cursor object to execute SQL queries
cursor = connection.cursor()

# Create the Recipes database (if it doesn't already exist)
cursor.execute("CREATE DATABASE IF NOT EXISTS Recipes;")
cursor.execute("USE Recipes;")

# Create Users table
cursor.execute("""
    CREATE TABLE IF NOT EXISTS Users (
        user_id INT AUTO_INCREMENT PRIMARY KEY,
        name VARCHAR(50) NOT NULL,
        ingredients TEXT
    );
""")

# Create Ingredients table (this was missing in your script)
cursor.execute("""
    CREATE TABLE IF NOT EXISTS Ingredients (
        ingredient_id INT AUTO_INCREMENT PRIMARY KEY,
        name VARCHAR(255) NOT NULL
    );
""")

# Create Recipes table
cursor.execute("""
    CREATE TABLE IF NOT EXISTS Recipes (
        recipe_id INT PRIMARY KEY,
        name VARCHAR(200) NOT NULL,
        ingredients TEXT,
        tags TEXT
    );
""")

# Create Users table (you had a duplicate with a lowercase "users" in your script)
cursor.execute("""
    CREATE TABLE IF NOT EXISTS users (
        user_id INT PRIMARY KEY,
        username VARCHAR(255) -- Optional if needed
    );
""")

# Create user_ingredients table (assumes ingredients table exists)
cursor.execute("""
    CREATE TABLE IF NOT EXISTS user_ingredients (
        user_id INT,
        ingredient_id INT,
        PRIMARY KEY (user_id, ingredient_id),
        FOREIGN KEY (user_id) REFERENCES users(user_id),
        FOREIGN KEY (ingredient_id) REFERENCES Ingredients(ingredient_id)
    );
""")
cursor.executemany("""
INSERT INTO Recipes (recipe_id, name, ingredients, tags) VALUES
(1, 'Grilled Garlic Cheese Grits', '["water", "grits", "salt", "cheddar cheese", "garlic", "olive oil"]', NULL),
(2, 'Simple Shrimp and Andouille Jambalaya', '["onion", "red bell pepper", "garlic cloves", "large shrimp", "salt", "hot pepper sauce", "vegetable oil", "andouille sausage", "long grain rice", "bay leaves", "diced tomatoes", "clam juice", "fresh parsley"]', NULL),
(3, 'black-and-white bean salad', '["1 cup canned white beans, rinsed and drained", "1 cup canned black beans, rinsed and drained", "1 large tomatoes, diced", "1 small onion, diced", "1 stalk celery, diced", "1 tablespoon white wine vinegar", "2 tablespoons Italian parsley, minced", "1/8 teaspoon table salt, to taste", "1/8 teaspoon black pepper, to taste", "1-2 teaspoon olive oil, to taste"]', NULL),
(4, 'Crock Pot Italian Zucchini', '["zucchini", "yellow squash", "diced tomatoes", "onion", "garlic", "green bell pepper", "italian seasoning", "water", "salt and pepper"]', '["weeknight", "time-to-make", "course", "main-ingredient", "preparation", "occasion", "side-dishes", "vegetables", "easy", "beginner-cook", "fall", "vegetarian", "winter", "crock-pot-slow-cooker", "dietary", "seasonal", "squash", "equipment", "3-steps-or-less"]'),
(5, 'Beef Stew With Dried Cherries', '["beef stew meat", "flour", "salt", "allspice", "cinnamon", "black pepper", "vegetable oil", "onions", "dried sour cherries", "sugar", "water", "dry red wine", "beef stock", "mushroom"]', '["time-to-make", "course", "main-ingredient", "preparation", "main-dish", "beef", "easy", "meat", "4-hours-or-less"]'),
(6, 'Hot Sweet Almond Brittle', '["slivered almonds", "cider vinegar", "sugar", "sugar", "salt", "ground cumin", "ground coriander", "cayenne pepper"]', '["time-to-make", "course", "preparation", "desserts", "candy", "dietary", "low-cholesterol", "low-in-something", "4-hours-or-less"]'),
(7, 'Asparagus Omelette Wraps', '["eggs", "milk", "fresh sage", "fresh thyme", "garlic cloves", "pecorino cheese", "asparagus", "extra virgin olive oil"]', NULL),
(8, 'Potato-Crab Chowder', '["butter", "onion", "garlic", "potatoes", "flour", "milk", "black pepper", "nutmeg", "creamed corn", "low sodium chicken broth", "lump crabmeat", "cayenne pepper", "parsley"]', NULL),
(9, 'Sweet and Simple Sloppy Joes', '["lean ground beef", "ketchup", "heinz chili sauce", "white vinegar", "sugar", "prepared yellow mustard", "onion powder"]', '["30-minutes-or-less", "time-to-make", "course", "main-ingredient", "preparation", "lunch", "beef", "easy", "beginner-cook", "dietary", "high-protein", "low-carb", "inexpensive", "ground-beef", "high-in-something", "low-in-something", "meat"]'),
(10, 'Golden Chocolate Chip Muffins', '["butter", "granulated sugar", "baking powder", "salt", "vanilla extract", "eggs", "milk", "whole wheat flour", "chocolate chips", "decorator sugar"]', NULL),
(11, 'Potato Chip Chocolate Chip Cookies', '["all-purpose flour", "baking soda", "nutmeg", "margarine", "sugar", "dark brown sugar", "egg", "egg white", "vanilla", "potato chips", "semi-sweet chocolate chips"]', NULL),
(12, 'Steak Au Poivre', '["unsalted beef stock", "onion", "carrot", "bay leaf", "thyme", "whole black peppercorn", "black peppercorns", "green peppercorn", "new york strip steaks", "vegetable oil", "unsalted butter", "shallots", "cognac", "dry white wine", "parsley"]', NULL),
(13, 'Mushroom Ravioli', '["button mushrooms", "portabella mushrooms", "olive oil", "butter", "shallots", "garlic cloves", "salt", "wonton wrappers", "cornstarch", "1% low-fat milk", "all-purpose flour", "fresh parmesan cheese", "fresh chives", "salt", "fresh ground black pepper"]', NULL),
(14, 'Santa Fe-Tastic Chicken Tortilla Soup', '["vegetable oil", "vegetable oil", "corn on the cob", "red bell pepper", "chicken breast tenders", "poultry seasoning", "cumin", "salt and pepper", "zucchini", "yellow onion", "garlic cloves", "chipotle chile in adobo", "stewed tomatoes", "tomato sauce", "chicken stock", "blue corn tortilla chips", "cheddar cheese", "sour cream", "red onion", "cilantro", "avocado", "lemon, juice of"]', '["60-minutes-or-less", "time-to-make", "course", "main-ingredient", "cuisine", "preparation", "north-american", "soups-stews", "poultry", "american", "southwestern-united-states", "tex-mex", "chicken", "meat", "chicken-breasts"]'),
(15, 'Mashed Plantains With Leeks and Fresh Herbs', '["water", "low sodium chicken broth", "plantains", "unsalted butter", "extra virgin olive oil", "leek", "fresh thyme", "fresh italian parsley", "sour cream", "ground cumin", "pecans", "butter"]', NULL),
(16, 'Mexican Macaroni and Beef', '["elbow macaroni", "ground beef", "onion", "chili without beans", "cottage cheese", "corn chips", "salt", "chili powder", "buttered bread crumb"]', NULL),
(17, 'Pantry Clearing Chili Bean Soup', '["onion", "green pepper", "carrots", "celery rib", "frozen corn", "black beans", "pink beans", "crushed pineapple in juice", "french lentils", "diced tomatoes with juice", "tomato soup", "water", "chili powder", "garlic powder", "cumin", "cayenne pepper", "liquid smoke"]', '["course", "main-ingredient", "preparation", "occasion", "main-dish", "soups-stews", "beans", "vegetables", "easy", "vegan", "vegetarian", "chili", "crock-pot-slow-cooker", "dietary", "comfort-food", "lentils", "black-beans", "taste-mood", "equipment", "3-steps-or-less"]'),
(18, 'Silky Chocolate Kefir Tarts', '["bittersweet chocolate chips", "sugar", "flour", "kosher salt", "eggs", "kefir", "vanilla", "pie crusts"]', '["60-minutes-or-less", "time-to-make", "course", "preparation", "occasion", "pies-and-tarts", "tarts", "desserts", "dinner-party", "holiday-event", "pies"]'),
(19, 'Mushroom Lasagna: Gluten Free and Pasta Free!', '["fresh mushrooms", "margarine", "olive oil", "eggs", "garlic salt", "italian seasoning", "parsley flakes", "ricotta cheese", "part-skim mozzarella cheese", "italian cheese blend", "pasta sauce"]', '["time-to-make", "course", "preparation", "main-dish", "vegetarian", "dietary", "gluten-free", "egg-free", "free-of-something", "4-hours-or-less"]'),
(20, 'Creme Brulee', '["3 cups heavy cream", "1 piece vanilla bean, pierced", "1/4 cup sugar", "3 eggs", "3 egg yolks", "1/2 cup dark brown sugar", "fresh raspberry", "1 vanilla bean", "4 1/2 ounces baking chocolate", "4 1/2 ounces pralines", "1 cup pecans, finely chopped or 1 cup brazil nut", "3 ounces coffee beans, finely ground (Espresso, French Roast, etc.)", "2 bananas", "1 tablespoon butter", "2 tablespoons brandy", "2 teaspoons brown sugar"]', NULL),
(21, 'Chocolate Biscuits', '["self rising flour", "butter", "superfine sugar", "chocolate chips", "milk"]', '["30-minutes-or-less", "time-to-make", "course", "cuisine", "preparation", "north-american", "5-ingredients-or-less", "desserts", "easy", "cookies-and-brownies", "dietary", "high-calcium", "high-in-something"]'),
(22, 'Ridiculously Easy Chicago-Style Pizza Pie', '["frozen pie crusts", "italian sausage", "onion", "mushrooms", "mozzarella cheese", "parmesan cheese", "pizza sauce", "italian seasoning", "parmesan cheese"]', NULL),
(23, 'Makrout a Louz - Algerian Almond Cakes #2', NULL, NULL);
""")
cursor.executemany("""
INSERT IGNORE INTO Ingredients (name) VALUES
('water'),
('grits'),
('salt'),
('cheddar cheese'),
('garlic'),
('olive oil'),
('onion'),
('red bell pepper'),
('garlic cloves'),
('large shrimp'),
('hot pepper sauce'),
('vegetable oil'),
('andouille sausage'),
('long grain rice'),
('bay leaves'),
('diced tomatoes'),
('clam juice'),
('fresh parsley'),
('canned white beans'),
('canned black beans'),
('tomatoes'),
('small onion'),
('celery'),
('white wine vinegar'),
('Italian parsley'),
('table salt'),
('black pepper'),
('zucchini'),
('yellow squash'),
('green bell pepper'),
('italian seasoning'),
('flour'),
('allspice'),
('cinnamon'),
('onions'),
('dried sour cherries'),
('sugar'),
('dry red wine'),
('beef stock'),
('mushroom'),
('slivered almonds'),
('cider vinegar'),
('ground cumin'),
('ground coriander'),
('cayenne pepper'),
('eggs'),
('milk'),
('fresh sage'),
('fresh thyme'),
('pecorino cheese'),
('asparagus'),
('butter'),
('potatoes'),
('nutmeg'),
('creamed corn'),
('low sodium chicken broth'),
('lump crabmeat'),
('parsley'),
('lean ground beef'),
('ketchup'),
('heinz chili sauce'),
('white vinegar'),
('prepared yellow mustard'),
('onion powder'),
('granulated sugar'),
('baking powder'),
('vanilla extract'),
('whole wheat flour'),
('chocolate chips'),
('decorator sugar'),
('all-purpose flour'),
('baking soda'),
('margarine'),
('dark brown sugar'),
('egg white'),
('vanilla'),
('potato chips'),
('semi-sweet chocolate chips'),
('unsalted beef stock'),
('carrot'),
('bay leaf'),
('whole black peppercorn'),
('green peppercorn'),
('new york strip steaks'),
('unsalted butter'),
('shallots'),
('cognac'),
('dry white wine'),
('button mushrooms'),
('portabella mushrooms'),
('wonton wrappers'),
('cornstarch'),
('1% low-fat milk'),
('fresh parmesan cheese'),
('fresh chives'),
('chipotle chile in adobo'),
('stewed tomatoes'),
('tomato sauce'),
('chicken stock'),
('blue corn tortilla chips'),
('sour cream'),
('red onion'),
('cilantro'),
('avocado'),
('lemon'),
('plantains'),
('leek'),
('fresh italian parsley'),
('pecans'),
('elbow macaroni'),
('chili without beans'),
('cottage cheese'),
('corn chips'),
('chili powder'),
('buttered bread crumb'),
('pink beans'),
('crushed pineapple in juice'),
('french lentils'),
('diced tomatoes with juice'),
('tomato soup'),
('garlic powder'),
('liquid smoke'),
('bittersweet chocolate chips'),
('kosher salt'),
('kefir'),
('pie crusts'),
('self rising flour'),
('superfine sugar'),
('frozen pie crusts'),
('italian sausage'),
('mozzarella cheese'),
('parmesan cheese'),
('pizza sauce'),
('pralines'),
('coffee beans'),
('brazil nut'),
('bananas'),
('brandy'),
('brown sugar'),
('vanilla bean'),
('baking chocolate'),
('raspberry');
""")
cursor.executemany("""
INSERT INTO users (user_id) VALUES 
(1), 
(2), 
(3), 
(4);""")
cursor.executemany("""
INSERT INTO user_ingredients (user_id, ingredient_id)
SELECT 1, ingredient_id FROM ingredients WHERE name IN (
'water', 'salt', 'cheddar cheese', 'garlic', 'olive oil', 'onion', 'red bell pepper', 
'garlic cloves', 'large shrimp', 'hot pepper sauce', 'vegetable oil', 'andouille sausage', 
'long grain rice', 'bay leaves', 'diced tomatoes', 'clam juice', 'fresh parsley', 
'canned white beans', 'canned black beans', 'tomatoes', 'small onion', 'celery', 
'white wine vinegar', 'Italian parsley', 'table salt', 'black pepper', 'zucchini', 
'green bell pepper', 'italian seasoning', 'flour', 'allspice', 'cinnamon', 'onions', 
'sugar', 'dry red wine', 'beef stock', 'mushroom', 'slivered almonds', 
'cider vinegar', 'ground cumin', 'ground coriander', 'cayenne pepper', 
'eggs', 'milk', 'fresh thyme', 'pecorino cheese', 'asparagus', 'butter', 
'potatoes', 'nutmeg', 'low sodium chicken broth', 'parsley', 'lean ground beef', 
'ketchup', 'heinz chili sauce', 'prepared yellow mustard', 'onion powder', 
'granulated sugar', 'baking powder', 'vanilla extract', 'whole wheat flour', 
'chocolate chips', 'decorator sugar', 'baking soda', 'margarine', 
'egg white', 'potato chips', 'semi-sweet chocolate chips', 'unsalted beef stock', 
'carrot', 'bay leaf', 'whole black peppercorn', 'new york strip steaks', 
'unsalted butter', 'shallots', 'dry white wine', 'button mushrooms', 
'cornstarch', '1% low-fat milk', 'fresh parmesan cheese', 'fresh chives', 
'stewed tomatoes', 'tomato sauce', 'blue corn tortilla chips', 
'red onion', 'avocado', 'lemon', 'plantains', 'fresh italian parsley', 
'pink beans', 'frozen pie crusts', 'parmesan cheese', 'pralines', 
'coffee beans', 'brandy', 'brown sugausersr', 'vanilla bean', 'baking chocolate'
);""")
cursor.executemany("""
INSERT INTO user_ingredients (user_id, ingredient_id)
SELECT 2, ingredient_id FROM ingredients WHERE name IN (
'water', 'salt', 'cheddar cheese', 'garlic', 'olive oil', 'onion', 'red bell pepper', 
'garlic cloves', 'large shrimp', 'hot pepper sauce', 'vegetable oil', 'andouille sausage', 
'long grain rice', 'bay leaves', 'diced tomatoes', 'clam juice', 'fresh parsley', 
'canned white beans', 'canned black beans', 'tomatoes', 'small onion', 'celery', 
'white wine vinegar', 'Italian parsley', 'table salt', 'black pepper', 'zucchini', 
'green bell pepper', 'italian seasoning', 'flour', 'allspice', 'cinnamon', 'onions', 
'sugar', 'dry red wine', 'beef stock', 'mushroom', 'slivered almonds', 
'cider vinegar', 'ground cumin', 'ground coriander', 'cayenne pepper', 
'eggs', 'milk', 'fresh thyme', 'pecorino cheese', 'asparagus', 'butter', 
'potatoes', 'nutmeg', 'low sodium chicken broth', 'parsley', 'lean ground beef', 
'ketchup', 'heinz chili sauce', 'prepared yellow mustard', 'onion powder', 
'granulated sugar', 'baking powder', 'vanilla extract', 'whole wheat flour', 
'chocolate chips', 'decorator sugar', 'baking soda', 'margarine', 
'egg white', 'potato chips', 'semi-sweet chocolate chips', 'unsalted beef stock', 
'carrot', 'bay leaf', 'whole black peppercorn', 'new york strip steaks', 
'unsalted butter', 'shallots', 'dry white wine', 'button mushrooms', 
'cornstarch', '1% low-fat milk', 'fresh parmesan cheese', 'fresh chives', 
'stewed tomatoes', 'tomato sauce', 'blue corn tortilla chips', 
'red onion', 'avocado', 'lemon', 'plantains', 'fresh italian parsley', 
'pink beans', 'frozen pie crusts', 'parmesan cheese', 'pralines', 
'coffee beans', 'brandy', 'brown sugausersr', 'vanilla bean', 'baking chocolate'

);""")
cursor.executemany("""
INSERT INTO user_ingredients (user_id, ingredient_id)
SELECT 3, ingredient_id FROM ingredients WHERE name IN (
'water', 'salt', 'garlic', 'olive oil', 'red bell pepper', 'garlic cloves', 
'large shrimp', 'hot pepper sauce', 'vegetable oil', 'andouille sausage', 
'long grain rice', 'bay leaves', 'clam juice', 'fresh parsley', 
'canned white beans', 'canned black beans', 'small onion', 'celery', 
'white wine vinegar', 'Italian parsley', 'table salt', 'black pepper', 
'yellow squash', 'italian seasoning', 'flour', 'allspice', 'cinnamon', 
'onions', 'dried sour cherries', 'sugar', 'dry red wine', 'beef stock', 
'mushroom', 'slivered almonds', 'cider vinegar', 'ground cumin', 
'eggs', 'fresh sage', 'fresh thyme', 'pecorino cheese', 'butter', 
'potatoes', 'nutmeg', 'parsley', 'lean ground beef', 
'heinz chili sauce', 'white vinegar', 'onion powder', 
'granulated sugar', 'baking powder', 'chocolate chips', 
'all-purpose flour', 'baking soda', 'dark brown sugar', 
'egg white', 'vanilla', 'semi-sweet chocolate chips', 
'unsalted beef stock', 'carrot', 'bay leaf', 
'whole black peppercorn', 'new york strip steaks', 
'dry white wine', 'portabella mushrooms', 
'cornstarch', 'fresh parmesan cheese', 'chipotle chile in adobo', 
'tomato sauce', 'chicken stock', 'blue corn tortilla chips', 
'red onion', 'cilantro', 'avocado', 'lemon', 
'fresh italian parsley', 'pink beans', 'corn chips', 
'chili powder', 'french lentils', 'bittersweet chocolate chips', 
'kosher salt', 'mozzarella cheese', 'pecans', 
'brandy', 'brown sugar', 'vanilla bean', 'raspberry'

);""")
cursor.executemany("""
INSERT INTO user_ingredients (user_id, ingredient_id)
SELECT 4, ingredient_id FROM ingredients WHERE name IN (
'water', 'grits', 'salt', 'garlic', 'olive oil', 'onion', 
'red bell pepper', 'garlic cloves', 'large shrimp', 
'vegetable oil', 'andouille sausage', 'long grain rice', 
'clam juice', 'canned white beans', 'canned black beans', 
'celery', 'white wine vinegar', 'Italian parsley', 'table salt', 
'black pepper', 'zucchini', 'green bell pepper', 
'italian seasoning', 'cinnamon', 'onions', 'dried sour cherries', 
'sugar', 'dry red wine', 'beef stock', 'slivered almonds', 
'cider vinegar', 'ground coriander', 'cayenne pepper', 
'milk', 'fresh sage', 'pecorino cheese', 'asparagus', 
'nutmeg', 'creamed corn', 'parsley', 'ketchup', 
'prepared yellow mustard', 'onion powder', 'granulated sugar', 
'decorator sugar', 'baking soda', 'margarine', 
'potato chips', 'unsalted beef stock', 'bay leaf', 
'whole black peppercorn', 'green peppercorn', 
'button mushrooms', '1% low-fat milk', 'fresh parmesan cheese', 
'chipotle chile in adobo', 'stewed tomatoes', 
'chicken stock', 'sour cream', 'lemon', 
'fresh italian parsley', 'pralines', 'coffee beans', 
'brazil nut', 'brown sugar', 'vanilla bean', 
'baking chocolate', 'avocado'
);
""")



# Commit the changes
connection.commit()

# Close the cursor and connection
cursor.close()
connection.close()

print("Database and tables created successfully!")
