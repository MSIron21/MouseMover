from pyHM import mouse

def main():
    
    print("ready")
    x1 = x2 = x4 = x8 = x16 = x32 = x64 = x128 = 0
    y1 = y2 = y4 = y8 = y16 = y32 = y64 = y128 = 0

    
    while(True):
        user_input = input("valid: 128, 64, 32, 16, 8, 4, 2, 1, move, X: ")
        
        match user_input:
            case "128":
                x128, y128 = mouse.get_current_position()
                print(f"pozycja 128: {x128}, {y128}")
            case "64":
                x64, y64 = mouse.get_current_position()
                print(f"pozycja 64: {x64}, {y64}")
            case "32":
                x32, y32 = mouse.get_current_position()
                print(f"pozycja 32: {x32}, {y32}")
            case "16":
                x16, y16 = mouse.get_current_position()
                print(f"pozycja 16: {x16}, {y16}")
            case "8":
                x8, y8 = mouse.get_current_position()
                print(f"pozycja 8: {x8}, {y8}")
            case "4":
                x4, y4 = mouse.get_current_position()
                print(f"pozycja 4: {x4}, {y4}")
            case "4":
                x2, y2 = mouse.get_current_position()
                print(f"pozycja 2: {x2}, {y2}")
            case "1":
                x1, y1 = mouse.get_current_position()
                print(f"pozycja 1: {x1}, {y1}")
            case "move":
                while(True):
                    user_number = input("valid: Int, X: ")
                    if user_number == "X":
                        break
                    else:
                        liczba = list(bin(int(user_number))[2:][::-1])
                        needed = 8
                        dodac = needed - len(liczba)
                        if dodac > 0:
                            liczba.extend(['0'] * dodac)
                        if liczba[0] == "1":
                            mouse.click(x=x1, y=y1)
                        if liczba[1] == "1":
                            mouse.click(x=x2, y=y2)
                        if liczba[2] == "1":
                            mouse.click(x=x4, y=y4)
                        if liczba[3] == "1":
                            mouse.click(x=x8, y=y8)
                        if liczba[4] == "1":
                            mouse.click(x=x16, y=y16)
                        if liczba[5] == "1":
                            mouse.click(x=x32, y=y32)
                        if liczba[6] == "1":
                            mouse.click(x=x64, y=y64)
                        if liczba[7] == "1":
                            mouse.click(x=x128, y=y128)
            case "X":
                break
            case _:
                print("You fucked up")


if __name__ == "__main__":
    main()