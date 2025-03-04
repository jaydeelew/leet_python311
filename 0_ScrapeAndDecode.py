import requests
from bs4 import BeautifulSoup


def scrape_and_decode(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")

    char_locations = []
    # Find all table rows in the document
    rows = soup.find_all("tr")

    # Skip the header row
    for row in rows[1:]:
        # Locate and isolate the table data
        cols = row.find_all("td")
        x = int(cols[0].text.strip())
        char = cols[1].text.strip()
        y = int(cols[2].text.strip())
        char_locations.append((char, x, y))

    # Find grid dimensions and add one to max_x and max_y
    max_x = max_y = 0
    for _, x, y in char_locations:
        max_x = max(max_x, x)
        max_y = max(max_y, y)
    max_x += 1
    max_y += 1

    # Create empty grid filled with spaces
    grid = [[" " for _ in range(max_x)] for _ in range(max_y)]

    # Fill in the characters according to their coordinates
    for char, x, y in char_locations:
        grid[y][x] = char

    # Print the grid
    for row in reversed(grid):
        print("".join(row))

    # for row in grid:
    #     print("".join(row))


url = (
    # "https://docs.google.com/document/d/e/2PACX-1vRMx5YQlZNa3ra8dYYxmv-QIQ3YJe8tbI3kqcuC7lQiZm-CSEznKfN_HYNSpoXcZIV3Y_O3YoUB1ecq/pub"
    "https://docs.google.com/document/d/e/2PACX-1vQGUck9HIFCyezsrBSnmENk5ieJuYwpt7YHYEzeNJkIb9OSDdx-ov2nRNReKQyey-cwJOoEKUhLmN9z/pub"
)

scrape_and_decode(url)
