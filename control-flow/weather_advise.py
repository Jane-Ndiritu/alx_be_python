weather = input( "What's the weather like today? (sunny/rainy/cold):")
if weather == "sunny":
    print("sunny")
    print("Wear a t-shirt and sunglasses.")
elif weather == "rainy":
    print("rainy")
    print("Don't forget your umbrella and a raincoat")
elif weather == "cold":
    print("cold")
    print("Make sure to wear a warm coat and a scarf.")
else:
    print(f" Sorry, I don't have recommendations for this weather")