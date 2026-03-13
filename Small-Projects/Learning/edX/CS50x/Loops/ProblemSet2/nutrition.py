item = input("Item: ")

fruits_cal = {
    "apple" : {
        "calories" : 130
    },
    "avocado" : {
        "calories" : 50
    },
    "banana" : {
        "calories" : 110
    },
    "cantaloupe" : {
        "calories" : 50
    },
    "grapefruit" : {
        "calories" : 60
    },
    "grapes" : {
        "calories" : 90
    },
    "honeydew melon" : {
        "calories" : 50
    },
    "kiwifruit" : {
        "calories" : 90
    },
    "lemon" : {
        "calories" : 15
    },
    "nectarine" : {
        "calories" : 60
    },
    "orange" : {
        "calories" : 80
    },
    "peach" : {
        "calories" : 60
    },
    "pear" : {
        "calories" : 100
    },
    "pineapple" : {
        "calories" : 50
    },
    "plums" : {
        "calories" : 70
    },
    "lemon" : {
        "calories" : 15
    },
    "sweet cherries" : {
        "calories" : 100
    },
    "tangerine" : {
        "calories" : 50
    },
    "watermelon" : {
        "calories" : 80
    },
}

if item.lower() in fruits_cal:
    if fruits_cal[item.lower()]:
        print(f'Calories: {fruits_cal[item.lower()]["calories"]}')