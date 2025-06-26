def total_salary(path):
    try:
        with open(path, 'r', encoding='utf-8') as file:
            salaries = []

            for line in file:
                parts = line.strip().split(',')

                if len(parts) == 2:
                    name = parts[0].strip()
                    salary_str = parts[1].strip()

                    if salary_str.isdigit():
                        salaries.append(int(salary_str))

            if not salaries:
                return (0, 0)

            total = sum(salaries)
            average = total // len(salaries)
            return (total, average)

    except FileNotFoundError:
        print(f"Файл не знайдено : {path}")
        return (0, 0)
    except Exception as e:
        print(f"Сталася помилка: {e}")
        return (0, 0)


total, average = total_salary('salary_file.txt')
print(f"Загальна сума заробітної плати: {total}, Середня заробітна плата: {average}")


def get_cats_info(path):
    cats = []
    try:
        with open(path, 'r', encoding='utf-8') as file:
            for line in file:
                parts = line.strip().split(',')
                if len(parts) == 3:
                    cat_id = parts[0].strip()
                    name = parts[1].strip()
                    age = parts[2].strip()
                    cat = {
                        "id": cat_id,
                        "name": name,
                        "age": age
                    }
                    cats.append(cat)
    except FileNotFoundError:
        print(f"Файл не знайдено : {path}")
    except Exception as e:
        print(f"Сталася помилка: {e}")

    return cats


cats_info = get_cats_info('cats_file.txt')
for cat in cats_info:
    print(f"{cat['name']} ({cat['age']} років) — ID: {cat['id']}")

