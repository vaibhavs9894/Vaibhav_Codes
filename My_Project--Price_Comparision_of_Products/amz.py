import requests
from bs4 import BeautifulSoup
import pandas as pd
import PriceApp

data = {"products": [], "prices": [], "ratings": []}

url = "https://www.amazon.in/s?k="
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36"
}
products_class_rows = "sg-col-4-of-12 sg-col-8-of-16 sg-col-16-of-24 sg-col-12-of-20 sg-col-24-of-32 sg-col sg-col-28-of-36 sg-col-20-of-28"
products_class_boxes = "sg-col-4-of-24 sg-col-4-of-12 sg-col-4-of-36 s-result-item s-asin sg-col-4-of-28 sg-col-4-of-16 sg-col sg-col-4-of-20 sg-col-4-of-32"


def getRequest():
    search_input = input("Enter product name : ").replace(" ", "+")
    # print("getting userInput...")
    # search_input = PriceApp.product
    # print("Product is : ", search_input)

    link = url + search_input + "&ref=nb_sb_noss_2"

    source = requests.get(link, headers=headers)
    content = source.text
    soup = BeautifulSoup(content, "lxml")

    products = soup.findAll("div", attrs={"class": products_class_rows})

    # for i in range(1, len(products) // 4):
    #     print(products[i])
    # print(len(products))
    # print(type(products))

    # print(products[1])

    if len(products) != 1:
        for product in products:
            try:
                name = product.find(
                    "span", attrs={"class": "a-size-medium a-color-base a-text-normal"}
                )
                print(name.text[:60])
                data["products"].append(name.text[:60])

                try:
                    price = product.find("span", attrs={"class": "a-price-whole"})
                    print(price.text)
                    data["prices"].append(int(price.text.replace(",", "")))
                except AttributeError:
                    print("Not Available")
                    data["prices"].append("Not available")

                try:
                    rating = product.find("span", attrs={"class": "a-icon-alt"})
                    print(rating.text)
                    data["ratings"].append(rating.text[:3])
                except AttributeError:
                    print("Not Available")
                    data["ratings"].append("Not available")

            except AttributeError:
                continue
    else:
        # products not in row form
        # add for loop for scraping product boxes
        print("No product available")
        data["products"].append("No products available")
        data["prices"].append("NA")
        data["ratings"].append("NA")

    print("Total products = ", len(products) - 1)

    df = pd.DataFrame(
        {
            "Product": data["products"],
            "Price": data["prices"],
            "Rating": data["ratings"],
        }
    )
    df.to_csv("amz.csv", index=False, encoding="utf-8")


if __name__ == "__main__":
    getRequest()


# def getRequest():
#     # search_input = input("Enter product name : ").replace(" ", "+")
#     print("getting userInput...")
#     search_input = PriceApp.product
#     print("Product is : ", search_input)

#     link = url + search_input + "&ref=nb_sb_noss_2"

#     source = requests.get(link, headers=headers)
#     content = source.text
#     soup = BeautifulSoup(content, "lxml")

#     for a in soup.findAll("div", attrs={"class": products_class_rows}):

#         try:
#             name = a.find(
#                 "span", attrs={"class": "a-size-medium a-color-base a-text-normal"}
#             )
#             data["products"].append(name.text[:60])

#             try:
#                 price = a.find("span", attrs={"class": "a-price-whole"})
#                 # or a-offscreen for price with rupee symbol
#                 data["prices"].append(int(price.text.replace(",", "")))
#             except AttributeError:
#                 data["prices"].append("Not available")

#             try:
#                 rating = a.find("span", attrs={"class": "a-icon-alt"})
#                 data["ratings"].append(rating.text[:3])
#             except AttributeError:
#                 data["ratings"].append("Not available")

#         except AttributeError:
#             continue

#     df = pd.DataFrame(
#         {
#             "Product": data["products"],
#             "Price": data["prices"],
#             "Rating": data["ratings"],
#         }
#     )
#     df.to_csv("amz.csv", index=False, encoding="utf-8")
