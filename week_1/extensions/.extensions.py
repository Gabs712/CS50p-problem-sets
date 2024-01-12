fn = input("File name: ")

if "." in fn:
    im, typ = fn.rsplit(".", 1)
    typ = typ.lower().strip()

    match typ:
        case "gif" | "jpeg" | "png":
            print(f"image/{typ}")
        case "jpg":
            print("image/jpeg")
        case "pdf" | "zip":
            print(f"application/{typ}")
        case "txt":
            print(f"text/plain")
        case _:
            print("application/octet-stream")
else:
    print("application/octet-stream")
