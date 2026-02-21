import random, os

# Generate a random integer between 1 and 100

random_number = random.randint(1, 100)
print(f"Random integer number between 1 and 100: {random_number}")

random_float = random.uniform(1, 100)
print(f"Random float number between 1 and 100: {random_float}")

randrange_number = random.randrange(1, 100, 5)
print(f"Random number between 1 and 100 with step 5: {randrange_number}")

chemin = "/Users/Chris/TrainingPython/Basics"
dossier = os.path.join(chemin, "TestModuleOS")
dossier1 = os.path.join(chemin, "TestModuleOS1")
dossier2 = os.path.join(chemin, "TestModuleOS2", "makedirs")

# Create the directory
os.mkdir(dossier)
print(f"Directory created at: {dossier}")

os.makedirs(dossier1, exist_ok=True)
print(f"Directories created at: {dossier1}")

# Create nested directories
if not os.path.exists(dossier2):
    os.makedirs(dossier2)
    print(f"Directories created at: {dossier2}")

# Remove the directory
os.rmdir(dossier)
print(f"Directory removed at: {dossier}")

os.removedirs(dossier1)
print(f"Directories removed at: {dossier1}")

# Remove nested directories
if os.path.exists(dossier2):
    os.removedirs(dossier2)
    print(f"Directories removed at: {dossier2}")
