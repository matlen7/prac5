
HEXIDECIMAL_NAMES = {"BLACK": "#000000","BROWN": "#a52a2a", "BURLYWOOD": "#deb887", "CADETBLUE": "#5f9ea0", "CHOCOLATE":
                     "#d2691e", "CORAL": "#ff7f50", "CORNFLOWERBLUE": "#6495ed", "DARKGOLDENROD": "#b8860b", "DARKGREEN":
                     "#006400", "DARKORCHID": "#9932cc"}

colour = input("Enter a colour name: ")
while colour.upper() != "QUIT":
    if colour.upper() in HEXIDECIMAL_NAMES:
        print(colour.upper(), "has the code", HEXIDECIMAL_NAMES[colour.upper()])
    else:
        print("Invalid input")
    colour = input("Enter a colour name: ")