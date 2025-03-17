import requests

def random_meal():
    url = "https://api.freeapi.app/api/v1/public/meals?page=1&limit=10&query=rice"
    response = requests.get(url)
    data = response.json()

    # Validation
    if data.get("success") and "data" in data:
        meal_data = data["data"].get("data", [])

        if len(meal_data) > 1: 
            meal =  meal_data[1].get("strMeal")
            meal_area = meal_data[1].get("strArea")
            meal_instruction = meal_data[1].get("strInstructions")
            return meal, meal_area, meal_instruction  
        else: 
            raise Exception("Not found meal data")   
        
    else:
        raise Exception("Failed to fetch data")



def main():
    try:
        meal, meal_area, meal_instruction = random_meal()
        print("*" * 180)
        print(f"Meal Name: {meal}\nFrom: {meal_area}\nInstructions: {meal_instruction}")
        print("*" * 180)

    except Exception as e:
        print(str(e))

if __name__ == "__main__":
    main()