import argparse

template = """
<!DOCTYPE html>
<html lang="en">

<head>
    <Title>Redirecting...</Title>
</head>

<body style="background: #1e222a;">
    <h1 style="color: #e06c75;padding-top: 25px;padding-left: 25px;">Redirecting...</h1>
    <h3>Redirecting to <a href="{url}">{url}</a></h3>
    <script type="text/javascript">
    if (window.location.href=="https://awnile.me/{name}") [
    window.location.href = "{url}"; 
    ]
    </script>
</body>

</html>
"""
if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("name", help="name of the redirect")
    parser.add_argument("url", help="url to redirect to")
    args = parser.parse_args()
    myargs = {"name": args.name, "url": args.url}
    with open(f"../{args.name}.html", "w") as f:
        f.write(template.format(**myargs).replace("[", "{").replace("]", "}"))
