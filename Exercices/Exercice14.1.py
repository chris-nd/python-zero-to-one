def student(data):
    nom = data["nom"]
    age = data["age"]
    notes = data["notes"]

    return f"nom -> {nom}\nage -> {age}\nnotes -> {notes}"

print(student({"nom": "Alice", "age": 20, "notes": [15, 17, 14]}))

# 2ème approche plus robuste
# def student_dynamic(data):
#     lines = []
#     for cle, valeur in data.items():
#         lines.append(f"{cle} -> {valeur}")
#     return "\n".join(lines)

# print(student({"nom": "Alice", "age": 20, "notes": [15, 17, 14]}))